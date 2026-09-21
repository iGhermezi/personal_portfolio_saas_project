from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class AuthRateThrottle(AnonRateThrottle):
    scope = 'auth'


class SensitiveActionThrottle(UserRateThrottle):
    scope = 'sensitive_action'