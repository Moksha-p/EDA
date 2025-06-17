from django.db import models


class Order(models.Model):
    user = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    status = models.CharField(max_length=50,default='placed')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user} - {self.item}"
    

    

