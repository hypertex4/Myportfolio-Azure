from django.db import models


# Create your models here.
class Contact(models.Model):
    project_type = models.CharField(max_length=100)
    budget_range = models.CharField(max_length=30)
    deadline = models.CharField(max_length=30,null=True,blank=True)
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    