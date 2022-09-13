from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# общий класс для учителей и учиников
class AbstractPerson(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    birthday = models.DateField() #2001-12-31
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def fullname(self):
        return f"{self.name} {self.surname} {self.patronymic}"

# объязательный КЛАСС что-бы наследовать
    class Meta:
        abstract = True


class Teacher(AbstractPerson):
    pass

class Student(AbstractPerson):
    pass