.. cx-doc documentation master file, created by
   sphinx-quickstart on Tue Nov 24 14:10:43 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


===========================================
Contract Exchange Extension 1.0 - Draft 1.6
===========================================

.. container:: contributor

 | Nat Sakimura, Nomura Research Institute,Inc.
 | Masaki Nishitani, Nomura Research Institute,Inc.
 | Hideki Nara, Tact Communications,Inc.

Abstract

This extension defines 1) An extensible Contract format, 2) Protocol to exchange the Contract.
Contact consists of Proposal and Agreement. The Proposer creates a signed Proposal and send it to the counter party. The counter party, upon agreeing to it, signs the Agreement. The combination of the Proposal and Agreement is the mutually signed contract, which is potentially legally binding. This Contract needs to be stored by both parties for a given length of time, usually spanning over many years depending on jurisdictions.

As these document size may be large while the user agent capability may be limited (e.g., mobile phones), sending them via direct communication and passing only the small reference called "Artifact" through the user agents are advisable. Therefore, as the protocol, use of Artifact Binding is strongly recommended.


.. sectnum::  

Terminology
===========
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC2119] (Bradner, S., Key words for use in RFCs to Indicate Requirement Levels, March 1997.).


Definitions and Conventions
---------------------------

All OpenID Contract Exchange messages MUST contain the following extension namespace declaration, as specified in the Extensions section of OpenID-Authentication-2.0: 

The XML Path structure is expressed in a XPath_ notation. 

.. _XPath: http://www.w3.org/TR/2007/REC-xpath20-20070123/

Overview
========

The contract exchange service extension is identified by the URI "http://openid.net/srv/cx/1.0/#". Support of this extension is advertised by having this url in /XRDS/XRD/Service/Type or /XRD/Link/rel.

For the exchange of the contract, this extension uses Attribute Exchange.    

.. note::

   This version of CX expects that AX fetch request can contain "value". This extension is being discussed under `the AX 1.1 working group`_. 

..  _`the AX 1.1 working group`: https://openid.pbworks.com/OpenID_Attribute_Exchange_Extention_1_1

The request parameters detailed here MUST be sent using the [OpenID.authentication2.0] (specs@openid.net, OpenID Authentication 2.0 - Final, August 2007.) extension mechanism. 


Contract Document
=================

Contract is a document that testifies that the parties involved  have agreed to what is written in it. The workflow for establishing such contract document varies, but in this extension, the following model is taken:

 1. There are typically 4 actors, A, SA, B, SB, where SA and SB are the designated signatory of A and B respectively.
 2. Proposer, A,  creates the contract proposal and signs and sends it to the other party.
 3. B examines the proposal and if it decides to accept, let SB sign it
 4. A obtains the signed copy of the contract.

Such contract can be used for various purposes not only for online transactions.

There can be many Contract format: It could be profiled in XML, JSON(RFC4627_), XDI_, etc. In this extension, since XML parser and `XML Signature`_ facilities are available for XRD processing, we define a XML contract profile. This section explains semantics of each element. For an example, refer to Appendix B.

.. _`XML Signature`: http://www.w3.org/TR/xmldsig-core/
.. _XDI: http://www.xdi.org/
.. _RFC4627: http://tools.ietf.org/html/rfc4627


Contract Template 
-----------------

A Contract Template is a document which describes the detail of agreement, waranty, disclamier and other legal statements that binds the parties in the CX Contract document. A proposing party MUST include the CX Template in the CX Contract document.

A Contract Template MUST be discoverable by the RP using XRD, XRDS or Yadis protocol.

.. note::

   A Contract Template discovery NEEDS to be further discussed.
   For XRDS, <XRD> of which <Type/> is ``Template URL`` SHOULD be the CX service which a relying party is looking at.

Human Readable Text
~~~~~~~~~~~~~~~~~~~

A Contract Template MUST be formatted in a human readable text because it MUST be read by the User when he/she wants to authorize the CX Contract at a service provider. Simple markup like reStructuredText, markdown, textile or others CAN be used to format CX Templates. text/plain is the deafult content type for CX Templates.

