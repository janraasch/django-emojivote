from django.db import models


class Emoji(models.Model):
    character = models.CharField(max_length=2)
    name = models.CharField(max_length=50)
    votes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-votes"]

    def __str__(self):
        return f"{self.character} {self.name}"
