from django.db import models


# Create your models here.

class Company(models.Model):
    """Контакт для юр. лица"""
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)

    owner_first_name = models.CharField(max_length=255)
    owner_last_name = models.CharField(max_length=255)

    website = models.URLField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Individual(models.Model):
    """Контакт для физ. лица, который также можнт работать в компании"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth = models.CharField(max_length=255, null=True, blank=True)

    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'