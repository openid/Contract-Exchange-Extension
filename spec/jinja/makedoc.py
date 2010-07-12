import os
from jinja2 import Environment,FileSystemLoader
from jinja2 import Template
#
from docutils.parsers import rst
from docutils.utils import *
#


def  load_params(name):
    p = rst.Parser()
    doc = new_document( name )
    doc.settings.tab_width=4
    doc.settings.pep_references =1
    doc.settings.rfc_references =1
    p.parse( open(name +'.rst').read(),doc )

    params  = [ {'name': i[0].rawsource, 'note':[ j.rawsource for j in i[1][0]] } for i in doc[0] ]
    return params

if __name__ == '__main__':

    env = Environment(loader= FileSystemLoader(os.path.join(os.path.dirname(__file__), '')))
    t=env.get_template('rfc.tmpl')
    #t=env.get_template('abstract.tmpl')
    
    
    
    ctx = {'request':load_params('request') }
    print t.render(ctx).encode('utf-8')

