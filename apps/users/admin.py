from django.contrib import admin
from .models import Member, Patron
# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_reviewed', 'is_approved', 'is_coach', 'created_at', 'updated_at')

    actions = [
                'approve_all',
                'disapprove_all',
                'coach_all',
                'revoke_coach',
                'mark_as_viewed',
                'set_default_password',
            ]

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
