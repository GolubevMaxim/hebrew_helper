from django.db import models


class MemoryCards(models.Model):
    word_in_russian = models.CharField(max_length=100)
    word_in_hebrew = models.CharField(max_length=100)

    image = models.ImageField(upload_to='memory_cards/images/')
    pronunciation = models.FileField(upload_to='memory_cards/pronunciation')

    class Meta:
        verbose_name = 'Memory Card'
        verbose_name_plural = 'Memory Cards'
