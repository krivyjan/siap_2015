<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
    <html>
        <body>
            <div>
                <h1>Záväzná prihláška na školenie</h1>
                <p>
                    <label>Osobné informácie:</label>
                    <h3>
                        <small>Titul: </small><xsl:value-of select="application/degree"/>&#160;
                        <small>Meno: </small><xsl:value-of select="application/first_name"/>&#160;
                        <small>Priezvisko: </small><xsl:value-of select="application/last_name"/>
                    </h3>
                </p>
                <p>
                    <label>Pracovné informácie:</label>
                    <h4>
                        <small>Firma: </small><xsl:value-of select="application/company"/>&#160;
                        <small>Pobočka: </small><xsl:value-of select="application/division"/>&#160;
                        <small>Pozícia: </small><xsl:value-of select="application/position"/>
                    </h4>
                </p>
                <p>
                    <label>Kontaktné informácie:</label>
                    <h4>
                        <small>E-mail: </small><xsl:value-of select="application/e_mail"/>&#160;
                        <small>Telefónne číslo: </small><xsl:value-of select="application/phone"/>
                    </h4>
                </p>
                <p>
                    <label>Adresa:</label>
                    <h4>
                        <small>Štát: </small><xsl:value-of select="application/state"/>&#160;
                        <small>Obec: </small><xsl:value-of select="application/city"/>&#160;
                        <small>PSČ: </small><xsl:value-of select="application/postal_code"/>
                    </h4>
                </p>
            </div>
            <div>
                <label>Vybrané školenia:</label>
                <xsl:for-each select="application/courses/course[priority=1]">
                    <h4>
                        <small>Priorita: </small>1<br/>
                        <small>Názov: </small><xsl:value-of select="name"/>&#160;
                        <small>Termín: </small><xsl:value-of select="date"/>
                    </h4>
                </xsl:for-each>
                <xsl:for-each select="application/courses/course[priority=2]">
                    <h4>
                        <small>Priorita: </small>2<br/>
                        <small>Názov: </small><xsl:value-of select="name"/>&#160;
                        <small>Termín: </small><xsl:value-of select="date"/>
                    </h4>
                </xsl:for-each>
                <xsl:for-each select="application/courses/course[priority=3]">
                    <h4>
                        <small>Priorita: </small>3<br/>
                        <small>Názov: </small><xsl:value-of select="name"/>&#160;
                        <small>Termín: </small><xsl:value-of select="date"/>
                    </h4>
                </xsl:for-each>
            </div>
        </body>
    </html>
    </xsl:template>
</xsl:stylesheet>