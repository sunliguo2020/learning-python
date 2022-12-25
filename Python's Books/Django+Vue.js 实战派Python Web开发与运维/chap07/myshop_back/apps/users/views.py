from django.shortcuts import render

from apps.users import forms


# Create your views here.
def user_reg(request):
    if request.method == 'GET':
        form_obj = forms.UserRegForm()
        return render(request, 'shop/user_reg.html', {'form_obj': form_obj})
