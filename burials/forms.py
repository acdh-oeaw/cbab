from dal import autocomplete
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *


class BurialSiteForm(forms.ModelForm):

    class Meta:
        model = BurialSite
        fields = "__all__"
        widgets = {
            'location': autocomplete.ModelSelect2(
                url='burials:place-autocomplete'),
            'geographical_coordinate_reference_system': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=geographicalreferencesystem'),
            'topography': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Topography'),
            'distance_to_next_settlement': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Distance to next settlement'),
            'type_of_burial_site': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Type of burial site'),
            'dating': autocomplete.ModelSelect2Multiple(
                url='../../skos-constraint-ac/?scheme=Dating'),
            'absolute_dating': autocomplete.ModelSelect2Multiple(
                url='vocabs-ac:skosconcept-autocomplete'),     # absolute dating has no list so far - 'List of all data from the row 107'
            'reference': autocomplete.ModelSelect2Multiple(
                url='burials:book-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(BurialSiteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class BurialGroupForm(forms.ModelForm):

    class Meta:
        model = BurialGroup
        fields = "__all__"
        widgets = {
            'burial_site': autocomplete.ModelSelect2(
                url='burials:burialsite-autocomplete'),
            'burial_group_type': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Burial group type'),
            'material': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Material'),
        }

    def __init__(self, *args, **kwargs):
        super(BurialGroupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class BurialForm(forms.ModelForm):

    class Meta:
        model = Burial
        fields = "__all__"
        widgets = {
            'burial_group': autocomplete.ModelSelect2(
                url='burials:burialgroup-autocomplete'),
            'burial_site': autocomplete.ModelSelect2(
                url='burials:burialsite-autocomplete'),
            'burial_type': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Burial type'),
            'construction': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Burial construction'),
            'arrangement': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Burial arrangement'),
            'cover_type': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Cover type'),
            'grave_pit_form': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Grave pit form'),
            'grave_pit_orientation': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Grave pit orientation'),
        }

    def __init__(self, *args, **kwargs):
        super(BurialForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class UrnCoverForm(forms.ModelForm):

    class Meta:
        model = UrnCover
        fields = "__all__"
        widgets = {
            'basic_shape': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Basic shape of urn cover'),
        }

    def __init__(self, *args, **kwargs):
        super(UrnCoverForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class UrnForm(forms.ModelForm):

    class Meta:
        model = Urn
        fields = "__all__"
        widgets = {
            'burial': autocomplete.ModelSelect2(
                url='burials:burial-autocomplete'),
            'basic_shape': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Basic shape of urn'),
            'cover': autocomplete.ModelSelect2(
                url='burials:urncover-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(UrnForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class GraveGoodForm(forms.ModelForm):

    class Meta:
        model = GraveGood
        fields = "__all__"
        widgets = {
            'burial': autocomplete.ModelSelect2(
                url='burials:burial-autocomplete'),
            'name': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Grave good name'),
            'material': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Material'),
            'condition': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Condition'),
            'position': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Position'),
        }

    def __init__(self, *args, **kwargs):
        super(GraveGoodForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class GraveGoodOtherForm(forms.ModelForm):

    class Meta:
        model = GraveGoodOther
        fields = "__all__"
        widgets = {
            'burial': autocomplete.ModelSelect2(
                url='burials:burial-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(GraveGoodOtherForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class DeadBodyRemainsForm(forms.ModelForm):

    class Meta:
        model = DeadBodyRemains
        fields = "__all__"
        widgets = {
            'burial': autocomplete.ModelSelect2(
                url='burials:burial-autocomplete'),
            'age': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Age'),
            'gender': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Gender'),
            'temperature': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Cremation temperature'),
        }

    def __init__(self, *args, **kwargs):
        super(DeadBodyRemainsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)
