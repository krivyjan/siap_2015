<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"  xmlns:egonp="http://schemas.gov.sk/form/ED.DeliveryStatus/1.2">
<xsl:output method="xhtml" xpath-default-namespace="http://www.w3.org/1999/xhtml" indent="yes" omit-xml-declaration="yes"/>
<xsl:template match="/">
<xsl:text disable-output-escaping='yes'>&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"&gt;</xsl:text>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
<meta http-equiv="X-UA-Compatible" content="IE=8" />
<title>DeliveryStatus</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
<meta name="language" content="sk-SK" />
<style type="text/css">
body {
    font-family: 'Open Sans', 'Segoe UI', 'Trebuchet MS', 'Geneva CE', lucida, sans-serif;
    background-color:transparent;
    color: #646464;
}
.ui-tabs {
    padding: .2em;
    position: relative;
    zoom: 1;
}
.ui-widget-content {
    background: #f9f9f9;
    border: 2px solid #d4d4d4;
    color: #3e3e3e;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    -ms-border-radius: 5px;
    -o-border-radius: 5px;
    border-radius: 5px
}
.ui-widget-header {
    font-weight: 400;
    border: 1px solid #5f5247;
    background-color: #5f5247;
    color: #fff;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    -ms-border-radius: 5px;
    -o-border-radius: 5px;
    border-radius: 5px
}
.clear { clear: both; }
.layoutMain {
    margin: 0px auto;
    padding: 5px 5px 5px 5px;
}
.layoutRow { margin-bottom: 5px; }
.caption { /*width: 100%; border-bottom: solid 1px black;*/ }
.nocaption > .caption { border: 0px !important; }
.nocaption > .caption span {
    background: none !important;
    display: none;
}
.caption .title { padding-left: 5px; }
.headercorrection {
    margin: 0px;
}
.labelVis {
    float: left;
    font-weight: bold;
    font-family: 'Open Sans', 'Segoe UI', 'Trebuchet MS', 'Geneva CE', lucida, sans-serif;
    line-height: 25px;
    margin: 0px 18px 0px 0px;
    padding: 0;
    width: 190px;
}
.contentVis {
    float: left;
    line-height: 25px;
    margin: 0px;
    padding: 0px;
    vertical-align: top;
}
.wordwrap {
   white-space: pre-wrap;
   white-space: -moz-pre-wrap;
   white-space: -pre-wrap;
   white-space: -o-pre-wrap;
   word-wrap: break-word;
}
</style>
</head>
<body>
<div id="main" class="layoutMain">
<xsl:for-each select="/egonp:DeliveryStatus"><div id="" class="layoutRow ui-tabs ui-widget-content" title="" >
<div class="caption ui-widget-header">
<div class="headercorrection">Informácia o aktuálnom stave doručovania</div>
</div>
<xsl:if test="/egonp:DeliveryStatus/egonp:MessageID/text()"><div><label class="labelVis">MessageID: </label><span class="contentVis wordwrap"><xsl:value-of select="./egonp:MessageID"/></span></div><div class="clear"></div></xsl:if>
<xsl:for-each select="/egonp:DeliveryStatus/egonp:State"><div id="" class="layoutRow ui-tabs ui-widget-content" title="" >
<div class="caption ui-widget-header">
<div class="headercorrection">Stav doručovania</div>
</div>
<xsl:if test="/egonp:DeliveryStatus/egonp:State/egonp:Status/text()"><div><label class="labelVis">Identifikátor stavu: </label><span class="contentVis wordwrap"><xsl:value-of select="./egonp:Status"/></span></div><div class="clear"></div></xsl:if>
<xsl:if test="/egonp:DeliveryStatus/egonp:State/egonp:StatusText/text()"><div><label class="labelVis">Stav: </label><span class="contentVis wordwrap"><xsl:value-of select="./egonp:StatusText"/></span></div><div class="clear"></div></xsl:if>
<xsl:if test="/egonp:DeliveryStatus/egonp:State/egonp:StatusTime/text()"><div><label class="labelVis">Čas stavu: </label><span class="contentVis wordwrap"><xsl:call-template name="formatToSkDate"><xsl:with-param name="date" select="./egonp:StatusTime" /></xsl:call-template></span></div><div class="clear"></div></xsl:if>
</div>
</xsl:for-each></div>
</xsl:for-each></div>
</body>
</html>
</xsl:template>
<xsl:template name="formatToSkDate">
<xsl:param name="date" />
<xsl:value-of select="concat(substring($date, 9, 2), '.', substring($date, 6, 2), '.', substring($date, 1, 4))" />
</xsl:template>
</xsl:stylesheet>