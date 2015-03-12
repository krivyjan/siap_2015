<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
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
</xsl:stylesheet>