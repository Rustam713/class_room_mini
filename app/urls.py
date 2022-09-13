
from django.urls import path, include
from .views import *
from .urls_yask import urlpatterns_yask



urlpatterns = [
    path('main/', index),
    path('api/v1/auth', include('djoser.urls')),
    path("api/v1/auth-token/", include('djoser.urls.authtoken')),
    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('api/v1/student/create/', StudentCreateView.as_view()),
    path('api/v2/teacher/create/', TeacherCreateView.as_view()),
    path('api/v1/student/list/', StudentListView.as_view()),
    path('api/v2/teacher/list/', TeacherListView.as_view()),
    path('api/v1/student/detail/<int:pk>', StudentDetailView.as_view()),
    path('api/v2/teacher/detail/<int:pk>', TeacherDetailView.as_view())
] + urlpatterns_yask