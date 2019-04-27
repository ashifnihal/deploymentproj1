from django.contrib import admin
from testapp.models import CarDataModel
class CarAdmin(admin.ModelAdmin):
    list_display=['id','sno','brand','model','fuel','year','cc','mobileno']
admin.site.register(CarDataModel,CarAdmin)


# Register your models here.
