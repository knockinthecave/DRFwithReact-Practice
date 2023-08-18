from django.db import models

# Create your models here.


class Worker(models.Model):
    wid = models.IntegerField(primary_key=True)
    workerName = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'Worker'