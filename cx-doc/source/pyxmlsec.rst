.. cx-doc documentation master file, created by
   sphinx-quickstart on Tue Nov 24 14:10:43 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

========
PyXMLSec
========

About PyXMLSec
==============

PyXMLSec_ is a Python binding for XML Security Library(xmlsec_). xmlsec itself depends on LibXML2_.

.. _PyXMLSec: http://pyxmlsec.labs.libre-entreprise.org/
.. _xmlsec: http://www.aleksey.com/xmlsec/
.. _LibXML2: http://xmlsoft.org/


Importing and initializing  libxml2
===================================

libxml2 can be imported like following:

.. code-block:: python

 import libxml2


It's better to initialize the library:

.. code-block:: python

    libxml2.initParser()
    libxml2.substituteEntitiesDefault(1)

Importing and initializing PyXMLSec 
===================================

PyXMLSec_ can be imported like following:

.. code-block:: python

    import xmlsec


It's better to initialize the library:

.. code-block:: python

    xmlsec.cryptoShutdown()
    xmlsec.cryptoAppShutdown()
    xmlsec.shutdown()

Loading a X.509 private key
===========================

To load a PEM formatted  X.509 private key file, this function works:

.. code-block:: python

    def _load_private_key(self,pri_key_file):
        ret= xmlsec.cryptoAppKeyLoad(pri_key_file , xmlsec.KeyDataFormatPem,
                                  None, None, None)
        ret.setName(pri_key_file)
        return ret

.. _signing_a_xml:

Signing a XML
=============

To sign a XML and produce Enveloped Signature XML document, following function works:

.. code-block:: python

    def _sign_xml(self,private_key,certificate,src_xml):
        '''
        Sign a XML
        '''

        # XML document object from a given string
        doc = libxml2.parseDoc(src_xml.encode('UTF-8'))

        # create a signature node(Encrpyted Signature mode) : <Signature>
        signNode = xmlsec.TmplSignature(doc, xmlsec.transformExclC14NId(),
                                    xmlsec.transformRsaSha1Id(), None)
        doc.getRootElement().addChild(signNode)

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

Providing a Digital Signature Context
=====================================

A digital signature context is provided for a given certificate list and used to verify a signed XML.

.. code-block:: python

    def _create_dsig_context(self,certs):
        manager = xmlsec.KeysMngr()
        assert(manager)

        assert( xmlsec.cryptoAppDefaultKeysMngrInit(manager) >= 0 )

        for c in certs:
            print "loading ",c , "as a certificate to Key Manager..."
            assert( manager.certLoad(c,xmlsec.KeyDataFormatPem,
                         xmlsec.KeyDataTypeTrusted) >=0 )

        return xmlsec.DSigCtx(manager)


Verifying a Signed XML
======================

To verify a signed XML , following function works:

.. code-block:: python

    def _verify_xml(self,signed_xml_text,tmp_certfile='/tmp/temp_cert.pem'):
        '''
        Verify a signed XML
        '''

        # Load XML
        doc = libxml2.parseDoc(signed_xml_text.encode('UTF-8'))

        # get <Signature/> node.
        node = xmlsec.findNode(doc.getRootElement(),
                           xmlsec.NodeSignature, xmlsec.DSigNs)

        # create a temporal PEM file exported from <X509Certificate/>.
        open(tmp_certfile,'w').write( '-----BEGIN CERTIFICATE-----\n%s\n-----END CERTIFICATE-----\n' %  (
            xmlsec.findNode(
                doc.getRootElement() , #libxml2.parseDoc(self.signed_xml.encode('UTF-8')).getRootElement(),
                xmlsec.NodeX509Certificate,xmlsec.DSigNs).content
            ))

        # Create a Digital Signature Context 
        dsig_ctx = self._create_dsig_context([tmp_certfile])
        assert( dsig_ctx )

        # Verify the signature
        assert( dsig_ctx.verify(node) >= 0 )
        return ( dsig_ctx.status == xmlsec.DSigStatusSucceeded )

