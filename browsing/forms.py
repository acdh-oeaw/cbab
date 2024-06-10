from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import Accordion, AccordionGroup


class GenericFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(GenericFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.add_input(Submit("Filter", "search"))


class MainListFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(MainListFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        # self.helper.form_tag = False
        self.add_input(Submit("Filter", "Search"))
        self.layout = Layout(
            Accordion(
                AccordionGroup(
                    "Burial search options",
                    "burial_id",
                    "burial_group",
                    "burial_type",
                    "C14_dendro",
                    "absolute_age",
                    "secondary_burial",
                    "displaced",
                    "extraordinary_burial",
                    "construction",
                    "arrangement",
                    "cover",
                    "cover_type",
                    "grave_pit_form",
                    "grave_pit_orientation",
                    "length",
                    "width",
                    "diameter",
                    "height",
                    "filling_objects",
                    "intentionally_deposited",
                    "filling",
                    "post_holes",
                    "surface_identification_mark",
                    "erdgraebchen",
                    "other_features",
                    css_id="burial_search_fields",
                    active=False,
                ),
                AccordionGroup(
                    "Burial site search options",
                    "burial_site__name",
                    "burial_site__alternative_name",
                    "burial_site__location",
                    "burial_site__topography",
                    "burial_site__excavation",
                    "burial_site__distance_to_next_settlement",
                    "burial_site__type_of_burial_site",
                    "burial_site__disturbance",
                    "burial_site__total_graves",
                    "burial_site__dating",
                    "burial_site__absolute_dating",
                    css_id="burial_site_search_options",
                ),
                AccordionGroup(
                    "Urn and Urn Cover related search options",
                    "urn__basic_shape",
                    "urn__urn_type",
                    "urn__variation",
                    "urn__urn_id",
                    "urn__urncover_exists",
                    "urn__urncover__basic_shape",
                    "urn__urncover__upside_down",
                    "urn__urncover__fragment",
                    "urn__urncover__cover_id",
                    css_id="urn_and_urn_cover_search_options",
                ),
                AccordionGroup(
                    "Grave Good search options",
                    "gravegood__name",
                    "gravegood__material",
                    "gravegood__condition",
                    "gravegood__position",
                    "gravegood__amount_countable",
                    css_id="grave_good_search_options",
                ),
                AccordionGroup(
                    "Organic Grave Good search options",
                    "gravegoodother__food",
                    "gravegoodother__other_organic_grave_good",
                    "gravegoodother__position",
                    "gravegoodother__amount_countable",
                    css_id="organic_grave_good_search_options",
                ),
                AccordionGroup(
                    "Anthropology search options",
                    "deadbodyremains__age",
                    "deadbodyremains__gender",
                    "deadbodyremains__temperature",
                    "deadbodyremains__position",
                    "deadbodyremains__weight",
                    "deadbodyremains__pathology",
                    "deadbodyremains__total_weight",
                    "deadbodyremains__amount_countable",
                    css_id="anthropology_search_options",
                ),
                AccordionGroup(
                    "Animal Remains search options",
                    "animalremains__species",
                    "animalremains__age",
                    "animalremains__sex",
                    "animalremains__weight",
                    "animalremains__position",
                    "animalremains__amount_countable",
                    css_id="animal_remains_search_options",
                ),
                css_id="accordion",
            )
        )
