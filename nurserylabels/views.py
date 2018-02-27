import json
import io
import os

from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.utils.safestring import mark_safe

from mezzanine.conf import settings as mez_settings

from nurserylabels.models import CultivarLabel
from nurserylabels.utils import generate_nursery_front_label_csv
from nurserylabels.services import NURSERY_LABEL_DAL

# Create your views here.


def delete_previous_order(request, order_id):
    if order_id:
        NURSERY_LABEL_DAL.delete_previous_labor_order(order_id)
    return redirect('create-nursery-labels')


def create_nursery_labels(request):
    previous_orders_data = {}
    previous_orders = NURSERY_LABEL_DAL.get_previous_label_orders(request.user)
    for obj in previous_orders:
        previous_orders_data[obj] = [mark_safe(item) for item in obj.data.split('&&&')]
    data = {
        'OF_API_USERNAME': settings.OF_API_USERNAME,
        'OF_API_PASSWORD': settings.OF_API_PASSWORD,
        'settings': settings,
        'previous_orders': previous_orders_data,
    }

    return render(request, 'nurserylabels/create-nursery-labels.html', context=data)


def print_labels(request):
    data_list = []
    obj_for_saving = []
    for key in request.POST:
        value = request.POST[key]
        if not key.startswith('cultivar'):
            continue
        value = value.replace('&&&', '\'')
        obj_for_saving.append(value)
        cultivar = json.loads(value)
        label = CultivarLabel()
        for i in range(int(cultivar['count'])):
            label.name = cultivar['name']
            label.species = cultivar['species']
            label.ripens = cultivar['ripens_early']
            data_list.append(label)
    if mez_settings.NURSERY_FRONT_LABEL_PATH:
        if not mez_settings.NURSERY_BACK_LABEL_PATH:
            response = HttpResponse(status=500)
        else:
            front_path = mez_settings.NURSERY_FRONT_LABEL_PATH
            back_path = mez_settings.NURSERY_BACK_LABEL_PATH
            if not os.path.exists(os.path.dirname(front_path)):
                os.makedirs(os.path.dirname(front_path))
            if not os.path.exists(os.path.dirname(back_path)):
                os.makedirs(os.path.dirname(back_path))
            with open(mez_settings.NURSERY_FRONT_LABEL_PATH, 'w') as outFile:
                generate_nursery_front_label_csv(outFile, data_list)
            with open(mez_settings.NURSERY_BACK_LABEL_PATH, 'w') as outFile:
                generate_nursery_front_label_csv(outFile, data_list)
            response = redirect('create-nursery-labels')
    else:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="front-labels.csv"'
        generate_nursery_front_label_csv(response, data_list)
    if obj_for_saving:
        concat = ''
        for obj in obj_for_saving:
            concat += obj
            concat += '&&&'
        if concat:  # Remove the last few &&&
            concat = concat[0:-3]
        NURSERY_LABEL_DAL.create_previous_label_order(request.user, concat)
    return response

