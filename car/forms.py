from django import forms
from .models import CarModel,UserComment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'
        
        
        
        
class  RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'required'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'required'}))
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None
            
            
class UserChangeData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None

class CommentForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = ['name','email','commentText']
            

            
        


