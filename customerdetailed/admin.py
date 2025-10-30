from django.contrib import admin
from .models import Profile, CustomerDetailed

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role']
    list_filter = ['role']
    search_fields = ['user__username']

@admin.register(CustomerDetailed)
class CustomerDetailedAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'created_by', 'team', 'created_at']
    list_filter = ['team', 'created_by']
    search_fields = ['name', 'company', 'created_by__username']


