Eash attribute and element is decribed as following with cardinality:

``/Contract/@id`` [Required]

 A global unique Identifier of type string that identifies this contracrt. 

``/Contract/Type`` [One] 

 Either http://openid.net/srv/cx/1.0/#proposal or http://opeind.net/srv/cx/1.0#agreement

``/Contract/DateTime`` 

 The creation dateTime of this Proposal or Agreement. 

``/Contract/Party`` [Two or More]

 A placeholder for the information related to the party.  While a proposal may include two or more Parties, an Agreement may contain only one. 

``/Contract/Party/URL`` [One]

 This element is the URI (or XRI) which sepcifiy the composing party.

``/Contract/Party/Rel`` [One]

 Indicates the type of the party. One of followings:

- http://openid.net/srv/cx/1.0/#proposer
- http://openid.net/srv/cx/1.0/#acceptor
- http://openid.net/srv/cx/1.0/#proxy_acceptor


``/Contract/Party/xmldsig:Signature`` [One]

 Signature are applied in the same way as defined in XRD 1.0 "`XRD Signature`_".

.. _`XRD Signature`: http://www.oasis-open.org/apps/group_public/download.php/35274/xrd-1.0-wd10.html#signature

``/Contract/Party/obligations`` [One]

 Placeholder for specifying the obligation of the party. 

``/Contract/Party/obligations/param`` [Zero or More]

 0 or more of the parameters that describes a portion of the party's obligation. 

``/Contract/Party/obligations/param/@type`` [One]

 Parameter type URL of this particular parameter.  Some of them are defined in the appendix of this specification. 
 Notably, ``http://openid.net/srv/cx/1.0/axreq`` MUST be supported by all implementations. 

``/Contract/Party/obligations/param/@id`` [One]

 Shortcut name of this parameter.  {{parameter_name}}s in CX Template CAN be replaced by the value of this element.


``/Contract/Service/Type`` [One]

 URI which specify which CX Service is used by a  Relying Party

``/Contract/Service/URL`` [One]

 OP service endpoint reuqested by a Relying Party

``/Contract/Service/Template`` [Zero or One] 

 Base64 encoded CX Template text publish from the URL specified by /Conract/Service/Type. 
 Template text MUST be in UTF-8 encoding. 
 {{name}}s in CX Template is replaced by the value of the element of which the @id is equal to 'name'.  
 Exists only in a proposal. 

``/Contract/Original`` [Zero or One]

 The requesting document has no Original element.
 The base64-encoded original requesting XML document.
