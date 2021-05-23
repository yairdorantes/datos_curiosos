from django.shortcuts import render,redirect
from .forms import formupost
from .models import Dato
from django.contrib import messages
import random
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def view_dato(request):
    if request.method == 'POST':
        form = formupost(request.POST,request.FILES)
        if form.is_valid():
            datosf = form.save(commit=False)
            datosf.save()
            return redirect('sorted_data')
    form = formupost()
    messages.success(request,f'¡Tu dato se ha enviado con éxito, ya solo falta ser aprovado!')
    return render(request,'Datos/create_data.html',{'form':form})
@csrf_exempt
def sorted(request):

    lista = []
    datos_order = Dato.objects.all().order_by('-id')
    
    for i in datos_order:
        lista.append(i)
    random.shuffle(lista)
    queryset = request.GET.get('buscar')
    
    if queryset:
        lista = Dato.objects.filter(
            Q(id__icontains = queryset) | 
            Q(autor = queryset)
        )
    
    if request.method == 'POST':
        some_var = request.POST.getlist('check')
        if some_var == ['on']:
            
            return render(request, 'Datos/index.html',{'shuffle_data':datos_order})
        elif some_var == '':
            return render(request, 'Datos/index.html',{'shuffle_data':lista})
    return render(request, 'Datos/index.html',{'shuffle_data':lista})
@csrf_exempt
def sorted_two(request):
    lista = []
    datos_order = Dato.objects.all().order_by('-id')
    for i in datos_order:
        lista.append(i)
    random.shuffle(lista)
    queryset = request.GET.get('buscar')
    
    if queryset:
        lista = Dato.objects.filter(
            Q(id__icontains = queryset) | 
            Q(autor = queryset)
        )
    if request.method == 'POST':
        some_var = request.POST.getlist('check')
        if some_var == ['on']:
            
            return render(request, 'Datos/two.html',{'shuffle_data':datos_order})
        elif some_var == '':
            return render(request, 'Datos/two.html',{'shuffle_data':lista})
    return render(request, 'Datos/two.html',{'shuffle_data':lista})

 

def news(request):
    datos_order = Dato.objects.all().order_by('-id')
    return render(request, 'Datos/news.html',{'suffle_data':datos_order})


