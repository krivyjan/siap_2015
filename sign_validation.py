# coding: utf-8
__author__ = 'Ján Krivý'

from xml.dom.minidom import parse

xml_files = ["priklady/01XadesT.xml","priklady/02XadesT.xml","priklady/03XadesT.xml","priklady/04XadesT.xml","priklady/05XadesT.xml","priklady/06XadesT.xml","priklady/07XadesT.xml","priklady/08XadesT.xml","priklady/09XadesT.xml","priklady/10XadesT.xml","priklady/11XadesT.xml","priklady/12XadesT.xml","priklady/XadesT.xml"]
xml_file = "priklady/01XadesT.xml"
#xml_file = "priklady/02XadesT.xml"
#xml_file = "priklady/03XadesT.xml"
#xml_file = "priklady/04XadesT.xml"
#xml_file = "priklady/05XadesT.xml"
#xml_file = "priklady/06XadesT.xml"
#xml_file = "priklady/07XadesT.xml"
#xml_file = "priklady/08XadesT.xml"
#xml_file = "priklady/09XadesT.xml"
#xml_file = "priklady/10XadesT.xml"
#xml_file = "priklady/11XadesT.xml"
#xml_file = "priklady/12XadesT.xml"
#xml_file = "priklady/XadesT.xml"

uri_signatureMethod = set(['http://www.w3.org/2000/09/xmldsig#dsa-sha1','http://www.w3.org/2000/09/xmldsig#rsa-sha1','http://www.w3.org/2001/04/xmldsig-more#rsa-sha256','http://www.w3.org/2001/04/xmldsig-more#rsa-sha384','http://www.w3.org/2001/04/xmldsig-more#rsa-sha512'])
uri_canonicalizationMethod = set(['http://www.w3.org/TR/2001/REC-xml-c14n-20010315'])

def have_child(child, root):
    childs=set()
    for item in root.childNodes:
        childs.add(item.nodeName)
    return child in childs

def get_childs(child,root):
    node = list()
    for item in root.childNodes:
        #print item.nodeName
        if item.nodeName == child:
            node.append(item)
    return node

def get_child(child,root):
    node = None
    for item in root.childNodes:
        #print item.nodeName
        if item.nodeName == child:
            return item
    return node


#root = sign._get_firstChild()
#print root.tagName
#print root.nodeName
#print root.nodeValue
#attr= root.attributes
#print attr.item(0).name
#print attr.item(0).value
xml_files = [xml_files[0]]
for file in xml_files:
    print 'spracovavam xml file: ' + file
    sign = parse(xml_file)
    root = sign._get_firstChild()
    #1
    #1.1 overenie korenoveho elementu
    if not root.nodeName == "xzep:DataEnvelope":
        print "Korenovy element sa nerovna xzep:DataEnvelope"
        continue
    root_attr = root.attributes

    #1.2 overenie atributov korenoveho elementu
    try:
        #v dokumentacii bola hodnota attributu xmlns:xzep = "http://www.ditec.sk/ep/signature_formats/xades_zep/v1.0"
        if not root_attr['xmlns:xzep'].value == "http://www.ditec.sk/ep/signature_formats/xades_zep/v1.01" and root_attr['xmlns:ds'].value == "http://www.w3.org/2000/09/xmldsig#":
            print 'Atributy korenoveho elementu maju nespravne hodnoty'
            continue
    except KeyError:
        print "Korenovy element neobsahuje jeden z atributov xmlns:xzep a xmlns:ds"
        continue

    #1.3 overenie, ci root obsahuje podelement ds:Signature
    signature = get_child('ds:Signature',root)
    if not signature:
        print "Korenovy element neobsahuje podelement ds:Signature"
        continue

    #2
    #2.1
    signedInfo = get_child('ds:SignedInfo',signature)
    if not signedInfo:
        print 'Element ds:Signature neobsauje ds:SignedInfo'
        continue

    signatureMethod = get_child('ds:SignatureMethod',signedInfo)
    #print signatureMethod
    if not signatureMethod:
        print 'Element signedInfo neobsahuje element ds:SignatureMethod'
        continue
    try:
        if not signatureMethod.attributes['Algorithm'].value in uri_signatureMethod:
            print 'Element Algorithm SignatureMethod neobsahuje validnu URI'
            continue
    except KeyError:
        print 'Element signatureMethod neobsauje atribut Algoritm'
        continue

    canonicalizationMethod = get_child('ds:CanonicalizationMethod',signedInfo)
    #print canonicalizationMethod
    if not canonicalizationMethod:
        print 'Element signedInfo neobsahuje element ds:CanonicalizationMethod'
        continue
    try:
        if not canonicalizationMethod.attributes['Algorithm'].value in uri_canonicalizationMethod:
            print 'Element Algorithm SignatureMethod neobsahuje validnu URI'
            continue
    except KeyError:
        print 'Element signatureMethod neobsauje atribut Algoritm'
        continue
