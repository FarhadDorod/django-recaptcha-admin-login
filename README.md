# django-recaptcha-admin-login
This repository contains the code and instructions for implementing Google Recaptcha on the Django admin login page. The goal is to add an extra layer of security to your Django admin site by requiring users to pass a Google Recaptcha challenge before logging in.

![image](https://github.com/FarhadDorod/django-recaptcha-admin-login/assets/30026587/aac33ca1-b05c-49cb-979f-831847d48c2f)

. The login system utilizes the Django framework, a powerful and popular Python web framework. It leverages the built-in authentication system provided by Django to handle user authentication and authorization. The system also incorporates reCAPTCHA, a widely used security measure, to prevent automated bots from accessing the admin page.

. To enhance the user experience, the system utilizes Django's messaging framework to display error messages in a user-friendly manner. These messages are displayed on the login page, providing immediate feedback to the user.

. The login process begins when a user submits their credentials through a login form. The system then validates the reCAPTCHA, username and password entered by the user. If the credentials are correct, the user is redirected to the admin page. In case of invalid credentials, the system displays appropriate error messages to the user, such as "Invalid reCAPTCHA," "Please enter a correct Username and Password," or "An error occurred, please try again."





