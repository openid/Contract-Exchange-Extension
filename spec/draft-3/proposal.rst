* type 

    * string(URI)
    * http://specs.openid.net/cx/1.0/#proposal

* id  

    * string(URI)
    * unique identifier for a specific Proposal specified by Proposer

* proposer_id 

    * string(URI)
    * Identifier for Proposer

* reqs

    * array of object( {{ xref.JSON_SIMPLE_SIGN_1_0 }} )
    * JSON array of Requests Token.

* notify

    * optional,string(URI)
    * Signatory MAY directly send message to this URI.  As described later in "{{ xref.notify_contract_status }}" section later, Signatory MAY notify the status of  Contract to Proposer.

* proposer_certs

    * string(base64url)
    * Base64URL formatted string version of Proposer's DER (defined in {{ xref.X_690 }} ) encoded X.509 certificate used for this {{ xref.JSON_SIMPLE_SIGN_1_0 }} envelope.
