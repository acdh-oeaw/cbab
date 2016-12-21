import lxml.etree as ET
from .models import SkosConcept, SkosConceptScheme, SkosLabel


class SkosReader(object):

    """
    reads a skos file (RDF/XML) and returns a list of dictionaries
    containing rdf:Description properties
    concept-id: (URL)
    notation: (derived from concept-id)
    pref_labels: (list of labels)
    skos:broader: (list of broader elements)
    skos:narrower: ...
    skos:closeMatch ...
    skos:inScheme: (list of all conceptSchemes a concept is related to
    """

    def __init__(self, skosfile):
        self.ns_skos = "http://www.w3.org/2004/02/skos/core#"
        self.ns_rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
        self.skosfile = skosfile

        try:
            self.tree = ET.parse(skosfile)
            self.parsed_file = ET.tostring(self.tree, encoding="utf-8")
        except:
            self.parsed_file = "parsing didn't work"

        try:
            self.extractedDescriptions = self.tree.findall(
                'rdf:Description', namespaces={"rdf": self.ns_rdf})
            self.numberOfextractedDescriptions = len(self.extractedDescriptions)
        except:
            self.extractedDescriptions = "rdf:Descriptions could not be extracted."
            self.numberOfextractedDescriptions = 0

    def returnDescriptions(self):
        descriptions = []
        for x in self.extractedDescriptions:
            description = {}
            temp_type = x.find('rdf:type', namespaces={"rdf": self.ns_rdf})
            if temp_type is not None:
                description["type"] = temp_type.attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource']
            else:
                description["type"] = "no type"
            description["id"] = x.attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about']
            description["notation"] = x.find('skos:notation', namespaces={"skos": self.ns_skos})

            skos_pref_labels = []
            for y in x.findall('skos:prefLabel', namespaces={"skos": self.ns_skos}):
                skos_label = {}
                skos_label['text'] = y.text
                skos_label['lang'] = y.attrib['{http://www.w3.org/XML/1998/namespace}lang']
                skos_pref_labels.append(skos_label)
            description["pref_labels"] = skos_pref_labels

            skos_alt_labels = []
            for y in x.findall('skos:altLabel', namespaces={"skos": self.ns_skos}):
                skos_label = {}
                skos_label['text'] = y.text
                skos_label['lang'] = y.attrib['{http://www.w3.org/XML/1998/namespace}lang']
                skos_alt_labels.append(skos_label)
            description["alt_labels"] = skos_alt_labels

            skos_broader = []
            for y in x.findall('skos:broader', namespaces={"skos": self.ns_skos}):
                broader = {}
                broader['uri'] = y.attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource']
                broader['notation'] = broader['uri'].split('/')[-1]
                skos_broader.append(broader)
            description['broader'] = skos_broader

            skos_narrower = []
            for y in x.findall('skos:narrower', namespaces={"skos": self.ns_skos}):
                narrower = {}
                narrower['uri'] = y.attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource']
                narrower['notation'] = narrower['uri'].split('/')[-1]
                skos_narrower.append(narrower)
            description['narrower'] = skos_narrower

            skos_closeMatch = []
            for y in x.findall('skos:closeMatch', namespaces={"skos": self.ns_skos}):
                closeMatch = {}
                closeMatch['uri'] = y.attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource']
                closeMatch['notation'] = closeMatch['uri'].split('/')[-1]
                skos_closeMatch.append(closeMatch)
            description['closeMatch'] = skos_closeMatch

            skos_schemes = []
            for y in x.findall('skos:inScheme', namespaces={"skos": self.ns_skos}):
                skos_schemes.append(
                    y.attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource'])
            description["schemes"] = skos_schemes
            descriptions.append(description)
        return descriptions

    def countConcepts(self):
        return len(self.returnDescriptions())


class SkosImporter(SkosReader):

    """Imports concepts and concept schemes to django application/database"""

    def importConcepts(self):
        concepts_before = len(SkosConcept.objects.all())
        num_description_type_concept = 0
        num_description_type_concept_scheme = 0
        for x in self.returnDescriptions():
            if x["type"] == "http://www.w3.org/2004/02/skos/core#ConceptScheme":
                temp_concept_scheme, _ = SkosConceptScheme.objects.get_or_create(legacy_id=x["id"])
                temp_concept_scheme.save()
                num_description_type_concept_scheme += 1

            else:
                temp_uri = x['id']
                temp_notation = temp_uri.split('/')[-1]
                temp_concept, _ = SkosConcept.objects.get_or_create(
                    legacy_id=temp_uri, notation=temp_notation)
                try:
                    temp_concept.pref_label = x['pref_labels'][0]["text"]
                    temp_concept.pref_label_lang = x['pref_labels']["lang"]
                except:
                    pass
                temp_concept.save()

                for y in x['pref_labels'][1:]:
                    temp_label, _ = SkosLabel.objects.get_or_create(
                        label=y["text"],
                        isoCode=y["lang"],
                        label_type="prefLabel"
                    )
                    temp_concept.label = [temp_label]
                    temp_concept.save()

                for y in x['alt_labels'][1:]:
                    temp_label, _ = SkosLabel.objects.get_or_create(
                        label=y["text"],
                        isoCode=y["lang"],
                        label_type="altLabel"
                    )
                    temp_concept.label = [temp_label]
                    temp_concept.save()

                for z in x['schemes']:
                    temp_scheme, _ = SkosConceptScheme.objects.get_or_create(
                        legacy_id=z
                    )
                    temp_scheme.dc_title = self.skosfile
                    temp_scheme.save()
                    temp_concept.scheme = [temp_scheme]
                    temp_concept.save()

                for y in x['broader']:
                    temp_broader, _ = SkosConcept.objects.get_or_create(
                        legacy_id=y["uri"], notation=y["notation"])
                    temp_broader.save()
                    temp_concept.skos_broader = [temp_broader]
                    temp_concept.save()

                for y in x['narrower']:
                    temp_narrower, _ = SkosConcept.objects.get_or_create(
                        legacy_id=y["uri"], notation=y["notation"])
                    temp_narrower.save()
                    temp_concept.skos_narrower = [temp_narrower]
                    temp_concept.save()

                for y in x['closeMatch']:
                    temp_closeMatch, _ = SkosConcept.objects.get_or_create(
                        legacy_id=y["uri"], notation=y["notation"])
                    temp_closeMatch.save()
                    temp_concept.skos_closematch = [temp_closeMatch]
                    temp_concept.save()

                num_description_type_concept += 1
        concepts_after = len(SkosConcept.objects.all())
        summary = "#descr. type 'concept': {} |  #descr. type 'conceptSchemes': {}".format(
            num_description_type_concept, num_description_type_concept_scheme
        )

        report = {'summary': summary, 'before': concepts_before, 'after': concepts_after}
        return report

    def test_if_class_works(self):
        check = "Works!"
        return check
