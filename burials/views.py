from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import *
from .forms import *

# Create your views here.


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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BurialSiteCreate, self).dispatch(*args, **kwargs)


class BurialSiteUpdate(UpdateView):
    model = BurialSite
    form_class = BurialSiteForm
    template_name = 'burials/burialsite_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BurialSiteUpdate, self).dispatch(*args, **kwargs)


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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BurialGroupCreate, self).dispatch(*args, **kwargs)


class BurialGroupUpdate(UpdateView):
    model = BurialGroup
    form_class = BurialGroupForm
    template_name = 'burials/burialgroup_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BurialGroupUpdate, self).dispatch(*args, **kwargs)


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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BurialCreate, self).dispatch(*args, **kwargs)


class BurialUpdate(UpdateView):
    model = Burial
    form_class = BurialForm
    template_name = 'burials/burial_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BurialUpdate, self).dispatch(*args, **kwargs)


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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UrnCoverCreate, self).dispatch(*args, **kwargs)


class UrnCoverUpdate(UpdateView):
    model = UrnCover
    form_class = UrnCoverForm
    template_name = 'burials/urncover_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UrnCoverUpdate, self).dispatch(*args, **kwargs)


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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UrnCreate, self).dispatch(*args, **kwargs)


class UrnUpdate(UpdateView):
    model = Urn
    form_class = UrnForm
    template_name = 'burials/urn_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UrnUpdate, self).dispatch(*args, **kwargs)


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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GraveGoodCreate, self).dispatch(*args, **kwargs)


class GraveGoodUpdate(UpdateView):
    model = GraveGood
    form_class = GraveGoodForm
    template_name = 'burials/gravegood_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GraveGoodUpdate, self).dispatch(*args, **kwargs)


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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GraveGoodOther, self).dispatch(*args, **kwargs)


class GraveGoodOtherUpdate(UpdateView):
    model = GraveGoodOther
    form_class = GraveGoodOtherForm
    template_name = 'burials/gravegoodother_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GraveGoodOtherUpdate, self).dispatch(*args, **kwargs)


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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeadBodyRemainsCreate, self).dispatch(*args, **kwargs)


class DeadBodyRemainsUpdate(UpdateView):
    model = DeadBodyRemains
    form_class = DeadBodyRemainsForm
    template_name = 'burials/deadbodyremains_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeadBodyRemainsUpdate, self).dispatch(*args, **kwargs)
