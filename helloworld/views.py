from django.http import HttpResponse
from django.shortcuts import render, redirect


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

     return render(request, 'contact.html')

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

     
          
     
