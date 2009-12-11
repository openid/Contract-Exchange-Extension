# -*- coding: utf-8 -*-
import sys 
import base64
import hashlib
from certs import rsa
import uuid
import time


_template='../xml/cx-sample-template.rst'

doc = unicode(''.join(open(_template).readlines()),'utf-8')

template_digest=hashlib.sha256(doc).hexdigest()
template_base64=base64.encodestring(doc)

PROPOSAL=u'''<?xml version="1.0" encoding="UTF-8" ?>
<Contract id="%s">
    <Type>http://openid.net/srv/cx/1.0/#proposal</Type>
    <Datetime>%s</Datetime>
    <Party>
        <URL>http://netshop.com</URL>
        <Rel>http://openid.net/srv/cx/1.0/#proposer</Rel>
        <obligations>
            <param type="http://cxop.net/cx/payment/totalamount" id="taotalamount" >500.0</param>
            <param type="http://cxop.net/cx/payment/title" id="title">Python Books</param>
        </obligations>
    </Party>
    <Party>
        <Id>=hdknr</Id>
        <Rel>http://openid.net/srv/cx/1.0/#proposer</Rel>
        <obligations/>
    </Party>
    <Service>
        <Type>http://cxop.net/cx/payment#sha256:%s</Type>
        <URL>http://cxop.net/openid/</URL>
    </Service>
    <TemplateURL>http://cxop.net/cx/payment#sha256:%s</TemplateURL>
    <Template>%s</Template>
</Contract>''' % ( 
    uuid.uuid1().hex, time.strftime('%Y-%m-%dT%H:%M:%S+9:00',time.localtime()),
    template_digest, template_digest, template_base64 )

from myxmlsec import XmlSec

x=XmlSec()
rp=rsa.generate('netshop.com')
doc=x.sign_xml( rp.prikey,rp.cert , PROPOSAL)

doc.saveFile('../xml/sample_proposal.xml')


original_base64=base64.encodestring(doc.serialize())
CONTRACT=u'''<?xml version="1.0" encoding="UTF-8" ?>
<Contract id="%s" >
    <Type>http://openid.net/srv/cx/1.0/#contract</Type>
    <Datetime>%s</Datetime>
    <Party>
        <URL>http://cxop.net</URL>
        <Rel>http://openid.net/srv/cx/1.0/#acceptor</Rel>
        <obligations>
            <param type="http://cxop.net/cx/payment/statuscode" id="statuscode" >200</param>
            <param type="http://cxop.net/cx/payment/description" id="description">OK</param>
        </obligations>
    </Party>
    <Original>%s</Original>
</Contract>''' % (
    uuid.uuid1().hex,time.strftime('%Y-%m-%dT%H:%M:%S+9:00',time.localtime()), original_base64 )

x=XmlSec()
op=rsa.generate('cxop.net')
doc=x.sign_xml( op.prikey,op.cert , CONTRACT)

doc.saveFile('../xml/sample_contract.xml')
