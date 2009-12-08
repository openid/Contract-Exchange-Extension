import os,sys
import re
import unittest
#
import libxml2 
import xmlsec
#


from certs import rsa
#
import base64

class PyXMLSecTest(unittest.TestCase):
    def init(self):
        self.rp = rsa.generate('rp.deb')
        self.op = rsa.generate('op.deb')

        self.manager = None

        self.proposal_xml ='''<?xml version="1.0" encoding="UTF-8"?>
<!-- OpenID CX Proposal -->
<Proposal>
  <Name>Sample Proposal</Name> 
</Proposal>
'''
        self.contract_xml ='''<?xml version="1.0" encoding="UTF-8"?>
<!-- OpenID CX Contract -->
<Contract>
    <Name>Sample Proposal</Name> 
    <Rp></Rp>
</Contract>
'''

    def setUp(self):
        self.init()
        print "setting up ...."
        print "*******************************"

        libxml2.initParser()
        libxml2.substituteEntitiesDefault(1)
        print "indent string =",libxml2.thrDefTreeIndentString("\t"),"/"
        print "indent =",libxml2.thrDefIndentTreeOutput(1)

        xmlsec.init() 
        print "xmlsec version =" ,xmlsec.checkVersion() 
        xmlsec.cryptoAppInit(None)
        xmlsec.cryptoInit()

    def tearDown(self):
        print "*******************************"

        if self.manager:
            self.manager.destroy()

        xmlsec.cryptoShutdown()
        xmlsec.cryptoAppShutdown()
        xmlsec.shutdown()
        
        libxml2.cleanupParser()

        print "tearing down ...."

    def _load_private_key(self,pri_key_file):
        '''
        Load a private key file(PEM)
        '''
        ret= xmlsec.cryptoAppKeyLoad(pri_key_file , xmlsec.KeyDataFormatPem,
                                  None, None, None)
        ret.setName(pri_key_file)
        return ret

    def testLoadKey(self):
        '''
        TEST: loading private key
        '''
        print "testLoadKey:"
        key = self._load_private_key(self.rp.prikey)
        self.failUnlessEqual(key.name , self.rp.prikey ,'PEM file name error')

    def _sign_xml(self,private_key,certificate,src_xml,at_child=False):
        '''
        Sign a XML 
        '''

        # XML document object from a given string
        doc = libxml2.parseDoc(src_xml.encode('UTF-8'))

        # create a signature node(Encrpyted Signature mode) : <Signature>
        signNode = xmlsec.TmplSignature(doc, xmlsec.transformExclC14NId(),
                                    xmlsec.transformRsaSha1Id(), None)

        signing_node = doc.getRootElement().firstElementChild()  if at_child else doc.getRootElement()
        signing_node.addChild(signNode)

        # create a reference : <Reference>
        refNode = signNode.addReference(xmlsec.transformSha1Id(),
                                    None, None, None)
        refNode.addTransform(xmlsec.transformEnvelopedId())

        # X.509 node <KeyInfo>
        keyInfoNode = signNode.ensureKeyInfo(None)
        keyInfoNode.addX509Data()

        # Load a private key
        key = self._load_private_key(private_key)
    
        # Key and the Certificate loading
        xmlsec.cryptoAppKeyCertLoad(key, certificate, xmlsec.KeyDataFormatPem)

        # Sign the XML : <SignatureValue> and others...
        dsig_ctx = xmlsec.DSigCtx()
        dsig_ctx.signKey = key
        dsig_ctx.sign(signNode)
        dsig_ctx.destroy()

        return doc

    def testSignXml(self):
        '''
        TEST: Sign a very simple XML
        '''
        src_xml ='''<?xml version="1.0" encoding="UTF-8"?>
<Envelope xmlns="urn:envelope">
  <Data>
    Hello, World!
  </Data>
</Envelope>
'''
        print "testSignXml:"
        doc = self._sign_xml( self.rp.prikey,self.rp.cert , src_xml ) 
        
        print doc.serialize(encoding='UTF-8',format=4)
