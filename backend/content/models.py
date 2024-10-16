# content/models.py

from django.db import models
from django.contrib.auth.models import User

class Content(models.Model):
    USER_CONTENT_CHOICES = [
        ('social_media', 'Social Media Post'),
        ('blog', 'Blog Post'),
        ('product_description', 'Product Description'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contents')
    content_type = models.CharField(max_length=50, choices=USER_CONTENT_CHOICES)
    prompt = models.TextField()
    generated_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.content_type} by {self.user.username} on {self.created_at}"
