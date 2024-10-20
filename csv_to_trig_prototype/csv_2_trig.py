import csv
from rdflib import *
from argparse import ArgumentParser


def csv2trig(fn):

    fin = open(fn,'r')
    reader = csv.reader(fin)
    h=next(reader)
    ng = ConjunctiveGraph()
    for r in reader:
        if len(r) < 4: continue
        s = URIRef(r[1].replace("<","").replace(">",""))
        p = URIRef(r[2].replace("<","").replace(">",""))
        o = None
        if r[3] != 'L':
            o=URIRef(r[3].replace("<","").replace(">",""))
        else:
            if r[6] is not None:
                o=Literal(r[4],lang=r[6])
            else:
                o=Literal(r[4],datatype=URIRef(r[5]))
        g = URIRef(r[0].replace("<","").replace(">",""))
        sg = ng.get_context(g)
        sg.add((s,p,o))

    open(fn.replace('.csv','.trig'),'w').write(ng.serialize(format = 'trig'))
    
if __name__ == """__main__""":
    
    parser =  ArgumentParser()
    

    parser.add_argument('filename') 
    
    args = parser.parse_args()
    
    filename = args.filename
    if filename[-4:] == '.csv':
        csv2trig(filename)