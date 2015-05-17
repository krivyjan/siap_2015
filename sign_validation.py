# coding: utf-8
__author__ = 'Ján Krivý'

from xml.dom.minidom import parse
#from xml.dom.ext import c14n
from lxml import etree
import hashlib

class endException(Exception):
    pass

class endForException(Exception):
    pass

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

uri_signatureMethod = {'http://www.w3.org/2000/09/xmldsig#dsa-sha1', 'http://www.w3.org/2000/09/xmldsig#rsa-sha1',
                       'http://www.w3.org/2001/04/xmldsig-more#rsa-sha256',
                       'http://www.w3.org/2001/04/xmldsig-more#rsa-sha384',
                       'http://www.w3.org/2001/04/xmldsig-more#rsa-sha512'}
uri_digestMethod = {"http://www.w3.org/2000/09/xmldsig#sha1", "http://www.w3.org/2001/04/xmldsig-more#sha224",
                    "http://www.w3.org/2001/04/xmlenc#sha256", "http://www.w3.org/2001/04/xmldsig-more#sha384",
                    "http://www.w3.org/2001/04/xmlenc#sha512"}
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
    for item in root.childNodes:
        #print item.nodeName
        if item.nodeName == child:
            return item
    print 'element ' + root.nodeName + ' neobsahuje element' + child
    return None

def get_child2(child,root):
    for item in root.childNodes:
        #print item.nodeName
        if item.nodeName == child:
            return item
    #print 'element ' + root.nodeName + ' neobsahuje element' + child
    return None

def get_attr(node,attr):
    try:
        item = node.attributes[attr]
        return item
    except KeyError:
        return None

def attribute(node,attr,value=None):
    try:
        item = node.attributes[attr]
        if not value:
            return True
        else:
            if item.value in value:
                return True
            else:
                print 'Atribut ' + attr + ' elementu ' + node.nodeName + ' neobsahuje hodnotu ' + str(value)
                return False
    except KeyError:
        print 'Element ' + node.nodeName + ' neobsahuje attribut ' + attr
        return False

def crete_dict(sign):
    elements = sign.getElementsByTagName('ds:Manifest')
    elements.extend(sign.getElementsByTagName('ds:KeyInfo'))
    elements.extend(sign.getElementsByTagName('ds:SignatureProperties'))
    elements.extend(sign.getElementsByTagName('xades:SignedProperties'))
    result = dict()
    for element in elements:
        id = get_attr(element,'Id').value
        result[id] = element
    return result

def get_object(element,value):
    elements = element.getElementsByTagName('ds:Object')
    for element in elements:
        id = get_attr(element,'Id')
        if id.value == value:
            return element
    return False

def hash(element,alg,value,can):
    value = value.decode('base64')
    tmp = etree.fromstring(element.toxml())
    element_can = etree.tostring(tmp,method=can)
    alg = alg.split('#')
    alg = alg[-1]
    if alg=='sha1':
        hash_value = hashlib.sha1(element_can).digest()
        return hash_value==value
    elif alg=='sha224':
        hash_value = hashlib.sha224(element_can).digest()
        return hash_value==value
    elif alg=='sha256':
        hash_value = hashlib.sha256(element_can).digest()
        return hash_value==value
    elif alg=='sha384':
        hash_value = hashlib.sha384(element_can).digest()
        return hash_value==value
    elif alg=='sha512':
        hash_value = hashlib.sha512(element_can).digest()
        return hash_value==value
    else:
        print 'neplatna metoda: ' + alg
        return False


def get_hash(element,alg,can):
    tmp = etree.fromstring(element.toxml())
    element_can = etree.tostring(tmp,method=can)
    alg = alg.split('#')
    alg = alg[-1]
    if alg=='sha1':
        hash_value = hashlib.sha1(element_can).digest()
        return hash_value
    elif alg=='sha224':
        hash_value = hashlib.sha224(element_can).digest()
        return hash_value
    elif alg=='sha256':
        hash_value = hashlib.sha256(element_can).digest()
        return hash_value
    elif alg=='sha384':
        hash_value = hashlib.sha384(element_can).digest()
        return hash_value
    elif alg=='sha512':
        hash_value = hashlib.sha512(element_can).digest()
        return hash_value
    else:
        print 'neplatna metoda: ' + alg
        return False

