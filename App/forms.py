from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm

class AuthAdminForm(AuthenticationForm):
    """
        Custom authentication form for admin users.
        Includes captcha field for additional security.
    """
    captcha = settings.GOOGLE_RECAPTCHA_SITE_KEY
