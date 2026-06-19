from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ContactForm
from .models import Student


def require_login(request):
     if not request.session.get('username'):
          return redirect('/login/')
     return None

def homepageview(request):
     login_redirect = require_login(request)
     if login_redirect:
          return login_redirect

     username = request.session.get('username')
     return render(request, 'home.html', {'username': username})

def aboutusview(request):
     login_redirect = require_login(request)
     if login_redirect:
          return login_redirect

     return render(request, 'about.html')

def contactusview(request):
     login_redirect = require_login(request)
     if login_redirect:
          return login_redirect

     form = ContactForm()
     message_sent = False
     error = None

     if request.method == 'POST':
          form = ContactForm(request.POST)
          if form.is_valid():
               name = form.cleaned_data['name']
               email = form.cleaned_data['email']
               subject = form.cleaned_data['subject']
               message = form.cleaned_data['message']

               full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

               send_mail(
                    subject=subject,
                    message=full_message,
                    from_email=None,
                    recipient_list=['admin@example.com'],
                    fail_silently=False,
               )
               message_sent = True
               form = ContactForm()
          else:
               error = 'Please correct the errors below.'

     return render(request, 'contact.html', {
          'form': form,
          'message_sent': message_sent,
          'error': error,
     })

def formview(request):
     login_redirect = require_login(request)
     if login_redirect:
          return login_redirect

     result = None
     error = None

     if request.method == 'POST':
          first_value = request.POST.get('first_value', '').strip()
          second_value = request.POST.get('second_value', '').strip()

          print('Form submitted:')
          print('First value:', first_value)
          print('Second value:', second_value)

          try:
               number_one = float(first_value)
               number_two = float(second_value)
               result = number_one + number_two
               print('Sum:', result)
          except ValueError:
               error = 'Please enter valid numbers in both fields.'

     context = {
          'result': result,
          'error': error,
     }
     return render(request, 'form.html', context)

def loginpageview(request):
     if request.method == 'POST':
          email = request.POST.get('email', '').strip()

          if email:
               username = email.split('@', 1)[0]
               request.session['username'] = username
               return redirect('/')

     return render(request, 'loginpage.html')

def logoutview(request):
     request.session.pop('username', None)
     return redirect('/login/')

def storeview(request):
     login_redirect = require_login(request)
     if login_redirect:
          return login_redirect

     return render(request, 'store.html')


def addstudentform(request):
     login_redirect = require_login(request)
     if login_redirect:
          return login_redirect

     return render(request, 'add-student.html')


def addstudentformprocess(request):
     login_redirect = require_login(request)
     if login_redirect:
          return login_redirect

     if request.method != 'POST':
          return redirect('/add-student/')

     txt1 = request.POST.get('txt1', '').strip()
     txt2 = request.POST.get('txt2', '').strip()
     txt3 = request.POST.get('txt3', '').strip()
     txt4 = request.POST.get('txt4', '').strip()

     Student.objects.create(name=txt1, mobile=txt2, email=txt3, address=txt4)
     return redirect('/students/')


def student_list(request):
     login_redirect = require_login(request)
     if login_redirect:
          return login_redirect

     students = Student.objects.all().order_by('id')
     return render(request, 'students-list.html', {'students': students})


def student_create(request):
     login_redirect = require_login(request)
     if login_redirect:
          return login_redirect

     if request.method == 'POST':
          name = request.POST.get('name', '').strip()
          mobile = request.POST.get('mobile', '').strip()
          email = request.POST.get('email', '').strip()
          address = request.POST.get('address', '').strip()

          if name and mobile and email and address:
               Student.objects.create(name=name, mobile=mobile, email=email, address=address)
               return redirect('/students/')

          return render(request, 'student-form.html', {
               'title': 'Add Student',
               'student': {'name': name, 'mobile': mobile, 'email': email, 'address': address},
               'error': 'All fields are required.',
          })

     return render(request, 'student-form.html', {'title': 'Add Student'})


def student_update(request, student_id):
     login_redirect = require_login(request)
     if login_redirect:
          return login_redirect

     student = get_object_or_404(Student, id=student_id)

     if request.method == 'POST':
          name = request.POST.get('name', '').strip()
          mobile = request.POST.get('mobile', '').strip()
          email = request.POST.get('email', '').strip()
          address = request.POST.get('address', '').strip()

          if name and mobile and email and address:
               student.name = name
               student.mobile = mobile
               student.email = email
               student.address = address
               student.save()
               return redirect('/students/')

          return render(request, 'student-form.html', {
               'title': 'Edit Student',
               'student': student,
               'error': 'All fields are required.',
          })

     return render(request, 'student-form.html', {'title': 'Edit Student', 'student': student})


def student_delete(request, student_id):
     login_redirect = require_login(request)
     if login_redirect:
          return login_redirect

     student = get_object_or_404(Student, id=student_id)

     if request.method == 'POST':
          student.delete()
          return redirect('/students/')

     return render(request, 'student-delete.html', {'student': student})


def savesessiondata(request):
     login_redirect = require_login(request)
     if login_redirect:
          return login_redirect

     request.session['username'] = 'soham'
     return HttpResponse('session data saved')
def getsessiondata(request):
     login_redirect = require_login(request)
     if login_redirect:
          return login_redirect

     if request.session.get('username'):
          username = request.session['username']
          return HttpResponse(username)
     else:          
          return HttpResponse('no session data found')

def deletesessiondata(request):
     login_redirect = require_login(request)
     if login_redirect:
          return login_redirect

     request.session.pop('username', None)
     return HttpResponse('session data deleted')
def getsessiondata2(request):
     login_redirect = require_login(request)
     if login_redirect:
          return login_redirect

     username = request.session.get('username', 'no session data found')
     return HttpResponse(username)

     
          
     
