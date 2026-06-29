from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def certificate_list(request):
    return render(request, "certificates/certificate_list.html")

def issue_certificate(request, student_id):
    return render(request, "certificates/issue_certificate.html")