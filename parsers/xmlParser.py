__author__ = 'Jan'

from lxml import etree

class XmlParser():

    def __init__(self,xsd_file,xsl_file):
        self.xsd_file = xsd_file
        self.xsl_file = xsl_file
        with open(xsd_file, 'r') as f:
            schema_root = etree.XML(f.read())
        schema = etree.XMLSchema(schema_root)
        self.xml_schema = etree.XMLParser(schema=schema)

        self.xslt = etree.parse(xsl_file)

    def validate(self, xml):
        try:
            etree.fromstring(xml, self.xml_schema)
            return True
        except Exception as err:
            return err

    def transform(self, xml):
        trans = etree.XSLT(self.xslt)
        return str(trans(xml))

    def string_schema(self):
        f = open(self.xsd_file,'r')
        schema_string = f.read()
        return schema_string

    def string_transformation(self):
        f = open(self.xsl_file,'r')
        transf_string = f.read()
        return transf_string



