from django.db import models

class Categories(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices=Categories.choices,
        default=Categories.GR,
    )
    Approved = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return self.title 

    def full_name(self):
        return self.title + self.sub_title


    full_name.admin_order_field = 'title'