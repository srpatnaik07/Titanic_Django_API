from django.contrib import admin
from django.urls import path,include
from titanic_app import views
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'titanic',views.TitanicViewset)

urlpatterns = [
    path(r'api/',include(router.urls)),
    path('',RedirectView.as_view(url='api/')),
]