Templating 
~~~~~~~~~~

A Template variable is in the form ``{{parameter_name}}``. 
Any variable should be replaced by the corresponding value 
defined in the CX contract document, where 
@id is equal to the ``parameter_name``. 

When the provider shows the contract text to the end user 
to obtain the signing authorization, 
the provider should substitute the values into the variables.


Template URL and Digest
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The digest data for a CX Template  MUST be provided throught the discovery process. The default digest algorithm is SHA256.  

Contract Template URL should be in the form of 

  http://uri_of_contract_template#digest_algorithm:digest

For example: 
  http://example.com/contract/ToS.rst#sha256:cd825a6919f0483208a42145500555ab381ce99983036f9ff996a206cb436929


Contract Document Constructs
------------------------------

Because the CX protocol can be used for web services for critical business transactions, a CX Contract document SHOULD be a "legal contract"  which contains obligations of each parties including the remedy to the cases where it has been breached. 

Common Contract Constructs
~~~~~~~~~~~~~~~~~~~~~~~~~~

CX Contracts and CX Templates include common contract contstructs like warranty , disclaimer or other legal and business statements based on the Common Law(Anglo-American Law).  

Examples of common contract construsts used in CX are listed at `Appendix. B<common_contract_constructs>`,


Contract Document Structure
---------------------------

The default format for ``Contract Exchange`` (CX) document is XML. The non-repudiation for the XML document in CX is achieved by ``XML Signature Syntax and Processing(Second Edition)`` (xmldsig-core_).

.. _xmldsig-core: http://www.w3.org/TR/xmldsig-core/

CX uses Envelopped Signature defined in xmldsig-core_ . 
Canonicalization method MUST be Exclusive Canonicalization. 

.. note::
  c14n- may have multiple dialects: need to check. 

Original Document and  Counter Signature
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To achieve mutual non-repudiation, the contract document needs to be mutually digitaly signed. In CX, this is achieved through signing the document that includes the original signed proposal in Base 64 format. The specifics will be defined below. 

Contract XML Basic Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The basic structure of Contract XML is defined as following XML Schema:

.. include:: ../xml/cx.xsd.rst

.. include:: _cx_xsd_description.rst


Proposal and Agreement Validation
---------------------------------

Signature for each of Proposal and Agreement should be validated according to `XML Signature`_. The validity of the respective ds:KeyInfo is determined by first obtaining the signed XRD from the Party's identity url and perfoming following comparison operation. 

- /XRD/Subject == /Contract/Party/id 
- /XRD/ds:Signature/ds:KeyInfo/ds:X509Data/ds:X509Certificate == /Contract/Party/ds:Signature/ds:KeyInfo/ds:X509Data/ds:X509Certificate. When there is certificate change in the ds:X509Data, the chain must be checked in the same manner. 

Storage and Timestamping
------------------------

The Contract is supposed to act as a proof of agreement in case of dispute at a later date. 
Since contracts may be long term documents, there is a risk that are not so relevant in transient processing, such as Algorithm Compromise. Thus, care should be taken to appropriately process the contract through Timestamping etc. 


Protocol
========

Discovery
---------

Discovery of the contract exchange service extension is achieved via the mechanism described in [OpenID.authentication2.0] (specs@openid.net, OpenID Authentication 2.0 - Final, August 2007.). The attribute exchange namespace "http://openid.net/srv/cx/1.0/#" MUST be listed as /xrds/xrd/Service/Type element in the XRDS discovery document or /xrd/Link/rel element in the XRD 1.0 discovery document. The discovered XRDS MUST have an XRD/CanonicalID and XRD/ds:Signature. All of the party involved MUST publish an XRD. 

.. note::

    Discussion: RP Discovery needed for contract invalidation, RP Verification by OP, etc. (=nat, 2009-08-12) 

Sending Proposal
----------------

