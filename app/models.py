from django.db import models

# Create your models here.

class Endereco(models.Model):
    ESTADO_CHOICES={
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraíma'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocatins')

    }
    rua = models.CharField(max_length=100, null= False, blank= False)
    numero = models.IntegerField(null=False, blank= False)
    bairro = models.CharField(max_length=100, null= False, blank= False)
    cidade = models.CharField(max_length=100, null= False, blank= False)
    estado = models.CharField(choices=ESTADO_CHOICES, max_length=2, null= False, blank= False)

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=100, null=False, blank=False)
    endereco = models.OneToOneField(to=Endereco, on_delete=models.SET_NULL, null=True)
