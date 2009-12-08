.. cx-doc documentation master file, created by
   sphinx-quickstart on Tue Nov 24 14:10:43 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===========
CX Contract
===========

A CX Contract is a document to be exchanged between parties included in a contract.


Non-Repudiative Document
========================

The default format for ``Contract Exchange`` (CX) document is XML. The non-repudiation for the XML document in CX is guaranteed by ``XML Signature Syntax and Processing(Second Edition)`` (xmldsig-core_).

.. _xmldsig-core: http://www.w3.org/TR/xmldsig-core/

Enveloped XML Signature
-----------------------

The xmldsig-core_ defines following three method to deliver the signature of a XML Document :

 - Detached Signature

   The signature is over content external to the Signature element, and can be identified via a URI or transform. Consequently, the signature is "detached" from the content it signs. This definition typically applies to separate data objects, but it also includes the instance where the Signature and data object reside within the same XML document but are sibling elements.

 - Enveloping Signature

   The signature is over content found within an Object element of the signature itself. The Object (or its content) is identified via a Reference (via a URI fragment identifier or transform).
  
 - Enveloped Signature

   The signature is over the XML content that contains the signature as an element. The content provides the root XML document element. Obviously, enveloped signatures must take care not to include their own value in the calculation of the SignatureValue.


CX expected the Enveloped Signature for a XML Signature document.

Following :ref:`Signing a XML<signing_a_xml>`, the next simple XML text 

.. code-block:: xml

    <!--
    testSignXMerialize()
    -->
    <Envelope xmlns="urn:envelope">
      <Data>
        Hello, World!
      </Data>
    </Envelope>

is signed into this XML:

.. code-block:: xml 

    <?xml version="1.0" encoding="UTF-8"?>
    <!--
    testSignXMerialize()
    -->
    <Envelope xmlns="urn:envelope">
      <Data>
        Hello, World!
      </Data>
      <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
        <SignedInfo>
          <CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
          <SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
          <Reference>
            <Transforms>
              <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
            </Transforms>
            <DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
            <DigestValue>
    BG5RjqaoAUu661eSbtxYc3T1WqQ=
            </DigestValue>
          </Reference>
        </SignedInfo>
        <SignatureValue>
    m5UI5IbVfLYViD6CmRZjW1y6KkPFUt7nrnZmg3ecolhQlRUSTQhE+Kxbg+d2RHrk
    3jvoGBwBUavpUZ9UaHPb5dZgm1SlkB9FPT8Jsz5BZYIJier9yvRvqAPQraXH8BPL
    SUIDqLv4+8+yv2o6g5APzlCEwS7fCpoLtKjj1ZaUNWQ=
        </SignatureValue>
        <KeyInfo>
          <X509Data>
            <X509Certificate>
    MIIB/zCCAWgCCQDdijVcf/XGpDANBgkqhkiG9w0BAQUFADBEMRAwDgYDVQQDEwdy
    cC5kZWIgMRQwEgYDVQQLEwtzeXMucnAuZGViIDENMAsGA1UEChMEc3lzIDELMAkG
    A1UEBhMCSlAwHhcNMDkxMTI2MDcwNzA1WhcNMDkxMjI2MDcwNzA1WjBEMRAwDgYD
    VQQDEwdycC5kZWIgMRQwEgYDVQQLEwtzeXMucnAuZGViIDENMAsGA1UEChMEc3lz
    IDELMAkGA1UEBhMCSlAwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAKsL9cpd
    9iOsCHIj8rd54ajkOIcZezGP35ZxdnUxbTA0EL7STYsSdC2qpIS3jcbP2qGCvzJ8
    4ATCjTDRSL2ZH/CjdABlyJOcKj7GOqlyLu2jgkbdE4vye5r9DuJQvYjx4FIZSpBI
    Jwj6bjIH9uL2dthL90zQvoErEEdhsoWu1nmzAgMBAAEwDQYJKoZIhvcNAQEFBQAD
    gYEAEOrwLo0wiTS+0r4p0ra3GsQYWuGzGipEogro6WvVOCRuGck3bT8+Rao9I3ns
    rkqcO6t3eGhFe0mK+rH1UTEu5KweLmhNpddoaUNIIr405jidy1/NSmnFGXfTECA9
    Xm0frXwN9MOJg9okHeCwjwb6Cf9e/Lpoor2w+yaG8vSX3ik=
            </X509Certificate>
          </X509Data>
        </KeyInfo>
      </Signature>
    </Envelope>

Original Document and  Counter Signature
----------------------------------------

To be mutually non-repuidative, The CX contract, a returning document from OP to RP, MUST be singed XML form including  the signature of the original CX proposal document in signed XML form initiated by RP. 
The returning document makes counter signature to the original XML document becuase the original XML document MUST be base64-encoded and held at /Contract/Original element.


.. _contract_xml_structure:

Contract XML Basic  Structure
=============================

The basic structure of Contract XML is defined as followings:

.. code-block:: xml 

    <?xml version="1.0" encoding="UTF-8" ?>
    <Contract>
        <Party><!-- URI/XRI for the composing party --></Party>
        <Id><!-- Document identifier --></Id>
        <Rel>Relation in this Contract</Rel>
        <Service>
            <Type><!-- CX Servie identfier --></Type>
            <service_parameter><!-- any service parameter for CX Service specified by <Type/> --></service_parameter>
        </Service>
        <Template>
            <!--
            Base64 form of the CX Template for CX Serive. Exists only in proposing Contract.    
            -->
        </Template>
        <Original>
            <!--
            Original Document.
            Base64 form of the requested CX Contract XML document. Exists only in repsonding Contract. 
            -->
        </Original>
        <Signature>
            <!--
            W3C XML Security xmldsig-core ``Enveloped Signature`` element nodes
            -->
        </Signature>
    </Contract> 


Composing Party(Party element)
------------------------------

This element is the URI or XRI which sepcifiy the composing party.

Document Identifier (Id element)
---------------------------------

This node identifies single Contract XML and the value of this MUST be unique at composing party which is specified by <Party/>.

Relation in this Contract(Rel element) 
--------------------------------------

This means the type  the party. One of followings:

- http://openid.net/srv/cx/1.0#proposer
- http://openid.net/srv/cx/1.0#acceptor

Service Description(Service element and its descendents )
---------------------------------------------------------

This holds paramters to the CX Service endpoint. This node is extensible and freely add any XML node.
The respnding Contract can hold this element if service provider returns any data value.

Service Type(Type element)
~~~~~~~~~~~~~~~~~~~~~~~~~~

This MUST be a CX Service type URI which describes an actual sevice provided at the CX Service endpoint.

Service Parameter(service_paramter element)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Any element can be specified under the <Service/>. Those element's values SHOULD be processed by CX Service identified by <Type/>  at the CX Service endpoint.
Also {{service_parameter}}s in CX Template CAN be replaced by element's value at the service provider.

Contract Template(Template element)
-----------------------------------

CX Template text MUST be base64-encoded and held at here.

Original Document(Original element)
-----------------------------------

The requesting document has no Original element.
The original requesting XML document MUST be base64-encoded and held at here.
