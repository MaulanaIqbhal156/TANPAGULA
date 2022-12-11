from django.shortcuts import render
from .rxml import *
<<<<<<< HEAD

# Create your views here.
def index(request):
	return render(request, 'index.html', {'root':root})
=======


# Create your views here.

def index(request):
	return render(request, 'index.html',)
>>>>>>> 6da9a26cc8b255632672a869af9c36c8d7d3562e
