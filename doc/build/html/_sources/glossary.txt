.. _glossary:

========
Glossary
========


Terminology
================

.. glossary::

    Party
        Entity which is bound to a contract and one of Client , Server , Proposer and Signatory.
        Party may be a web server or a smart device client.

    End User
        Person who has privillege of controlling Personal Information. End User MUST be identified at OpenID Provider and MAY authorize Contract to be signed and valid.

    Personal Information
        Data which is own by End User and can be accessed to permitted Party.

    Contract
        Document to prove that Party can access Personal Information under stated condition.

    Contract Identifier
        Unique URI to specify a particular contract. All :term:`Contract Part` has the same contract identfier.
        :term:`Contract` can be transmitted from this URI as data endpoint.

    Client
        Personal Information user.

    Server
        Personal Information holder. Exposes the Personal Information endpoint.

    Proposer
        Contract process initiator. Orchestrates the process of data access authorization between Clients and Server with the help of Signatory. OpenID Artifact Binding 1.0 (Protivity Government Services and Nomura Research Institute, “OpenID Artifact Binding 1.0,” September 2010.) [OPENID_AB]Relying Party.

    Signatory
        Contract signer in the charge of the End User. OpenID Artifact Binding 1.0 (Protivity Government Services and Nomura Research Institute, “OpenID Artifact Binding 1.0,” September 2010.) [OPENID_AB] Provider.

    Request
        Document to describe what data is wanted by Client

    Proposal
        Document to hold a couple of Request and delivered to Signatory by Proposer to start the CX process.

    Acceptance
        Document to describe how the privacy data can be accessed.

    Contract Part
        Document which compose Contract and hold a couple of Acceptance and securely distributed to specific Party.

    Token
        Signed JSON object which serialized into a formated string. Format is defined i nJSON Simple Sign 1.0 (Protivity Government Services and Nomura Research Institute, “JSON Simple Sign ver.1 draft00,” September 2010.) [JSON_SIMPLE_SIGN_1_0].

    Service
        Data or experience provided by Proposer to End User. Some Services consist of couple of End User's Personal Information which are provided by Server and used by Client. Parties MUST fulfill Contract to collaborate to provide Service.

    OpenID AX
        "OpenID Attribute Exchange is an OpenID service extension for exchanging identity information between endpoints. Messages for retrieval and storage of identity information are provided." - `OpenID Attribute Exchange 1.0 <http://openid.net/specs/openid-attribute-exchange-1_0.html>`_ .

    typeURI
        URI to describe data schema. Used in :term:`OpenID AX`. `AXSchema.org <http://www.axschema.org/>`_  is a community project to define attribute types for use with OpenID Attribute Exchange.

    LRDD
        LRDD (pronounced 'lard') provides a process for obtaining information  about a resource identified by a Uniform Resource Identifier (URI).
        See http://www.delicious.com/hdknr/LRDD
