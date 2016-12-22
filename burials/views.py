from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import *
from .forms import *

# Create your views here.


###BurialSite
class BurialSiteDetailView(DetailView):
    model = BurialSite
    template_name = 'burials/burialsite_detail.html'


class BurialSiteListView(ListView):
    model = BurialSite
    template_name = 'burials/burialsite_list.html'


class BurialSiteCreate(CreateView):
    model = BurialSite
    template_name = 'burials/burialsite_create.html'
    form_class = BurialSiteForm


class BurialSiteUpdate(UpdateView):
    model = BurialSite
    form_class = BurialSiteForm
    template_name = 'burials/burialsite_create.html'

###BurialGroup
class BurialGroupDetailView(DetailView):
    model = BurialGroup
    template_name = 'burials/burialgroup_detail.html'


class BurialGroupListView(ListView):
    model = BurialGroup
    template_name = 'burials/burialgroup_list.html'


class BurialGroupCreate(CreateView):
    model = BurialGroup
    template_name = 'burials/burialgroup_create.html'
    form_class = BurialGroupForm


class BurialGroupUpdate(UpdateView):
    model = BurialGroup
    form_class = BurialGroupForm
    template_name = 'burials/burialgroup_create.html'

#Burial
class BurialDetailView(DetailView):
    model = Burial
    template_name = 'burials/burial_detail.html'


class BurialListView(ListView):
    model = Burial
    template_name = 'burials/burial_list.html'


class BurialCreate(CreateView):
    model = Burial
    template_name = 'burials/burial_create.html'
    form_class = BurialForm


class BurialUpdate(UpdateView):
    model = Burial
    form_class = BurialForm
    template_name = 'burials/burial_create.html'

#UrnCover
class UrnCoverDetailView(DetailView):
    model = UrnCover
    template_name = 'burials/urncover_detail.html'


class UrnCoverListView(ListView):
    model = UrnCover
    template_name = 'burials/urncover_list.html'


class UrnCoverCreate(CreateView):
    model = UrnCover
    template_name = 'burials/urncover_create.html'
    form_class = UrnCoverForm


class UrnCoverUpdate(UpdateView):
    model = UrnCover
    form_class = UrnCoverForm
    template_name = 'burials/urncover_create.html'

#Urn
class UrnDetailView(DetailView):
    model = Urn
    template_name = 'burials/urn_detail.html'


class UrnListView(ListView):
    model = Urn
    template_name = 'burials/urn_list.html'


class UrnCreate(CreateView):
    model = Urn
    template_name = 'burials/urn_create.html'
    form_class = UrnForm


class UrnUpdate(UpdateView):
    model = Urn
    form_class = UrnForm
    template_name = 'burials/urn_create.html'

#GraveGood
class GraveGoodDetailView(DetailView):
    model = GraveGood
    template_name = 'burials/gravegood_detail.html'


class GraveGoodListView(ListView):
    model = GraveGood
    template_name = 'burials/gravegood_list.html'


class GraveGoodCreate(CreateView):
    model = GraveGood
    template_name = 'burials/gravegood_create.html'
    form_class = GraveGoodForm


class GraveGoodUpdate(UpdateView):
    model = GraveGood
    form_class = GraveGoodForm
    template_name = 'burials/gravegood_create.html'

#GraveGoodOther
class GraveGoodOtherDetailView(DetailView):
    model = GraveGoodOther
    template_name = 'burials/gravegoodother_detail.html'


class GraveGoodOtherListView(ListView):
    model = GraveGoodOther
    template_name = 'burials/gravegoodother_list.html'


class GraveGoodOtherCreate(CreateView):
    model = GraveGoodOther
    template_name = 'burials/gravegoodother_create.html'
    form_class = GraveGoodOtherForm


class GraveGoodOtherUpdate(UpdateView):
    model = GraveGoodOther
    form_class = GraveGoodOtherForm
    template_name = 'burials/gravegoodother_create.html'

#DeadBodyRemains
class DeadBodyRemainsDetailView(DetailView):
    model = DeadBodyRemains
    template_name = 'burials/deadbodyremains_detail.html'


class DeadBodyRemainsListView(ListView):
    model = DeadBodyRemains
    template_name = 'burials/deadbodyremains_list.html'


class DeadBodyRemainsCreate(CreateView):
    model = DeadBodyRemains
    template_name = 'burials/deadbodyremains_create.html'
    form_class = DeadBodyRemainsForm


class DeadBodyRemainsUpdate(UpdateView):
    model = DeadBodyRemains
    form_class = DeadBodyRemainsForm
    template_name = 'burials/deadbodyremains_create.html'



