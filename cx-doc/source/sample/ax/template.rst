===========================
AX:Template
===========================

Advertising the Supporting CX Contract
======================================

Because an OP can serve multile type of CX Contract, it must advertise list of supporting CX contract in some way , e.g, in its developers' web pages. 
If Google,Inc supports CX for its OpenID services, is may put CX contract information on http://code.google.com/intl/ja/apis/accounts/docs/OpenID.html .

Every CX contarct is signed based on the corresponding CX Tempalte which describes the detail of agreement, waranty , disclamier and other juridistic statement to be enforced not to breach by parties included in a CX Contract. 

CX Template
============

CX Template is specified as a unique URI. As with the fictional Google case, the URI could be the following::

    https://www.google.com/accounts/o8/cx/attribute_exchange?sha256=

CX Template for the Attribute Exchange Seenario
==================================================================



Service advertises the following CX Contract Template::

     ===========================
     Bookstore Payment Agreement
     ===========================
     
     Proposer: {{ proposer_name }}
     -----------------------------------------
     
      {{ proposer }}
     
     Acceptor: {{ acceptor_name }} 
     -----------------------------------------
     
      {{ acceptor }}
     
     Order:
     -----------------------------------------
     
      Order Date: 2010-01-01T09:00:00Z
     
      {{ purchase_items }} 
     
      Price: USD{{ price }}
      Purchaser: {{ acceptor_name }}
     
      Shipping Address:
     
       - Name: {{ name }}
       - Address: {{ address }} 
       - Phone: {{ phone }}
     
      Shipping Method: {{shipping}}
      Payment: OpenID4us Payment Service
     
     Purpose of use of data:
     -----------------------
     
      Ship to the purchaser
      Once only.
      Max Liability for breach: The Billing amount
