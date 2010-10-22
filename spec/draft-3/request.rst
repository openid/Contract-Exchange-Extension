* type

    * string(URI)
    * http://specs.openid.net/cx/1.0/#request"

* id

    * optional,string(URI))
    *  Identifier for the particular Request file

* client_id

    * string(URI)
    * Identifier for Client.

* server_id

    * optional,string(URI) 
    * Identifier for Server.
    * This parameter MAY be specified only when Client wants End User to permit to use a particular service.
    * In this case, Client has already known the service endpoint.

* payment_to

    * optional,string(any)
    * End User SHOULD be given "payment_to" from  Client for every CX service request to the service endpoint of Contract.

* payment_from

    * optional,string(any)
    * End User SHOULD pay  "payment_from" to  Client for every CX service request of Contract. 

* template

    * optional,string(any)
    * End User MAY read "template" text to agree to create  Contract. 

* template_type

    * optiona,string(Content-Type)
    * Type of text provided by "template". Default is "text/plain".

* endpoint

    * optional,string(URI)
    * URI from which data is provieded at Server.

* notify

    * optional,string(URI)
    * Notifiation endpoint directely called by Party like Propose if Contract is provieded.

* identity

    * optional,string
    * End user's OpenID identfier at Server

* client_certs

    * string(base64url)
    * The PEM formatted string version of client_id's X.509 certificate used for this {{ xref.JSON_SIMPLE_SIGN_1_0 }} JSON.

* server_certs

    * optional,string(base64url)
    * The PEM formatted string version of server_id's X.509 certificate used when "server_id" specified in Request. 
