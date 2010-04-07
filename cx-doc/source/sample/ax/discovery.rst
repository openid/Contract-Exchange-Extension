==================
AX:Discovery
==================


XRDS Discovery
==============
An OpenID CX Service can be discovered through `XRDS-Based Discovery <http://openid.net/specs/openid-authentication-2_0.html#discovery>`_ .

Suppose that the `Google OpenID Provider service <http://code.google.com/intl/ja/apis/accounts/docs/OpenID.html>`_ support the contract based attribute exchange using CX extension. 

If you request the following YADIS discovery request ,

.. code-block::  bash

    (main)hdknr@deblen:~/examples$ python
    Python 2.5.2 (r252:60911, Jan 24 2010, 14:53:14) 
    [GCC 4.3.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.

.. code-block::  python

    >>> import urllib2
    >>> req = urllib2.Request('https://www.google.com/accounts/o8/id',headers={'Accept':'text/html; q=0.3, application/xhtml+xml; q=0.5, application/xrds+xml'})
    >>> res = urllib2.urlopen(req)
    >>> 

the following XRDS should be returned. 

.. code-block:: python

    >>> res = urllib2.urlopen(req)
    >>> for i in res.readlines():
    ...     print i,
    ... 

.. include:: xrds.xml.inc


.. note::

    This particular XRDS has no xmlns attribute in any element because PyXMLSec produces errors if it is specified. 
    This error Should be investigated sometime later.

XRDS in XML Signagure
=====================

But the returning XRDS MUST be signed like this

.. include:: xrds.xml.signed.inc


CX Service Endpoint
===================

After parsing and validating the XRDS, a Relying Party must find the XRD/Service/Type element with a CX namespace url as its value::

    http://openid.net/srv/cx/1.0/#

Because  the CX is a OpenID Extension and alse based on the OpenID AX, indispensable XRD/Service/Type elements must be also specifed.

For "OP Identifier" senario, the OpenID Type url must be::

    http://specs.openid.net/auth/2.0/server

If the End User specified user idetnfier to discover,  the URL must be ::

    http://specs.openid.net/auth/2.0/signon    

For OpenID AX, the Type url must be::

    http://openid.net/srv/ax/1.0

If all XRD/Service/Type urls are find, the XRD/Service is the one you look at and the endpoint to the service is the value of XRD/Service/URI.

