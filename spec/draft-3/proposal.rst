* type 

    * string(URI)
    * http://specs.openid.net/cx/1.0/#proposal

* id  

    * string(URI)
    * unique identifier specified by the RP

* reqs

    * array of object(OAuth Signature Envelope Token)
    * JSON array of  CX Requests in token string format.

* notify

    * optional,string(URI)
    * OP MAY directly send message to this URI.  As described later in Notification, an OP MAY notify the status of a CX Contract to the RP.
