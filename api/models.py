from django.db import models

class user(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=200)
    Contact=models.IntegerField()
    Address=models.CharField(max_length=150)
    class Meta:
        db_table = 'myapi'
        

    
