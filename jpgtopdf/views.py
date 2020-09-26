from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import img2pdf
from PIL import Image
import os
from django.conf import settings
from datetime import datetime
import time
from fpdf import FPDF
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound

pdf = FPDF()
# Create your views here.


def jpgtopdf(request):
        if request.method == 'POST' and request.FILES['file_photo']:
            myfile = request.FILES['file_photo']
            fs = FileSystemStorage()

            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            image = Image.open(settings.MEDIA_ROOT+"/"+filename)
            file_name_only = str(time.strftime("%Y%m%d-%H%M%S"))+filename.split('.')[0].replace(" ", "")
            print(file_name_only)
            pdf_path = (settings.MEDIA_ROOT+"/"+file_name_only+".pdf")
            print("new line for new branch")
            print("one more branch")
            pdf_bytes = img2pdf.convert(image.filename)
            file = open(pdf_path, "wb")
            file.write(pdf_bytes)
            image.close()
            file.close()
            fs = FileSystemStorage()
            filename = pdf_path
            if fs.exists(filename):
                with fs.open(filename) as pdf:
                    response = HttpResponse(pdf, content_type='application/pdf')
                    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
                    return response
            else:
                return HttpResponseNotFound('The requested pdf was not found in our server.')
            return render(request,'home.html')
        else:
            return render(request,'home.html')

