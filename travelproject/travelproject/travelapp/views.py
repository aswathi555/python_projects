from django.shortcuts import render
from.models import travel
from.models import guide
from.models import guide1
# Create your views here.
def demo(request):
    obj=travel.objects.all()
    obj1=guide.objects.all()
    # obj2 = guide1.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})