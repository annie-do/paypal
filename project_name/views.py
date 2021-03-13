from django.shortcuts import render, redirect
## import HttpResponse
from django.http import HttpResponse

def payment(request):
    return render(request, 'templates/payment.html')