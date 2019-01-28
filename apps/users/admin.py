from functools import update_wrapper
import random

from django.contrib.auth.hashers import make_password
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path

from .models import Member, Patron
from ..instruments.models import Instrument
# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):

    change_list_template = 'users_admin.html'
    list_display = ('first_name', 'last_name', 'email', 'is_reviewed', 'is_approved', 'is_coach', 'created_at', 'updated_at')

    actions = [
                'approve_all',
                'disapprove_all',
                'coach_all',
                'revoke_coach',
                'mark_as_viewed',
                'set_default_password',
            ]


    def get_urls(self):
        # Security wrapper for django, otherwise the route will be unprotected
        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            
            wrapper.model_admin = self
            return update_wrapper(wrapper, view)

        default_urls = super().get_urls()
        
        custom_urls = [
            path('import-test-users/', wrap(self.import_test_users), name="import_test_users"),
        ]
        
        #Since django does left-right (in-order) scanning of urls, it's important to put our custom ones first.
        return custom_urls + default_urls

    # Dirty test-users method, will replace later.  Clean it up and put it in a test suite.
    def import_test_users(self, req):
        from .test_users import test_users


        for test_user in test_users:
            primary_instruments_available = Instrument.objects.filter(primary_users__isnull=True)
            if not primary_instruments_available:
                primary_instruments_available = Instrument.objects.all()
            test_user['primary_instrument'] = random.choice(primary_instruments_available)
            
            secondary_instruments_available = Instrument.objects.filter(secondary_users__isnull=True)
            if not secondary_instruments_available:
                secondary_instruments_available = Instrument.objects.all()
            test_user['secondary_instrument'] = random.choice(secondary_instruments_available)
            
            test_user['password'] = make_password('password')

        for test_user in test_users:
            Member.objects.create(**test_user)

        return redirect('..')


    def approve_all(self, request, selected_members):
        selected_members.update(is_approved=True, is_reviewed=True)
    approve_all.short_description = 'Approve and review all checked members.'

    def disapprove_all(self, request, selected_members):
        selected_members.update(is_approved=False, is_reviewed=True)
    disapprove_all.short_description = 'Deny and review all checked members.'

    def coach_all(self, request, selected_members):
        selected_members.update(is_coach=True, is_reviewed=True, is_approved=True)
    coach_all.short_description = 'Approve and set coach status for all checked members.'

    def revoke_coach(self, request, selected_members):
        selected_members.update(is_coach=False, is_reviewed=True)
    revoke_coach.short_description = 'Remove coach status for all checked members.'

    def mark_as_viewed(self, request, selected_members):
        selected_members.update(is_reviewed=True)
    mark_as_viewed.short_description = 'Review all checked members.'

    def set_default_password(self, request, selected_members):
        for member in selected_members:
            member.password = Member.objects.generate_new_password()
            member.save()
    set_default_password.short_description = 'Set new passwords for all selected members.'

@admin.register(Patron)
class PatronAdmin(admin.ModelAdmin):
    pass
