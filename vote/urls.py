from django.urls import path

from . import views

urlpatterns = [
    path("", views.emoji_list, name="emoji_list"),
    path("vote/<int:pk>/", views.emoji_vote, name="emoji_vote"),
]
