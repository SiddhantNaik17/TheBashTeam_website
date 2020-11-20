from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views.generic import FormView
from django.views.generic.base import View

from website.mixins import RequestFormAttachMixin, NextUrlMixin
from accounts.forms import LoginForm

User = get_user_model()


class LoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        next_path = self.get_next_url()
        return redirect(next_path)
