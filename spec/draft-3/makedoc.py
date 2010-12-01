# -*- coding: utf-8 -*-

import os
from datetime import datetime
from jinja2 import Environment,FileSystemLoader
from jinja2 import Template
#
from docutils.parsers import rst
from docutils.utils import *
#


def  load_params(name,p):
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
    
    # XREF
    xref =  {'JSON_SIMPLE_SIGN_1_0': 'JSON Simple Sign 1.0' ,
             'JSON_SIMPLE_ENC_1_0' : 'JSON Simple Encryption 1.0' ,
             'OPENID_AB' : 'OpenID Artifact Binding 1.0',
             'JSON': 'JSON(Javascript Object Notation)',
             'X_690': 'X.690',
             'advertising_service' : 'Advertising Service',
             'notify_contract_status' : 'Notify Contract Status',
            }
    for (k,v) in xref.iteritems():
        xref[k] = '<xref target="%s">%s</xref>' % (k,v)
    
    #*.rst
    p = {'xref': xref }
    ctx = dict([ [r,load_params(r,p)]  
            for r in [ 'terms','request','proposal',
                        'acceptance','contract','status',
                        'data_request','access_log_file','access_log',
                    ] ] )  

    ctx.update( dict(zip(['Year','Month','Day'],datetime.now().today().strftime("%Y %B %d").split(' '))) )
#    ctx = {'request':load_params('request'), 'signed_request':load_params('signed_request'), }


    ctx['xref'] = xref
    ctx['cxurl'] = 'http://openid.net/specs/cx/1.0/' 

    return Template(t.render(ctx).encode('utf-8')).render(ctx).encode('utf-8')

if __name__ == '__main__':
    fname = "%s/openid-cx.%s.xml"% (
                    os.path.dirname( os.path.dirname(os.path.abspath(__file__))),
                    os.path.basename(os.path.dirname(os.path.abspath(__file__))).split('.')[0] )
    open(fname,"w").write( make())
