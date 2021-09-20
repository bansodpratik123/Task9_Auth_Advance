from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DocumentForm,LaptopModelForm

from .models import Documents, Laptops

# Create your views here.
def homepageView(request):
    return render(request, 'Product/Homepage.html', {})

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'Product/FileUpload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'Product/FileUpload.html')

def addLaptopView(request):
    form=LaptopModelForm()
    if request.method=='POST':
        form=LaptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showlaptop')
    template_name='Product/AddLaptopForm.html'
    context={'form':form}
    return render(request, template_name, context)

def showLaptopView(request):
    print('in showlaptop')
    records=Laptops.objects.all()
    for record in records:
        n=record.id
        print(n)

    image=Documents.objects.filter(ModelName=n)
    print(image)
    template_name='Product/ShowLaptop.html'
    context={'records':records,'image':image}
    return render(request, template_name, context)

def DocumentsModelUpload(request):
    if request.method == 'POST':
        print('before request.files')
        form=DocumentForm(request.POST, request.FILES)
        print('before valid')
        if form.is_valid():
            print('before save')
            form.save()
            print('saved')
            return redirect('showfiles')
    else:
        form=DocumentForm()
    return render(request, 'Product/FileUpload.html', {'form':form})

def gallery(request):
    img = Documents.objects.all()
    print(img)

    return render(request,'Product/ShowFiles.html',{"img":img})
    # return render(request,'Product/ShowFiles.html',{"img":img, 'media_url':settings.MEDIA_URL})