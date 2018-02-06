from django.shortcuts import render
from django.conf import settings

# Create your views here.


def create_nursery_labels(request):
    data = {
        'settings': settings,
    }


    if request.method == 'GET':
        return render(request, 'nurserylabels/create-nursery-labels.html', context=data)
    return None

class CultivarAutocomplete:
    pass
