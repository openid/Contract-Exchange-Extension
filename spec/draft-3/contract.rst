* type

    * string(URI)
    * http://specs.openid.net/cx/1.0/#contract_part

* id 

    * opitinal,string(URI) 
    * Identifier to this Contract

* contract_id

    * string(URI) 
    * Unique URL given by Signatory. All Contract Part provided to each Party from Proposal MUST be same. 

* party_id

    * string(URI)
    * client_id, server_id or proposer_id of this Contract.   

* proposal_id

    * string(URI) 
    * Identifier to original Proposal. Fragment(#) MUST be appended to the end of the original Proposal URI. The value of the fragment is the digest of the Propsal itself after optional digesting prefix separated colon(":").  Default digesting algorithm is SHA-256, so default prefix is "sha256:" if it is not specified.

* acceptances

    * array of object(Acceptance)
    * JSON array of Acceptance  

* signatory_certs

    * string(base64url)
    * The PEM formatted string version of Signatory's X.509 certificate used for this {{ xref.JSON_SIMPLE_SIGN_1_0 }} JSON.

