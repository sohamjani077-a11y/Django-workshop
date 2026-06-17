from django.shortcuts import render
from .forms import ContactForm

def homepageview(request):
     return render(request, 'home.html')

def aboutusview(request):
     return render(request, 'about.html')

def contactusview(request):
     if request.method == 'POST':
          form = ContactForm(request.POST)
          if form.is_valid():
               name = form.cleaned_data['name']
               email = form.cleaned_data['email']
               subject = form.cleaned_data['subject']
               message = form.cleaned_data['message']
               
               # Here you can add logic to send email or save to database
               # For now, we'll just pass it to the template
               context = {
                    'form': form,
                    'success': True,
                    'submitted_data': {
                         'name': name,
                         'email': email,
                         'subject': subject,
                         'message': message
                    }
               }
               return render(request, 'contact.html', context)
     else:
          form = ContactForm()
          context = {'form': form}
     
     return render(request, 'contact.html', context)