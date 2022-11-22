from django.shortcuts import render
from .rcsv import *


# Create your views here.
# rows = []
# file = with open('Cars.csv','r') as csvfile:
# 	csvreader = csv.reader('csvfile')
# 	rows = list(csvreader)

def index(request):
	return render(request, 'index.html', {'rows':rows})