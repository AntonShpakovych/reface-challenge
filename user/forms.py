from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs[
            "placeholder"
        ] = "Enter your email"
        self.fields["password1"].widget.attrs[
            "placeholder"
        ] = "Create your password"
        self.fields["password2"].widget.attrs[
            "placeholder"
        ] = "Confirm your password"

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("email", "password1", "password2")


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "Enter email"
        self.fields["password"].widget.attrs["placeholder"] = "Enter password"
