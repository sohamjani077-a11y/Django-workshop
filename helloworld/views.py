from django.shortcuts import render

def homepageview(request):
     return render(request, 'home.html')

def aboutusview(request):
     return render(request, 'about.html')

def contactusview(request):
     return render(request, 'contact.html')

def formview(request):
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

def storeview(request):
     return render(request, 'store.html')
