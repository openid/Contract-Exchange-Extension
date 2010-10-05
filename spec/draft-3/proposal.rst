* type 

    * string(URI)
    * http://specs.openid.net/cx/1.0/#proposal

* id  

    * string(URI)
    * unique identifier for a specific CX Proposal specified by the RP

* proposer_id 

    * string(URI)
    * Identifier for RP. 

* reqs

    * array of object( {{ xref.JSON_SIMPLE_SIGN_1_0 }} )
    * JSON array of  CX Requests in token string format.

* notify

    * optional,string(URI)
    * OP MAY directly send message to this URI.  As described later in Notification, an OP MAY notify the status of a CX Contract to the RP.

* proposer_certs

    * string(base64url)
    * The PEM formatted string version of RP's X.509 certificate used for this {{ xref.JSON_SIMPLE_SIGN_1_0 }} envelope.
