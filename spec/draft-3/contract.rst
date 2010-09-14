* type

    * string(URI)
    * http://specs.openid.net/cx/1.0/#contract

* id 

    * opitinal,string(URI) 
    * Identifier to this Contract

* contract_id

    * string(URI) 
    * unique URL given by OP
    * OP MUST return this CX Contract in encrypted payload using requester's public key. A request MUST be a party bound to this CX Contract.
    * All Contracts produced from a Proposal MUST be same id.

* party_id

    * string(URI)
    * client_id or server id for a Proposal.
    * contract_id + party_id MUST be globally unqiue.

* proposal_id

    * string(URI) 
    * Identifier to original Proposal. Fragment(#) MUST be appended to the end of the original Proposal URI. The value of the fragment is the digest of the Propsal itself after optional digesting prefix separated colon(":").  Default digesting algorithm is SHA-256, so default prefix is "sha256:" if it is not specified.

* acceptances

    * array of object(Acceptance)
    * JSON array of  CX Acceptance  
