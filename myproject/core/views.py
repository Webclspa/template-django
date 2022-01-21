from django.shortcuts import render
from .models import Illustration
# Create your views here.

def frontpage(request):
    illustration = Illustration.objects.all
    print(illustration)
    context = {
        'illustration': illustration,
	}
    return render(request, 'frontpage.html', context)
