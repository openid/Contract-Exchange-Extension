.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <Contract id="e4bf53a8e97211de93e00800272c981e">
        <Type>http://openid.net/srv/cx/1.0/#proposal</Type>
        <Datetime>2009-12-15T21:10:54+9:00</Datetime>
        <Party id="http://netshop.com" >
            <Rel>http://openid.net/srv/cx/1.0/#proposer</Rel>
            <obligations>
                <param type="http://cxop.net/cx/payment/totalamount" id="taotalamount">500.0</param>
                <param type="http://cxop.net/cx/payment/title" id="title">Python Books</param>
            </obligations>
        <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <SignedInfo>
    <CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
    <SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
    <Reference>
    <Transforms>
    <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
    </Transforms>
    <DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
    <DigestValue>vSS75vnUZ/OIAkkEGr4qUjr9O2c=</DigestValue>
    </Reference>
    </SignedInfo>
    <SignatureValue>gzfVURVGlKV7UCa7kj+TyHrHU/QmPDSDw85zPzjv+/qPpAQs+2RepfoZCfBqWE1H
    V1bl307CGPDBllg4Wd3IVZViInm4j1d28/M1BA45YJdD2BOhlkf6laFI5lKXwQQe
    oEgSDZ/6ll/+s1rCU6WfZK30x2eaa6j+ZM9njsosAyE=</SignatureValue>
    <KeyInfo>
    <X509Data>
    <X509Certificate>MIICEzCCAXwCCQDFGL222nxEqDANBgkqhkiG9w0BAQUFADBOMRUwEwYDVQQDEwxu
    ZXRzaG9wLmNvbSAxGTAXBgNVBAsTEHN5cy5uZXRzaG9wLmNvbSAxDTALBgNVBAoT
    BHN5cyAxCzAJBgNVBAYTAkpQMB4XDTA5MTIxNTEyMTA1NFoXDTEwMDExNDEyMTA1
    NFowTjEVMBMGA1UEAxMMbmV0c2hvcC5jb20gMRkwFwYDVQQLExBzeXMubmV0c2hv
    cC5jb20gMQ0wCwYDVQQKEwRzeXMgMQswCQYDVQQGEwJKUDCBnzANBgkqhkiG9w0B
    AQEFAAOBjQAwgYkCgYEAtsFDpf8IYU0GHpSZMM0PgWZ7ANvbnuqv2haiCmYvVjq3
    X8Lpwb8RZY9TN5nckuAeQcNlTh8lL6Bz3v/mgwvGLuM57rLt4Rj9cbQfF8V5T+oV
    wOxsLnQB9KJHzn21Y5LdpVgGpdCvT6h8Utw9+8EHovRd2IDo2g1Mn2NuLZNP13MC
    AwEAATANBgkqhkiG9w0BAQUFAAOBgQCd+et9R8fDuGH3jyw9xEgBF73fs/06U++X
    IyJyFGDQNIZf2iKm6ZJSzjCCQsoRUlu74NP34PAq3RcPe9g6+MpN45J51dlAG2Xm
    MZ+u3qaTaAM2PBDSZM0SAa5AeOZ3w53naoIHRQjRHTTWEcrY9PQatHajq+De5IZg
    uFAx2HjGzA==</X509Certificate>
    </X509Data>
    </KeyInfo>
    </Signature></Party>
        <Party id="=hdknr">
            <Rel>http://openid.net/srv/cx/1.0/#proposer</Rel>
            <obligations/>
        </Party>
        <Service>
            <Type>http://cxop.net/cx/payment#sha256:40ea725769e6221908f08675014cff1b13e8399a5eb5555c21687d487da0b66c</Type>
            <URL>http://cxop.net/openid/</URL>
        </Service>
        <Template>PT09PT09PT09PT09PT09PT09PT09PT09PT09CklOVEVSTkVUIFBBWU1NRU5UIEFHUkVFTUVOVAo9
    PT09PT09PT09PT09PT09PT09PT09PT09PT0KCldoZXJlYXMge3tlbmRfdXNlcn19IHBheXMgZm9y
    IHRoZSBzZXJ2aWNlcyBwcm92aWRlZCBieSB7e3NlcnZpY2VfcHJvdmlkZXJ9fSBhdCB0aGUge3sg
    b3BfcHJvdm9kZXJ9fSdzIHBheW1lbnQgc2VydmljZS4gCgogMS4gICB7e2VuZF91c2VyfX0gbXVz
    dCBwYXkgdG8ge3sgb3BfcHJvdmlkZXJ9fSB1bnRpbCB0aGUgZGF5IHNwZWNpZmllZCBpbiB0aGUg
    IkNyZWRpdCBDYXJkIFBheW1lbnQgQWdyZWVtZW50IiBiZXR3ZWVuIHt7IG9wX3Byb3ZpZGVyfX0g
    YW5kIAogICAgICB7e2VuZF91c2VyfX19LiBCb3RoIG9mIHRoZW0gbXVzdCBmb2xsb3cgYWxsIHdh
    cnJhbnRpZXMgYW5kIGRpc2NsYWltZXIgd3JpdHRlcm4gb24gdGhlIGFncmVlbWVudC4KCgogMi4g
    ICB7e3NlcnZpY2VfcHJvdmlkZXJ9fSBtdXN0IGJlIHBhaWQgYnkge3sgb3BfcHJvdmlkZXIgfX0g
    YmFzZWQgb24gdGhlICJEaWdpdGFsIFBheW1lbnQgU2VydmljZSBBZ3JlZW1lbnQiIGJldHdlZW4g
    e3sgb3BfcHJvdmlkZXIgfX0KICAgICAgYW5kIHt7IHNlcnZpY2VfcHJvdmlkZXIgfX0uIEJvdGgg
    b2YgdGhlbSBtdXN0IGZvbGxvdyBhbGwgd2FycmFudGllcyBhbmQgZGlzY2xhaW1lciAgd3JpdHRl
    cm4gb24gdGhlIGFncmVlbWVudC4KCiAzLiAgIHt7c2VydmljZV9wcm92aWRlcn19IG11c3QgZGln
    aXRhbGx5IHNpZ24gdGhlIGFncmVlbWVudCBiYXNlZCBvbiB0aGlzIGRvY3VtZW50LgoKIDQuICAg
    e3tvcF9wcm92aWRlcn19IG11c3QgZGlnaXRhbGx5IHNpZ24gdGhlIGFncmVlbWVudCBiYXNlZCBv
    biB0aGlzIGRvY3VtZW50IG9uIHRoZSBiZWhhbGYgb2Yge3sgZW5kX3VzZXIgfX0uCgp7e3NlcnZp
    Y2VfcHJvdmlkZXJ9fQotLS0tLS0tLS0tLS0tLS0tLS0tLQoKIEJ5OiAgICAgIHt7cHJvcG9zZXJf
    c2lnbmF0b3J5fX0KCiBUaXRsZTogICB7e3Byb3Bvc2VyX3RpdGxlfX0KCiBEYXRlOiAgICB7e25v
    d319Cgp7e2VuZF91c2VyfX0KLS0tLS0tLS0tLS0tCgogQnk6ICAgICAge3tlbmRfdXNlcn19Cgog
    VGl0bGU6ICAge3tlbmRfdXNlcl90aXRsZX19CgogRGF0ZTogICAge3tub3d9fQoKCnt7b3BfcHJv
    dmlkZXJ9fQotLS0tLS0tLS0tLS0tLS0KCiBCeTogICAgICB7e2FjY2VwdG9yX3NpZ25hdG9yeX19
    CiAKIFRpdGxlOiAgIHt7YWNjZXB0b3JfdGl0bGV9fQogIAogRGF0ZTogICAge3tub3d9fQoK
    </Template>
    </Contract>
