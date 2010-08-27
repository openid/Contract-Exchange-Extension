* cx_encoding

    * Value: "Base64", "CBC-256-128-PKCS5_PADDING".
    * If cx_encoding is "CBC-256-128-PKCS5_PADDING", the following parameters MUST be returned in addition.

* cx_enc_key

    * Shared key to encrypt the message in "Encryption Base String" form. This key itself is encrypted asymmetrically with decryptors' public key included in the Contract and base 64 encoded. 
    * Value: base64 string.

* cx_enc_iv

    * Type URI for initialization vector used in a block encryption.
