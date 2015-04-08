<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="text" omit-xml-declaration="yes"/>
    <xsl:template match="/">
        Záväzná prihláška na školenie

        Osobné informácie:

           Titul: <xsl:value-of select="application/degree"/>
           Meno: <xsl:value-of select="application/first_name"/>
           Priezvisko: <xsl:value-of select="application/last_name"/>

        Pracovné informácie: 


           Firma: <xsl:value-of select="application/company"/> 
           Pobočka: <xsl:value-of select="application/division"/> 
           Pozícia: <xsl:value-of select="application/position"/> 

        Kontaktné informácie: 

           E-mail: <xsl:value-of select="application/e_mail"/> 
           Pozícia: <xsl:value-of select="application/phone"/> 

        Adresa: 

           Štát: <xsl:value-of select="application/state"/> 
           Obec: <xsl:value-of select="application/city"/> 
           PSČ: <xsl:value-of select="application/postal_code"/> 

        Vybrané školenia: 

        <xsl:for-each select="application/courses/course[priority=1]">
            Priorita: 1 
            Názov: <xsl:value-of select="name"/> Termín: <xsl:value-of select="date"/> 
        </xsl:for-each>

        <xsl:for-each select="application/courses/course[priority=2]">
            Priorita: 2 
            Názov: <xsl:value-of select="name"/> Termín: <xsl:value-of select="date"/> 
        </xsl:for-each>

        <xsl:for-each select="application/courses/course[priority=3]">
            Priorita: 3 
            Názov: <xsl:value-of select="name"/> Termín: <xsl:value-of select="date"/> 
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>