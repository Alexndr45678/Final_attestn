from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("create/", views.recipe_create, name="create"),
    path("register/", views.register, name="register"),
    path("<int:pk>/edit/", views.recipe_edit, name="edit"),
    path("<int:pk>/delete/", views.recipe_delete, name="delete"),
    path("category/create/", views.category_create, name="category_create"),
    path("recipes/<int:pk>/", views.recipe_detail, name="recipe_detail"),
    path("recipes/create/", views.recipe_create, name="recipe_create"),
    path("recipes/<int:pk>/edit/", views.recipe_edit, name="recipe_edit"),
]
