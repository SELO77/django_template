from rest_framework.throttling import AnonRateThrottle


class PreSingUpThrottle(AnonRateThrottle):
    scope = 'presignup'
