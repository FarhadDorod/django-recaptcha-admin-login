from django.contrib.auth import authenticate, login
from .recaptcha import is_recaptcha_true


def login_to_admin_page(request):
    """
        Logs in the user to the admin page.

        Args:
            request: The HTTP request object.

        Returns:
            If the user is successfully logged in, returns None.
            If the reCAPTCHA validation fails, returns "InvalidReCAPTCHA".
            If there is an error during the reCAPTCHA validation, returns "Error".
    """
    try:
        username = request.POST.get("username")
        password = request.POST.get("password")
        recaptcha_response = is_recaptcha_true(request.POST.get('g-recaptcha-response'))
        
        if recaptcha_response['success'] == False:
            return "InvalidReCAPTCHA"
        
        if recaptcha_response == "Error":
            return "Error"
    
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return "Successfully"
        else:
            return "UsernameAndPasswordError"
    except Exception:
        return "Error"