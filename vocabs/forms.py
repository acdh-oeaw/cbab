from dal import autocomplete
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import SkosConcept, SkosConceptScheme, SkosLabel


class UploadFileForm(forms.Form):
    file = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'import'),)


class SkosConceptForm(forms.ModelForm):
    class Meta:
        model = SkosConcept
        fields = "__all__"
        widgets = {
            'label': autocomplete.ModelSelect2Multiple(url='vocabs:skoslabel-autocomplete'),
            'skos_broader': autocomplete.ModelSelect2Multiple(
                url='vocabs:skosconcept-autocomplete'),
            'skos_narrower': autocomplete.ModelSelect2Multiple(
                url='vocabs:skosconcept-autocomplete'),
            'skos_related': autocomplete.ModelSelect2Multiple(
                url='vocabs:skosconcept-autocomplete'),
            'skos_broadmatch': autocomplete.ModelSelect2Multiple(
                url='vocabs:skosconcept-autocomplete'),
            'skos_exactmatch': autocomplete.ModelSelect2Multiple(
                url='vocabs:skosconcept-autocomplete'),
            'scheme': autocomplete.ModelSelect2Multiple(url='vocabs:skosconceptscheme-autocomplete')
        }

    def __init__(self, *args, **kwargs):
        super(SkosConceptForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class SkosConceptSchemeForm(forms.ModelForm):
    class Meta:
        model = SkosConceptScheme
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SkosConceptSchemeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class SkosLabelForm(forms.ModelForm):
    class Meta:
        model = SkosLabel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SkosLabelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)
