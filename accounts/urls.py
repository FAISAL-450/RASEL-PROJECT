from django.urls import path
from . import views

urlpatterns = [
    path('debug-claims/', views.debug_claims, name='debug_claims'),
]







