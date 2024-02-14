from django.contrib import admin

# Register your models here.
from saveform.models import stdent_data,attendence
class stddataAdmin(admin.ModelAdmin):
    list_display=('name','email','joining_date','course','roll_no','duration')
admin.site.register(stdent_data,stddataAdmin)
class attendenseAdmin(admin.ModelAdmin):
    list_display=('topic','Date','intime','outtime','message')
admin.site.register(attendence,attendenseAdmin)