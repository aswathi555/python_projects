from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import  movie
from.forms import movieform

# Create your views here.
def index(request):
    movies=movie.objects.all()
    context={
        'movielist':movies
    }
    return render(request,"index.html",context)

def details(request,movie_id):
    movies=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movies})

def add_movie(request):
    if request.method=='POST':
        mname=request.POST.get('name')
        mdesc = request.POST.get('desc')
        myear = request.POST.get('year')
        mimg = request.FILES['img']
        movie1=movie(name=mname,desc=mdesc,year=myear,img=mimg)
        movie1.save()

    return  render(request,"add.html")

def update(request,id):
    movie1=movie.objects.get(id=id)
    form=movieform(request.POST or None , request.FILES,instance=movie1)
    if form.is_valid():
        form.save()
        return  redirect('/')
    return  render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie1=movie.objects.get(id=id)
        movie1.delete()
        return redirect('/')
    return render(request,"delete.html")
