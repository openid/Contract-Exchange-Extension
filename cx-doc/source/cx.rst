.. cx-doc documentation master file, created by
   sphinx-quickstart on Tue Nov 24 14:10:43 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=================
Contract eXchange
=================

A contract is an exchange of promises between two or more parties for the doing or not doing of something specified and enforceable by law. Contract eXchange(CX) is the process framework for parties in the Internet to exchange such promises on consuming and providing Web services.

CX Contract
===========

A CX Contract is a form to be exchanged between parties and can be non-repuidiative proof of the ability of consuming and providing web services between each other engaged in the contract.

.. image:: cx_at_a_glance.png
   
Party
-----

A party is an entity who owes obligation to other parties bound to a CX Contract.
A party's public key  MUST be assured with its X.509 certificate signed by a proper certificate authority(CA).

Obligation
----------

An obligation is owed by a party to others parties bound to the same CX Contract.
Obligation endpoints MUST provide data service to proper parties for the obligation stated in the CX Contract.

Proposal
--------

A proposal is a CX Contract document before an End User argrees and sign at his/her signatory. 
A proposal MUST be counter-signed by all parties excluding the End User's signatory.

Contract
---------

A contract is a CX Contract document made of a CX proposal and a digital signature for the proposal.
A contract MUST be specified by a URI and  requested by any party bound to the contract.


CX Template
===========

A CX Template is a document which describes the detail of agreement, waranty , disclamier and other juridistic statement to be enforced not to breach by parties bound to the CX Contract during fullfilling their obligations.
The CX Template MUST be refered in a CX Contract document.

CX Protocol
===========

The CX Protocal defined following process:

- Discovering CX Service
- Proposing CX Contract 
- Accepting a proposal
- Authroizing a CX Contract 
- Reponding a CX Contract
- Requesting data

CX is thought to be bound to OpenID Authentication and Extension protocols.
