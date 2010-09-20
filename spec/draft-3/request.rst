* type

    * string(URI)
    * http://specs.openid.net/cx/1.0/#request"

* id

    * optional,string(URI))
    *  Identifier for the particular CX Request file

* client_id

    * string(URI)
    * Identifier for the requesting party.

* server_id

    * optional,string(URI) 
    * Identifier for the responding party
    * This parameter MAY be specified only  when a requesting party want the End User to use a particular service.
    * In this case, the requesting party has already known the service endpoint.

* payment_to

    * optional,string(any)
    * End User SHOULD be given "payment_to" from the party specified by  "client_id" for every CX service request to the service endpoint provided the party  identified by "server_id".

* payment_from

    * optional,string(any)
    * End User SHOULD pay  "payment_from" to  the party specified by  "client_id" for every CX service request 

* template

    * optional,string(any)
    * End User MAY read "template" text to accept a CX Contract. 

* endpoint

    * optional,string(URI)
    * URI from which data is provieded at the responding party specified by 'server_id' 

* notify

    * optional,string(URI)
    * Notifiation endpoint directely called by RP if CX Contract is provieded.

* identifier

    * optional,string
    * End user's identfier at the responding party specified by 'server_id'
