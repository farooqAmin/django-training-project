from django.contrib import admin
from .models import Address, UserProfile

# Register your models here.


class AddressAdmin(admin.ModelAdmin):
    model = Address


class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ("user", )
    # save_as = True
    # search_fields = ['user__username', 'type']
    # show_full_result_count = True
    # view_on_site = False

    # change_list_template = "index.html"

    # model = UserProfile
    # inlines = [AddressAdmin, ]


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Address)
