from django.urls import path

from rest_framework import routers

from people_search.views.student_search import StudentSearch
from people_search.views.faculty_search import FacultySearch

app_name = 'people_search'
router = routers.DefaultRouter()

router.register(r'student_search',StudentSearch,basename="student_search")
router.register(r'faculty_search',FacultySearch,basename="faculty_search")

urlpatterns = [

]

urlpatterns += router.urls
