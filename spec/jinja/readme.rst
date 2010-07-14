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
