from django.db import models

class Carousel(models.Model):
    img = models.CharField(max_length=300)

    class Meta:
        db_table='carousel'

    def __str__(self):
        return self.img


class Banner(models.Model):
    url = models.CharField(max_length=100)
    img = models.CharField(max_length=50)

    class Meta:
        db_table='banner'

    def __str__(self):
        return self.img

class CardFront(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    img = models.CharField(max_length=50)
    alt = models.CharField(max_length=50)
    creci = models.CharField(max_length=15)

    class Meta:
        db_table='cardfront'

    def __str__(self):
        return self.title