from django.contrib import admin
from lung_classifier.models import CovidModel, LungCancerCtModel, LungCancerModel

# Register your models here.
admin.site.register(CovidModel)
admin.site.register(LungCancerCtModel)
admin.site.register(LungCancerModel)