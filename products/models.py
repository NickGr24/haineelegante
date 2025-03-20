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
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preț (RON)")
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
