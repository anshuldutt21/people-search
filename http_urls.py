from django.urls import path

from rest_framework import routers

from people_search.views.student_search import StudentSearch

app_name = 'people_search'
router = routers.DefaultRouter()

router.register(r'',StudentSearch,basename="student_search")

urlpatterns = [

]

urlpatterns += router.urls
