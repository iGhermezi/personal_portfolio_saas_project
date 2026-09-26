from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.urls import path, reverse
from django.utils import timezone
from django.utils.html import format_html

from .models import PremiumRequest, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'email_verified',
        'has_active_subscription',
        'is_staff',
    )

    search_fields = (
        'username',
        'email',
    )

    list_filter = (
        'email_verified',
        'has_active_subscription',
        'is_staff',
    )


@admin.register(PremiumRequest)
class PremiumRequestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'user_email',
        'status',
        'created_at',
        'reviewed_at',
        'approve_button',
    )

    list_filter = (
        'status',
        'created_at',
    )

    search_fields = (
        'user__username',
        'user__email',
    )

    readonly_fields = (
        'user',
        'status',
        'created_at',
        'reviewed_at',
        'reviewed_by',
    )

    ordering = (
        '-created_at',
    )

    def user_email(self, obj):
        return obj.user.email

    user_email.short_description = 'Email'

    def approve_button(self, obj):
        if obj.status == PremiumRequest.STATUS_APPROVED:
            return format_html(
                '<span style="color: green; font-weight: 600;">'
                '✓ Approved'
                '</span>'
            )

        url = reverse(
            'admin:approve_premium_request',
            args=[obj.pk],
        )

        return format_html(
            '<a class="button" href="{}">'
            'Approve Premium'
            '</a>',
            url,
        )

    approve_button.short_description = 'Action'

    def get_urls(self):
        urls = super().get_urls()

        custom_urls = [
            path(
                '<int:request_id>/approve/',
                self.admin_site.admin_view(
                    self.approve_request
                ),
                name='approve_premium_request',
            ),
        ]

        return custom_urls + urls

    def approve_request(self, request, request_id):
        if request.method != 'POST':
            request = request

        premium_request = PremiumRequest.objects.select_related(
            'user'
        ).get(
            pk=request_id
        )

        if premium_request.status == PremiumRequest.STATUS_APPROVED:
            self.message_user(
                request,
                'This Premium request has already been approved.',
                level=messages.WARNING,
            )

            return HttpResponseRedirect(
                reverse(
                    'admin:accounts_premiumrequest_changelist'
                )
            )

        user = premium_request.user

        user.has_active_subscription = True
        user.save(
            update_fields=['has_active_subscription']
        )

        premium_request.status = (
            PremiumRequest.STATUS_APPROVED
        )
        premium_request.reviewed_at = timezone.now()
        premium_request.reviewed_by = request.user
        premium_request.save(
            update_fields=[
                'status',
                'reviewed_at',
                'reviewed_by',
            ]
        )

        self.message_user(
            request,
            f'Premium access activated for {user.email}.',
            level=messages.SUCCESS,
        )

        return HttpResponseRedirect(
            reverse(
                'admin:accounts_premiumrequest_changelist'
            )
        )