from django.db import models

class Todo(models.Model):
    title = models.TextField(blank=True)
    reminder = models.DateTimeField(null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} {self.title}'