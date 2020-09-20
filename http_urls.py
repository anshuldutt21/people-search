from django.urls import path

from people_search.views.hello_world import HelloWorld

app_name = 'people_search'

urlpatterns = [
    path('', HelloWorld.as_view(), name='hello_world'),
]
