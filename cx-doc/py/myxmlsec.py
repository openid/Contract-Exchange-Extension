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

class XmlSec(object):

    def __init__(self):
        libxml2.initParser()
        libxml2.substituteEntitiesDefault(1)

        xmlsec.init()
        xmlsec.cryptoAppInit(None)
        xmlsec.cryptoInit()


    def load_private_key(self,pri_key_file):
        '''
        Load a private key file(PEM)
        '''
        ret= xmlsec.cryptoAppKeyLoad(pri_key_file , xmlsec.KeyDataFormatPem, None, None, None)
        ret.setName(pri_key_file)
        return ret

    def sign_xml(self,private_key,certificate,src_xml,at_child=False):
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
        key = self.load_private_key(private_key)
    
        # Key and the Certificate loading
        xmlsec.cryptoAppKeyCertLoad(key, certificate, xmlsec.KeyDataFormatPem)

        # Sign the XML : <SignatureValue> and others...
        dsig_ctx = xmlsec.DSigCtx()
        dsig_ctx.signKey = key
        dsig_ctx.sign(signNode)
        dsig_ctx.destroy()

        return doc

    def load_trusted_certs(self,certfile):
        manager = xmlsec.KeysMngr()
        assert(manager)

        assert( xmlsec.cryptoAppDefaultKeysMngrInit(manager) >= 0 )

        certs =  [ certfile ] 

        for c in certs:
            print "loading ",c , "as a certificate to Key Manager..."
            assert( manager.certLoad(c,xmlsec.KeyDataFormatPem,
                         xmlsec.KeyDataTypeTrusted) >=0 ) 
        
        return manager

    def create_dsig_context(self,certs):
        manager = xmlsec.KeysMngr()
        assert(manager)

        assert( xmlsec.cryptoAppDefaultKeysMngrInit(manager) >= 0 )

        for c in certs:
            print "loading ",c , "as a certificate to Key Manager..."
            assert( manager.certLoad(c,xmlsec.KeyDataFormatPem,
                         xmlsec.KeyDataTypeTrusted) >=0 ) 

        return xmlsec.DSigCtx(manager)

    def verify_xml(self,signed_xml_text,tmp_certfile='/tmp/temp_cert.pem'):
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
        
