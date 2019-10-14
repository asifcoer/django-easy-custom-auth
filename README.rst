=====
DJANGO EASY CUSTOM AUTH
=====

django easy custom auth is a simple Django app to provide all user related funtionalities. User signup, login, logout, change password, forgot password all is set with all templates. You can customize templates easily by putting their path in your settings file. 

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "django_easy_custom_auth" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'customauth',
    ]

2. Define the login, logout and login_redirect url in your project settings.py like this::

    LOGIN_URL = '/ca/login/'
    LOGIN_REDIRECT_URL = '/ca/'
    LOGOUT_REDIRECT_URL = LOGIN_URL

3. Include the custom_auth URLconf in your project urls.py like this::

    path('ca/', include('customauth.urls')),

4. Run `python manage.py migrate` to create the user model if already not done.

5. Start the development server and visit http://127.0.0.1:8000/ca/
   to signup.


Override templates
------------------

Define the templates path as below. change the customauth with your app name, if you have put templates in your app or define path accordingly. 

    # custom auth settings
    SIGNUP_HTML = 'customauth/signup.html'
    LOGIN_HTML = 'customauth/login.html'
    CHANGE_PASSWORD_FORM_HTML = 'customauth/change_password_form.html'
    PASSWORD_RESET_COMPLETE_HTML = 'customauth/password_reset_complete.html'
    PASSWORD_RESET_CONFIRM_HTML = 'customauth/password_reset_confirm.html'
    PASSWORD_RESET_DONE_HTML = 'customauth/password_reset_done.html'
    PASSWORD_RESET_EMAIL_HTML = 'customauth/password_reset_email.html'
    PASSWORD_RESET_FORM_HTML = 'customauth/password_reset_form.html'
    PASSWORD_RESET_SUBJECT_TXT = 'customauth/password_reset_subject.txt'

