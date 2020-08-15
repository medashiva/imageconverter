from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import img2pdf
from PIL import Image
import os
from django.conf import settings

from fpdf import FPDF
pdf = FPDF()
# Create your views here.


def jpgtopdf(request):
        if request.method == 'POST' and request.FILES['file_photo']:
            myfile = request.FILES['file_photo']
            fs = FileSystemStorage()

            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            image = Image.open(settings.MEDIA_ROOT+"/"+filename)
            file_name_only = filename.split('.')[0]
            print(file_name_only)
            pdf_path = (settings.MEDIA_ROOT+"/"+file_name_only+".pdf")

            pdf_bytes = img2pdf.convert(image.filename)
            file = open(pdf_path, "wb")
            file.write(pdf_bytes)
            image.close()
            file.close()
            return render(request,'home.html')
        else:
            return render(request,'home.html')