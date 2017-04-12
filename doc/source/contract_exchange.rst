.. _contract_exchange:

==================
Contract Exchange 
==================


Protocol
=================

Contract Exchange(CX) is a protocol to create :term:`Contract`, to share privacy data and to provide access log.

 - Creating Contact
  
   - Proposal process & Agreement process
   - Contract provisioning with encrypted JSON

 - Sharing privacy data

   - Encrypted JSON

 - Access log

   - Negotiating metadata
   - Encypted JSON

Components
===========

CX consists of the following components.

- OpenID Artifact Binding
- JSON
- X.509 and PKI
- JSON Simple Sign
- JSON Simple Encryption
- Token

 - Token is a serialization format in the process of JSON SImple Sign.


Process
========

- Service Advertisement
 
  - :term:`Client` provides :term:`Request`.
  - :term:`Proposer` collects all necessary :term:`Request` from all :term:`Client`.
  - :term:`Proposer` advertise his service.

- Proposal 

  - :term:`End User` starts CX procedure for the service provied by :term:`Proposer`.

- Agreement

  - :term:`End User` agrees the :term:`Proposal` and :term:`Signatory` creates a :term:`Contract`.

- Contract Provisioning

 - :term:`Proposer` gets his :term:`Contract Part`.
 - :term:`Proposer` is notified his :term:`Contract Part` available.
 - :term:`Client` is notified his :term:`Contract Part` available.
 - :term:`Server` realizes that  his :term:`Contract Part` available.

- Personal Information Sharing

 - :term:`Client` request :term:`End User` s privacy data at :term:`Server`.

- Log Gathering

 - :term:`Signatory` collects all access log from all :term:`Client` and :term:`Server`.

Party
=====


Client
------

- Client describe what privacy data he want to provide some services in Request token .
- Client request privacy data to  Server.

.. graphviz::

   digraph {
      graph [ rankdir = LR ];
      Client [shape = box ,height=1.0 ,width=1.0];
      Server [shape = box ,height=1.0 ,width=1.0];
      "Personal Information" [shape = hexagon];

      "Client" -> "Server" [label = "request(client id + contract id)"];
      "Server" -> "Personal Information" [arrowhead="none"];
   }

Server
------

- Server response encrypted privacy data to Client.

.. graphviz::

   digraph {
      graph [ rankdir = LR ];
      Client [shape = box ,height=1.0 ,width=1.0];
      Server [shape = box ,height=1.0 ,width=1.0];
      "Personal Information" [shape = hexagon];

      "Client" -> "Server" [label = "response(encypted privacy data)",arrowhead=none,arrowtail=normal];
      "Server" -> "Personal Information" [arrowhead="none"];
   }

