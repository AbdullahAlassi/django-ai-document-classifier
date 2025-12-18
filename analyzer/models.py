from django.db import models

# Creating model
class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    predicted_category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title