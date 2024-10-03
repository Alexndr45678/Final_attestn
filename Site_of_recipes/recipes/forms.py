from django.forms import ModelForm, CharField, PasswordInput, ValidationError
from django.contrib.auth.models import User
from .models import Recipe, Category


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ("title", "description", "cooking_time", "categories", "image")


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


# class RegisterForm(ModelForm):
#     class Meta:
#         model = User
#         password1 = CharField(widget=PasswordInput())
#         password2 = CharField(widget=PasswordInput())

#     def clean_password_old(self):
#         cleaned_data = self.cleaned_data
#         password_old = cleaned_data.get("password_old")
#         if not User.check_password(password_old):
#             raise ValidationError("Passwords is not correct")
#         else:
#             return cleaned_data

#     def clean(self):
#         cleaned_data = self.cleaned_data
#         password1 = cleaned_data.get("password1")
#         password2 = cleaned_data.get("password2")

#         if password1 != password2:
#             raise ValidationError("Passwords must be same")
#         else:
#             return cleaned_data
