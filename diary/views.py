from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def write(request):
    if request.method == 'GET':
        #print(request.method)
        return render(request, 'write.html')
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        tags = request.POST.getlist('tags')
        pessoas = request.POST.getlist('pessoas')
        texto = request.POST.get('texto')
        return HttpResponse(f'{titulo} - {tags} - {pessoas}, - {texto}')
