from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import UserRegisterFrom
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'

class LogoutView(BaseLogoutView):
    pass

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterFrom
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    # FCV for email verification
    def form_valid(self, form):
        self.object = form.save()
        send_mail(
            subject='Верификация по почте',
            message=f'Это подтверждение регистрации пользователя {self.object.email}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)





