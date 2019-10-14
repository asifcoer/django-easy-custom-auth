from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.edit import FormView,CreateView
from django.views.generic import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

# Create your views here.

class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customauth/index.html', )


class SignupView(CreateView):
    template_name = settings.SIGNUP_HTML if hasattr(settings, 'SIGNUP_HTML') else 'customauth/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('customauth:login')


class LoginView(auth_views.LoginView):
    template_name = settings.LOGIN_HTML if hasattr(settings, 'LOGIN_HTML') else 'customauth/login.html'
    def form_invalid(self, form):
        messages.add_message(self.request, messages.WARNING, "Username or Password incorrect.")
        return super(LoginView, self).form_invalid(form)


class LogoutView(auth_views.LogoutView):
    pass


class PasswordChangeView(auth_views.PasswordChangeView):
    success_url = reverse_lazy('customauth:login')
    template_name = settings.CHANGE_PASSWORD_FORM_HTML if hasattr(settings, 'CHANGE_PASSWORD_FORM_HTML') else 'customauth/change_password_form.html'
    def form_valid(self, form):
        msz = 'Your password has been changed successfully'
        messages.add_message(self.request, messages.SUCCESS, msz)
        return super().form_valid(form)


class PasswordResetView(auth_views.PasswordResetView):
    success_url = reverse_lazy('customauth:password_reset_done')
    email_template_name = settings.PASSWORD_RESET_EMAIL_HTML if hasattr(settings, 'PASSWORD_RESET_EMAIL_HTML') else 'customauth/password_reset_email.html'
    subject_template_name = settings.PASSWORD_RESET_SUBJECT_TXT if hasattr(settings, 'PASSWORD_RESET_SUBJECT_TXT') else 'customauth/password_reset_subject.txt'
    template_name = settings.PASSWORD_RESET_FORM_HTML if hasattr(settings, 'PASSWORD_RESET_FORM_HTML') else 'customauth/password_reset_form.html'


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = settings.PASSWORD_RESET_DONE_HTML if hasattr(settings, 'PASSWORD_RESET_DONE_HTML') else 'customauth/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy('customauth:password_reset_complete')
    template_name = settings.PASSWORD_RESET_CONFIRM_HTML if hasattr(settings, 'PASSWORD_RESET_CONFIRM_HTML') else 'customauth/password_reset_confirm.html'

    
class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    success_url = reverse_lazy('customauth:login')
    template_name = settings.PASSWORD_RESET_COMPLETE_HTML if hasattr(settings, 'PASSWORD_RESET_COMPLETE_HTML') else 'customauth/password_reset_complete.html'


