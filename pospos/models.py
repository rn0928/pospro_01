from django.db import models

# Create your models here.
from django.utils.timezone import now


class Posting(models.Model):

    """コメント."""

    name = models.CharField(verbose_name='名前', max_length=100,
                            blank=False, null=False)
    post = models.TextField(verbose_name='コメント')
    created_at = models.DateTimeField(verbose_name='daytime', default=now)

    class Meta:
        db_table = "posting"