from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Nome')
    last_name = models.CharField(max_length=100, verbose_name='Sobrenome')
    about_me = models.TextField(blank=True, null=True, verbose_name='Sobre mim')
    birthday = models.DateTimeField(null=True, verbose_name='Aniversário')
    member_since = models.DateTimeField(auto_now=True, verbose_name='Member since')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.name

    def get_birthday(self):
        return self.birthday.strftime('%d/%m/%Y %H:%M Hrs')

    def get_member_since(self):
        return self.member_since.strftime('%Y-%m-%dT%H:%M')

class Midia(models.Model):
    MIDIA_CHOICES = (
        ("S", "Série"),
        ("F", "Filme"),
    )

    MIDIA_NOTA = ((1, "Um"),(2, "Dois"),(3 ,"Três"),(4, "Quatro"),(5, "Cinco"),(6, "Seis"),(7, "Sete"),(8, "Oito"),(9, "Nove"),(10, "Dez"))
    titulo = models.CharField(max_length=100)
    sinopse = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=100, choices=MIDIA_CHOICES, blank=False, null=False)
    nota = models.IntegerField(choices=MIDIA_NOTA)
    avaliacao = models.TextField(blank=True, null=True)
    lancamento = models.DateTimeField(null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
            db_table = "midia"

    def __str__(self):
            return self.titulo

    def get_lancamento(self):
            return self.lancamento.strftime('%Y')    

