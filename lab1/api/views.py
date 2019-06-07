import datetime

from django.http import HttpResponse

# Create your views here.
from api.models import Student


def index(request):
    return HttpResponse('<h1> Index works <h1>')


def time(request):
    return HttpResponse('<h1>{0}<h1>'.format(datetime.datetime.now()))


def multiply(request, a, b):
    return HttpResponse('<h1>{0}<h1>'.format(a * b))


def student_detail(request, id):
    #create
    #save
    #filter
    #get
    student = Student.objects.filter(id=id)

    return HttpResponse('<h1> {0} <h1>'.format(student.name))


def students(request):
    students = Student.objects.all()
    str = ''
    for student in students:
        str += '<p> {0} {1}<p>'.format(student.name, student.gpa)
    return HttpResponse(str)


def student_filter(request, name):
    print(name)
    students = Student.objects.filter(name=name)
    str = ''
    for student in students:
        str += '<p> {0} {1}<p>'.format(student.name, student.gpa)
    return HttpResponse(str)
