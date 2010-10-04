Draft-3
=======

Knows Issue and TODO
----------------------

- "3.2.1.  Non-Normative Examples" MUST be rewritten.
- Signature is going to be based on "JSON Simple Sign 1.0<json-simple-sign-1_0_>"
- Encryption is going to be based on "JSON Simple Encryption 1.0<json-simple-enc-1_0_>".

.. _json-simple-sign-1_0 : http://bitbucket.org/openid/ab/raw/4325e6a219dd/json-simple-sign-1_0.html
.. _json-simple-enc-1_0 : http://bitbucket.org/openid/ab/raw/4325e6a219dd/json-simple-enc-1_0.html
   


File Structure
--------------


1. README
~~~~~~~~~

- readme.rst

2. GENERATOR
~~~~~~~~~~~~

- __init__.py           
- makedoc.py  

3. Jinja Template
~~~~~~~~~~~~~~~~~~

Some template(.tmpl file) include sample JSON files (.json).
Some template referes external parameters defined ReST file ( .rst ) which are processed in makedoc.py before Jinja2 processing.

::

        rfc.tmpl  
         |
         +--  front.tmpl  
         |     +-- abstract.tmpl
         +--  middle.tmpl
         |     |
         |     +-- requirement_notation.tmpl 
         |     +--  definition_convention.tmpl
         |     +-- overview.tmpl
         |     +-- files.tmpl
         |     |     +-- json.tmpl
         |     |     +-- structures.tmpl
         |     |     |     +-- non-normative_examples.tmpl
         |     |     |     +-- request.tmpl ( request.rst / request.json )
         |     |     |     +-- proposal.tmpl ( proposal.rst / proposal.json )
         |     |     |     +-- acceptance.tmpl (acceptance.rst / acceptance.json )
         |     |     |     +-- contract.tmpl (contract.rst / contract.json )
         |     |     |     +-- status.tmpl (status.rst / status.json )
         |     |     |
         |     |     +-- storage_timestamping.tmpl
         |     +-- protocol.tmpl
         |     |           +-- sending_proposal.tmpl
         |     |           +-- accepting_proposal.tmpl
         |     |           +-- receiving_contract.tmpl
         |     |           +-- notify_contract_status.tmpl
         |     |           +-- data_request.tmpl ( data_request.rst , encrypted_response.rst    )
         |     +-- security_considerations.tmpl
         |     +-- acknowlegements.tmpl
         +-- back.tmpl


Partial Contract
----------------

- http://t.co/VRG8pgw

- Proposal is referered by only its identifier with fragments.
- A party MUST be given simple ordinal number or like that. 

 -  A partial contract is specified with CX Contract identifier with this ordinal number.


Reuquest
--------

- Related Reuqest and their signatures are dropped.
- endpoint added.

OpenID Contract Exchange
========================

- makedoc.py genrate XML for RFC
- using Jinja2 for templating
- main template is "rfc.tmpl"
- python makedoc.py  > openid-cx-draft-2.xml


Preparations
============

- Python 
- Jinja2 ( for templating )
- docutils ( for reStructredText processing )

Structure 
=========

- main tempalte is "rfc.tmpl" which is targed by "makedoc.py" to render.
- Parameter lists used in this document are simple reStrucuturedText file with ".rst" .
- Parameter lists are parsed into Python 'dict's.  Those are packed into Jinja2 "context" in "makedock.py". 
- `*.json` files are inserted as non-normatived example in the spec document.
