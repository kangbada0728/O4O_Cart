from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from raspberry.detectQR import *
# Create your views here.
def index(request):
    return HttpResponse("hello")

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        print(request)
        data = request.FILES['content'] # or self.files['image'] in your form
        name = request.GET['image_name']
        #print(name)
        path = default_storage.save(name, ContentFile(data.read()))
        detectQR(name)
        return HttpResponse("upload_file fin")
