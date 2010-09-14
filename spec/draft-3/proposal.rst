* type 

    * string(URI)
    * http://specs.openid.net/cx/1.0/#proposal

* id  

    * string(URI)
    * unique identifier specified by the RP

* reqs

    * array of object(Signed Request)
    *  JSON array of  CX  Signed Requests

* sighash 

    *  string(base64url)
    *  SHA256( reqs[0].sigs + reqs[1].sigs ... + reqs[n].sigs)

* hashalg

    *  optional,string
    *  A hash algorithm used for calculating sighash member.
    *  "SHA256" is default.

* endpoint

    * optional,string(URI)
    * OP MAY directly send message to this URI.  As described later in Notification, an OP MAY notify the status of a CX Contract to the RP.
