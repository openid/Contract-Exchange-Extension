* type

    * string(URI)
    * {{cxurl}}#request"

* id

    * optional,string(URI))
    *  Identifier for the particular Request file

* client_id

    * string(URI)
    * Identifier for Client.

* server_id

    * optional,string(URI) 
    * Identifier for Server.
    * This parameter MAY be specified only when Client wants End User to permit to use a particular service.  In this case, Client has already known the service endpoint.

* payment_to

    * optional,string(any)
    * End User SHOULD be given "payment_to" from  Client for every CX service request to the service endpoint of Contract.

* payment_from

    * optional,string(any)
    * End User SHOULD pay  "payment_from" to  Client for every CX service request of Contract. 

* template

    * optional,string(any)
    * This describes what Client wants as Presonal Information. Also conditions or jurisdic statement SHOULD be stated or refered for utilizing End User's Personal Information.  End User MAY read this text to agree to create  Contract. 

* template_type

    * optiona,string(Content-Type)
    * Type of text provided by "template". Default is "text/plain".

* endpoint

    * optional,string(URI)
    * URI from which data is provieded at Server. Specified only when Client want Personal Information from a specific Server.

* notify

    * optional,string(URI)
    * Notifiation endpoint directely called by Party like Propose if Contract is provieded. Notification protocol described in "{{ xref.notify_contract_status }}" section later.

* identity

    * optional,string
    * End user's OpenID identfier at Server.  Mostly is not specified.

* client_certs

    * string(base64url)
    * Base64URL formatted string version of client_id's DER( defined in {{ xref.X_690 }} )  encoded  X.509 certificate used for this {{ xref.JSON_SIMPLE_SIGN_1_0 }} JSON.

* server_certs

    * optional,string(base64url)
    * Base64URL formatted string version of server_id's DER( defined in {{ xref.X_690 }} )  encoded X.509 certificate used when "server_id" specified in Request. 
