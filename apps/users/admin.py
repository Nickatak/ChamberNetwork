from django.contrib import admin
from .models import Member
# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_reviewed', 'is_approved',)