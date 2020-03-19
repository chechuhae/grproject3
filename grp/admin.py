from django.contrib import admin
from grp import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_name', 'user_surname', 'city',
                    'birth_date')
    list_filter = ('user_name', 'user_surname', 'city',
                    'birth_date')
    search_fields = ('user_name', 'user_surname')


