========================
Specfication Task List
========================


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


Contract Information Detail
===========================

Contract information should be described more clearly. Cardinality must be stated. 

