import os.path

from django.shortcuts import render, HttpResponse, redirect
from .forms import UserInfoForm, UserInfo_Msg_form, ImgFileForm, UserBaseInfoModelForm
from .models import ImgFile


# Create your views here.
def upload_file(request):
    if request.method == 'GET':
        return render(request, '5/upload.html')
    if request.method == 'POST':
        # 获取上传的文件。如果没有文件，则默认为None
        myfile = request.FILES.get('myfile', None)
        if myfile:
            path = 'media/uploads'
            if not os.path.exists(path):
                os.makedirs(path)
            dest = open(os.path.join(path, myfile.name), 'wb+')
            for chunk in myfile.chunks():
                dest.write(chunk)
            dest.close()
            return HttpResponse('上传完成！')
        else:
            return HttpResponse('没有上传文件!')


def userinfo_form(request):
    """
    <form method="Post">
  <input type="hidden" name="csrfmiddlewaretoken" value="17RxpPdGh2Jwice4MTFHQgAgRPw6zmLZx8Kp1nCPYXpxmQBDb8EoNsOeChajV5Uz">
  <p>
    <label for="id_username">用户名称:</label>
    <input type="text" name="username" class="form-control" placeholder="请输入用户名称" minlength="6" required id="id_username">
</p>
 <p>
    <label for="id_password">密码:</label>
    <input type="password" name="password" class="password" maxlength="10" minlength="6" required id="id_password">
</p>
<p>
    <label for="id_age">年龄:</label>
    <input type="number" name="age" value="1" required id="id_age">
</p>
 <p>
    <label for="id_mobile">手机号码:</label>
    <input type="text" name="mobile" required id="id_mobile">
 </p>
<p>
    <label for="id_status">用户状态:</label>
    <select name="status" required id="id_status">
  <option value="" selected>请选择</option>

  <option value="1">正常</option>

  <option value="2">无效</option>

</select>
 </p>
 <p>
    <label for="id_createdate">创建时间:</label>
    <input type="text" name="createdate" id="id_createdate">
</p>
  <input type = 'submit' value="提交">
</form>
    """
    if request.method == 'GET':
        myform = UserInfoForm()
        print(type(myform))
        # <class 'app5.forms.UserInfoForm'>
        return render(request, '5/userinfo.html', {'form_obj': myform})


def userinfo_msg_form(request):
    if request.method == "GET":
        myform = UserInfo_Msg_form()
        return render(request, '5/userinfoform.html', {'form_obj': myform})
    if request.method == "POST":
        f = UserInfo_Msg_form(request.POST)
        if f.is_valid():
            # print(f.clean())
            # {'username': '11111111',
            # 'password': '11111111',
            # 'age': 111111, 'mobile': '11111111', 'status': '1', 'createdate': None}

            print(f.cleaned_data.get('username'))
            print(f.data)
        else:
            errors = f.errors
            print(errors)
            return render(request, '5/userinfoform.html', {'form_obj': f, 'errors': errors})

        return render(request, '5/userinfoform.html', {'form_obj': f})


def imgfileform(request):
    if request.method == 'GET':
        f = ImgFileForm()
        return render(request, '5/upload_form.html', {'form_obj': f})
    else:
        f = ImgFileForm(data=request.POST, files=request.FILES)
        if f.is_valid():
            # print(f.clean())
            # {'name': '222', 'headimg': <InMemoryUploadedFile: 13315028795322919.png (image/png)>}
            name = f.cleaned_data['name']
            headimg = f.cleaned_data['headimg']
            # print(type(headimg)) #<class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
            userimg = ImgFile(name=name, headimg=headimg)
            # print(userimg)
            # userimg.name = name
            # userimg.heading = headimg
            userimg.save()
            # print(type(userimg)) #<class 'app5.models.ImgFile'>
            print('上传成功')
            return render(request, '5/upload_form.html', {"form_obj": f, 'user': userimg})


def user_add(request):
    if request.method == "GET":
        form = UserBaseInfoModelForm()
        # print(type(form))
        # for item in form:
        #     print(item)
        #     print(type(item))
        context = {
            'form': form
        }
        return render(request, 'user_add.html', context)
    form = UserBaseInfoModelForm(data=request.POST)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect('/user/list')
    return render(request, 'user_add.html', context)
