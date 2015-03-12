<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="text" omit-xml-declaration="yes"/>
    <xsl:template match="/">
        Záväzná prihláška na školenie&#xA;&#xA;

        Osobné informácie:&#xA;&#xA;

           Titul: <xsl:value-of select="application/degree"/>&#xA;
           Meno: <xsl:value-of select="application/first_name"/>&#xA;
           Priezvisko: <xsl:value-of select="application/last_name"/>&#xA;

        Pracovné informácie:&#xA;&#xA;


           Firma: <xsl:value-of select="application/company"/>&#xA;
           Pobočka: <xsl:value-of select="application/division"/>&#xA;
           Pozícia: <xsl:value-of select="application/position"/>&#xA;

        Kontaktné informácie:&#xA;&#xA;

           E-mail: <xsl:value-of select="application/e_mail"/>&#xA;
           Pozícia: <xsl:value-of select="application/phone"/>&#xA;

        Adresa:&#xA;&#xA;

           Štát: <xsl:value-of select="application/state"/>&#xA;
           Obec: <xsl:value-of select="application/city"/>&#xA;
           PSČ: <xsl:value-of select="application/postal_code"/>&#xA;

        Vybrané školenia:&#xA;&#xA;

        <xsl:for-each select="application/courses/course[priority=1]">
            Priorita: 1&#xA;
            Názov: <xsl:value-of select="name"/> Termín: <xsl:value-of select="date"/>&#xA;&#xA;
        </xsl:for-each>

        <xsl:for-each select="application/courses/course[priority=2]">
            Priorita: 2&#xA;
            Názov: <xsl:value-of select="name"/> Termín: <xsl:value-of select="date"/>&#xA;&#xA;
        </xsl:for-each>

        <xsl:for-each select="application/courses/course[priority=3]">
            Priorita: 3&#xA;
            Názov: <xsl:value-of select="name"/> Termín: <xsl:value-of select="date"/>&#xA;&#xA;
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>