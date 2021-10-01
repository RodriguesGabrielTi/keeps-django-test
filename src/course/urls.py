from django.urls import path

from course.views.views import CourseViewSet

_list = {'get': 'list',
         'post': 'create'}

_detail = {'get': 'retrieve',
           'put': 'update',
           'patch': 'partial_update',
           'delete': 'destroy'}

urlpatterns = [
    path('', CourseViewSet.as_view(_list), name='courses-list'),
    path('<uuid:pk>', CourseViewSet.as_view(_detail), name='courses-detail')
]
