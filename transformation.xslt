<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
    Záväzná prihláška na školenie \n\n

===========================================================================\n
Osobné informácie: \n
----------------------------------------------------------------------------
|                                                                          |\n
|   Titul: <xsl:value-of select="application/degree"/>                     |\n
|   Meno: <xsl:value-of select="application/first_name"/>                  |\n
|   Priezvisko: <xsl:value-of select="application/last_name"/>             |\n
|                                                                          |\n
----------------------------------------------------------------------------\n
\n\n
Pracovné informácie: \n
----------------------------------------------------------------------------\n
|                                                                           |\n
|   Firma: <xsl:value-of select="application/company"/>                     |\n
|   Pobočka: <xsl:value-of select="application/division"/>                  |\n
|   Pozícia: <xsl:value-of select="application/position"/>                  |\n
|                                                                           |\n
----------------------------------------------------------------------------\n
\n\n
Kontaktné informácie: \n
----------------------------------------------------------------------------\n
|                                                                           |\n
|   E-mail: <xsl:value-of select="application/e_mail"/>                     |\n
|   Pozícia: <xsl:value-of select="application/phone"/>                     |\n
|                                                                           |\n
----------------------------------------------------------------------------\n
\n\n
Adresa: \n
----------------------------------------------------------------------------
|                                                                           |\n
|   Štát: <xsl:value-of select="application/state"/>                        |\n
|   Obec: <xsl:value-of select="application/city"/>                         |\n
|   PSČ: <xsl:value-of select="application/postal_code"/>                   |\n
|                                                                           |\n
----------------------------------------------------------------------------\n
\n\n
Vybrané školenia: \n
----------------------------------------------------------------------------\n
\n\n

<xsl:for-each select="application/courses/course[priority=1]">
Priorita: 1\n
Názov: <xsl:value-of select="name"/> Termín: <xsl:value-of select="date"/>\n\n
</xsl:for-each>

<xsl:for-each select="application/courses/course[priority=2]">
Priorita: 2\n
Názov: <xsl:value-of select="name"/> Termín: <xsl:value-of select="date"/>\n\n
</xsl:for-each>

<xsl:for-each select="application/courses/course[priority=3]">
Priorita: 3\n
Názov: <xsl:value-of select="name"/> Termín: <xsl:value-of select="date"/>\n\n
</xsl:for-each>
----------------------------------------------------------------------------\n
    </xsl:template>
</xsl:stylesheet>