from gym.models import Service
from django.shortcuts import render

from gym.models import Banners

# Create your views here.


def home(request):
    banners = Banners.objects.all()
    services = Service.objects.all()[:3]
    context = {
        "banners": banners,
        "services": services,
    }
    return render(request, "gym/index.html", context)
