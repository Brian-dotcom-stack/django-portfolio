from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)  # A short title for the About page
    description = models.TextField()  # A longer text field for the About description
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically adds timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updates timestamp when modified

    def __str__(self):
        return self.title  # String representation of the model
