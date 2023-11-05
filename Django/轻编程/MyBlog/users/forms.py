from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=15)
    password = forms.CharField(label='密码', min_length=6, widget=forms.PasswordInput())

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username == password:
            raise forms.ValidationError('密码不能与用户名一样！')
        return password
    
class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='密码', 
                               min_length=6, 
                               widget=forms.PasswordInput(attrs={
                                'class': 'input', 
                                'placeholder': '密码'}))
    password1 = forms.CharField(label='再次密码', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': '再次密码'}))
    class Meta:
        model = User
        fields = ('username', 'password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        exists = User.objects.filter(username=username).exists()
        if exists:
            raise forms.ValidationError("用户名已经存在！")
        return username

    def clean_password1(self):
        data = self.cleaned_data
        password = data['password']
        password1 = data['password1']
        if password != password1:
            raise forms.ValidationError('两次输入的密码不一致，请修改!')
        return password