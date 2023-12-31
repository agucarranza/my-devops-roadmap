from django.db import models

# Create your models here.

class Quote(models.Model):
    quote_text = models.CharField(max_length=200, null=False)
    pub_date = models.DateTimeField("date published")
