import PIL.Image
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
    img = models.ImageField(upload_to='products/%Y/%m/%d')
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save()
        img = PIL.Image.open(self.img.path)
        width, height = img.size

        if width > 300 and height > 300:
            img.thumbnail((width, height))

        if height < width:
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))

        elif width < height:
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))

        if width > 450 and height > 450:
            img.thumbnail((450, 450))

        img.save(self.img.path)
