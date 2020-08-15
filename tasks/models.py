from django.db import models

# Create your models here.


class Task(models.Model):

    STATES = (
        ('new', 'new'),
        ('in_progress', 'in_progress'),
        ('done', 'done'),
    )

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50, blank=True)
    state = models.CharField(choices=STATES, max_length=125, default='new')
    link_to = models.ForeignKey('self', on_delete=models.CASCADE, related_name="linked_tasks", blank=True, null=True)