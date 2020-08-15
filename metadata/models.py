
from django.db import models
class Metadata(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    string = models.TextField( null = True, blank = True)

    def __str__(self):
        return self.name if self.name else self.pk

class Document(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to = 'Document/', null = True, blank = True)

    def __str__(self):
        return self.name if self.name else self.pk