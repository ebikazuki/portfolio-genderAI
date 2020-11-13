from django.urls import path
from . import views

app_name = 'works'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('genderai/',views.GenderView.as_view(), name='gender'),
    #path('genderai/func/',views.genderai, name='func'),
]

