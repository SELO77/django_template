REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
        'core.throttling.PreSingUpThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '20/sec',
        'user': '50/sec',
        'presignup': '5/min'
    }
}

print("* Loaded DRF settings.")