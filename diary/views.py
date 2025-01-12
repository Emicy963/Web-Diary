from django.shortcuts import render, redirect
from .models import People, Diary
from datetime import datetime, timedelta
from django.http import HttpResponse

def home(request):
    texts = Diary.objects.all().order_by('create_at')[:3]
    return render(request, 'home.html', {'texts': texts})

def write(request):
    if request.method == 'GET':
        peoples = People.objects.all()

        return render(request, 'write.html', {'peoples': peoples})
    elif request.method == 'POST':
        title = request.POST.get('titulo')
        tags = request.POST.getlist('tags')
        peoples = request.POST.getlist('pessoas')
        text = request.POST.get('texto')

        #if len(title.strip()) == 0 or len(text.strip()):
        #   """Adicionar Mensagens de Erro"""
        #    return redirect('write')
        
        diary = Diary(
            title=title,
            text=text
        )
        diary.set_tags(tags)
        diary.save()

        for i in peoples:
            people = People.objects.get(id=i)
            diary.people.add(people)
        
        diary.save()

        return HttpResponse(f'{title} - {tags} - {peoples}, - {text}')
    
def create_people(request):
    if request.method == 'GET':
        return render(request, 'people.html')
    elif request.method == 'POST':
        name = request.POST.get('nome')
        picture = request.FILES.get('foto')

        people = People(
            name=name,
            picture=picture
        )
        people.save()
        return redirect('write')

def day(request):
    date = request.GET.get('data')
    format_date = datetime.strptime(date, '%Y-%m-%d')
    diarys = Diary.objects.filter(create_at__gte=format_date).filter(create_at__lte=format_date + timedelta(days=1))
    return render(request, 'day.html', {'diarys': diarys, 'total': diarys.count(), 'data': date})

def delete_day(request):
    day = datetime.strptime(request.GET.get('data'), '%Y-%m-%d')
    diarys = Diary.objects.filter(create_at__gte=day).filter(create_at__lte=day + timedelta(days=1))
    diarys.delete()
    return redirect('home')
