from rdflib import *
import re


class NamespaceDict(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"'DotDict' object has no attribute '{key}'")

    def __setattr__(self, key, value):
        self[key] = value

def build_namespace( 
            ontology_resource_locator:str, 
            rdf_format:str='ttl', 
            label_source:URIRef=RDFS.label )-> NamespaceDict:

    g=Graph().parse(ontology_resource_locator, format = rdf_format)



    res = [r for r in g.query(f'SELECT * WHERE {{?r <{label_source}> ?label}}')]
    return NamespaceDict({ re.sub("\W+","_",r.asdict().get('label')) : r.get('r') for r in res}) 


    