A CX Proposal document is sent as the parameter of AX fetch request.
The details of AX fetch request parameters are as follows:

    ``openid.ax.mode``

        REQUIRED. Value: "fetch_request"

    ``openid.ax.type.cx``

        REQUIRED. Value: "http://openid.net/srv/cx/1.0/#" .

    ``openid.ax.value.cx``

        REQUIRED. Value: Actual CX proposal document. Base64 encoded.

    ``openid.ax.required``

        REQUIRED. Value: 'cx' MUST be included in the AX required list.

    
    ``openid.ax.update_url``

        OPTIONAL. Value: The URL which an OP MAY send a message to notify the change of status. The paramters of this message is described in  :ref:`notification`. 

Writing Aggreement
------------------

The end user who has logged into the OP MUST be prompted to browse and agree to the proposal sent from the RP. OP MUST verify if the end user has enough right to authorize the signing before creating the counter signature. 

Receiving Contract
------------------

CX Contract is returned as the value of AX fetch request. 
The details of AX fetch resonse parameters are as follows:

    ``openid.ax.mode``

        REQUIRED. Value: "fetch_response"

    ``openid.ax.type.cx``

        REQUIRED. Value: "http://openid.net/srv/cx/1.0/#" .

    ``openid.ax.value.cx``

        REQUIRED. Value: Actual CX Contract document. Base64 encoded.


Encrypting the payload
---------------------------

The CX Payload can be sent or returned in ecrypted text. In addition to the usual AX fetch request and response parameters, the following paramters MUST be sent to enable the decryption of the payload.


    ``openid.ax.type.cx_encoding``

        Value: "http://openid.net/srv/cx/1.0/#encoding". 

    ``openid.ax.value.cx_encoding``

        Value: "Base64", "CBC-256-128-PKCS5_PADDING".

               If cx_encoding is "CBC-256-128-PKCS5_PADDING", the following parameters MUST be returned in addition.

    ``openid.ax.type.cx_enc_key``

        Value: "http://openid.net/srv/cx/1.0/#enc_key". 


    ``openid.ax.value.cx_enc_key``

        Shared key to encrypt the message in "Encryption Base String" form. This key itself is encrypted asymmetrically with decryptor's public key included in the Contract and base 64 encoded.
        Value: base64 string.


    ``openid.ax.type.cx_enc_iv``

        Type URI for initialization vector used in a block encryption.
        Value: "http://openid.net/srv/cx/1.0/#enc_iv". 

    ``openid.ax.value.cx_enc_iv``

        Value: base64 string

.. _notification:

Notify the Contract Status
--------------------------

The OP can notify the status of the contract to the RP using OpenID AX `update_url`. As with the case of other AX messages, the notification message is `unsolicited possitive assertion` including the following parameters.

    ``openid.ax.mode``

        REQUIRED. Value: "fetch_response"

    ``openid.ax.type.cxstat``

        REQUIRED. Value: "http://openid.net/srv/cx/1.0/#status" .

    ``openid.ax.value.cxstat``

        REQUIRED. Value: Any string to specify the Contract and its status. The RP SHOULD reqeust a `Direct Assertion Request` to the OP endpoint of which `openid.artifact` MUST be this value.


If the RP receive this message and verify that it is a valid `unsolicited possitive assertion` message, the RP SHOULD request the contract and its status by requesting a `Direct Assertion Request`. RP SHUOLD describe the contract and its status to the End User, but the procedure is out of the scope of this specification.

Security Considerations
=======================

Non-repudiation
---------------

Since CX is a message oriented public key based signing protocol, it offers non-repudiation unlike plain OpenID Authenticaion 2.0. 

Man-in-the-middle
-----------------

RP must verify the validity of the OP's identity and public key and vice versa. 

Eavesdropping
--------------

When encryption mode is used, the payload is encrypted and only the real recipient can decipher it. Thus, obtaining sensitive data through eavesdropping is very difficult.

Malicious Providers
-------------------

Malicious Providers that is behaving correctly according to this protocol cannot be coped within this protocol. It has to do the checking of the certificate with some assurance services and/or reputation services including RBL and white list.

Phishing Attack
---------------