#root = sign._get_firstChild()
#print root.tagName
#print root.nodeName
#print root.nodeValue
#attr= root.attributes
#print attr.item(0).name
#print attr.item(0).value
#xml_files = [xml_files[0]]
for file in xml_files:
    try:
        print 'spracovavam xml file: ' + file
        sign = parse(file)
        root = sign._get_firstChild()
        #1
        #1.1 overenie korenoveho elementu
        if not root.nodeName == "xzep:DataEnvelope":
            raise endException("Korenovy element sa nerovna xzep:DataEnvelope")

        #1.2 overenie atributov korenoveho elementu
        if not attribute(root,'xmlns:xzep',set(["http://www.ditec.sk/ep/signature_formats/xades_zep/v1.0"])): #v dokumentacii bola hodnota attributu xmlns:xzep = "http://www.ditec.sk/ep/signature_formats/xades_zep/v1.0"
            raise endException
        if not attribute(root,'xmlns:ds',set(["http://www.w3.org/2000/09/xmldsig#"])):
            raise endException

        #1.3 overenie, ci root obsahuje podelement ds:Signature
        signature = get_child('ds:Signature',root)
        if not signature:
            raise endException("Korenovy element neobsahuje podelement ds:Signature")

        if not attribute(signature,'Id'):
            raise endException
        if not attribute(signature,'xmlns:ds'):
            raise endException

        #1.4
        signatureValue = get_child('ds:SignatureValue',signature)
        if not attribute(signatureValue,'Id'):
            raise endException()


        #2
        #2.1
        #overenie ci signature obsahuje signedInfo
        signedInfo = get_child('ds:SignedInfo',signature)
        if not signedInfo:
            raise endException

        signatureMethod = get_child('ds:SignatureMethod',signedInfo)
        #print signatureMethod
        if not signatureMethod:
            raise endException
        #2.1.1
        if not attribute(signatureMethod,'Algorithm',uri_signatureMethod):
            raise endException

        canonicalizationMethod = get_child('ds:CanonicalizationMethod',signedInfo)
        #print canonicalizationMethod
        if not canonicalizationMethod:
            raise endException

        if not attribute(canonicalizationMethod,'Algorithm',uri_canonicalizationMethod):
            raise endException


        #2.3
        references =  get_childs('ds:Reference',signedInfo)
        uris = list()
        values = dict()
        alg = dict()
        for reference in references:
            transforms = get_child('ds:Transforms',reference)
            if not transforms:
                raise endException
            transform = get_child('ds:Transform',transforms)
            if not transform:
                raise endException
            if not attribute(transform,'Algorithm',set(["http://www.w3.org/TR/2001/REC-xml-c14n-20010315"])):
                raise endException
            digestMethod = get_child('ds:DigestMethod',reference)

            if not digestMethod:
                raise endException
            if not attribute(digestMethod,'Algorithm',uri_digestMethod):
                raise endException
            uri = get_attr(reference,'URI').value
            uris.append(uri[1:])
            #print reference
            values[uri[1:]]= get_child('ds:DigestValue',reference).firstChild.nodeValue
            alg[uri[1:]]= get_attr(get_child('ds:DigestMethod',reference),'Algorithm').value


        keyinfo = None
        signatureproperties = None
        signedproperies=None
        manifest=list()
        elements = crete_dict(sign)
        tmp_uri = None
        try:
            for uri in uris:
                tmp_uri = uri
                element = elements[uri]
                if element.nodeName=='xades:SignedProperties' and not signedproperies:
                    signedproperies=element
                elif element.nodeName=='ds:SignatureProperties' and not signatureproperties:
                    signatureproperties=element
                elif element.nodeName=='ds:KeyInfo' and not keyinfo:
                    keyinfo=element
                elif element.nodeName=='ds:Manifest':
                    manifest.append(element)
                else:
                    print str(element.nodeName) + ' sa vyskytuje viackrat alebo je zleho typu'
                    raise endForException
        except KeyError:
            print 'Dane uri neukazuje na ziadny element: ' + str(tmp_uri)
            raise endException
        except endForException:
            print 'test'
            raise endException
        if not keyinfo:
            print 'element keyinfo sa nenasiel'
            raise endException
        if not signatureproperties:
            print 'element signatureproperties sa nenasiel'
            raise endException
        if not signedproperies:
            print 'element signedproperties sa nenasiel'
            raise endException

        if not hash(keyinfo,alg[get_attr(keyinfo,'Id').value],values[get_attr(keyinfo,'Id').value],'c14n'):
            print 'Nesedi hash value s digest value pre element keyinfo'
            raise endException
        if not hash(signatureproperties,alg[get_attr(signatureproperties,'Id').value],values[get_attr(signatureproperties,'Id').value],'c14n'):
            print 'Nesedi hash value s digest value pre element signatureproperties'
            raise endException
        if not hash(signedproperies,alg[get_attr(signedproperies,'Id').value],values[get_attr(signedproperies,'Id').value],'c14n'):
            print 'Nesedi hash value s digest value pre element signatureproperties'
            raise endException

        for element in manifest:
            if not hash(element,alg[get_attr(element,'Id').value],values[get_attr(element,'Id').value],'c14n'):
                print 'Nesedi hash value s digest value pre element manifest'
                raise endException


        #2.4
        keyinfo = get_child('ds:KeyInfo',signature)
        if not keyinfo:
            print 'Element signature neobsahuje element KeyInfo'
            raise endException
        if not attribute(keyinfo,'Id'):
            print 'Keyinfo v signature neobsahuje attr Id'
            raise endException

        signatureproperties = signature.getElementsByTagName('ds:SignatureProperties')[0]

        if not signatureproperties:
            raise endException('element signature neobsahuje podelement signatureproperties')
        if not attribute(signatureproperties,'Id'):
            raise endException('element signatureproperties neobsahuje atribut Id')

        signatureproperty = get_childs('ds:SignatureProperty',signatureproperties)
        if not signatureproperty:
            raise endException('Signature properties neobsahuje elementy signature property')

        if not (get_child2('xzep:SignatureVersion', signatureproperty[0]) and get_child2('xzep:ProductInfos',signatureproperty[1])) or (get_child2('xzep:SignatureVersion', signatureproperty[1]) and get_child2('xzep:ProductInfos',signatureproperty[0])):
            raise endException('Elementy neobsahuju SignatureVersion a ProductInfos podla formatu podpisu')

        x509data = get_child('ds:X509Data',keyinfo)
        if not x509data:
            raise endException('KeyInfo neobsahuje element x509data')
        #ds:X509Certificate
        #ds:X509IssuerSerial
        #ds:X509SubjectName
        certificate = get_child('ds:X509Certificate',x509data)
        issuerSerial = get_child('ds:X509IssuerSerial',x509data)
        subjectName = get_child('ds:X509SubjectName',x509data)
        #print certificate
        #print issuerSerial
        #print subjectName
        #print certificate.firstChild.nodeValue

        #Pomocou bcCrypto vytiahnem z elementu ds:X509Certificate: IssuerCertificate  a SubjectName a porovnam s hodnotami vyssie

        alg = get_attr(signatureMethod,'Algorithm').value.split('#')[-1].split('-')
        #print alg

        signedInfo_hash = get_hash(signedInfo,alg[1],'c14n')
        #print signedInfo_hash

        #ziskanie public key
        #rsa signedInfo_hash
        #porovnanie s SignatureValue



        #2.5
        dsObjects = signature.getElementsByTagName('ds:Object')
        #print dsObjects[-1].toprettyxml()
        for manifest in get_childs('ds:Manifest',dsObjects[-1]): #dsObjects[-1].toprettyxml()
            if not attribute(manifest,'Id'):
                raise endException
            reference = get_childs('ds:Reference',manifest)
            if not len(reference)==1:
                raise endException('ds:Object -> last manifest neobsahuje prave jeden objekt ds:Reference')
            reference=reference[0]
            uri = get_attr(reference,'URI').value[1:]
            object = get_object(sign,uri)
            if not object:
                raise endException('Uri v last manifest neukazuje na ds:Object')

            transforms = get_child('ds:Transforms',reference)

            transform = get_child('ds:Transform',transforms)
            #print transform.toprettyxml()
            #print get_attr(transform,'Algorithm').value
            if not get_attr(transform,'Algorithm').value == "http://www.w3.org/TR/2001/REC-xml-c14n-20010315":
                raise endException('2.5 nesedli value atributu Algorithm v transform')
            digestMethod = get_child('ds:DigestMethod',reference)
            digestValue = get_child('ds:DigestValue',reference).firstChild.nodeValue

            alg = get_attr(digestMethod,'Algorithm').value
            if not alg in uri_digestMethod:
                raise endException('2.5 nesedi digestmethod algorithm')

            if not hash(object,alg,digestValue,'c14n'):
                raise endException('2.5 vypocitany hash nesedi s digestvalue ')


        #3
        unsignedProp = sign.getElementsByTagName('xades:UnsignedProperties')[0]
        unsignedsignatureProp = get_child('xades:UnsignedSignatureProperties',unsignedProp)
        signTimeStamp = get_child('xades:SignatureTimeStamp',unsignedsignatureProp)
        encapsulatedTimeStamp = get_child('xades:EncapsulatedTimeStamp',signTimeStamp)
        #print encapsulatedTimeStamp

            #xades:UnsignedProperties => xades:UnsignedSignatureProperties =>xades:SignatureTimeStamp => xades:EncapsulatedTimeStamp
            #potrebujem zaciatok a koniec casovej peciatky
            #MessageImprint == SignatureValue


        #4

    except endException as exc:
        print exc
        print 'koncim s validaciou podpisu'
        continue







