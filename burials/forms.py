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
            'geographical_coordinate_reference_system': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Position of the cremated remains'),
            'topography': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Topography'),
            'distance_to_next_settlement': autocomplete.ModelSelect2(
                url='vocabs:skosconcept-autocomplete'),
            'type_of_burial_site': autocomplete.ModelSelect2(
                url='vocabs:skosconcept-autocomplete'),
            'dating': autocomplete.ModelSelect2Multiple(
                url='vocabs:skosconcept-autocomplete'),
            'absolute_dating': autocomplete.ModelSelect2Multiple(
                url='vocabs:skosconcept-autocomplete'),
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
            'burial_group_type': autocomplete.ModelSelect2(
                url='vocabs:skosconcept-autocomplete'),
            'material': autocomplete.ModelSelect2(
                url='vocabs:skosconcept-autocomplete'),
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
            'burial_type': autocomplete.ModelSelect2(
                url='vocabs:skosconcept-autocomplete'),
            'material': autocomplete.ModelSelect2(
                url='vocabs:skosconcept-autocomplete'),
            'construction': autocomplete.ModelSelect2(
                url='vocabs:skosconcept-autocomplete'),
            'arrangement': autocomplete.ModelSelect2(
                url='vocabs:skosconcept-autocomplete'),
            'cover_type': autocomplete.ModelSelect2(
                url='vocabs:skosconcept-autocomplete'),
            'grave_pit_form': autocomplete.ModelSelect2(
                url='vocabs:skosconcept-autocomplete'),
            'grave_pit_orientation': autocomplete.ModelSelect2(
                url='vocabs:skosconcept-autocomplete'),
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

    def __init__(self, *args, **kwargs):
        super(DeadBodyRemainsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)
