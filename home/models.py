from django.db import models

class InfoAdminUser(models.Model):
    name = models.CharField(max_length=100)
    birth = models.CharField(max_length=100)
    email = models.EmailField(default=0)
    phone = models.CharField(max_length=30)
    introduce = models.TextField(blank=True)
    introduce2 = models.TextField(blank=True)
    introduce3 = models.TextField(blank=True)

    def __str__(self):
        return self.name