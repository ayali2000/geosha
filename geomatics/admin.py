from django.contrib import admin

# Register your models here.
from geomatics.models import *

class AdminAns(admin.ModelAdmin):
    list_display = ['quest','user','ans','date_ans']

class AdminQuest(admin.ModelAdmin):
    list_display = ["user","question","date_ask"]    

admin.site.register(Quest,AdminQuest)
admin.site.register(Ans,AdminAns)
