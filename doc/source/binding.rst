=====================
Binding(Draft)
=====================

* THIS IS UNDER RESEARCH AND NOT DEFINED IN THE SPEC.

Binding 
-------

Binding is a process for :term:`Signatory` 

   - to discover a :term:`Server` and an endpoint for the requested :term:`Personal Information` stated in :term:`Request` by a :term:`Client` , and
   - to create :term:`Acceptance` for the Server and Client to share Personal Information.

Personal Information
--------------------

To share Personal Information between parties, the following itmes MUST be negotiated at least.

    - Data type
    - Data format

Data type SHOULD be understood by human as well as machines. At least the :term:`Signatory` and :term:`Proposer` MUST be able to tell an End User what exactly the service he is going to use expects as his Personal Information.

Data format MUST be negotiable between a Server and a Client to process a given Personal Information into service experiences. 


Client
------

Client should be able to describe what Personal Information it wants and what format it expects in Request file in someway.

:term:`OpenID AX` :term:`typeURI` is a way to specify the type and format of data an entity expects.

Proposer
---------

A Proposer is the entity providing service experiences to End Users with helps of some Clients. When an End User visits the Proposer to use advertised service, the Proposer MUST describe what is the provided service  and what Personal Information MUST be expected to provide that service.  Only when the End User can understood what he must to do, a process is going to be proceeded. 

Signatory
---------

A Signatory MUST tell the End User what his Personal Information is expected again at the time when the :term:`Contract` is created after or before he is authenticated at the Signatory.

When creating :term:`Acceptance` for the Contract, Signatory MUST state the endpoint from which the Personl Information is published, user identifier of whom End User is identfied at the entity and other parameter related to the End User and entities. To discover the endpoint, the Signatory MUST know the exact type of Personal Information, which Server manages the data and whether the Server publish the data in the format requested by a Client.

This is the Binding process.

Static Binding
===============

One possible binding is a static binding. Static binding table should be provided by Signatory in advance  and End User just select a Server to create a Contract for a particular Request.  In this binding, End User don't have to know exact data type and format. Only Signatory MUST know that.

Dynamic Binding
================

Another possible binding is a dynamic one. In this binding, an End User should expect which Server manages his requested Personal Information and be able to specify the Server identfier. 

A discovery process MUST be defined for this binding. What? :term:`LRDD` with some extensions? 

