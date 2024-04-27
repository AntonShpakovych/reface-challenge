from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View

from config.settings import LOGIN_REDIRECT_URL
from user.forms import CustomUserCreationForm, CustomAuthenticationForm


class LoginOrSignUp(View):
    login_object_name = "form_login"
    signup_object_name = "form_signup"
    form_to_render_name = "form_to_render"
    template_name = "registration/login.html"
    login_form_class = CustomAuthenticationForm
    signup_form_class = CustomUserCreationForm

    def get(self, request):
        return render(request, self.template_name, context={
            self.login_object_name: self.login_form_class(request=request),
            self.signup_object_name: self.signup_form_class()
        })

    def post(self, request):
        form = (
            self.login_form_class(data=request.POST, request=request)
            if self.is_form_login(request=request)
            else self.signup_form_class(request.POST)
        )

        if form.is_valid():
            return self._form_valid(request=request, form=form)
        return self._form_invalid(request, form=form)

    def is_form_login(self, request):
        return self.login_object_name in request.POST

    def _handle_form_valid(self, request, form):
        if self.is_form_login(request=request):
            login(request, user=form.get_user())
        else:
            form.save()
            login(request, user=form.instance)

    def _hande_form_invalid(self, request, form):
        if self.is_form_login(request=request):
            return {
                self.login_object_name: form,
                self.signup_object_name: self.signup_form_class(),
                self.form_to_render_name: self.login_object_name
            }
        return {
            self.login_object_name: self.login_form_class(),
            self.signup_object_name: form,
            self.form_to_render_name: self.signup_object_name
        }

    def _form_valid(self, request, form):
        self._handle_form_valid(request=request, form=form)
        return redirect(LOGIN_REDIRECT_URL)

    def _form_invalid(self, request, form):
        context = self._hande_form_invalid(request, form=form)
        return render(request, self.template_name, context=context)
