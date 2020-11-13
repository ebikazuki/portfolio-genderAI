from django import forms


#class ImgForm(forms.Form):
    #img = forms.ImageField(label="画像", upload_to="sample/")


from .models import Sample


class ImgForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ('img',)
