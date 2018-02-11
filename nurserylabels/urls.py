from django.conf.urls import include, url

from nurserylabels import views, models



urlpatterns = [
    url('^nursery/labels/$', views.create_nursery_labels, name='create-nursery-labels'),
    url('^nursery/labels/delete/(?P<order_id>\d+)$', views.delete_previous_order, name='delete-previous-order'),
    url('^nursery/labels/print/$', views.print_labels, name='print-nursery-labels'),

    #url('^autocomplete/cultivar/$',
    #    views.CultivarAutocomplete.as_view(model=models.Cultivar, create_field='name', ),
    #    name='cultivar-autocomplete'),
]
