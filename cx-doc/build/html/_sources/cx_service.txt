.. cx-doc documentation master file, created by
   sphinx-quickstart on Tue Nov 24 14:10:43 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==========================
CX Service and CX Template
==========================

CX Serivice
===========

A CX Service is a Web service provided by a service provider.

Identifier and Discovery
------------------------

A CX Service endpoint  MUST be discovered by any party using CX Service identifier and service provider's identifier. 
XRDS/XRD discovery can be used for OpenID CX protocol.

For example, if you discover the following server identifier::

   http://op.com/

Here is an example of a XRDS :

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <XRDS>
      <XRD>
      <Service priority="0">
      <Type>http://specs.openid.net/auth/2.0/server</Type>
      <Type>http://openid.net/srv/ax/1.0</Type>
      <Type>http://openid.net/srv/cx/1.0/#</Type>
      <Type>http://op.com/cx/payment.txt?sha256=c8d6c46425bf83b6eebcf9fb24ac5ff7599e97f7b24973e53ae114a1a072ec67</URI>
      <URI>https://op.com/op/openid/</URI>
      </Service>
      </XRD>
    </XRDS>


This XRDS describes the following.

1. https://op.com/op/openid/ is the OpenID Authentication 2.0  for http://op.com/

    The CX is an extension of the OpenID Authentication protocal.

2. This endpoint support the OpenID AX extension (1.0).

    The CX is dependent on the AX extension to deliver the CX message.

3. This endpoint also support the OpenID CX extension (1.0).

    So a Relying Party can exchange the CX Contract messages through the OP endpoint.

4. This endpoint can process the "payment" contract through this endpoint.

    The details of the contract and service is described in the content published by this URI.
    The base64 encoded SHA-256 digest of this document must be this.::

        c8d6c46425bf83b6eebcf9fb24ac5ff7599e97f7b24973e53ae114a1a072ec67

What is CX Template ?
=====================

A CX Template is a document which describes the detail of agreement, waranty, disclamier and other juridistic statement to be enforced not to breached by parties included in a CX Contract. A proposing party MUST include the CX Template in the CX Contract document. 

A CX Template MUST include statements described at ``Common Contract Constructs Based on Typical Contract Terms``.

Getting CX Template
-------------------

A CX Template MUST be advertised by a service provider and discoverd by CX Service identifier.
A CX Tempalte MUST be publicly fetched using HTTP GET protocol.

The digest data of a CX Template  MUST be provided throught the discovery process. The default digest algorithm is SHA256.

Contract Template URL should be in the form of

  http://uri_of_contract_template#digest_algorithm:digest

For example:
  http://example.com/contract/ToS.rst#sha256:cd825a6919f0483208a42145500555ab381ce99983036f9ff996a206cb436929



CX Template Format
==================

Human Readable Text
-------------------

A CX Template MUST be formatted in a human readable text because it MUST be browsed by a User  when he/she want to authorize the CX Contract at a service provider.
Simple markup like reStructuredText, markdown, textile or others CAN be used to format CX Templates. text/plain is the deafult content type for CX Templates.

Templating 
----------

{{service_parameter}} can be used in a CX Template. A service provider can replace those string with the text of correspoinding XML node <service_parameter/> specifiend in CX Contract when the service provider display the content of the contract to the End User before he/she authorizes the contract.

See more about <service_parameter/> at :ref:`Contract XML Basic Structure<contract_xml_structure>`, 

Document Digest
---------------

Digest data MUST be provided for a CX Template.  Digest MUST be strong enough. SHA256 is good.
This disgest data is specified to fetch the template document itself.

Common Contract Constructs Based on Typical Contract Terms
==========================================================

Cardinal nubers associated with each item indicate wheterh the items is "Optional"(0 or more) or "Mandatory" (1 or more) and whether there might be multiplies of each.
Note that very few items are required to establish a legally enforceable contract.  

In a court of law, the party seeking to enforce the contract must show that there are following items:

- offer 
- acceptance
- consideration
- parties
- description of goods or services
- quantity of goods or services
- price to be paid in exchange for those goods or services

The court will also require evidence of assent. 

Contract Terms
--------------

Here are common items that must or may be included in a contract:

``Contract Identifier``

  (0 or more)

  ex., contract or purchase order number

``Parties``

  (2 or more) 

  identification may include, for example, legal name, jurisdiction of establishment or registration [ex., “a business corporation organized under the laws of the State of New York” or “company registration no. xyz with the Hamburg Chamber of Commerce and Industry”], place of residence or headquarters.

``Individual Signatories``

  (2 or more)

