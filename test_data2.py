#coding: utf-8
__author__ = 'Ján Krivý'


class Data:
    def __init__(self):
        self.xml = """<?xml version="1.0" encoding="UTF-8"?>
<application>
    <degree>Ing.</degree>
    <first_name>Homer</first_name>
    <last_name>Simpson</last_name>
    <company>Springfield Nuclear Plant</company>
    <division>Sector 7-G</division>
    <position>Safety Engineer</position>
    <e_mail>homerJay@mailme.com</e_mail>
    <phone>+421 912 345 678</phone>
    <state>Kansas</state>
    <city>Springfield</city>
    <postal_code>845 45</postal_code>
    <courses>
        <course>
            <name>Univerzálne Windows aplikácie</name>
            <priority>3</priority>
            <date>3.3.2015</date>
        </course>
        <course>
            <name>Data Warehousing Fundamentals Certification Course</name>
            <priority>2</priority>
            <date>10.3.2015</date>
        </course>
        <course>
            <name>Pokrocilé webové aplikácie</name>
            <priority>1</priority>
            <date>5.3.2015</date>
        </course>
    </courses>
</application>"""
        self.schema = """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <xs:simpleType name="Degree">
        <xs:restriction base="xs:string">
            <xs:enumeration value="Bc."/>
            <xs:enumeration value="Mgr."/>
            <xs:enumeration value="Mgr. art."/>
            <xs:enumeration value="Ing."/>
            <xs:enumeration value="Ing. arch."/>
            <xs:enumeration value="RNDr."/>
            <xs:enumeration value="PharmDr."/>
            <xs:enumeration value="PhDr."/>
            <xs:enumeration value="JUDr."/>
            <xs:enumeration value="PaedDr."/>
            <xs:enumeration value="ThDr."/>
            <xs:enumeration value="MUDr."/>
            <xs:enumeration value="MDDr."/>
            <xs:enumeration value="MVDr."/>
            <xs:enumeration value="MBA"/>
            <xs:enumeration value="ThLic."/>
            <xs:enumeration value="PhD."/>
            <xs:enumeration value="ArtD."/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="Priority">
        <xs:restriction base="xs:positiveInteger">
            <xs:pattern value="[1-3]"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="StringType">
        <xs:restriction base="xs:normalizedString">
            <xs:minLength value="0" />
            <xs:maxLength value="50" />
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="DateType">
        <xs:restriction base="xs:string">
            <xs:pattern value="\d{1,2}(\.)\d{1,2}(\.)\d{4}"></xs:pattern>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="Email">
        <xs:restriction base="xs:string">
            <xs:pattern value="[^@]+@[^\.]+\..+"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="Phone">
        <xs:restriction base="xs:string">
            <xs:pattern value="(\+421)? 9?\d{2} ?\d{3} ?\d{3}"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="PostalCode">
        <xs:restriction base="xs:string">
            <xs:pattern value="\d{3}\s?\d{2}"/>
        </xs:restriction>
    </xs:simpleType>

    <xs:element name="application">
    <xs:complexType>
    <xs:sequence>
        <xs:element name="degree" type="Degree" minOccurs="1" maxOccurs="1" />
        <xs:element name="first_name" type="StringType" minOccurs="1" maxOccurs="1" />
        <xs:element name="last_name" type="StringType" minOccurs="1" maxOccurs="1" />
        <xs:element name="company" type="StringType" minOccurs="1" maxOccurs="1" />
        <xs:element name="division" type="StringType" minOccurs="1" maxOccurs="1" />
        <xs:element name="position" type="StringType" minOccurs="1" maxOccurs="1" />
        <xs:element name="e_mail" type="Email" minOccurs="1" maxOccurs="1" />
        <xs:element name="phone" type="Phone" minOccurs="1" maxOccurs="1" />
        <xs:element name="state" type="StringType" minOccurs="1" maxOccurs="1" />
        <xs:element name="city" type="StringType" minOccurs="1" maxOccurs="1" />
        <xs:element name="postal_code" type="PostalCode" minOccurs="1" maxOccurs="1" />
        <xs:element name="courses" minOccurs="1" maxOccurs="1">
        <xs:complexType>
        <xs:sequence>
            <xs:element name="course" minOccurs="1" maxOccurs="3">
                <xs:complexType>
                <xs:sequence>
                    <xs:element name="name" type="StringType" minOccurs="1" maxOccurs="1" />
                    <xs:element name="priority" type="Priority" minOccurs="1" maxOccurs="1" />
                    <xs:element name="date" type="DateType" minOccurs="1" maxOccurs="1" />
                </xs:sequence>
                </xs:complexType>
                <xs:unique name="uniquePriority">
                    <xs:selector xpath="priority"/>
                    <xs:field xpath="."/>
                </xs:unique>
            </xs:element>
        </xs:sequence>
        </xs:complexType>
        </xs:element>
    </xs:sequence>
    </xs:complexType>
    </xs:element>
</xs:schema>"""
        self.transformation= """<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="text" omit-xml-declaration="yes"/>
    <xsl:template match="/">
        Záväzná prihláška na školenie<xsl:text>&#10;&#13;</xsl:text>

        Osobné informácie:<xsl:text>&#10;&#13;</xsl:text>

           Titul: <xsl:value-of select="application/degree"/><xsl:text>&#10;&#13;</xsl:text>
           Meno: <xsl:value-of select="application/first_name"/><xsl:text>&#10;&#13;</xsl:text>
           Priezvisko: <xsl:value-of select="application/last_name"/><xsl:text>&#10;&#13;</xsl:text>

        Pracovné informácie:<xsl:text>&#10;&#13;</xsl:text>


           Firma: <xsl:value-of select="application/company"/><xsl:text>&#10;&#13;</xsl:text>
           Pobočka: <xsl:value-of select="application/division"/><xsl:text>&#10;&#13;</xsl:text>
           Pozícia: <xsl:value-of select="application/position"/><xsl:text>&#10;&#13;</xsl:text>

        Kontaktné informácie:<xsl:text>&#10;&#13;</xsl:text>

           E-mail: <xsl:value-of select="application/e_mail"/><xsl:text>&#10;&#13;</xsl:text>
           Pozícia: <xsl:value-of select="application/phone"/><xsl:text>&#10;&#13;</xsl:text>

        Adresa:<xsl:text>&#10;&#13;</xsl:text>

           Štát: <xsl:value-of select="application/state"/><xsl:text>&#10;&#13;</xsl:text>
           Obec: <xsl:value-of select="application/city"/><xsl:text>&#10;&#13;</xsl:text>
           PSČ: <xsl:value-of select="application/postal_code"/><xsl:text>&#10;&#13;</xsl:text>

        Vybrané školenia:<xsl:text>&#10;&#13;</xsl:text>

        <xsl:for-each select="application/courses/course[priority=1]">
            Priorita: 1<xsl:text>&#10;&#13;</xsl:text>
            Názov: <xsl:value-of select="name"/> Termín: <xsl:value-of select="date"/><xsl:text>&#10;&#13;</xsl:text>
        </xsl:for-each>

        <xsl:for-each select="application/courses/course[priority=2]">
            Priorita: 2<xsl:text>&#10;&#13;</xsl:text>
            Názov: <xsl:value-of select="name"/> Termín: <xsl:value-of select="date"/><xsl:text>&#10;&#13;</xsl:text>
        </xsl:for-each>

        <xsl:for-each select="application/courses/course[priority=3]">
            Priorita: 3<xsl:text>&#10;&#13;</xsl:text>
            Názov: <xsl:value-of select="name"/> Termín: <xsl:value-of select="date"/><xsl:text>&#10;&#13;</xsl:text>
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>"""