import urllib.request
import json

from django.conf import settings

def is_recaptcha_true(recaptcha_response):
    """
        Verify if the reCAPTCHA response is true.

        Args:
            recaptcha_response (str): The user's reCAPTCHA response.

        Returns:
            bool: True if the reCAPTCHA response is valid, False otherwise.
    """
    try:
        url = "https://www.google.com/recaptcha/api/siteverify"
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response,
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        return result
    except:
        return str("Error")