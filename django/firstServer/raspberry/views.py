from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Create your views here.
def index(request):
    return HttpResponse("hello")

@csrf_exempt    
def upload_file(request):
    if request.method == 'POST':
        data = request.FILES['content'] # or self.files['image'] in your form
        path = default_storage.save('saved.jpg', ContentFile(data.read()))
        return HttpResponse("upload_file fin")

    