from django import forms
from .models import Dato
class formupost(forms.ModelForm):
    class Meta:
        model = Dato
        fields = ('autor','contenido','imagen')
    '''
    def clean_picture(self):
       picture = self.cleaned_data.get("imagen")
       if not picture:
           raise forms.ValidationError("No image!")
       else:
           w, h = get_image_dimensions(picture)
           if w < 1500:
               raise forms.ValidationError("The image is %i pixel wide. It's supposed to be 100px" % w)
           if h < 2160:
               raise forms.ValidationError("The image is %i pixel high. It's supposed to be 200px" % h)
       return picture
       '''
       