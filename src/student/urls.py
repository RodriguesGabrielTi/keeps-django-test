from django.urls import path

from student.views.views import StudentViewSet

_list = {'get': 'list',
         'post': 'create'}

_detail = {'get': 'retrieve',
           'put': 'update',
           'patch': 'partial_update',
           'delete': 'destroy'}

urlpatterns = [
    path('', StudentViewSet.as_view(_list), name='students-list'),
    path('<uuid:pk>', StudentViewSet.as_view(_detail), name='students-detail')
]
