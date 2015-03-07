<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
    <html>
        <body>
            <div>
                <h1>Záväzná prihláška na školenie</h1>
                <p>
                    <label>Osobné informácie:</label>
                    <h2>
                        <xsl:value-of select="application/degree"/>&#160;
                        <xsl:value-of select="application/first_name"/>&#160;
                        <xsl:value-of select="application/last_name"/>
                    </h2>
                </p>
                <p>
                    <label>Pracovné informácie:</label>
                    <h4>
                        <div>Firma: <small><xsl:value-of select="application/company"/></small></div>
                        <div>Pobočka: <small><xsl:value-of select="application/division"/></small></div>
                        <div>Pozícia: <small><xsl:value-of select="application/position"/></small></div>
                    </h4>
                </p>
                <p>
                    <label>Kontaktné informácie:</label>
                    <h4>
                        <div>E-mail: <small><xsl:value-of select="application/e_mail"/></small></div>
                        <div>Telefónne číslo: <small><xsl:value-of select="application/phone"/></small></div>
                    </h4>
                    <h4>
                        <div>
                            Adresa: <small><xsl:value-of select="application/city"/>,&#160;
                            <xsl:value-of select="application/postal_code"/>,&#160;
                            <xsl:value-of select="application/state"/></small>
                        </div>
                    </h4>
                </p>
            </div>
            <div>
                <xsl:for-each select="application/courses/course[priority=1]">
                    <div>
                        Účastník sa NAJVIAC túži zúčastniť kurzu: <b><xsl:value-of select="name"/></b>, ktorý sa bude konať dňa: <b><xsl:value-of select="date"/></b>
                    </div>
                </xsl:for-each>
                <xsl:for-each select="application/courses/course[priority=2]">
                    <div>
                        Účastník sa TROCHU MENEJ túži zúčastniť kurzu: <b><xsl:value-of select="name"/></b>, ktorý sa bude konať dňa: <b><xsl:value-of select="date"/></b>
                    </div>
                </xsl:for-each>
                <xsl:for-each select="application/courses/course[priority=3]">
                    <div>
                        Účastník sa NAJMENEJ, ALE PREDSA, túži zúčastniť kurzu: <b><xsl:value-of select="name"/></b>, ktorý sa bude konať dňa: <b><xsl:value-of select="date"/></b>
                    </div>
                </xsl:for-each>
            </div>
        </body>
    </html>
    </xsl:template>
</xsl:stylesheet>