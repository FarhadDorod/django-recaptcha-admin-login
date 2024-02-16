from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from DjangoRecaptchaAdminLogin.identity import login_to_admin_page

def login(request):
    """
        The function `login` handles the login process for an admin page, displaying error messages based on
        the login status.
        
        :param request: The "request" parameter is an object that represents the HTTP request made by the
        user. It contains information such as the user's session, cookies, and the data sent in the request
        :return: an HTTP response redirect to different URLs based on the login status.
    """
    login_status = login_to_admin_page(request)
    if login_status == "InvalidReCAPTCHA":
        messages.error(request, 'Invalid reCAPTCHA. Please try again.')
        return HttpResponseRedirect('/admin/')
    if login_status == "Successfully":
        return HttpResponseRedirect('/admin')
    elif login_status == "UsernameAndPasswordError":
        messages.error(
            request, 'Please enter a correct Username and Password.')
        return HttpResponseRedirect('/admin')
    elif login_status == "Error":
        messages.error(request, 'An error occurred please try another time.')
        return HttpResponseRedirect('/admin')

def home(request):
    """
        Renders the index.html page for the user.

        Args:
            request: The HTTP request object.

        Returns:
            A rendered response for the index.html page.
    """
    return render(request, 'index.html')
