from django.contrib import admin
from omniport.admin.site import omnipotence
from people_search.models.profile import Profile

omnipotence.register(Profile)