#        doc.formatDump(sys.stdout,2)

    def _load_trusted_certs(self,certfile):
        manager = xmlsec.KeysMngr()
        assert(manager)

        assert( xmlsec.cryptoAppDefaultKeysMngrInit(manager) >= 0 )

        certs =  [ certfile ] 

        for c in certs:
            print "loading ",c , "as a certificate to Key Manager..."
            assert( manager.certLoad(c,xmlsec.KeyDataFormatPem,
                         xmlsec.KeyDataTypeTrusted) >=0 ) 
        
        return manager

    def _create_dsig_context(self,certs):
        manager = xmlsec.KeysMngr()
        assert(manager)

        assert( xmlsec.cryptoAppDefaultKeysMngrInit(manager) >= 0 )

        for c in certs:
            print "loading ",c , "as a certificate to Key Manager..."
            assert( manager.certLoad(c,xmlsec.KeyDataFormatPem,
                         xmlsec.KeyDataTypeTrusted) >=0 ) 

        return xmlsec.DSigCtx(manager)

    def _verify_xml(self,signed_xml_text,tmp_certfile='/tmp/temp_cert.pem'):
        '''
        Verify a signed XML
        '''
        doc = libxml2.parseDoc(signed_xml_text.encode('UTF-8'))

        node = xmlsec.findNode(doc.getRootElement(),
                           xmlsec.NodeSignature, xmlsec.DSigNs)

        # create a temporal PEM file
        open(tmp_certfile,'w').write( '-----BEGIN CERTIFICATE-----\n%s\n-----END CERTIFICATE-----\n' %  (
            xmlsec.findNode(
                doc.getRootElement() , #libxml2.parseDoc(self.signed_xml.encode('UTF-8')).getRootElement(),
                xmlsec.NodeX509Certificate,xmlsec.DSigNs).content
            ))

        # provide the Key Manager
#        manager = self._load_trusted_certs([tmp_certfile])

#        dsig_ctx = xmlsec.DSigCtx(manager ) 
        dsig_ctx = self._create_dsig_context([tmp_certfile]) 
        assert( dsig_ctx )
        assert( dsig_ctx.verify(node) >= 0 )
        assert( dsig_ctx.status == xmlsec.DSigStatusSucceeded )
        
        print "verification = OK! ",dsig_ctx.status

        return xmlsec.findNode(doc.getRootElement() , xmlsec.NodeSignatureValue,xmlsec.DSigNs).content
        
    def testSignXml2(self):
        '''
        TEST: Sign a very simple XML 
        '''
        src_xml ='''<?xml version="1.0" encoding="UTF-8"?>
<Envelope xmlns="urn:envelope">
  <Data>
    Hello, World!
  </Data>
</Envelope>
'''
        print "testSignXml:"
        doc = self._sign_xml( self.rp.prikey,self.rp.cert , src_xml )
        signed= doc.serialize()
        print signed
        ret1=self._verify_xml(signed )
        
        doc = self._sign_xml( self.rp.prikey,self.rp.cert , src_xml ,True) 
        signed= doc.serialize()
        print signed
        ret2= self._verify_xml(signed )

        print "same signature ?",(ret1==ret2)

##############################################################################

    def testXmlSignature(self):
        self._sign_xml()
#        print self.src_xml
#        print self.signed_xml
        self._verify_xml()
        
    def testXmlAppend(self):
        doc_proposal = libxml2.parseDoc(self.proposal_xml.encode('UTF-8'))
        doc_contract = libxml2.parseDoc(self.contract_xml.encode('UTF-8'))
    
        doc_contract.getRootElement().addChild( doc_proposal.getRootElement() )
        
        doc_contract.dump('-')

    #########

    def _create_key_manager(self,certificates):
        manager = xmlsec.KeysMngr()
        assert(manager)

        assert( xmlsec.cryptoAppDefaultKeysMngrInit(manager) >= 0 )

        for c in certificates:
            print "loading ",c , "as a certificate to Key Manager..."
            assert( manager.certLoad(c,xmlsec.KeyDataFormatPem, xmlsec.KeyDataTypeTrusted) >=0 ) 

        return manager

    def _create_key(self,keyfilename):
        key = xmlsec.cryptoAppKeyLoad(keyfilename, xmlsec.KeyDataFormatPem,
                                  None, None, None)
        key.setName(keyfilename)
        return key
        
    def _create_signed_xml(self,doc,keyfile,certfile):
        key = self._create_key(keyfile )
        signNode = xmlsec.TmplSignature(doc, xmlsec.transformExclC14NId(),
                                    xmlsec.transformRsaSha1Id(), None)

        doc.getRootElement().addChild(signNode)

        refNode = signNode.addReference(xmlsec.transformSha1Id(),
                                    None, None, None)

        refNode.addTransform(xmlsec.transformEnvelopedId())

        keyInfoNode = signNode.ensureKeyInfo(None)
        keyInfoNode.addX509Data()

        dsig_ctx = xmlsec.DSigCtx()

        dsig_ctx.signKey = key

        xmlsec.cryptoAppKeyCertLoad(key, certfile , xmlsec.KeyDataFormatPem)

        dsig_ctx.sign(signNode)

        ret = doc.serialize()

        dsig_ctx.destroy()
        doc.freeDoc()

        return ret
    
    def _verify_signed_xml(self,doc,certfile):

        print doc.serialize()
        node = xmlsec.findNode(doc.getRootElement(),
                           xmlsec.NodeSignature, xmlsec.DSigNs)
        assert ( node != None )
