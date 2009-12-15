.. code-block:: xml

 <?xml version="1.0" encoding="UTF-8"?>
 <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" xmlns:xmldsig="http://www.w3.org/2000/09/xmldsig#">
  <xs:import namespace="http://www.w3.org/2000/09/xmldsig#" schemaLocation="http://www.w3.org/TR/xmldsig-core/xmldsig-core-schema.xsd" />
  <xs:element name="Contract">
    <xs:complexType>
      <xs:sequence>
        <xs:element ref="Type" minOccurs="1" maxOccurs="1" />
        <xs:element ref="Datetime" minOccurs="1" maxOccurs="1" />
        <xs:element maxOccurs="unbounded" ref="Party"/>
        <xs:element ref="Service" minOccurs="0" maxOccurs="1" />
        <xs:element ref="TemplateURL" minOccurs="0" maxOccurs="1" />
        <xs:element ref="Template" minOccurs="0" maxOccurs="1" />
        <xs:element ref="Original" minOccurs="0" maxOccurs="1" />
      </xs:sequence>
      <xs:attribute name="id" use="required" type="xs:string"/>
    </xs:complexType>
  </xs:element>
  <xs:element name="Datetime" type="xs:string" />
  <xs:element name="Party">
    <xs:complexType>
      <xs:sequence>
        <xs:element ref="URL" minOccurs="1" maxOccurs="1" />
        <xs:element ref="Rel" minOccurs="1" maxOccurs="1"/>
        <xs:element ref="obligations" minOccurs="1" maxOccurs="1" />
        <xs:element minOccurs="0" maxOccurs="1" ref="xmldsig:Signature"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element name="Rel"  type="xs:anyURI" />
  <xs:element name="obligations">
    <xs:complexType>
      <xs:sequence>
        <xs:element maxOccurs="unbounded" ref="param" minOccurs="0"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element name="param">
    <xs:complexType>
      <xs:simpleContent>
        <xs:extension base="xs:string">
          <xs:attribute name="id" use="required" type="xs:string" />
          <xs:attribute name="type" use="required" type="xs:anyURI" />
        </xs:extension>
      </xs:simpleContent>
    </xs:complexType>
  </xs:element>
  <xs:element name="Service">
    <xs:complexType>
      <xs:sequence>
        <xs:element ref="Type"/>
        <xs:element ref="URL"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element name="TemplateURL"  type="xs:anyURI" />
  <xs:element name="Template" type="xs:base64Binary" />
  <xs:element name="Original" type="xs:base64Binary" />
  <xs:element name="Type"  type="xs:anyURI" />
  <xs:element name="URL"   type="xs:anyURI" />
 </xs:schema>
