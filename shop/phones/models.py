from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    images = models.ManyToManyField('Image')

    def get_absolute_url(self):
        return reverse('phones:product_detail', args=[self.pk, self.slug])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']
        index_together = [('id', 'slug')]


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('phones:list_categories', args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='media')
