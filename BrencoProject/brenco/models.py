from distutils.text_file import TextFile
from certifi import contents
from django.db import models

# Create your models here.
class BRENCO (models.Model):
    content=models.TextField()
