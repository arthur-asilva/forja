# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Adicionando os campos novos na visualização do Admin
fields = list(UserAdmin.fieldsets)
fields.append(
    ("Informações Extras", {'fields': ('bio', 'data_nascimento', 'telefone')})
)
UserAdmin.fieldsets = tuple(fields)

admin.site.register(User, UserAdmin)