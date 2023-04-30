from django import forms
from .models import    log , Review



class logf(forms.ModelForm):
    class Meta:
        model = log
        fields = ['user','password']
        widgets = {
            'user' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}    , render_value=True)
        }




class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer_name', 'product_or_service', 'rating', 'review_content']