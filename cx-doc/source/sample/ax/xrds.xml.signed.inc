.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <XRDS>
    <XRD>
    <Service priority="0">
    <Type>http://specs.openid.net/auth/2.0/server</Type>
    <Type>http://openid.net/srv/ax/1.0</Type>
    <Type>http://specs.openid.net/extensions/ui/1.0/mode/popup</Type>
    <Type>http://specs.openid.net/extensions/ui/1.0/icon</Type>
    <Type>http://specs.openid.net/extensions/pape/1.0</Type>
    <Type>http://openid.net/srv/cx/1.0/#</Type>
    <URI>https://www.google.com/accounts/o8/ud</URI>
    </Service>
    </XRD>
    <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <SignedInfo>
    <CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
    <SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
    <Reference>
    <Transforms>
    <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
    </Transforms>
    <DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
    <DigestValue>PJ9EM2ZreuTY8tfJDLJwctzhe+A=</DigestValue>
    </Reference>
    </SignedInfo>
    <SignatureValue>nfV5MwI2OlQ9bOJ71I8RlAw5MY031YuZD/A2zKzD3llEyDsc+oTqsPN9o4q34BiW
    CGG/FjlwDvQvlEvoAayzDjnCJ2w04S0NmkQxC9wYTsVfXFEQB1a7yjE1YCP487M1
    qoLLUTzrftxjjddoskSbxaC51SNmZNQSJ59dqD/ETlo=</SignatureValue>
    <KeyInfo>
    <X509Data>
    <X509Certificate>MIICHzCCAYgCCQCb8py2cYa9YjANBgkqhkiG9w0BAQUFADBUMRgwFgYDVQQDEw93
    d3cuZ29vZ2xlLmNvbSAxHDAaBgNVBAsTE3N5cy53d3cuZ29vZ2xlLmNvbSAxDTAL
    BgNVBAoTBHN5cyAxCzAJBgNVBAYTAkpQMB4XDTEwMDQwNzA0MTAzMFoXDTEwMDUw
    NzA0MTAzMFowVDEYMBYGA1UEAxMPd3d3Lmdvb2dsZS5jb20gMRwwGgYDVQQLExNz
    eXMud3d3Lmdvb2dsZS5jb20gMQ0wCwYDVQQKEwRzeXMgMQswCQYDVQQGEwJKUDCB
    nzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAwaeeccIQ0o3htlvUR6mFnmjmsQej
    BYsh3bzNEKCzBFjGPitixrqNkmon1mpbtBnYGsbYldUydlSWU3hGV5UO24JwH8Sz
    rUPpVC1MmaY6VyENlVcIdpui8IkCSpRBVklxXYF1hEAcuWBSpNsLq9W1f5+L+p2M
    6MDsvfq0cmIvV/8CAwEAATANBgkqhkiG9w0BAQUFAAOBgQAhTnm89c+yUqd//VlN
    Q2oWK/zdVAKlVRYRE910fGkkYIUFe9bd+HGHKSazq15B09ZevTwK5ahMJq2kyKfr
    igpzPyNiAWa/DpNsLYr2VUU02gLwxgEGXs6BmjfIxZh9eAIzg2FN8SQPs9eKp6c0
    RK6Tmmt9ro8lyn4wW9XR7kb83A==</X509Certificate>
    </X509Data>
    </KeyInfo>
    </Signature></XRDS>