from django.contrib import admin
from core.models import Profile, Midia 

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'birthday', 'about_me')
    list_filter = ('usuario', 'birthday')

admin.site.register(Profile, ProfileAdmin) 


class MidiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'sinopse', 'tipo', 'nota', 'avaliacao', 'lancamento', 'usuario')
    list_filter = ('lancamento', 'usuario')

admin.site.register(Midia, MidiaAdmin)