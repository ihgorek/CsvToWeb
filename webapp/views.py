from django.shortcuts import render


def index(request):
    return render(request, 'webapp/home.html')


def contact(request):
    return render(request, 'webapp/basic.html', {'content':['Email',
                                                      'test@test.ru']
                                                } )

# Create your views here.
