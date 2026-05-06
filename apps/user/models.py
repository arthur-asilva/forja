# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Adicione campos personalizados aqui
    # bio = models.TextField(max_length=500, blank=True)
    # data_nascimento = models.DateField(null=True, blank=True)
    # telefone = models.CharField(max_length=15, blank=True)
    cpf = models.CharField(max_length=11, blank=True)

    # Exemplo: mudar o campo de login para e-mail em vez de username
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # username ainda será pedido no createsuperuser

    def _str_(self):
        return self.username