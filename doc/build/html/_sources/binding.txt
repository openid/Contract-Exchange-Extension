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

LRDD Binding
=============

We can use :term:`LRDD` to discover a server, its endpoitns and other paramters.

End User specifies a Server identifier
---------------------------------------

After authenticated at :term:`Signatory`, an End User may specifiy the identifier of a Server by which his Personal Information is managed.

Alice has an account at a local storage and delivery company called "Agile Cats". 
She is buying a cosmetics at Hawaii based caompany called "Welina" and that coampany want to know where to deliver and how much it cost to deliver. 

Alice has not registered her delivery service at the Signatory, she is asked to specifiy the delivery servier Server URL. She fills the following URI :

.. code-block:: c 

    http://www.agile-cats.com/

Firstly, the Signatory checks if "Agile Cats" can provide :term:`OpenID CX` protocol and delivery service. So the Signatry makes HTTP "GET" request to :term:`host-meta` of the "Agile Cats" like this:

.. code-block:: c 

    GET /.well-known/host-meta HTTP/1.1
    Host: wwww.agile-cats.com

In turn, the "Agile Cat" return the following :term:`XRD` descriptor :

.. code-block:: xml


   <?xml version='1.0' encoding='UTF-8'?>
   <XRD xmlns='http://docs.oasis-open.org/ns/xri/xrd-1.0'
        xmlns:hm='http://host-meta.net/ns/1.0'>

       <hm:Host>www.agile-cat.com</hm:Host>
       <Property type='http://lrdd.net/priority/resource' />

       <Link rel='lrdd'     template='http://www.agile-cat.com?lrdd={uri}' />
       <Link rel='cx'     template='http://www.agile-cat.com?type={uri}' />

   </XRD>

Because the returned XRD has an Link element with "rel" attribute specified as "cx", the Signatory knows OpenID CX protocal is provided by "Agile Cats". 
The Signatory make reqeust to "template" URI template with "http://openid.net/specs/cx/service/delivery" because  "Welina" requests delivery service specified by that URI.

.. code-block:: c 

    GET /?type=http%3A%2F%2Fopenid.net%2Fspecs%2Fcx%2Fservice%2Fdelivery   HTTP/1.1
    Host: wwww.agile-cats.com

Then, a XRD for delivery service is returned like the followings.

.. code-block:: xml

   <?xml version='1.0' encoding='UTF-8'?>
   <XRD xmlns='http://docs.oasis-open.org/ns/xri/xrd-1.0'
        xmlns:hm='http://host-meta.net/ns/1.0'>

        <Subject>http://openid.net/specs/cx/service/delivery</Subject>
        <Link rel=http://openid.net/specs/cx/service/delivery</Subject>

        <Link rel='endpoint' href="http://www.agile-cats.com/cx/service/de>
        <Link rel='notify'   href="http://www.agile-cats.com/cx/service/delivery  />
        <Link rel='certs'    href="http://www.agile-cats.com/cx/cert/20101201 />

   </XRD>