Phising attack is a social engineering, so it should in principle be dealt with the non-knowledge-based authentication mechanism. This is clearly out of scope of this extension.

Private key compromise
----------------------

In the unlikely event of private key compromise, the party should immediately notify the CA as well as the counter party stated in the Contract document. This will minimize the damage by the incident.


Appendix A.  Parameters
========================

This specification defines a small set of common parameters that may be generally useful for the contracting purposes.  

``AX Request``

 - description: Used to convey the data that the requester requests. 
 - type URL: http://opneid.net/srv/cx/1.0#axreq
 - value: Attribute Exchange 1.1 string in tag=value&tag=value format as in X1.1. 
 - Conformance: MUST support. 

``Price to be paid by the party``

 - description: The price to be paid to execute this contract. 
 - type URL: http://openid.net/srv/cx/1.0/#price#currency where currency is replaced by the ISO currency code or 'other'
 - value: Decimal string when #currency is ISO code, and anyString when #currency is 'other'
 - Conformance: MUST support

``Maximum Liability assumed by the party``

 - description: The maximum liability assumed by the party  when there was a breach in the contract. 
 - type URL: http://openid.net/srv/cx/1.0/#damageslimit#currency where currency is replaced by the ISO currency code or 'other'
 - value: Decimal string when #currency is ISO code, and anyString when #currency is 'other'
 - Conformance: MUST support

``Contact``

 - description: The address at which the party can be reached at. 
 - type URL: http://openid.net/srv/cx/1.0/#contact
 - value: xs:string
 - Conformance: MUST support

``Datetime``

 - type URL: http://www.w3.orgg/TR/xmlschema-2/#datetime
 - value: The value defined as xs:dateTime in W3C XML Schema Datatypes specification, and MUST be expressed in UTC form, with no timme zone component (reprsented by the UTC 'Z' timezone). It must not specify the gime instants that corresponds to leap seconds. 
 - Conformance: MUST support. 

``String``

 - type URL: http://www.w3.orgg/TR/xmlschema-2/#string
 - value: UTF-8 string. 
 - Conformance: MUST support. 

Appendix B.  Examples
=====================

Proposal Sample
---------------

A sample Contract XML Proposal would look like as follows: 

.. include:: ../xml/sample_proposal.xml.rst 

Contract Sample
---------------

A sample Contract XML Contract would look like as follows: 

.. include:: ../xml/sample_contract.xml.rst 

.. _common_contract_constructs: 

Appendix C.  Common Contract Constructs used in CX 
==================================================

Followings are the list of common contract constructs. 
Each contract type should define some of the following 
as data type and utilize it in the template. 

``Contract Identifier``

  Defined as /Contract/Id in the core. 

``Parties``

  Stakeholders in a contract. Defined as /Contract/Party. 

``Individual Signatories``

  The person who signes on behalf of one of the Party. 
  Defined as /Contract/Party/ds:Signature/ds:KeyInfo.

``Title or Capacity of Signatories``

  Signers responsibility.  

``Date of Signature``

  Date of Signature. 

``Contact Details (for notices)``

  The address at which the parties can be contacted. 

``Actions, or Other Items  to be delivered``

  Description of goods, services. 

``Quantity to be Delivered``

``Price``

  This should include denomination of currency [ex., USD$], description of non-monetary consideration, any formula or external reference for calculation

``Date of delivery or  other performance``

``Place of delivery or other performance``

``Definitions``

``Conditions``

  Ex., performance contingent on certain events, payment contingent on standards of acceptance

``Warranties``

  Ex., warranty of non-infringement, warranty of conformance to stated specifications, warranty of legal authority, warranty of insurance coverage

``Relationship to other contracts``

  Ex., purchase order under a framework agreement

``Term of contract``

  May include renewal provisions

``Termination``

``Billing and payment``

  Ex., net 30 days, discounts, late penalties, wire transfers

``Governing Law``

  Ex., English law, Japanese law, law of California, German Civil Code

``Jurisdiction and forum``

  Ex., courts of general jurisdiction located in New York City

