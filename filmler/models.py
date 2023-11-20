from django.db import models
from django.utils.text import slugify

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=50)
    description=models.TextField()
    imageUrl=models.CharField(max_length=50, blank=False)
    slug=models.SlugField(default="",blank=True,editable=False, null=False, unique=True, db_index=True)

    def save(self, *args, **kwargs):
          self.slug=slugify(self.title)
          super().save(args,kwargs)

    def __str__(self):
        return f"{self.title}"

class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
      
      


# modeli oluşturduk. Bu modelin bir sql karşılığı olmalı. Uygulamamıza bir model ekledik bu 
# modeli baz alan bir sql güncellemesini uygulama tarafında migration ile oluşturup onu 
# veri tabanı sağlayıcısına göndermemiz gerekiyor