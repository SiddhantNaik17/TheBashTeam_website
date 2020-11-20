from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView

from website.mixins import RequestFormAttachMixin, NextUrlMixin
from accounts.forms import LoginForm, ProfileEditForm

User = get_user_model()


class LoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        next_path = self.get_next_url()
        return redirect(next_path)


class ProfileView(UpdateView):
    model = User
    form_class = ProfileEditForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user
