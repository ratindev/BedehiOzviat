# members/admin.py
from django.contrib import admin
from .models import Membership

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Family', 'codemeli', 'year', 'calculate_amount')  # Add any other fields you want to display in the list

    # Optionally, you can add search and filter options
    search_fields = ['year']
    list_filter = ['year']



