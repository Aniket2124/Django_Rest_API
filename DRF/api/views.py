from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
import rest_framework
from api.models import Student
from django.shortcuts import render
from.models import Student
from.serializers import StudentSerializer
# Create your views here.


def student_details(request):
    stu = Student.objects.get(id=1)
    print(stu)
    serializer = StudentSerializer(stu)
    # print(serializer) python data
    # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')
