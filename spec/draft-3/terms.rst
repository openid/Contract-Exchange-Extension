* Party 

    * Entity which is bound to a contract and one of Client , Server , Proposer and Signatory. 
    * Party may be a web server or a smart device client.

* End User

    * Person who has privillege of controlling Privacy Data. End User MUST be identified at OpenID Provider and MAY authorize Contract to be signed and valid.

* Privacy Data

    * Data  which is own by End User and  can be accessed to permitted Party.

* Contract

    * Document to prove that Party can access Privacy Data under stated condition.

* Client

    * Privacy Data user.

* Server

    * Privacy data holder.  Exposes the Privacy Data endpoint.

* Proposer

    * Contract process initiator. Orchestrates the process of data access authorization between Clients and Server with the help of Signatory. {{ xref.OPENID_AB }}Relying Party.

* Signatory

    * Contract signer in the charge of the End User. {{ xref.OPENID_AB }} Provider.

* Request

    * Document to describe what data is wanted by Client

* Proposal
 
    * Document to hold a couple of Request and delivered to Signatory by Proposer to start the CX process.

* Acceptance
 
    * Document to describe how the privacy data can be accessed.

* Contract Part
 
    * Document which compose Contract and hold a couple of Acceptance and securely distributed to specific Party.

