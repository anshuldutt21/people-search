from django.urls import path

from rest_framework import routers

from people_search.views.student_search import StudentSearch
from people_search.views.faculty_search import FacultySearch
from people_search.views.interest_search import InterestSearch

app_name = 'people_search'
router = routers.DefaultRouter()

router.register(r'student_search',StudentSearch,basename="student_search")
router.register(r'faculty_search',FacultySearch,basename="faculty_search")
router.register(r'interest_search',InterestSearch, basename="interest_search")


urlpatterns = [

]

urlpatterns += router.urls
