from django.shortcuts import render
import os 
from django.conf import settings

# Create your views here.
def demo_view(request):
    return render(request,'home.html')
def upload_view(request):
    # print("Saving to:", os.path.join(settings.MEDIA_ROOT, myfile.name))
    if request.method == 'POST' and request.FILES.get('myfiles'):
        print("File uploading..")
        myfile = request.FILES['myfiles']
        print(myfile.name)
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
        file_path = os.path.join(settings.MEDIA_ROOT, myfile.name)
        with open(file_path, 'wb+') as f:
            for chunk in myfile.chunks():
                f.write(chunk)
        print("File uploaded successfully")
    else:
        print("No file uploaded")
    return render(request, 'home.html')