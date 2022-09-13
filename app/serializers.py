from rest_framework import serializers
from .models import Student, Teacher

class StudentSerilizer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentDetailSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
