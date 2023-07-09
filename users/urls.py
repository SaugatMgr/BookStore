from django.urls import path
from .views import MyProfile

app_name = "users"

urlpatterns = [
    # Users Profile
    path("", MyProfile.as_view(), name="profile"),
]
