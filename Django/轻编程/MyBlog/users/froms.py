from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=15)
    password = forms.CharField(label='密码', min_length=6, widget=forms.PasswordInput())

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username == password:
            raise forms.ValidationError('密码不能与用户名一样！')
        return password