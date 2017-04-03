from dal import autocomplete
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
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
            'reference': autocomplete.ModelSelect2Multiple(
                url='burials:book-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(BurialSiteForm, self).__init__(*args, **kwargs)
        self.fields['lng'].required = True
        self.fields['lat'].required = True
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
            # 'burial_site': autocomplete.ModelSelect2(
            #     url='burials:burialsite-autocomplete'),
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
            # 'burial_group': autocomplete.ModelSelect2(
            #     url='burials:burialgroup-autocomplete'),
            # 'burial_site': autocomplete.ModelSelect2(
            #     url='burials:burialsite-autocomplete'),
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
            'filling': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Burial Filling Type'),
        }

    def __init__(self, *args, **kwargs):
        super(BurialForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)
        self.helper.layout = Layout(
            Fieldset(
                'Description',
                'burial_site',
                'burial_group',
                'burial_id',
                'burial_type',
                'C14_dendro',
                'absolute_age',
                'secondary_burial',
                'secondary_burial_text',
                'displaced',
                'displaced_text',
                'extraordinary_burial',
                'extraordinary_burial_text',
                'inhumation_burial_type',
                'bi_ritual_burial_type',
                'filling',
                css_class="separate-panel",
            ),
            Fieldset(
                'Grave architecture',
                'construction',
                'arrangement',
                'cover',
                'cover_type',
                'grave_pit_form',
                'grave_pit_orientation',
                'length',
                'width',
                'diameter',
                'height',
                'post_holes',
                'surface_identification_mark',
                'erdgraebchen',
                'other_features',
                css_class="separate-panel"
            )
        )


# class FillingObjectForm(forms.ModelForm):
#
#     class Meta:
#         model = FillingObject
#         fields = "__all__"
#         widgets = {
#             'filling_objects': autocomplete.ModelSelect2(
#                 url='../../skos-constraint-ac/?scheme=Burial Filling Objects'),
#         }
#
#     def __init__(self, *args, **kwargs):
#         super(FillingObjectForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_tag = True
#         self.helper.form_class = 'form-horizontal'
#         self.helper.label_class = 'col-md-3'
#         self.helper.field_class = 'col-md-9'
#         self.helper.add_input(Submit('submit', 'save'),)


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
            # 'burial': autocomplete.ModelSelect2(
            #     url='burials:burial-autocomplete',
            #     attrs={
            #     'data-placeholder': 'start typing burial number ...',
            #     'data-html': True,
            # },
            # ),
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
        fields = [
            'burial', 'urn', 'name', 'material', 'amount_countable', 'condition', 'position',
            'comment'
        ]
        widgets = {
            # 'burial': autocomplete.ModelSelect2(
            #     url='burials:burial-autocomplete'),
            'name': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=GraveGoodObject'),
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
        fields = [
            'burial', 'urn', 'food', 'other_organic_grave_good',
            'other_organic_grave_good_text', 'position', 'secondary_depostition', 'comment'
        ]
        widgets = {
            # 'burial': autocomplete.ModelSelect2(
            #     url='burials:burial-autocomplete'),
            'position': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Position'),
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
        fields = [
            'burial', 'urn', 'age', 'gender', 'temperature', 'weight', 'pathology', 'total_weight',
            'position', 'amount_countable', 'secondary_depostition', 'comment'
        ]
        widgets = {
            # 'burial': autocomplete.ModelSelect2(
            #     url='burials:burial-autocomplete'),
            'age': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Age'),
            'gender': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Gender'),
            'temperature': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Cremation temperature'),
            'position': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Position of the cremated remains'),
        }

    def __init__(self, *args, **kwargs):
        super(DeadBodyRemainsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class AnimalRemainsForm(forms.ModelForm):

    class Meta:
        model = AnimalRemains
        fields = [
            'burial', 'urn', 'species', 'age', 'sex', 'amount_countable',
            'position', 'secondary_depostition', 'comment'
        ]
        widgets = {
            # 'burial': autocomplete.ModelSelect2(
            #     url='burials:burial-autocomplete'),
            'species': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Species'),
            'position': autocomplete.ModelSelect2(
                url='../../skos-constraint-ac/?scheme=Position of the cremated remains'),
        }

    def __init__(self, *args, **kwargs):
        super(AnimalRemainsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)
