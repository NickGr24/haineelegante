from django.db import models

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Categorie")
    cover = models.ImageField(upload_to='categories/', null=True, blank=True, verbose_name="Imagine fon")
    slug = models.SlugField(unique=True, null=True, blank=True) 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categorii"

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Brand")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Brenduri"

class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Denumirea produsului")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categorie")
    description = models.TextField(verbose_name='Descriere', null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preț (MDL)")
    image = models.ImageField(upload_to='products/', verbose_name="Imagine")
    sizes = models.CharField(max_length=100, verbose_name="Mărimi disponibile", help_text="Exemplu: 42, 44, 46")
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Reducere (%)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data adăugării")

    def final_price(self):
        if self.discount:
            return round(self.price * (1 - self.discount / 100), 2)
        return self.price

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Produse"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/gallery/')

    def __str__(self):
        return f"Imagine pentru {self.product.title}"

class SliderImage(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titlu (opțional)", blank=True)
    image = models.ImageField(upload_to='slider/', verbose_name="Imagine")
    active = models.BooleanField(default=True, verbose_name="Activ")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordine")

    class Meta:
        ordering = ['order']
        verbose_name = "Imagine slider"
        verbose_name_plural = "Imagini slider"

    def __str__(self):
        return self.title or f"Imagine #{self.pk}"