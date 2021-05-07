from django.shortcuts import render
from django.http import HttpResponse
from finalproj.models import Coursedetails
from finalproj.models import Studentdetails
from finalproj.models import Enrollment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db import connection

# Create your views here.

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

@login_required
def dashboard(request):
    cursorobj = connection.cursor()
    cursorob = connection.cursor()
    coursecount = connection.cursor()
    freshcount= connection.cursor()
    sophcount= connection.cursor()
    junicount= connection.cursor()
    senicount= connection.cursor()
    cursorobj.execute("SELECT ROUND(AVG(gpa),2) as 'Average GPA' From finalproj_studentdetails;")
    cursorob.execute("SELECT COUNT(studentid) as 'Total Number of Students' From finalproj_studentdetails;")
    coursecount.execute("SELECT COUNT(coursetitle) FROM final_443.finalproj_coursedetails;")
    freshcount.execute("SELECT COUNT(year) from finalproj_studentdetails where year = 'Freshman';")
    sophcount.execute("SELECT COUNT(year) from finalproj_studentdetails where year = 'Sophomore';")
    junicount.execute("SELECT COUNT(year) from finalproj_studentdetails where year = 'Junior';")
    senicount.execute("SELECT COUNT(year) from finalproj_studentdetails where year = 'Senior';")
    dashdata = cursorobj.fetchone()
    boarddata = cursorob.fetchone()
    coursedata = coursecount.fetchone()
    freshdata = freshcount.fetchone()
    sophdata = sophcount.fetchone()
    junidata = junicount.fetchone()
    senidata = senicount.fetchone()
    print(dashdata)
    context = {'data': dashdata[0], 'count':boarddata[0], 'course':coursedata[0], 'fresh':freshdata[0], 'soph': sophdata[0], 'juni': junidata[0], 'seni': senidata[0]}
    return render(request, 'finalproj/dashboard.html', context)

@login_required
def login(request):
    context = {'name':'Dominick'}
    return render(request, 'finalproj/login.html', context)

@login_required
def students(request):
    studentdata = Studentdetails.objects.all()
    paginator = Paginator(studentdata, 10)
    page = request.GET.get('page')
    minidata = paginator.get_page(page)
    context = {'data':minidata}
    return render(request, 'finalproj/student.html', context)

@login_required
def enrollment(request):
    coursedata = Coursedetails.objects.all()
    studentdata = Studentdetails.objects.all()
    enrolldata = Enrollment.objects.all()
    context = {'course':coursedata, 'student':studentdata, 'enroll':enrolldata}
    return render(request, 'finalproj/enrollment.html', context)

@login_required
def course(request):
    coursedata = Coursedetails.objects.all()
    paginator = Paginator(coursedata, 10)
    page = request.GET.get('page')
    minidata = paginator.get_page(page)
    context = {'data':minidata}
    return render(request, 'finalproj/course.html', context)

def saveenroll(request):
    if('sid' and 'cname' in request.GET):
        studentid = request.GET.get('sid')
        courseid = request.GET.get('cname')
        #This checks for a student being double enrolled
        courseCheck = connection.cursor()
        courseCheck.execute("select studentname from finalproj_enrollment where coursename = '"+courseid+"';")
        courseCheckData = courseCheck.fetchall()
        courseArray = [i[0] for i in courseCheckData]
        print(courseArray)
        courseCount = courseArray.count(studentid)
        print(courseCount)

        #this checks for a student being in more than 3 classes
        studCheck = connection.cursor()
        studCheck.execute("select studentname from finalproj_enrollment where studentname = '"+studentid+"';")
        studCheckData = studCheck.fetchall()
        studArray = [i[0] for i in studCheckData]
        print(studArray)
        studCount = studArray.count(studentid)
        if(courseCount == 0 and studCount < 3):
            dataobj = Enrollment(studentname= studentid, coursename = courseid)
            dataobj.save()
        else:
            print('ERROR: Cant enroll student')
    return HttpResponse("Success")