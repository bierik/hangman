from django.urls import path, include
from api.routers import router
from api import views

urlpatterns = [
    path("", include(router.urls)),
    path("profile/", views.ProfileView.as_view()),
    path("config/", views.ConfigView.as_view())
]
