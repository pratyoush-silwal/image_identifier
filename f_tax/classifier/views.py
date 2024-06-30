# views.py
from django.shortcuts import render, redirect
from .forms import UploadImageForm
from .models import classifier

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form to create a Classifier instance
            instance = form.save()
            # Call save() method of the instance to process the image and classify
            instance.save()
            return redirect('upload_success', instance.id)
    else:
        form = UploadImageForm()
    return render(request, 'upload.html', {'form': form})

def upload_success(request, pk):
    image = classifier.objects.get(pk=pk)
    return render(request, 'upload_success.html', {'image': image})


def index(request):
    return render(request,'index.html')