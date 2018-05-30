from django.db import models

# Create your models here.


class TypedWord(models.Model):
    typed_word = models.CharField(max_length=50)
