from django.forms import ModelForm
from .models import Recipe, Category


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ("title", "description", "cooking_time", "categories", "image")


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
