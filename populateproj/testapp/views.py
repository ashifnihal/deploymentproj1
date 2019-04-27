from django.shortcuts import render
from testapp.models import CarDataModel
def car_display_view(request):
    cdata=CarDataModel.objects.all()
    sdata={'cdata':cdata}
    return render(request,'testapp/home.html',context=sdata)

# Create your views here.
