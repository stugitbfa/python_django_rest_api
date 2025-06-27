from django.db import models
import uuid
# Create your models here.
class BaseClass(models.Model):
    id = models.UUIDField(primary_key=True, blank=False, null=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Blog(BaseClass):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField()
