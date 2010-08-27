* type

    * string(URI)
    * "http://specs.openid.net/cx/1.0/#signed_request"

* id

    * string(URI)
    * URI which specify this signed request 
    * This  MAY is used by other CX Requests for describing the relation ships.

* client_certs

    * string(base64url)
    * The PEM formatted string version of client_id's X.509 certificate used for this Magic Envelope JSON.

* server_certs

    * optional,string(base64url)
    * The PEM formatted string version of server_id's X.509 certificate used when "server_id" specified in Request. 
