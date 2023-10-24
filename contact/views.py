from django.shortcuts import render,HttpResponse  
from .models import contact as cn
# Create your views here.
def home(request):
    return render(request,"contact/index.html") 

def contact(request):
    n=request.GET.get("nam")
    e=request.GET.get("email")
    o=request.GET.get("onvan")
    m=request.GET.get("matn")
    if(n!=None): 
      cn.objects.create(nam=n,email=e,onvan=o,matn=m)
      return HttpResponse("اطلاعات شما ثبت گردید") 
    return render(request,"contact/contact.html") 

