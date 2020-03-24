from django.contrib import admin
from grp import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_name', 'user_surname', 'city',
                    'birth_date')
    list_filter = ('user_name', 'user_surname', 'city',
                    'birth_date')
    search_fields = ('user_name', 'user_surname')


@admin.register(models.Cicle)
class CicleAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_cicle_first_date', 'last_cicle_last_date', 'counter',
                    'created')
    list_filter = ('user',)
    search_fields = ('user',)


