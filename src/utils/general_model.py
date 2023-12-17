from django.db import models
from django.utils.translation import gettext as _


class GeneralModel(models.Model):
    """to use in all models for tracking changes

    Args:
        created_date (datetime):
            Date and time when the model was initially created.
        updated_date (datetime): Date and time when the model was last updated.
    """

    created_date = models.DateTimeField(
        verbose_name=_('Created Time'),
        auto_now_add=True
    )
    updated_date = models.DateTimeField(
        verbose_name=_('Updated Time'),
        auto_now=True
    )

    class Meta:
        abstract = True
