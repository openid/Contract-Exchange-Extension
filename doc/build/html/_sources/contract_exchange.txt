.. _contract_exchange:

==================
Contract Exchange 
==================


Protocal
=================

Contract Exchange(CX) is a protocol to create :term:`Contract`, share privacy data and  provide access log.

Components
===========

CX consists of the following components.

- OpenID Artifact Binding
- JSON
- X.509 and PKI
- JSON Simple Sign
- JSON Simple Encryption


Process
========

- :term:`Client` provides :term:`Request`.
- :term:`Proposer` collects all necessary :term:`Request` from all :term:`Client`.
- :term:`Proposer` advertise his service.
- :term:`End User` starts CX procedure for the service provied by :term:`Proposer`.
- :term:`End User` agrees the :term:`Proposal` and :term:`Signatory` creates a :term:`Contract`.
- :term:`Proposer` gets his :term:`Contract Part`.
- :term:`Client` is notified his :term:`Contract Part` available.
- :term:`Server` is notified his :term:`Contract Part` available.
- :term:`Client` request :term:`End User` s privacy data at :term:`Server`.
- :term:`Signatory` collects all access log from all :term:`Client` and :term:`Server`.
