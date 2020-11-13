import swapper

from django.db import models

from people_search.constants import public_to_filters


class Profile(models.Model):
    """
    Model for checking which fields are public to
    which set of people
    """
    student = models.ForeignKey(
        to=swapper.get_model_name('kernel', 'Student'),
        on_delete=models.CASCADE,
        unique=True,
        related_name='people_search_student'
    )

    primary_email_id = models.CharField(
        max_length=20,
        choices=public_to_filters,
        default='all')

    primary_mobile_no = models.CharField(
        max_length=20, choices=public_to_filters, default='all')

    room_no = models.CharField(
        max_length=20,
        choices=public_to_filters,
        default='all')

    bhawan = models.CharField(
        max_length=20,
        choices=public_to_filters,
        default='all')
