from django.urls import path
from .views import trialbalance_dashboard

urlpatterns = [
    path('report/', trialbalance_dashboard, name='trialbalance_dashboard'),
]