``Waiver of Jury Trial``

``Arbitration / alternative dispute ?ゑｿｽresolution``

  Ex., ICC binding arbitration clause, arbitration to be conducted in Geneva, Switzerland

``Merger clause/ entire agreement``

  Provision stating that this is the entire agreement between the parties and excluding claims based on statement in advertising or negotiations.

``Survival``

  Clauses providing that certain terms, such as indemnification or confidentiality, survive expiration or termination of the contract

``Damages/Limitation of Liability``

  Provisions on calculation of damages, liquidated damages, limitation or exclusion of certain kinds of damages

``Warranty disclaimers``

``Indemnification`` 

``Third-party beneficiary rights``

``Relationship of Parties``

  Ex., provisions creating or disclaiming agency or employment relationship

``Confidentiality / Nondisclosure Publicity``

``Proprietary Rights, Ownership and Licensing of Intellectual Property``

``Assignment, Succession, Delegation``

``Legal and Regulatory Compliance`` 

  Ex., licensing obligations, export controls, data protection

``Notice Requirements``

``Force Majeure``

``Counterparts and Signatures``

  Provisions allowing signatures at different times; validity of multiple copies or printouts

``Other Terms``


Many other terms could be mentioned, especially in specific contexts such as loan agreements or lease contracts, but the items listed above are some of the most common in commercial contracts generally.


Normative References
====================

- [OpenIDAuthentication2.0]   specs@openid.net, OpenID Authentication 2.0, 2007 (TXT, HTML).
- [RFC1421]   Linn, J., Privacy Enhancement for Internet Electronic Mail, RFC 1421.
- [RFC2045]   Freed, N., Borenstein , N., and N. Vaudreuil , Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet Message Bodies, RFC 1421.
- [RFC2119]   Bradner, B., Key words for use in RFCs to Indicate Requirement Levels, RFC 2119, 1997.
- [RFC3339]   Klyne, G. and C. Newman, Date and Time on the Internet: Timestamps, RFC 3339.
- [RFC3629]   Yergeau, F., UTF-8, a transformation format of ISO 10646, RFC 3629.
- [X.509]     X.509 : Information technology - Open Systems Interconnection - The Directory: Public-key and attribute certificate frameworks, August 2005.
- [xmldisg-core] XML Signature Syntax and Processing (Second Edition)
- [XRIResolution2.0]  Reed, D. and G. Wachob, Ed., Extensible Resource Identifier (XRI) Resolution Version 2.0, April 2008.
- [Yadis]     Miller, J., Ed., Yadis Specification 1.0, 2005 (PDF, ODT). 

Authors' Addresses
==================

    Nat Sakimura
    Nomura Research Institute, Ltd.
    Marunouchi Kitaguchi Building, 1-6-5 Marunouchi
    Chiyoda-ku, Tokyo 100-0005
    Japan
    Email:      n-sakimura@nri.co.jp
    URI:    http://www.nri.co.jp/
     
    Masaki Nishitani
    Nomura Research Institute, Ltd.
    Marunouchi Kitaguchi Building, 1-6-5 Marunouchi
    Chiyoda-ku, Tokyo 100-0005
    Japan
    Email:      m-nishitani@nri.co.jp
    URI:    http://www.nri.co.jp/
     
    Hideki Nara
    TACT Communications,Inc
    Cross Side Building , 3-52-1 Sendagaya
    Shibuya-ku, Tokyo 151-0051
    Japan
    Email:      hdknr@ic-tact.co.jp
    URI:    http://www.ic-tact.co.jp



Document History
================

- 2009-08-10T06:48Z Initial Private Release
- 2009-08-11T01:48Z Fixed Security Consideration Text. Added Discussion point on invalidation interface.
- 2009-08-12T01:48Z Fixed typo "ax" to "cx" in 1.1. Removed "Thus" from 3.3. Fixed 4.4 paragraph. Date Update. 
- 2009-08-12T15:24Z Added some comments on direct communication. 
- 2009-11-24T06:48Z Revised and written in reStructuredText for a Sphinx document project
