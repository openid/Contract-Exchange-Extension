Draft-3
=======

Known Issue and TODO
----------------------

1.  Request is to be copied, or to be refered, or to be included to provide Acceptance.

  - Curently "copied"
  - =Nat suggested to be refered.
  - It should better to be included in Acceptance.
   
     - Point is "refering parameters in Request if those are not described in Acceptance".
     - If Proposer MUST provide the original Proposal endpoint, any party can download. Proposal contains Requests.
     - In such a case, a smart client can't be a Proposer.

2. Client can be notified by Proposer. How about Servers ?

  - Currently a Server gets to know when it firstly is requested Personal Information.
  - But someone may think it is too late.
  - At the time when Client's Request is bound to a Server's service ?

3. Service binding

  - What Personal Information is hosted by which Server.
  - Currently no discovery mechanizm is provided in CX.
  - At least, Signatory(OP) must catalog the list of Personal Information Server, endopint and X.509 certificate. The list must be indexed or selected by the type of Personal Information.
  - XRD,XRDS,..... some descripter should be defined? 

    - Go to `Discovery <http://trac.hdknr.com/wiki/Discovery>`_


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
         |     +-- definition_convention.tmpl
         |     +-- terms.tmpl ( terms.rst )
         |     +-- overview.tmpl
         |     |     +-- proposal.txt
         |     |     +-- contract_part_client.txt 
         |     |     +-- contract_part_server.txt 
         |     +-- files.tmpl
         |     |     +-- json.tmpl
         |     |     +-- structures.tmpl
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
         |     |           +-- data_request.tmpl ( data_request.rst  )
         |     |                      +--- access_log.templ 
         |     |                      ( access_log.rst,access_log_file.rst, access_log_file.jsong )
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
