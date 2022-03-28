from django.db import models
from django.contrib.auth.models import User

from app.utils.base_model import BaseModel


class URL(BaseModel):
    """
    URL model
    """
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="urls",
        null=True, blank=True
    )
    url = models.URLField(max_length=255, unique=True)

    class Meta:
        verbose_name = "URL"
        verbose_name_plural = "URLs"

    def __str__(self):
        return self.url