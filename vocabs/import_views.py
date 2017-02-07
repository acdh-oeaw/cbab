from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from .skos import SkosImporter
from .models import *


@login_required
def import_skos(request):
    context = {}
    if request.method == 'POST':
        context["form"] = UploadFileForm(request.POST, request.FILES)
        if context["form"].is_valid():
            file = request.FILES['file']
            skos = SkosImporter(file)
            context['worked'] = skos.importConcepts()
            return render(request, 'vocabs/import_skos.html', context)
    else:
        context["form"] = UploadFileForm()
        context['worked'] = "upload something first"
    return render(request, 'vocabs/import_skos.html', context)
