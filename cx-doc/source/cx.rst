.. cx-doc documentation master file, created by
   sphinx-quickstart on Tue Nov 24 14:10:43 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=================
Contract eXchange
=================

A contract is an exchange of promises between two or more parties for the doing or not doing of something specified and enforceable by law. Contract eXchange(CX) is the process framework for parties in the Internet to exchange such promises on consuming and providing Web services.


CX Service
==========

A CX Service is a Web service provided by a service provider and can be a formal business transactions certified by a CX Contract.
Because a CX Service MUST be specifed by an unique identfier like URI and advertised by a service provider, service consumers can easily discover the endpoint of the service.
Also this URI must publish the corresponding CX Template.

CX Template
===========

A CX Template is a document which describes the detail of agreement, waranty , disclamier and other juridistic statement to be enforced not to breach by parties included in a CX Service transaction.
The CX Template MUST be refered in a CX Contract.


CX Contract
===========

A CX Contract is a form to be exchanged between parties and can be non-repuidiative proof of consuming a CX Service. 

CX Protocal
===========

The CX Protocal defined following process:

- Discovering CX Service
- Proposing CX Contract 
- Accepting a proposal
- Authroizing a CX Contract 
- Reponding a CX Contract

CX is thought to be bound to OpenID Authentication and Extension protocols.
