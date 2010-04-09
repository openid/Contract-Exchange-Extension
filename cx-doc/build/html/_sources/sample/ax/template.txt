===========================
AX:Template
===========================

Advertising the Supporting CX Contract
======================================

Because an OP can serve multile type of CX Contract, it must advertise list of supporting CX contract in some way , e.g, in its developers' web pages. 
If Google,Inc supports CX for its OpenID services, is may put CX contract information on http://code.google.com/intl/ja/apis/accounts/docs/OpenID.html .

Every CX contarct is signed based on the corresponding CX Tempalte which describes the detail of agreement, waranty , disclamier and other juridistic statement to be enforced not to breach by parties included in a CX Contract. 

Get CX Template
==================

Service advertises the following CX Contract Template


.. include:: attribute_exchange.txt.inc


Becase the digest of the content must be calculated to the following, ::

    $ openssl dgst -sha256 attribute_exchange.txt
    SHA256(attribute_exchange.txt)= c8d6c46425bf83b6eebcf9fb24ac5ff7599e97f7b24973e53ae114a1a072ec67


the CX Template for the attribute exchange must be advertised to RP developers as the follwing URI. ::

    https://www.google.com/accounts/o8/cx/attribute_exchange.txt?sha256=c8d6c46425bf83b6eebcf9fb24ac5ff7599e97f7b24973e53ae114a1a072ec67

The RP requesting a CX Proposal for profile attribue exchange to  Google must download that template from the URI and must be encoded in base64 and contained as the valueof Party/Template element in the Proposal document::

    <Template>PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KR29vZ2xlIDogSWRlbnRp
    dHkgQXR0cmlidXRlIEV4Y2hhbmdlCj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09
    PT09PT09CgpQcm9wb3Nlcjoge3sgcHJvcG9zZXJfbmFtZSB9fQotLS0tLS0tLS0tLS0tLS0t
    LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKe3sgcHJvcG9zZXIgfX0KCkFjY2VwdG9yOiB7
    eyBhY2NlcHRvcl9uYW1lIH19IAotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t
    LS0tLS0tLQoKe3sgYWNjZXB0b3IgfX0KCkF0dHJpYnRlczoKLS0tLS0tLS0tLS0tLS0tLS0t
    LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCkhlcmUgaXMgdGhlIGxpc3Qgb2YgY2xhaW1lZCBh
    dHRyaWJ1ZXMgIAoKe3sgY2xhaW1lZF9hdHRyaWJ1ZXMgfX0gCgoKUHVycG9zZSBvZiB1c2Ug
    b2YgZGF0YToKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCkxpbWl0ZWQgdG8gZW50aXRpZXMg
    cGVybWl0dGVkIGJ5IHt7IGFjY2VwdG9yIH19Cg==
    </Template>

