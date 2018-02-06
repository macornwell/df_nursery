from django.forms.models import ModelForm
from django.forms.widgets import HiddenInput
from django import forms
from django.urls import reverse

from dal.autocomplete import ModelSelect2
from datetimewidget.widgets import DateWidget
from openfruit.taxonomy.models import Species, Cultivar, Genus, FruitingPlant
from openfruit.common.widgets import CustomRelatedFieldWidgetWrapper
from django_geo_db.models import Location



class NurseryLabelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(NurseryLabelForm,self).__init__(*args, **kwargs)
        self.fields['cultivar'].widget = CustomRelatedFieldWidgetWrapper(
                                                ModelSelect2(url='cultivar-autocomplete'),
                                                reverse('admin:taxonomy_cultivar_add') + "?_to_field=cultivar_id&_popup=1",
                                                True)
        self.fields['cultivar'].queryset = Cultivar.objects.all()

    class Media:
        ## media for the FilteredSelectMultiple widget
        css = {
            'all':('admin/' + 'css/widgets.css',),
        }
        # jsi18n is required by the widget
        js = ( 'admin/' + 'js/admin/RelatedObjectLookups.js',)

    class Meta:
        model = FruitingPlant
        fields = [
            'created_by',
            'species',
            'cultivar',
            'location',
            'date_planted',
        ]
        widgets = {
            'created_by': HiddenInput(),
            'species': ModelSelect2(url='species-autocomplete'),
            'cultivar': ModelSelect2(url='cultivar-autocomplete'),
            'location': ModelSelect2(url='location-autocomplete'),
            'date_planted': DateWidget(usel10n=True, bootstrap_version=3),
        }

