from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pandas as pd
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


@login_required
def import_xls(request):
    context = {}
    if request.method == 'POST':
        context["form"] = UploadFileForm(request.POST, request.FILES)
        if context["form"].is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            for i, row in df.iterrows():
                # create conceptSchemes
                scheme_title = row['conceptScheme'].split('|')[0]
                temp_scheme, _ = SkosConceptScheme.objects.get_or_create(dc_title=scheme_title)
                temp_scheme.save()
                # fetch labels and create SkosLabel objects
                concept_labels = str(row['1st order pref_label@eng | pref_label@ger']).split('|')
                if len(concept_labels) > 1:
                    pref_label, _ = SkosLabel.objects.get_or_create(
                        label=concept_labels[1],
                        label_type='prefLabel',
                        isoCode='ger'
                    )
                else:
                    pref_label, _ = SkosLabel.objects.get_or_create(
                        label="kein Label",
                        label_type='prefLabel',
                        isoCode='ger'
                    )
                # create first order concepts
                first_temp, _ = SkosConcept.objects.get_or_create(
                    pref_label=concept_labels[0],
                    pref_label_lang='eng'
                )
                first_temp.label.add(pref_label)
                first_temp.scheme.add(temp_scheme)
                first_temp.save()

                # create second order concepts
                if str(row['2nd order pref_label@eng | pref_label@ger']) != "nan":
                    second_concept_labels = row['2nd order pref_label@eng | pref_label@ger'].split('|')
                    if len(second_concept_labels) > 1:
                        second_pref_label, _ = SkosLabel.objects.get_or_create(
                            label=second_concept_labels[1],
                            label_type='prefLabel',
                            isoCode='ger'
                        )
                    else:
                        second_pref_label, _ = SkosLabel.objects.get_or_create(
                            label="kein Label",
                            label_type='prefLabel',
                            isoCode='ger'
                        )
                    second_temp, _ = SkosConcept.objects.get_or_create(
                        pref_label=second_concept_labels[0],
                        pref_label_lang='eng'
                    )
                    second_temp.label.add(second_pref_label)
                    second_temp.scheme.add(temp_scheme)
                    second_temp.skos_broader.add(first_temp)
                    second_temp.save()
                else:
                    pass
                # create third order concepts
                if str(row['3rd order pref_label@eng | pref_label@ger']) != "nan":
                    third_concept_labels = row['3rd order pref_label@eng | pref_label@ger'].split('|')
                    if len(third_concept_labels) > 1:
                        third_pref_label, _ = SkosLabel.objects.get_or_create(
                            label=third_concept_labels[1],
                            label_type='prefLabel',
                            isoCode='ger'
                        )
                    else:
                        third_pref_label, _ = SkosLabel.objects.get_or_create(
                            label="kein Label",
                            label_type='prefLabel',
                            isoCode='ger'
                        )
                    third_temp, _ = SkosConcept.objects.get_or_create(
                        pref_label=third_concept_labels[0],
                        pref_label_lang='eng'
                    )
                    third_temp.label.add(third_pref_label)
                    third_temp.scheme.add(temp_scheme)
                    third_temp.skos_broader.add(second_temp)
                    third_temp.save()
            context['worked'] = df
            return render(request, 'vocabs/import_skos.html', context)
    else:
        context["form"] = UploadFileForm()
        context['worked'] = "upload something first"
    return render(request, 'vocabs/import_skos.html', context)
