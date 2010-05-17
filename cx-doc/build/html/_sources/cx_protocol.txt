.. cx-doc documentation master file, created by
   sphinx-quickstart on Tue Nov 24 14:10:43 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


===========
CX Protocol
===========

OpenID CX is a protocol which bind CX Protocl to OpenID Authentication and Extension protocols.

Discovering OpenID CX Service
=============================

.. note::

    Description about  Yadis / XRDS / XRD  discovery.

Data Request
=============================

A :term:`Party` can reqeust data provided from other party's :term:`Obligations` endpoint declared in the CX Contract.

Endpoints
----------

 - The endpoints of a particular obligation  is specified as /Contract/Party/obligations/endpoint
 - Only parties who have permission can request data.
 - Permissions can be declared under /Contract/Party/obligations/to
 - `to` is an identifier to :term:`Party` which is one of /Contract/Party
 - If there is no `to` under /Contract/Party/obligations, any party bound to the CX Contract MAY request data.

Encryption
-----------

 - Data response MUST be encrypted with the requester's public key.
 - Encrpytion parameters should be returned in HTTP response headers

    - Shared key encrypted asynmmetriccally which requester's public key.
    - Optionally initialization vector (IV) for block ciphers
    - Optionally ecnryption paramter. Default is CBC-256-128-PKCS5_PADDING which means

        - Cipher is  :term:`CBC`
        - Shared key length is 256 bits.
        - Block size is 128 bits.
        - Padding is :term:`PKCS5`

Contract Request
-----------------

CX Contract idetifier issued by a :term:`Signatory` is used as a special obligation endpoint where the signatory MUST provide the contract itself.
The signatory MUST return the CX Contract to any party bound to that contract. Responding contract MUST be encrypted in the same manner as generic obligations.

Exchange documents by OpenID AX
===============================

OpenID CX is an application protocol of the `OpenID AX`_ . 

.. _`OpenID AX`: http://openid.net/specs/openid-attribute-exchange-1_0.html

Adding value to OpenID AX  fetch_request
----------------------------------------

OpenID CX is the protocol to exchange non-repudiative documents between parties. To exchange documents, OpenID CX is adapting `OpenID AX`_ Extension. There are two type of requests in OpenID AX : ``fetch_request`` and ``store_request``. Both of them can't fit to exchaning senario, we are extending the fetch_request to convery a source value to be exchanged into a returned value in ``fetch_response``.

Extendding JanRain python-openid
--------------------------------

=hdknr tried to extend JanRain_ python-openid_ to handle source value in AX ``fetch_request``. The patch is for the version 2.2.4 of python-openid_ and is available at http://code.hdknr.com/OpenID/AX/axx/libdiff.patch .

.. _python-openid: http://www.openidenabled.com/python-openid/
.. _JanRain: http://www.janrain.com/

The patch can be applied to a python-opneid installed in a Python virtualenv environment.

.. code-block:: bash

 (rp)hdknr@debuniid:~$ cdvirtualenv
 (rp)hdknr@debuniid:~/.virtualenvs/rp$ cd lib/python2.5/site-packages/openid/

 (rp)hdknr@debuniid:~/.virtualenvs/rp/lib/python2.5/site-packages/openid$ curl http://code.hdknr.com/OpenID/AX/axx/libdiff.patch | grep diff
   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                  Dload  Upload   Total   Spent    Left  Speed
   0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0diff -cr --exclude=_darcs --exclude='*.pyc' --exclude=test 2.x.x/openid/extensions/ax.py /home/hdknr/.virtualenvs/ax/lib/python2.5/site-packages/openid/extensions/ax.py
 100 14954  100 14954    0     0   9931      0  0:00:01  0:00:01 --:--:-- 12257
 (rp)hdknr@debuniid:~/.virtualenvs/rp/lib/python2.5/site-packages/openid$ curl http://code.hdknr.com/OpenID/AX/axx/libdiff.patch | patch -p8 -d .
   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                  Dload  Upload   Total   Spent    Left  Speed
 100 14954  100 14954    0     0  13684      0  0:00:01  0:00:01 --:--:-- 17995
 missing header for context diff at line 4 of patch
 can't find file to patch at input line 4
 Perhaps you used the wrong -p or --strip option?
 The text leading up to this was:
 --------------------------
 |diff -cr --exclude=_darcs --exclude='*.pyc' --exclude=test 2.x.x/openid/extensions/ax.py /home/hdknr/.virtualenvs/ax/lib/python2.5/site-packages/openid/extensions/ax.py
 |*** 2.x.x/openid/extensions/ax.py      2009-11-11 15:46:56.000000000 +0900
 |--- /home/hdknr/.virtualenvs/ax/lib/python2.5/site-packages/openid/extensions/ax.py    2009-11-13 17:53:31.000000000 +0900
 --------------------------
 File to patch: extensions/ax.py
 patching file extensions/ax.py


Code difference
~~~~~~~~~~~~~~~

Following difference  exists between the original JanRain_ code and the patch.

- If there is no "value" specified  to AXKeyValueMessage object, parseExtensionArgs() sets 0 length string to "value".
- FetchReqeust is derived from AXKeyValueMessage.
- AXKeyValueMessage.__init__(self) is called in FetchRequest.__init__(self).
- FetchRequest.getextensionArgs(): If there are values,  those are added to the returning key-value dictionary.
- FetchRequest.parseExtensionArgs() calles the base class( AXKeyValueMessage)'s parseExtensionArgs() at first. 

OpenID Authentication : Artifact Bindings
=========================================

Because CX documents can be quite large documents, it will be quite difficult for browser to convery safely the whole document indirectly between parties. OpenID CX expects that requesting parties can directly send propsals and receive contracts from OpenID provider. CX documents are able to be safely excanged by OpenID Authentication Artifact Binding, a draft procol which has been submitted to `OpenID Wiki`_ as OpenIDwithArtifactBinding_ by =nat .

.. _`OpenID Wiki`: http://wiki.openid.net/OpenIDwithArtifactBinding 
.. _OpenIDwithArtifactBinding: http://wiki.openid.net/OpenIDwithArtifactBinding 

OpenID Authentication Artifact Binding can be described in following char:

.. image:: openid_abx.jpg


