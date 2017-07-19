from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from .models import *
from .forms import *

# Create your views here.


class BurialSiteDetailView(DetailView):
    model = BurialSite
    template_name = 'burials/burialsite_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BurialSiteDetailView, self).get_context_data(**kwargs)
        context["dating_list"] = self.object.dating.all()
        context["reference_list"] = self.object.reference.all()
        context["burialgroup_list"] = BurialGroup.objects.filter(burial_site=self.object.id)
        context["burial_list"] = Burial.objects.filter(burial_site=self.object.id)
        return context


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

    def get_form_kwargs(self):
        kwargs = super(BurialSiteUpdate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    @method_decorator(permission_required('burialsite.change',  raise_exception=True))
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BurialSiteUpdate, self).dispatch(*args, **kwargs)


class BurialSiteDelete(DeleteView):
    model = BurialSite
    template_name = 'burials/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_burialsites')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BurialSiteDelete, self).dispatch(*args, **kwargs)


class BurialGroupDetailView(DetailView):
    model = BurialGroup
    template_name = 'burials/burialgroup_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BurialGroupDetailView, self).get_context_data(**kwargs)
        context["burial_list"] = Burial.objects.filter(burial_group=self.object.id)
        context["gravegood_list"] = GraveGood.objects.filter(burial=self.object.id)
        return context


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


class BurialGroupDelete(DeleteView):
    model = BurialGroup
    template_name = 'burials/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_burialgroups')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BurialGroupDelete, self).dispatch(*args, **kwargs)


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


class BurialDelete(DeleteView):
    model = Burial
    template_name = 'burials/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_burials')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BurialDelete, self).dispatch(*args, **kwargs)


# class FillingObjectDetailView(DetailView):
#     model = FillingObject
#     template_name = 'burials/burialfilling_detail.html'
#
#
# class FillingObjectListView(ListView):
#     model = FillingObject
#     template_name = 'burials/burialfilling_list.html'
#
#
# class FillingObjectCreate(CreateView):
#     model = FillingObject
#     template_name = 'burials/burialfilling_create.html'
#     form_class = FillingObjectForm
#
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(FillingObjectCreate, self).dispatch(*args, **kwargs)
#
#
# class FillingObjectDelete(DeleteView):
#     model = FillingObject
#     template_name = 'burials/confirm_delete.html'
#     success_url = reverse_lazy('browsing:browse_fillingobjects')
#
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(FillingObjectDelete, self).dispatch(*args, **kwargs)
#
#
# class FillingObjectUpdate(UpdateView):
#     model = FillingObject
#     form_class = FillingObjectForm
#     template_name = 'burials/burialfilling_create.html'
#
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(FillingObjectUpdate, self).dispatch(*args, **kwargs)


class UrnCoverDetailView(DetailView):
    model = UrnCover
    template_name = 'burials/urncover_detail.html'

    def get_context_data(self, **kwargs):
        context = super(UrnCoverDetailView, self).get_context_data(**kwargs)
        return context


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


class UrnCoverDelete(DeleteView):
    model = UrnCover
    template_name = 'burials/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_urncovers')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UrnCoverDelete, self).dispatch(*args, **kwargs)


class UrnDetailView(DetailView):
    model = Urn
    template_name = 'burials/urn_detail.html'

    def get_context_data(self, **kwargs):
        context = super(UrnDetailView, self).get_context_data(**kwargs)
        context["urncover_list"] = UrnCover.objects.filter(urn=self.object.id)
        return context


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


class UrnDelete(DeleteView):
    model = Urn
    template_name = 'burials/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_urns')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UrnDelete, self).dispatch(*args, **kwargs)


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


class GraveGoodDelete(DeleteView):
    model = GraveGood
    template_name = 'burials/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_gravegoods')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GraveGoodDelete, self).dispatch(*args, **kwargs)


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
        return super(GraveGoodOtherCreate, self).dispatch(*args, **kwargs)


class GraveGoodOtherUpdate(UpdateView):
    model = GraveGoodOther
    form_class = GraveGoodOtherForm
    template_name = 'burials/gravegoodother_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GraveGoodOtherUpdate, self).dispatch(*args, **kwargs)


class GraveGoodOtherDelete(DeleteView):
    model = GraveGoodOther
    template_name = 'burials/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_gravegoodsother')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GraveGoodOtherDelete, self).dispatch(*args, **kwargs)


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


class DeadBodyRemainsDelete(DeleteView):
    model = DeadBodyRemains
    template_name = 'burials/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_deadbodyremains')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeadBodyRemainsDelete, self).dispatch(*args, **kwargs)


class AnimalRemainsDetailView(DetailView):
    model = AnimalRemains
    template_name = 'burials/animalremains_detail.html'


class AnimalRemainsListView(ListView):
    model = AnimalRemains
    template_name = 'burials/animalremains_list.html'


class AnimalRemainsCreate(CreateView):
    model = AnimalRemains
    template_name = 'burials/animalremains_create.html'
    form_class = AnimalRemainsForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AnimalRemainsCreate, self).dispatch(*args, **kwargs)


class AnimalRemainsUpdate(UpdateView):
    model = AnimalRemains
    form_class = AnimalRemainsForm
    template_name = 'burials/animalremains_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AnimalRemainsUpdate, self).dispatch(*args, **kwargs)


class AnimalRemainsDelete(DeleteView):
    model = AnimalRemains
    template_name = 'burials/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_animalremains')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AnimalRemainsDelete, self).dispatch(*args, **kwargs)
