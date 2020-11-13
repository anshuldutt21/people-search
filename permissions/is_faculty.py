from rest_framework import permissions

from kernel.managers.get_role import get_role
from formula_one.mixins.period_mixin import ActiveStatus


def get_is_faculty_member(obj):
    """
    Checks if the authenticated user is a faculty member or not
    :param obj: an instance of Profile Model
    :return: a boolean if the authenticated user is a faculty member or not
    """
    return False
    role_faculty_member = get_role(
        person=obj,
        role_name='FacultyMember',
        active_status=ActiveStatus.IS_ACTIVE,
        silent=True,
    )
    return role_faculty_member is not None
