.. _privacy_data_and_contract:

=========================
Privacy Data and Contract
=========================

Privacy Data Sharing
====================

When sharing your privacy data, the following items must be considered.

- Meaning : What is your privacy data? How should your privacy data structured for sharing?
- Discovering : Where is your privacy data stored? 
- Granting : Who can access your privacy data?  
- Accessing : Does he have proper right to copy your privacy data?
- Utilizing : Is he keeping the privacy policy which you have enforced?  

OpenID CX for Privacy Data Sharing
==================================

OpenID CX protocol resolve like this.

- Meaning : Out of scope. OpenID AX with typeURI or other starndard can be used to negotiate.
- Discovering : Out of scope. :term:`Signatory` can be found by OpenID Authentication protocol. Privacy data source is to be bound at :term:`Signatory` in some way.
- Granting : :term:`Contract Part` is access token.
- Accessing : :term:`Client` who has his/her :term:`Contract Part` can request privacy data with :term:`Contract Identifier` in REST call specifeid by CX. Responded privacy data is encrypted with Client's public key stated in Contract Part.
- Utilizing :  :term:`Proposal` can describe or refer conditions under which privacy data is used. CX also provide access log rule.

So What is Contract?
============================

Contract is token with legal statement.

- Access token to your privacy data.
- Legal statement of the utilization of your privacy data.
