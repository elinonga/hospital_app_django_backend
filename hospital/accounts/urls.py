from django.urls import path
from .views import (
    UserProfileUpdateView,
    UserProfileCreateView,
    UserProfileDetailView,
)

urlpatterns = [
    path("profile/", UserProfileCreateView.as_view(), name="profile-create"),
    path("profile/<int:pk>/", UserProfileDetailView.as_view(), name="profile-detail"),
    path(
        "profile/<int:pk>/update",
        UserProfileUpdateView.as_view(),
        name="profile-update",
    ),
]
