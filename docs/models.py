from django.db import models

class Document(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    docfile = models.FileField(upload_to='documents')
