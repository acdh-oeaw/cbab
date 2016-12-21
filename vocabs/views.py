from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import SkosConcept, SkosConceptScheme, SkosLabel
from .forms import SkosConceptForm, SkosConceptSchemeForm, SkosLabelForm


class SkosConceptDetailView(DetailView):

    model = SkosConcept
    template_name = 'vocabs/skosconcept_detail.html'


class SkosConceptListView(ListView):

    model = SkosConcept
    template_name = 'vocabs/skosconcept_list.html'


class SkosConceptCreate(CreateView):

    model = SkosConcept
    template_name = 'vocabs/skosconcept_create.html'
    form_class = SkosConceptForm


class SkosConceptUpdate(UpdateView):

    model = SkosConcept
    form_class = SkosConceptForm
    template_name = 'vocabs/skosconcept_create.html'


#####################################################
#   ConceptScheme
#####################################################


class SkosConceptSchemeDetailView(DetailView):

    model = SkosConceptScheme
    template_name = 'vocabs/skosconceptscheme_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SkosConceptSchemeDetailView, self).get_context_data(**kwargs)
        context["concepts"] = SkosConcept.objects.filter(scheme=self.kwargs.get('pk'))
        return context


class SkosConceptSchemeListView(ListView):

    model = SkosConceptScheme
    template_name = 'vocabs/skosconceptscheme_list.html'


class SkosConceptSchemeCreate(CreateView):

    model = SkosConceptScheme
    form_class = SkosConceptSchemeForm
    template_name = 'vocabs/skosconceptscheme_create.html'


class SkosConceptSchemeUpdate(UpdateView):

    model = SkosConceptScheme
    form_class = SkosConceptSchemeForm
    template_name = 'vocabs/skosconceptscheme_create.html'


###################################################
# SkosLabel
###################################################


class SkosLabelDetailView(DetailView):

    model = SkosLabel
    template_name = 'vocabs/skoslabel_detail.html'


class SkosLabelListView(ListView):

    model = SkosLabel
    template_name = 'vocabs/skoslabel_list.html'


class SkosLabelCreate(CreateView):

    model = SkosLabel
    template_name = 'vocabs/skoslabel_create.html'
    form_class = SkosLabelForm


class SkosLabelUpdate(UpdateView):

    model = SkosLabel
    form_class = SkosLabelForm
    template_name = 'vocabs/skoslabel_create.html'
