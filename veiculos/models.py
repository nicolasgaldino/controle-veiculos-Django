from django.db import models

class Carros(models.Model):

  modelo_carro = models.CharField(
    verbose_name="Por favor, informe o modelo do carro",
    max_length=194,
  )

  marca_carro = models.CharField(
    verbose_name="Por favor, informe a marca do carro",
    max_length=194,
  )

  ano_carro = models.IntegerField(
    verbose_name="Por favor, informe o ano do carro",
  )

  class Meta:
    verbose_name = "Carro"
    verbose_name_plural = "Carros"
    db_table = "carros"

  def __str__(self):
    return self.modelo_carro
