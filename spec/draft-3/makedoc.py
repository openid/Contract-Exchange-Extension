# -*- coding: utf-8 -*-

import os
from datetime import datetime
from jinja2 import Environment,FileSystemLoader
from jinja2 import Template
#
from docutils.parsers import rst
from docutils.utils import *
#


def  load_params(name):
    # name.rst ファイルを読み込みます。
    p = rst.Parser()
    doc = new_document( name )
    doc.settings.tab_width=4
    doc.settings.pep_references =1
    doc.settings.rfc_references =1
    p.parse( open(name +'.rst').read(),doc )

    params  = [ {'name': i[0].rawsource, 'note':[ j.rawsource for j in i[1][0]] } for i in doc[0] ]
    return params


def make():
    env = Environment(loader= FileSystemLoader(os.path.join(os.path.dirname(__file__), '')))

    # rfc.tmpl がメインの枠のテンプレートです。
    t=env.get_template('rfc.tmpl')
    #t=env.get_template('abstract.tmpl')
    
    
    ctx = dict([ [r,load_params(r)]  
            for r in ['request','proposal',
                        'acceptance','contract','status',
                        'data_request',
                    ] ] )  
    ctx.update( dict(zip(['Year','Month','Day'],datetime.now().today().strftime("%Y %B %d").split(' '))) )
#    ctx = {'request':load_params('request'), 'signed_request':load_params('signed_request'), }
    return t.render(ctx).encode('utf-8')

if __name__ == '__main__':
    fname = "%s/openid-cx.%s.xml"% (
                    os.path.dirname( os.path.dirname(os.path.abspath(__file__))),
                    os.path.basename(os.path.dirname(os.path.abspath(__file__))).split('.')[0] )
    open(fname,"w").write( make())
