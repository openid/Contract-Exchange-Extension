* type 

    *  string(URI)
    *  "http://specs.openid.net/cx/1.0/#keys",   

* parties

    * array of string(URI)
    * JSON array of URI specifying  paties.

* keys

    * array of string 
    * JSON array of base64 form of shared keys.
    * So,   the same shared key MUST be used for the JSON Encrypted Envelope dedicated for the same party.
    * The order in keys MUST correspond the order of parties member.
