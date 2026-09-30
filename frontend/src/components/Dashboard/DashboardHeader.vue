<template>
  <header
    class="flex min-h-[76px] items-center justify-between rounded-3xl border border-violet-100 bg-white px-5 py-4 text-slate-800 shadow-[0_10px_40px_rgba(139,92,246,0.10)] sm:px-6"
    :dir="i18nStore.isRTL ? 'rtl' : 'ltr'"
  >
    <!-- Welcome -->
    <div class="min-w-0">
      <p class="text-xs font-semibold uppercase tracking-wide text-violet-500">
        {{ i18nStore.t("dashboard.dashboard") }}
      </p>

      <h1 class="mt-1 truncate text-lg font-bold text-slate-800 sm:text-xl">
        {{ i18nStore.t("dashboard.welcome") }},
        {{ authStore.user?.username || i18nStore.t("common.user") }} 👋
      </h1>
    </div>

    <!-- Profile -->
    <router-link
      to="/profile"
      class="group flex shrink-0 items-center rounded-full p-1.5 transition hover:bg-violet-50"
    >
      <div
        class="flex h-10 w-10 items-center justify-center overflow-hidden rounded-full bg-violet-100 text-sm font-bold text-violet-600 ring-2 ring-white transition group-hover:bg-violet-200"
      >
        {{ initial }}
      </div>

      <div
        class="hidden min-w-0 sm:block"
        :class="i18nStore.isRTL ? 'mr-3 text-right' : 'ml-3 text-left'"
      >
        <p class="max-w-[140px] truncate text-sm font-semibold text-slate-800">
          {{ authStore.user?.username || i18nStore.t("common.user") }}
        </p>

        <p class="text-xs text-slate-500">
          {{ i18nStore.t("dashboard.viewProfile") }}
        </p>
      </div>
    </router-link>
  </header>
</template>

<script setup>
import { computed } from "vue";

import { useAuthStore } from "../../stores/auth";
import { useI18nStore } from "../../stores/i18n";

const authStore = useAuthStore();
const i18nStore = useI18nStore();

const initial = computed(() => {
  return (
    authStore.user?.username?.charAt(0)?.toUpperCase() ||
    i18nStore.t("common.user").charAt(0)
  );
});
</script>