from django.urls import path
from . import views

urlpatterns = [
    # 🔹 Team dashboard: team members manage their own team's customers
    path('dashboard/', views.customerdetailed_dashboard, name='customerdetailed_dashboard'),

    # 🔹 Admin dashboard: staff users view all customer records
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),

    # ✏️ Edit customer entry
    path('dashboard/edit/<int:pk>/', views.edit_customer, name='edit_customer'),

    # 🗑️ Delete customer entry
    path('dashboard/delete/<int:pk>/', views.delete_customer, name='delete_customer'),
]



