from django.urls import include, path
from rest_framework import routers

from colors import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api/colors/', views.GetColorsAPI.as_view()),
]