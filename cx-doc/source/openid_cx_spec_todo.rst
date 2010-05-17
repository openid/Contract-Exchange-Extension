========================
Specfication Task List
========================


CX Templates can be hosted anywhere if those are not faked.
===========================================================

CX Template URL must be specified with hash digest like SHA-256

3.1.3.  Template URL and Digest
================================

Fragment or query string for a Template URL ?
------------------------------------------------

Current revision of document specify a `Templdate URL`  in the following format ::


    http://url_to_template/#digest_algorith:digest_value

But query strings like this should be better ::

    http://url_to_template/?digest_algorith=digest_value


Because the `flagment part` mean some portions or subsets of dereferenced resource specified URL prior to the number sign('#'). (:term:`RFC3986`)



Data Sharing Use Case
======================

Sharing privacry information stored in OP  to a RP is quite common use case for CX aplication.
We should provide example CX message for this kind of a use case.


Result
------

 - Data Sharing is "Data Requesting"
 - A Party owes :term:`Obligations` to other parties bound to an CX Contract
 - :term:`Obligations` has endpoints where a :term:`Party` provides web services
 - The endpoints of a particular obligation  is specified as /Contract/Party/obligations/endpoint
 - Only parties who have permission can request data.
 - Permissions can be declared under /Contract/Party/obligations/to 
 - `to` is an identifier to :term:`Party` which is one of /Contract/Party
 - If there is no `to` under /Contract/Party/obligations, any party bound to the CX Contract MAY request data.
 - CX Contract idetifier issued by a :term:`Signatory` is a special obligation endpoint where the signatory MUST provide the contract itself.
 - Data response MUST be encrypted with the requester's public key.
 - Encrpytion parameters should be returned in HTTP response headers

    - Shared key encrypted asynmmetriccally which requester's public key.
    - Optionally initialization vector (IV) for block ciphers
    - Optionally ecnryption paramter. Default is CBC-256-128-PKCS5_PADDING which means 

        - Cipher is  :term:`CBC`
        - Shared key length is 256 bits.
        - Block size is 128 bits. 
        - Padding is :term:`PKCS5`

Contract Information Detail
===========================

Contract information should be described more clearly. Cardinality must be stated. 

