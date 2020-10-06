from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_CHOICES = (
	    ("Completed", "Completed"),
	    ("In Progress", "In Progress"),
	    ("To Do", "To Do")
	)
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default = "Completed")


    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