``Title or Capacity of Signatories``

  (0 or more)

``Date of Signature``
  (0 or more)

``Contact Details (for notices)``

  (0 or more)

  Description of goods, services,

``Actions, or Other Items  to be delivered``

  (1 or more)

``Quantity to be Delivered``

  (0 or more)

  not applicable for all contracts

``Price``
  
  (1 or more)

  this should include denomination of currency [ex., USD$], description of non-monetary consideration, any formula or external reference for calculation

``Date of delivery or  other performance``

  (0 or more)

``Place of delivery or   other performance``

  (0 or more)

``Definitions``

  (0 or more)

``Conditions``

  (0 or more)

  ex., performance contingent on certain events, payment contingent on standards of acceptance

``Warranties``

  (0 or more)
  
  ex., warranty of non-infringement, warranty of conformance to stated specifications, warranty of legal authority, warranty of insurance coverage

``Relationship to other contracts``

  (0 or more)

  ex., purchase order under a framework agreement

``Term of contract``

  (0 or more)
  
  may include renewal provisions

``Termination``

  (0 or more)

``Billing and payment``

  (0 or more)

  ex., net 30 days, discounts, late penalties, wire transfers

``Governing Law``

  (0 or more)

  ex., English law, Japanese law, law of California, German Civil Code

``Jurisdiction and forum``

  (0 or more)

  ex., courts of general jurisdiction located in New York City

``Waiver of Jury Trial``

  (0 or more)

``Arbitration / alternative dispute  resolution``

  (0 or more)

  ex., ICC binding arbitration clause, arbitration to be conducted in Geneva, Switzerland

``Merger clause/ entire agreement``

  (0 more)

  provision stating that this is the entire agreement between the parties and excluding claims based on statement in advertising or negotiations.

``Survival``

  (0 or more)

  clauses providing that certain terms, such as indemnification or confidentiality, survive expiration or termination of the contract

``Damages/Limitation of Liability``

  (0 or more)

  provisions on calculation of damages, liquidated damages, limitation or exclusion of certain kinds of damages

``Warranty disclaimers``

  (0 or more)

``Indemnification`` 

  (0 or more)

``Third-party beneficiary rights``

  (0 or more)

``Relationship of Parties``

  (0 or more)

  ex., provisions creating or disclaiming agency or employment relationship

``Confidentiality / Nondisclosure Publicity``

  (0 or more)

``Proprietary Rights, Ownership and Licensing of Intellectual Property``

  (0 or more)

``Assignment, Succession, Delegation``

  (0 or more)

``Legal and Regulatory Compliance`` 

  (0 or more)

  ex., licensing obligations, export controls, data protection

``Notice Requirements``

  (0 or more)

``Force Majeure``

  (0 or more)

  obligations excused or deferred for “Acts of God,” war or civil disorder, trade union actions, etc.

``Counterparts and Signatures``

  (0 or more)

  provisions allowing signatures at different times; validity of multiple copies or printouts

``Other Terms`` 

  (0 or more)

Many other terms could be mentioned, especially in specific contexts such as loan agreements or lease contracts, but the items listed above are some of the most common in commercial contracts generally.

CX Contract Template Sample
===========================

.. code-block:: rst

    ===========================
    INTERNET PAYMMENT AGREEMENT
    ===========================
    
    Whereas {{end_user}} pays for the services provided by {{service_provider}} at the {{ op_provoder}}'s payment service.
    
     1.   {{end_user}} must pay to {{ op_provider}} until the day specified in the "Credit Card Payment Agreement" between {{ op_provider}} and
          {{end_user}}}. Both of them must follow all warranties and disclaimer writtern on the agreement.
    
    
     2.   {{service_provider}} must be paid by {{ op_provider }} based on the "Digital Payment Service Agreement" between {{ op_provider }}
          and {{ service_provider }}. Both of them must follow all warranties and disclaimer  writtern on the agreement.
    
     3.   {{service_provider}} must digitally sign the agreement based on this document.
    
     4.   {{op_provider}} must digitally sign the agreement based on this document on the behalf of {{ end_user }}.
    
    {{service_provider}}
    --------------------
    
     By:      {{proposer_signatory}}
    
     Title:   {{proposer_title}}
    
     Date:    {{now}}
    
    {{end_user}}
    ------------
    
     By:      {{end_user}}
    
     Title:   {{end_user_title}}
    
     Date:    {{now}}
    
    
    {{op_provider}}
    ---------------
    
     By:      {{acceptor_signatory}}
    
     Title:   {{acceptor_title}}
    
     Date:    {{now}}
    
