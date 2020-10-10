from django.urls import path

from rest_framework import routers

from people_search.views.student_search import StudentSearch
from people_search.views.faculty_search import FacultySearch
from people_search.views.interest_search import InterestSearch
from people_search.views.bhawan_search import BhawanSearch

app_name = 'people_search'
router = routers.DefaultRouter()

router.register(r'student_search',StudentSearch,basename="student_search")
router.register(r'faculty_search',FacultySearch,basename="faculty_search")
router.register(r'interest_search',InterestSearch, basename="interest_search")
router.register(r'student/bhawan_search',BhawanSearch, basename="bhawan_search")

urlpatterns = [

]

urlpatterns += router.urls
