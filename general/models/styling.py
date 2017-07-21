from django.db import models


class StyleCategory(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True
    )

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title


class Style(models.Model):
    title = models.CharField(
        max_length=255
    )
    category = models.ForeignKey(
        'general.StyleCategory',
        on_delete=models.PROTECT
    )
    css_class = models.CharField(
        max_length=255
    )

    class Meta:
        ordering = ('title', )
        unique_together = ('title', 'category')

    def __str__(self):
        return self.title
