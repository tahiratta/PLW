from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from accounts.models import User, Lender, Borrower



admin.site.register(Lender)
admin.site.register(Borrower)
admin.site.register(User)
# class UserAdmin(DjangoUserAdmin):
#
#
#     fieldsets = (
#         (None, {'fields': ('entity_name',)}),
#
#     )
#     add_fieldsets = (
#         (None,{
#             'classes': ('wide',),
#             'fields': ('entity_name',),
#         }),
#
#     )
#
#     list_display = ('entity_name',)
#
#     list_filter = ('entity_name',)
#
#     filter_horizontal=('entity_name',)
#
#     search_fields = ('entity_name',)
#
#     ordering = ('entity_name',)
from django.contrib import admin

# Register your models here.
