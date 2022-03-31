from django.db import models
import uuid

# Create your models here.
class Organisers(models.Model):
    Organiser_id = models.UUIDField(auto_created=True,default=uuid.uuid4, editable=False, primary_key=True,unique=True, serialize=False, verbose_name='organiserId')
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    description=models.TextField(max_length=2000)
    deleted = models.BooleanField(default=False)
    createAt=models.DateTimeField(auto_now_add=True)
   

class Events(models.Model):
    eventId = models.UUIDField(auto_created=True,default=uuid.uuid4, editable=False, primary_key=True, unique=True, serialize=False, verbose_name='eventId')
    title=models.CharField(max_length=100)
    starting_date = models.DateTimeField(auto_now_add=True)
    ending_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(null=False, max_length=100)
    createAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now_add=True)
    open = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    orgnaniser_id = models.ForeignKey(Organisers,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.title