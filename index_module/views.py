from .import_module import import_from_divar
from django.views.generic import ListView
from .models import Advertise
from django.shortcuts import render


# import schedule
# import time

# schedule.every(10).seconds.do(import_from_divar())


# Create your views here.

flag_first_run_timer = True

def home_page(request):
    global flag_first_run_timer
    # if flag_first_run_timer == True:
    import_from_divar()
    flag_first_run_timer = False
    advertises = Advertise.objects.order_by('-id')[:100]
    return render(request, 'index_module/index.html' , {
        'advertises': advertises
    })


# class HomeView(ListView):
#     template_name = 'index_module/index.html'
#     model = Advertise
#     context_object_name = 'advertises'
#     queryset = Advertise.objects.order_by('-id')[:50]
#     import_from_divar()
#     print('view continue')
