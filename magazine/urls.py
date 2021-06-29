from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('info', views.info),
    path('registration', views.registration),
    path('checkout', views.checkout),
    path('history', views.history),
]