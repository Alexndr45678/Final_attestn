from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import password_validators_help_texts
from .models import Recipe
from .forms import RecipeForm, CategoryForm


def index(request):
    recipes = Recipe.objects.order_by("-id")
    return render(request, "recipes/index.html", {"recipes": recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "recipes/recipe_detail.html", {"recipe": recipe})


def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect("recipes:index")
    else:
        form = RecipeForm()
    return render(request, "recipes/recipe_form.html", {"form": form})


def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipes:recipe_detail", pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "recipes/recipe_form.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("recipes:index")
    else:
        form = AuthenticationForm()
    return render(request, "recipes/login.html", {"form": form})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("recipes:index")
    else:
        form = UserCreationForm()
    return render(request, "recipes/register.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect("recipes:index")
    else:
        form = UserCreationForm()
    return render(request, "recipes/register.html", {"form": form})


def logout(request):
    auth_logout(request)
    return redirect("recipes:index")


def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recipes:index")
    else:
        form = CategoryForm()
        return password_validators_help_texts()
    return render(request, "recipes/category_form.html", {"form": form})


def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect("recipes:index")
    return render(request, "recipes/recipe_confirm_delete.html", {"recipe": recipe})
