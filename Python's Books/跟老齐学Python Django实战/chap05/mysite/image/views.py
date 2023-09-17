from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import ImageForm
from .models import Image


# Create your views here.

@csrf_exempt
@require_POST
def upload_image(request):
    print(request.POST)
    form = ImageForm(data=request.POST)
    # logging.debug(form)
    # print(f"form:{form}")
    if form.is_valid():
        try:
            new_item = form.save(commit=True)
            # print(new_item)
            # new_item.user = request.user
            # new_item.save()
            # print(new_item.image)
            return JsonResponse({'status': "1"})
        except Exception as e:
            # print(e)
            return JsonResponse({'status': 'str(e)'})
    else:
        return JsonResponse({"status": str(form.errors), "error_msg": 'form校验错误'})


def list_images(request):
    images = Image.objects.all()
    return render(request, 'image/list_images.html', {'images': images})
