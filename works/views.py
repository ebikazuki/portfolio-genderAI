from django.shortcuts import render
from django.views import generic
from works.forms import ImgForm
from .models import Sample
from ebikazuki.settings import *
import shutil
import os

class IndexView(generic.TemplateView):
    template_name = "index.html"

class GenderView(generic.FormView):
    template_name = "genderai.html"
    form_class = ImgForm

    def post(self, request, *args, **kwargs):
        form = ImgForm(request.POST)

        #mediaファイルを消す
        shutil.rmtree(MEDIA_ROOT)
        os.mkdir(MEDIA_ROOT)
        sample = Sample()
        sample.img = request.FILES['img']
        sample.save()

        img = request.FILES['img']
        sample_img = sample.img
        from works.gender import gender
        man_value = gender(img)
        if man_value > 0.5 :
            result = "MAN"
        else:
            result = "WOMAN"

        return render(request, self.template_name, {
            'form': self.form_class , 'result': result ,'sample_img': sample_img
        }
                      )






