from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Student, Teacher
from .permissions import IsIfOwner
from rest_framework.permissions import IsAuthenticated, IsAdminUser


def index(request):
    return render(request, template_name='app/index.html')


class StudentCreateView(generics.CreateAPIView):
    serializer_class = StudentSerilizer
    permission_classes = [IsAdminUser, ]


class TeacherCreateView(generics.CreateAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminUser, ]


class StudentListView(generics.ListAPIView):
    serializer_class = StudentSerilizer
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated, ]

class TeacherListView(generics.ListAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = [IsAuthenticated, ]


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentDetailSerilizer
    queryset = Student.objects.all()
    permission_classes = [IsIfOwner, IsAuthenticated]

class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherDetailSerializer
    queryset = Teacher.objects.all()
    permission_classes = [IsIfOwner, IsAuthenticated]