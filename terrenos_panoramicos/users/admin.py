from django.contrib import admin

#Models
from users.models import Profile


@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user','phone_number','picture','curp')
    list_display_links = ('pk','user')
    list_editable = ('phone_number','picture','curp')

    search_fields= (
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number'
        )
