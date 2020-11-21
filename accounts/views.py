from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views.generic import FormView

from website.mixins import RequestFormAttachMixin, NextUrlMixin
from accounts.forms import LoginForm, RegistrationForm

User = get_user_model()


class LoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        next_path = self.get_next_url()
        return redirect(next_path)


class RegistrationView(NextUrlMixin, RequestFormAttachMixin, FormView):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm

    def form_valid(self, form):
        next_path = self.get_next_url()
        return redirect(next_path)