#        print "@@@@",xmlsec.NodeSignature,xmlsec.DSigNs
        print "@@@@",type(node)

        # <Contract><Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
        ctxt = doc.xpathNewContext()
        ctxt.xpathRegisterNs('xmlns','http://www.w3.org/2000/09/xmldsig#')

        res = ctxt.xpathEval('/Contract/xmlns:Signature')

        if len(res) >0:
            print "@@@@ length =",len(res)
            node = res[0]
            cer = ctxt.xpathEval('/Contract/xmlns:Signature/xmlns:KeyInfo/xmlns:X509Data/xmlns:X509Certificate')
            if len(cer)>0:
                open(certfile,'w').write( '-----BEGIN CERTIFICATE-----\n%s\n-----END CERTIFICATE-----\n' %  (
                    cer[0].content
                ))
            else:
                print "no X.509"
                  
        else:
            open(certfile,'w').write( '-----BEGIN CERTIFICATE-----\n%s\n-----END CERTIFICATE-----\n' %  (
                xmlsec.findNode(
                    doc.getRootElement(),
                xmlsec.NodeX509Certificate,xmlsec.DSigNs).content
                ))
            print "no.........@@@@"

#        print "@@@@",dir(node)
#        print "@@@@ type(node)",type(node),node.__class__
#        print node.serialize()


        km = self._create_key_manager([certfile])

        dsig_ctx = xmlsec.DSigCtx(km) 
        assert( dsig_ctx )
        assert( dsig_ctx.verify(node) >= 0 )
        assert( dsig_ctx.status == xmlsec.DSigStatusSucceeded )
        
        print "verification = OK! ",dsig_ctx.status
        
        return ( dsig_ctx.status == xmlsec.DSigStatusSucceeded )
        

    def testCounterSign(self):
        self.signed_proposal_xml = self._create_signed_xml( 
                                libxml2.parseDoc(self.proposal_xml.encode('UTF-8')),
                                'rp.deb/pri.pem',
                                'rp.deb/cert.pem')

#        print self.signed_proposal_xml

        self.saved_proposal_cert='/tmp/proposal_cert.pem'
        
        proposal_doc = libxml2.parseDoc(self.signed_proposal_xml.encode('UTF-8'))
        proposal_doc.saveFile('/tmp/signed_proposal.xml')

        if self._verify_signed_xml(
                                proposal_doc,
                                self.saved_proposal_cert):
            print "Fine!!!!"

        contract_doc = libxml2.parseDoc(self.contract_xml.encode('UTF-8'))
    
#        contract_doc.getRootElement().addChild( proposal_doc.getRootElement() )
        ctxt = contract_doc.xpathNewContext()
        res = ctxt.xpathEval('/Contract/Rp')
        if len(res)>0 :
            res[0].addChild( proposal_doc.getRootElement() )
        

        self.signed_contract_xml = self._create_signed_xml( 
                                contract_doc,
                                'op.deb/pri.pem',
                                'op.deb/cert.pem')

#        print self.signed_contract_xml

        self.saved_contract_cert='/tmp/contract_cert.pem'
        
        contract_doc = libxml2.parseDoc(self.signed_contract_xml.encode('UTF-8'))
        contract_doc.saveFile('/tmp/signed_contract.xml')
         
        if len(res) >0:
            print "Yeah"

        ctx = contract_doc
        if self._verify_signed_xml(
                                contract_doc,
                                self.saved_contract_cert):
            print "Fine!!!!"
            
    def testSimpleSign(self):
        doc = libxml2.parseDoc('<MyDocument><SignMe><Name>hdknr</Name></SignMe></MyDocument>'.encode('UTF-8'))

        signNode = xmlsec.TmplSignature(doc, xmlsec.transformExclC14NId(),
                                    xmlsec.transformRsaSha1Id(), None)
        print "***********************\n",signNode.serialize()

        refNode = signNode.addReference(xmlsec.transformSha1Id(),
                                    None, None, None)
        print "***********************\n",signNode.serialize()

        refNode.addTransform(xmlsec.transformEnvelopedId())
        print "***********************\n",signNode.serialize()

if __name__ == '__main__':
    unittest.main()
