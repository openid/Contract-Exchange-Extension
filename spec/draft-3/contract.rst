* type

    * string(URI)
    * http://specs.openid.net/cx/1.0/#contract

* id 

    * string(URI) 
    * unique URL given by OP
    * OP MUST return this CX Contract in encrypted payload using requester's public key. A request MUST be a party bound to this CX Contract.

* signatory_certs 

    * stirng(base64url)
    * Base 65 form of  the OP's X.509 certificate
