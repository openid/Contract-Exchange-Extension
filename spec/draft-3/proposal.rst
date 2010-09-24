* type 

    * string(URI)
    * http://specs.openid.net/cx/1.0/#proposal

* id  

    * string(URI)
    * unique identifier specified by the RP

* reqs

    * array of object(OAuth Signature Envelope Token)
    * JSON array of  CX Requests in token string format.

* sighash 

    *  string(base64url)
    *  SHA256( reqs[0].sigs + reqs[1].sigs ... + reqs[n].sigs)

* hashalg

    *  optional,string
    *  A hash algorithm used for calculating sighash member.
    *  "SHA256" is default.

* notify

    * optional,string(URI)
    * OP MAY directly send message to this URI.  As described later in Notification, an OP MAY notify the status of a CX Contract to the RP.
