* endpoint

    *  REQUIRED Value: URI. 
    *  If this uri is  a contract identfier, the OP MUST return the CX Contract specified by this identfiier. 
    *  If this uri is  a endpoint of a CX Sdata, the party MUST return the data.

* party

    * REQUIRED Value: An identfier of a party bound to the CX Contract. The data responding party MUST encrypt the data ith the public key of this party, encode into a base64 string and returns in text/plain content type. 

* cx_id

    * REQUIRED for the obligation endpoint. Value: CX Contract identfier including the obligation. 
