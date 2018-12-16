from django.contrib import admin
from .models import Member
# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_reviewed', 'is_approved',)

    actions = ['approve_all']

    def approve_all(self, request, selected_members):
        selected_members.update(is_approved=True, is_reviewed=True)
    approve_all.short_description= 'Approve and review all checked members.'


