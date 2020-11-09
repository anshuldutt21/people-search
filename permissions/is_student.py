from rest_framework import permissions

from kernel.managers.get_role import get_role
from formula_one.mixins.period_mixin import ActiveStatus


def get_is_student(obj):
    """
    Checks if the authenticated user is a student or not
    :param obj: an instance of Profile
    :return: a boolean if the authenticated user is a student or not
    """
    role_student = get_role(
        person=obj,
        role_name='Student',
        active_status=ActiveStatus.IS_ACTIVE,
        silent=True,
    )
    return role_student is not None
