from pydoc import describe
from django.shortcuts import render,redirect 
from ventasApp.models import FormaPago 
from django.db.models import Q 
from ventasApp.forms import FormaPagoForm
from django.contrib import messages
from django.core.paginator import Paginator
import datetime

def dashboard(request):
    return render(request, "dashboard/dashboard.html")