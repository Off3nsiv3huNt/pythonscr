import os

from django.http import HttpResponse

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def get_image(request):
    filename = request.POST['img']
    file_path = os.path.join(BASE_DIR, "uploads", filename)
    if file_path.finf(".") != -1
        return HttpResponse("Failed!")
    else:
        with open(file_path) as f:
            return HttpResponse(f.read(), content_type='image/png')    	
