import base64,hashlib,uuid
params = {
    'id': uuid.uuid1().hex, 
    'template':  'attribute_exchange.txt',
    }
params['template_url' ] = 'https://www.google.com/accounts/o8/cx/%(template)s' % params
params['template_text'  ] = ''.join( open( params['template']).readlines())
params['template_base64'] = base64.encodestring( params['template_text'] )
params['template_sha256'] = hashlib.sha256(  params['template_text'] ).hexdigest()

doc='''<?xml version="1.0" encoding="UTF-8"?>
<Contract id="e4bf53a8e97211de93e00800272c981e">
    <Type>http://openid.net/srv/cx/1.0/#proposal</Type>
    <Datetime>2009-12-15T21:10:54+09:00</Datetime>
    <Party>
        <URL id="proposer" >http://bourgogneonline.com</URL>
        <Rel>http://openid.net/srv/cx/1.0/#proposer</Rel>
        <obligations>
            <param type="http://payment.hdknr.com/cx/proposer_name" id="proposer_name">Bourgone Online</param>
            <param type="http://payment.hdknr.com/cx/price" id="price">29.90</param>
            <param type="http://payment.hdknr.com/cx/title" id="title">OpenID: The Definitive Guide (Paperback)</param>
            <param type="http://payment.hdknr.com/cx/purchase_items" id="purchase_items">
ISBN-13: 978-0596153762 / Title: OpenID: The Definitive Guide (Paperback) / Unit: 1 / Price: USD29.99
            </param>
            <param type="http://payment.hdknr.com/cx/shipping" id="shipping">UPS</param>
        </obligations>

    </Party>
    <Party>
        <URL id="acceptor" >=hdknr</URL>
        <Rel>http://openid.net/srv/cx/1.0/#acceptor</Rel>
        <obligations>
            <param type="http://cxop.net/cx/payment/acceptor_name" id="acceptor_name">=hdknr</param>
        </obligations>
    </Party>
    <Party>
        <URL>http://payment.hdknr.com/</URL>
        <Rel>http://openid.net/srv/cx/1.0/#signer</Rel>
        <obligations/>
    </Party>
    <Service>
        <Type>http://payment.hdknr.com/cx/template_payment_usd#sha256:40ea725769e6221908f08675014cff1b13e8399a5eb5555c21687d487da0b66c</Type>
        <URL>http://payment.hdknr.com/openid/</URL>
    </Service>
    <TemplateURL>%(template_url)s?sha256=%(template_sha256)s</TemplateURL>
    <Template>%(template_base64)s</Template>
</Contract>
'''

print  doc % params
