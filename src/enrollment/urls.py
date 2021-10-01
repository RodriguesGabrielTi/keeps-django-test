from django.urls import path

from enrollment.views import EnrollmentViewSet

_list = {'get': 'list',
         'post': 'create'}

_detail = {'get': 'retrieve',
           'put': 'update',
           'patch': 'partial_update',
           'delete': 'destroy'}

urlpatterns = [
    path('', EnrollmentViewSet.as_view(_list), name='enrollments-list'),
    path('<uuid:pk>', EnrollmentViewSet.as_view(_detail), name='enrollments-detail')
]
