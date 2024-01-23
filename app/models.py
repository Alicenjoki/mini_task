from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
category=(
    ('Entertainment','Entertainment'),
    ('Food','Food'),
    ('Education','Education'),
    ('Sports','Sports'),

)
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length = 150)
    body = models.TextField()
    category = models.CharField(max_length=120, choices=category,null=True)
    image = models.ImageField(upload_to= 'uploads/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now = True )

    def __str__(self):
        return self.title