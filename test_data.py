#coding: utf-8
__author__ = 'Ján Krivý'

class Data:
    def __init__(self):
        self.xml = """<?xml version="1.0" encoding="windows-1250"?><dokument xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="universal.xsd"><hlavicka err="0"><typDP><rdp err="0">1</rdp><odp err="0">0</odp><ddp err="0">0</ddp></typDP><danovy_urad err="0"></danovy_urad><kod_do err="0"></kod_do><dic err="0">1234567890</dic><ico err="0"></ico><pravna_forma err="0">100</pravna_forma><obch_meno err="0">Firma FRK</obch_meno><sidlo><ulica err="0"></ulica><cislo err="0"></cislo><psc err="0"></psc><obec err="0">Bratislava</obec><stat err="0"></stat><tel err="0">0/</tel><fax err="0">0/</fax><banka><nazov_banky err="0"></nazov_banky><ucet err="0"></ucet><kod_banky err="0"></kod_banky></banka><banka><nazov_banky err="0"></nazov_banky><ucet err="0"></ucet><kod_banky err="0"></kod_banky></banka></sidlo><opravnena_osoba><priezvisko err="0"></priezvisko><meno err="0"></meno><titul err="0"></titul><postavenie err="0"></postavenie><sidlo_oo><ulicacislo err="0"></ulicacislo><psc err="0"></psc><obec err="0"></obec><stat err="0"></stat><tel err="0">0/</tel><fax err="0">0/</fax></sidlo_oo></opravnena_osoba><pocet_priloh err="0"></pocet_priloh><zdanovacie_obd><datum_od><den err="0"></den><mesiac err="0"></mesiac></datum_od><datum_do><den err="0"></den><mesiac err="0"></mesiac></datum_do><rok err="0"></rok></zdanovacie_obd><datum_vyplnenia err="0"></datum_vyplnenia></hlavicka><body><r100 err="0"></r100><r110 err="0"></r110><r120 err="0"></r120><r130 err="0"></r130><r140 err="0"></r140><r150 err="0"></r150><r160 err="0"></r160><r170 err="0"></r170><r180 err="0"></r180><r190 err="0"></r190><r200 err="0"></r200><r210 err="0"></r210><r220 err="0"></r220><r230 err="0"></r230><r240 err="0"></r240><r250 err="0"></r250><r260 err="0"></r260><r270 err="0"></r270><r280 err="0"></r280><r290 err="0"></r290><r300 err="0"></r300><r310 err="0"></r310><r320 err="0"></r320><r330 err="0"></r330><r400 err="0"></r400><r410 err="0"></r410><r420 err="0"></r420><r430 err="0"></r430><r440 err="0"></r440><r450 err="0"></r450><r460 err="0"></r460><r470 err="0"></r470><r500 err="0"></r500><r510 err="0"></r510><r600 err="0"></r600><r610><text err="0"></text><suma err="0"></suma></r610><r620><text err="0"></text><suma err="0"></suma></r620><r630 err="0"></r630><r640 err="0"></r640><r650 err="0"></r650><r700 err="0"></r700><r710 err="0"></r710><r800 err="0"></r800><r810><datum err="0"></datum><suma err="0"></suma></r810><r820><datum err="0"></datum><suma err="0"></suma></r820><r830 err="0"></r830><r840 err="0"></r840><r850 err="0"></r850><r900><datum err="0"></datum><suma err="0"></suma></r900><r901 err="0"></r901><r902 err="0"></r902><r910 err="0"></r910><ddp_datum err="0"></ddp_datum><r920 err="0"></r920><r930 err="0"></r930><r940 err="0"></r940><r950 err="0"></r950><r960 err="0"></r960><r970 err="0"></r970><tab_a><r01 err="0"></r01><r02 err="0"></r02><r03 err="0"></r03><r04 err="0"></r04><r05 err="0"></r05><r06 err="0"></r06><r07 err="0"></r07><r08 err="0"></r08><r09 err="0"></r09><r10 err="0"></r10><r11 err="0"></r11><r12 err="0"></r12><r13 err="0"></r13><r14 err="0"></r14><r15 err="0"></r15><r16 err="0"></r16><r17 err="0"></r17><r18 err="0"></r18><r19 err="0"></r19></tab_a><tab_b><r01 err="0"></r01><r02 err="0"></r02><r03 err="0"></r03></tab_b><tab_c><r01 err="0"></r01><r02 err="0"></r02><r03 err="0"></r03></tab_c><tab_d><r01 err="0"></r01><r02 err="0"></r02><r03 err="0"></r03><r04 err="0"></r04><r05 err="0"></r05></tab_d><tab_e><r01 err="0"></r01><r02 err="0"></r02><r03 err="0"></r03><r04 err="0"></r04><r05 err="0"></r05><r06 err="0"></r06></tab_e><tab_f><cast1><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok></cast1><cast2><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok></cast2><cast3><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok><riadok><s01 err="0"></s01><s02 err="0"></s02><s03 err="0"></s03><s04 err="0"></s04></riadok></cast3></tab_f><tab_g><r01 err="0"></r01><r02 err="0"></r02></tab_g><tab_h><r01 err="0"></r01><r02 err="0"></r02><r03 err="0"></r03><r04 err="0"></r04></tab_h></body></dokument>"""

        self.schema = """<?xml version="1.0" encoding="utf-8" ?>
<!-- XSD pre danove priznanie k dani z prijmov pravnickej osoby (DPPO) - verzia pre VDDI. -->
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">
	<xsd:annotation>
		<xsd:documentation>DPPO</xsd:documentation>
	</xsd:annotation>
	<!-- komplexny typ nad standardnym retazcom (podla w3) -->
	<xsd:complexType name="xsdStringType">
		<xsd:simpleContent>
			<xsd:extension base="xsd:string">
				<xsd:attribute name="pole" type="xsd:string" default="y" />
				<xsd:attribute name="funkcia" type="xsd:string" default="udajeOOsobe" />
				<xsd:attribute name="err" type="xsd:unsignedByte" use="required" />
			</xsd:extension>
		</xsd:simpleContent>
	</xsd:complexType>
	<!-- prazdny retazec-->
	<xsd:simpleType name="emptyStringType">
		<xsd:restriction base="xsd:string">
			<xsd:enumeration value="" />
		</xsd:restriction>
	</xsd:simpleType>
	<!-- prazdny alebo klasicky retazec-->
	<xsd:simpleType name="xStringType">
		<xsd:union memberTypes="emptyStringType xsd:string" />
	</xsd:simpleType>
	<xsd:complexType name="stringPType">
		<xsd:simpleContent>
			<xsd:extension base="xStringType">
				<xsd:attribute name="err" type="xsd:unsignedByte" use="required" />
				<xsd:attribute name="pole" type="xsd:string" default="y" />
			</xsd:extension>
		</xsd:simpleContent>
	</xsd:complexType>
	<!-- xEUDatumType je datum v tvare DD.MM.RRRR-->
	<xsd:simpleType name="xEUDatumType">
		<xsd:restriction base="xsd:string">
			<xsd:pattern value="\d\d?\.\d\d?\.\d\d\d\d" />
		</xsd:restriction>
	</xsd:simpleType>
	<!-- datum je prazdny retazec emptyString alebo xEUDatumType-->
	<xsd:simpleType name="xDatumType">
		<xsd:union memberTypes="emptyStringType xEUDatumType" />
	</xsd:simpleType>
	<!-- dokument (hlavny element) -->
	<xsd:element name="dokument">
		<xsd:complexType>
			<xsd:sequence>
				<xsd:element name="hlavicka" type="hlavickaType" />
				<xsd:element name="body" type="bodyType" />
			</xsd:sequence>
		</xsd:complexType>
	</xsd:element>
	<!-- hlavicka -->
	<xsd:complexType name="hlavickaType">
		<xsd:sequence>
			<xsd:element name="typDP" type="typDPType" />
			<xsd:element name="danovy_urad" type="xsdStringType" />
			<xsd:element name="kod_do" type="xsdStringType" />
			<xsd:element name="dic" type="xsdStringType" />
			<xsd:element name="ico" type="xsdStringType" />
			<xsd:element name="pravna_forma" type="xsdStringType" />
			<xsd:element name="obch_meno" type="xsdStringType" />
			<xsd:element name="sidlo" type="sidloType" />
			<xsd:element name="opravnena_osoba" type="opravnena_osobaType" />
			<xsd:element name="pocet_priloh" type="xsdStringType" />
			<xsd:element name="zdanovacie_obd" type="zdanovacieObdType" />
			<xsd:element name="datum_vyplnenia" type="xsdStringType" />
		</xsd:sequence>
		<xsd:attribute name="err" type="xsd:unsignedByte" use="required" />
	</xsd:complexType>
	<!-- boolean typ pre ano/nie policka -->
	<xsd:simpleType name="XUtypDP">
		<xsd:union memberTypes="emptyStringType xsd:boolean" />
	</xsd:simpleType>
	<xsd:complexType name="XtypDP">
		<xsd:simpleContent>
			<xsd:extension base="XUtypDP">
				<xsd:attribute name="pole" type="xsd:string" default="y" />
				<xsd:attribute name="funkcia" type="xsd:string" default="udajeOOsobe" />
				<xsd:attribute name="err" type="xsd:unsignedByte" use="required" />
			</xsd:extension>
		</xsd:simpleContent>
	</xsd:complexType>
	<xsd:complexType name="typDPType">
		<xsd:sequence>
			<xsd:element name="rdp" type="XtypDP" />
			<xsd:element name="odp" type="XtypDP" />
			<xsd:element name="ddp" type="XtypDP" />
		</xsd:sequence>
	</xsd:complexType>
	<!-- info o danovnikovi -->
	<xsd:complexType name="bankaType">
		<xsd:sequence>
			<xsd:element name="nazov_banky" type="xsdStringType" />
			<xsd:element name="ucet" type="xsdStringType" />
			<xsd:element name="kod_banky" type="xsdStringType" />
		</xsd:sequence>
	</xsd:complexType>
	<xsd:complexType name="sidloType">
		<xsd:sequence>
			<xsd:element name="ulica" type="xsdStringType" />
			<xsd:element name="cislo" type="xsdStringType" />
			<xsd:element name="psc" type="xsdStringType" />
			<xsd:element name="obec" type="xsdStringType" />
			<xsd:element name="stat" type="xsdStringType" />
			<xsd:element name="tel" type="xsdStringType" />
			<xsd:element name="fax" type="xsdStringType" />
			<xsd:element name="banka" type="bankaType" maxOccurs="2" />
		</xsd:sequence>
	</xsd:complexType>
	<xsd:complexType name="sidlo_ooType">
		<xsd:sequence>
			<xsd:element name="ulicacislo" type="xsdStringType" />
			<xsd:element name="psc" type="xsdStringType" />
			<xsd:element name="obec" type="xsdStringType" />
			<xsd:element name="stat" type="xsdStringType" />
			<xsd:element name="tel" type="xsdStringType" />
			<xsd:element name="fax" type="xsdStringType" />
		</xsd:sequence>
	</xsd:complexType>
	<xsd:complexType name="opravnena_osobaType">
		<xsd:sequence>
			<xsd:element name="priezvisko" type="xsdStringType" />
			<xsd:element name="meno" type="xsdStringType" />
			<xsd:element name="titul" type="xsdStringType" />
			<xsd:element name="postavenie" type="xsdStringType" />
			<xsd:element name="sidlo_oo" type="sidlo_ooType" />
		</xsd:sequence>
	</xsd:complexType>
	<!-- typ rok, obmedzeny bud na prazdny retazec alebo 4zn decimal -->
	<xsd:simpleType name="Xrok">
		<xsd:restriction base="xsd:string">
			<xsd:length value="4" />
			<xsd:pattern value="[0-9][0-9][0-9][0-9]" />
		</xsd:restriction>
	</xsd:simpleType>
	<!-- typ datum s atributom err -->
	<xsd:complexType name="datumZdanObdType">
		<xsd:sequence>
			<xsd:element name="den" type="xsdStringType" />
			<xsd:element name="mesiac" type="xsdStringType" />
		</xsd:sequence>
	</xsd:complexType>
	<xsd:complexType name="zdanovacieObdType">
		<xsd:sequence>
			<xsd:element name="datum_od" type="datumZdanObdType" />
			<xsd:element name="datum_do" type="datumZdanObdType" />
			<xsd:element name="rok" type="xsdStringType" />
		</xsd:sequence>
	</xsd:complexType>
	<!-- body -->
	<xsd:complexType name="bodyType">
		<xsd:sequence>
			<xsd:element name="r100" type="TdecimalPole" />
			<xsd:element name="r110" type="TdecimalPole" />
			<xsd:element name="r120" type="TdecimalPole" />
			<xsd:element name="r130" type="TdecimalPole" />
			<xsd:element name="r140" type="TdecimalPole" />
			<xsd:element name="r150" type="TdecimalPole" />
			<xsd:element name="r160" type="TdecimalPole" />
			<xsd:element name="r170" type="TdecimalPole" />
			<xsd:element name="r180" type="TdecimalPole" />
			<xsd:element name="r190" type="TdecimalPole" />
			<xsd:element name="r200" type="TdecimalPole" />
			<xsd:element name="r210" type="TdecimalPole" />
			<xsd:element name="r220" type="TdecimalPole" />
			<xsd:element name="r230" type="TdecimalPole" />
			<xsd:element name="r240" type="TdecimalPole" />
			<xsd:element name="r250" type="TdecimalPole" />
			<xsd:element name="r260" type="TdecimalPole" />
			<xsd:element name="r270" type="TdecimalPole" />
			<xsd:element name="r280" type="TdecimalPole" />
			<xsd:element name="r290" type="TdecimalPole" />
			<xsd:element name="r300" type="TdecimalPole" />
			<xsd:element name="r310" type="TdecimalPole" />
			<xsd:element name="r320" type="TdecimalPole" />
			<xsd:element name="r330" type="TdecimalPole" />
			<xsd:element name="r400" type="TdecimalPole" />
			<xsd:element name="r410" type="TdecimalPole" />
			<xsd:element name="r420" type="TdecimalPole" />
			<xsd:element name="r430" type="TdecimalPole" />
			<xsd:element name="r440" type="TdecimalPole" />
			<xsd:element name="r450" type="TdecimalPole" />
			<xsd:element name="r460" type="TdecimalPole" />
			<xsd:element name="r470" type="TdecimalPole" />
			<xsd:element name="r500" type="TdecimalPole" />
			<xsd:element name="r510" type="TdecimalPole" />
			<xsd:element name="r600" type="TdecimalPole" />
			<xsd:element name="r610" type="TtextSuma" />
			<xsd:element name="r620" type="TtextSuma" />
			<xsd:element name="r630" type="TdecimalPole" />
			<xsd:element name="r640" type="TdecimalPole" />
			<xsd:element name="r650" type="TdecimalPole" />
			<xsd:element name="r700" type="TdecimalPole" />
			<xsd:element name="r710" type="TdecimalPole" />
			<xsd:element name="r800" type="TdecimalPole" />
			<xsd:element name="r810" type="TdatumSuma" />
			<xsd:element name="r820" type="TdatumSuma" />
			<xsd:element name="r830" type="TdecimalPole" />
			<xsd:element name="r840" type="TdecimalPole" />
			<xsd:element name="r850" type="TdecimalPole" />
			<xsd:element name="r900" type="TdatumSuma" />
			<xsd:element name="r901" type="TdecimalPole" />
			<xsd:element name="r902" type="TdecimalPole" />
			<xsd:element name="r910" type="TdecimalPole" />
			<xsd:element name="ddp_datum" type="xsdStringType" />
			<xsd:element name="r920" type="xsdStringType" />
			<xsd:element name="r930" type="xsdStringType" />
			<xsd:element name="r940" type="xsdStringType" />
			<xsd:element name="r950" type="xsdStringType" />
			<xsd:element name="r960" type="xsdStringType" />
			<xsd:element name="r970" type="xsdStringType" />
			<xsd:element name="tab_a" type="Ttab_a" />
			<xsd:element name="tab_b" type="Ttab_b" />
			<xsd:element name="tab_c" type="Ttab_c" />
			<xsd:element name="tab_d" type="Ttab_d" />
			<xsd:element name="tab_e" type="Ttab_e" />
			<xsd:element name="tab_f" type="Ttab_f" />
			<xsd:element name="tab_g" type="Ttab_g" />
			<xsd:element name="tab_h" type="Ttab_h" />
		</xsd:sequence>
	</xsd:complexType>
	<!-- typ decimalne pole -->
	<xsd:simpleType name="Tdecimal">
		<xsd:restriction base="xsd:decimal" />
	</xsd:simpleType>
	<xsd:simpleType name="XdecimalPole">
		<xsd:union memberTypes="Tdecimal emptyStringType" />
	</xsd:simpleType>
	<xsd:complexType name="TdecimalPole">
		<xsd:simpleContent>
			<xsd:extension base="XdecimalPole">
				<xsd:attribute name="err" type="xsd:unsignedByte" use="required" />
				<xsd:attribute name="pole" type="xsd:string" default="y" />
			</xsd:extension>
		</xsd:simpleContent>
	</xsd:complexType>
	<!-- typ riadku kdde je datum aj cislo -->
	<xsd:complexType name="TdatumSuma">
		<xsd:sequence>
			<xsd:element name="datum" type="xsdStringType" />
			<xsd:element name="suma" type="TdecimalPole" />
		</xsd:sequence>
	</xsd:complexType>
	<!-- typ riadku kde je text aj cislo -->
	<xsd:complexType name="TtextSuma">
		<xsd:sequence>
			<xsd:element name="text" type="stringPType" />
			<xsd:element name="suma" type="TdecimalPole" />
		</xsd:sequence>
	</xsd:complexType>
	<!-- tabulka A -->
	<xsd:complexType name="Ttab_a">
		<xsd:sequence>
			<xsd:element name="r01" type="TdecimalPole" />
			<xsd:element name="r02" type="TdecimalPole" />
			<xsd:element name="r03" type="TdecimalPole" />
			<xsd:element name="r04" type="TdecimalPole" />
			<xsd:element name="r05" type="TdecimalPole" />
			<xsd:element name="r06" type="TdecimalPole" />
			<xsd:element name="r07" type="TdecimalPole" />
			<xsd:element name="r08" type="TdecimalPole" />
			<xsd:element name="r09" type="TdecimalPole" />
			<xsd:element name="r10" type="TdecimalPole" />
			<xsd:element name="r11" type="TdecimalPole" />
			<xsd:element name="r12" type="TdecimalPole" />
			<xsd:element name="r13" type="TdecimalPole" />
			<xsd:element name="r14" type="TdecimalPole" />
			<xsd:element name="r15" type="TdecimalPole" />
			<xsd:element name="r16" type="TdecimalPole" />
			<xsd:element name="r17" type="TdecimalPole" />
			<xsd:element name="r18" type="TdecimalPole" />
			<xsd:element name="r19" type="TdecimalPole" />
		</xsd:sequence>
	</xsd:complexType>
	<!-- tabulka B -->
	<xsd:complexType name="Ttab_b">
		<xsd:sequence>
			<xsd:element name="r01" type="TdecimalPole" />
			<xsd:element name="r02" type="TdecimalPole" />
			<xsd:element name="r03" type="TdecimalPole" />
		</xsd:sequence>
	</xsd:complexType>
	<!-- tabulka C -->
	<xsd:complexType name="Ttab_c">
		<xsd:sequence>
			<xsd:element name="r01" type="TdecimalPole" />
			<xsd:element name="r02" type="TdecimalPole" />
			<xsd:element name="r03" type="TdecimalPole" />
		</xsd:sequence>
	</xsd:complexType>
	<!-- tabulka D -->
	<xsd:complexType name="Ttab_d">
		<xsd:sequence>
			<xsd:element name="r01" type="TdecimalPole" />
			<xsd:element name="r02" type="TdecimalPole" />
			<xsd:element name="r03" type="TdecimalPole" />
			<xsd:element name="r04" type="TdecimalPole" />
			<xsd:element name="r05" type="TdecimalPole" />
		</xsd:sequence>
	</xsd:complexType>
	<!-- tabulka E -->
	<xsd:complexType name="Ttab_e">
		<xsd:sequence>
			<xsd:element name="r01" type="TdecimalPole" />
			<xsd:element name="r02" type="TdecimalPole" />
			<xsd:element name="r03" type="TdecimalPole" />
			<xsd:element name="r04" type="TdecimalPole" />
			<xsd:element name="r05" type="TdecimalPole" />
			<xsd:element name="r06" type="TdecimalPole" />
		</xsd:sequence>
	</xsd:complexType>
	<!-- tabulka F -->
	<xsd:complexType name="Ttab_f">
		<xsd:sequence>
			<xsd:element name="cast1" type="Tcast1" />
			<xsd:element name="cast2" type="Tcast2" />
			<xsd:element name="cast3" type="Tcast3" />
		</xsd:sequence>
	</xsd:complexType>
	<!-- tabulka G -->
	<xsd:complexType name="Ttab_g">
		<xsd:sequence>
			<xsd:element name="r01" type="TdecimalPole" />
			<xsd:element name="r02" type="TdecimalPole" />
		</xsd:sequence>
	</xsd:complexType>
	<!-- tabulka H -->
	<xsd:complexType name="Ttab_h">
		<xsd:sequence>
			<xsd:element name="r01" type="TdecimalPole" />
			<xsd:element name="r02" type="TdecimalPole" />
			<xsd:element name="r03" type="TdecimalPole" />
			<xsd:element name="r04" type="TdecimalPole" />
		</xsd:sequence>
	</xsd:complexType>
	<xsd:complexType name="Tstlpce">
		<xsd:sequence>
			<xsd:element name="s01" type="TdecimalPole" />
			<xsd:element name="s02" type="TdecimalPole" />
			<xsd:element name="s03" type="TdecimalPole" />
			<xsd:element name="s04" type="TdecimalPole" />
		</xsd:sequence>
	</xsd:complexType>
	<!-- cast 1 tabulky F -->
	<xsd:complexType name="Tcast1">
		<xsd:sequence>
			<xsd:element name="riadok" type="Tstlpce" minOccurs="8" maxOccurs="8" />
		</xsd:sequence>
	</xsd:complexType>
	<!-- cast 2 tabulky F -->
	<xsd:complexType name="Tcast2">
		<xsd:sequence>
			<xsd:element name="riadok" type="Tstlpce" minOccurs="8" maxOccurs="8" />
		</xsd:sequence>
	</xsd:complexType>
	<!-- cast 3 tabulky F -->
	<xsd:complexType name="Tcast3">
		<xsd:sequence>
			<xsd:element name="riadok" type="Tstlpce" minOccurs="8" maxOccurs="8" />
		</xsd:sequence>
	</xsd:complexType>
</xsd:schema>"""

        self.transformation = """<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format">






	<xsl:output method="text" omit-xml-declaration="yes" encoding="ISO-8859-2"/>


	<xsl:template match="banka">
Názov banky alebo pobočky zahraničnej banky:<xsl:value-of select="nazov_banky"/>
Číslo účtu:<xsl:value-of select="ucet"/>
Kód banky:<xsl:value-of select="kod_banky"/>
	</xsl:template>



















	<xsl:template match="cast1/riadok">
Zdaňovacie obdobie:<xsl:value-of select="s01"/>
Celková výška daňovej straty umorovanej podľa zákona č. 286/1992 Zb.:<xsl:value-of select="s02"/>
Celková výška daňovej straty umorovanej podľa zákona č. 366/1999 Z. z. vykázaná za jedno zdaň. obdobie:<xsl:value-of select="s03"/>
Celková výška daňovej straty umorovanej podľa zákona č. 366/1999 Z. z. vykázaná v úhrne najviac za tri zdaň. obdobia:<xsl:value-of select="s04"/>
	</xsl:template>

	<xsl:template match="cast2/riadok">
Zdaňovacie obdobie:<xsl:value-of select="s01"/>
Pomerná časť daňovej straty umorovanej v zdaňovacom období podľa zákona č. 286/1992 Zb.:<xsl:value-of select="s02"/>
Pomerná časť daňovej straty umorovanej v zdaňovacom období podľa zákona č. 366/1999 Z. z.:<xsl:value-of select="s03"/>
Pomerná časť daňovej straty umorovanej v zdaňovacom období spolu:<xsl:value-of select="s04"/>
	</xsl:template>

	<xsl:template match="cast3/riadok">
Zdaňovacie obdobie:<xsl:value-of select="s01"/>
Skutočne vykázaný základ dane v zdaňovacom období:<xsl:value-of select="s02"/>
Suma základu dane nad 150 tis. Sk:<xsl:value-of select="s03"/>
Skutočne umorená strata:<xsl:value-of select="s04"/>
	</xsl:template>

	<xsl:template match="/">DAŇOVÉ PRIZNANIE K DANI Z PRÍJMOV PRÁVNICKYCH OSÔB
PODĽA ZÁKONA č. 366/1999 Z. z. O DANIACH Z PRÍJMOV
V ZNENÍ NESKORŠÍCH PREDPISOV (ĎALEJ LEN "ZÁKON") PO

Daňové identifikačné číslo:<xsl:value-of select="/dokument/hlavicka/dic"/>
IČO:<xsl:value-of select="/dokument/hlavicka/ico"/>
Právna forma:<xsl:value-of select="/dokument/hlavicka/pravna_forma"/>
Druh daňového priznania:<xsl:if test="/dokument/hlavicka/typDP/rdp = '1'"></xsl:if><xsl:if test="/dokument/hlavicka/typDP/odp = '1'">opravné </xsl:if><xsl:if test="/dokument/hlavicka/typDP/ddp = '1'">dodatočné </xsl:if>daňové priznanie
Za zdaňovacie obdobie od:<xsl:value-of select="/dokument/hlavicka/zdanovacie_obd/datum_od/den"/>.<xsl:value-of select="/dokument/hlavicka/zdanovacie_obd/datum_od/mesiac"/>.
Za zdaňovacie obdobie do:<xsl:value-of select="/dokument/hlavicka/zdanovacie_obd/datum_do/den"/>.<xsl:value-of select="/dokument/hlavicka/zdanovacie_obd/datum_do/mesiac"/>.<xsl:value-of select="/dokument/hlavicka/zdanovacie_obd/rok"/>

I.ČASŤ - ÚDAJE O PRÁVNICKEJ OSOBE
Obchodné meno:<xsl:value-of select="/dokument/hlavicka/obch_meno"/>

SÍDLO
Ulica:<xsl:value-of select="/dokument/hlavicka/sidlo/ulica"/>
Číslo:<xsl:value-of select="/dokument/hlavicka/sidlo/cislo"/>
PSČ:<xsl:value-of select="/dokument/hlavicka/sidlo/psc"/>
Obec:<xsl:value-of select="/dokument/hlavicka/sidlo/obec"/>
Štát:<xsl:value-of select="/dokument/hlavicka/sidlo/stat"/>
Telefón:<xsl:value-of select="/dokument/hlavicka/sidlo/tel"/>
Fax:<xsl:value-of select="/dokument/hlavicka/sidlo/fax"/>
<xsl:apply-templates select="/dokument/hlavicka/sidlo/banka"/>

OSOBA OPRÁVNENÁ NA PODANIE DAŇOVÉHO PRIZNANIA ZA PRÁVNICKÚ OSOBU
Priezvisko:<xsl:value-of select="/dokument/hlavicka/opravnena_osoba/priezvisko"/>
Meno:<xsl:value-of select="/dokument/hlavicka/opravnena_osoba/meno"/>
Titul:<xsl:value-of select="/dokument/hlavicka/opravnena_osoba/titul"/>
Postavenie vzhľadom k právnickej osobe:<xsl:value-of select="/dokument/hlavicka/opravnena_osoba/postavenie"/>
Ulica a číslo:<xsl:value-of select="/dokument/hlavicka/opravnena_osoba/sidlo_oo/ulicacislo"/>
PSČ:<xsl:value-of select="/dokument/hlavicka/opravnena_osoba/sidlo_oo/psc"/>
Obec:<xsl:value-of select="/dokument/hlavicka/opravnena_osoba/sidlo_oo/obec"/>
Štát:<xsl:value-of select="/dokument/hlavicka/opravnena_osoba/sidlo_oo/stat"/>
Telefón:<xsl:value-of select="/dokument/hlavicka/opravnena_osoba/sidlo_oo/tel"/>
Fax:<xsl:value-of select="/dokument/hlavicka/opravnena_osoba/sidlo_oo/fax"/>

Počet príloh:<xsl:value-of select="/dokument/hlavicka/pocet_priloh"/>

II. ČASŤ - VÝPOČET ZÁKLADU DANE A URČENIE VÝSLEDNÉHO VZŤAHU K ŠTÁTNEMU ROZPOČTU
Hospodársky výsledok pred zdanením (zisk +, strata -) alebo rozdiel medzi príjmami a výdavkami (§ 23 ods. 2 zákona) (r. 1- r. 2 tabuľky H - III. časť):<xsl:value-of select="/dokument/body/r100"/>

POLOŽKY ZVYŠUJÚCE HOSPODÁRSKY VÝSLEDOK ALEBO ROZDIEL MEDZI PRÍJMAMI A VÝDAVKAMI
Sumy, ktoré neoprávnene skrátili príjmy a sumy nepeňažných plnení, ak nie sú súčasťou riadku 100:<xsl:value-of select="/dokument/body/r110"/>
Sumy podľa § 23 ods. 3 písm. f) a g) zákona prijaté v zdaňovacom období, za ktoré sa priznanie podáva, ak nie sú súčasťou riadku 100:<xsl:value-of select="/dokument/body/r120"/>
Výdavky (náklady), ktoré nie sú daňovými výdavkami podľa § 25 zákona alebo ktoré boli vynaložené v rozpore alebo nad rozsah § 24 zákona, okrem súm uvedených na r. 140, 150 a 180 (tab. A - III. časť):<xsl:value-of select="/dokument/body/r130"/>
Sumy podľa § 24 ods. 3 zákona a sumy zmluvných pokút, ktoré neboli zaplatené do termínu vyplývajúceho z § 23 ods. 3 zákona:<xsl:value-of select="/dokument/body/r140"/>
Rozdiel, o ktorý odpisy hmotného majetku uplatnené v účtovníctve prevyšujú daňové odpisy tohto majetku (tabuľka B - III. časť):<xsl:value-of select="/dokument/body/r150"/>
Rozdiel medzi vyšším ocenením nepeňažného vkladu do základného imania a cenou podľa § 23 ods. 21 zákona:<xsl:value-of select="/dokument/body/r160"/>
Úprava (zvýšenie) základu dane v prípade zrušenia daňovníka likvidáciou alebo zrušením konkurzu (§ 20 ods. 2 a § 23 ods. 12 zákona):<xsl:value-of select="/dokument/body/r170"/>
Ostatné položky vyžadujúce riadok 100, neuvedené v r. 110 až 170:<xsl:value-of select="/dokument/body/r180"/>
Príjmy, ktoré sú predmetom dane podľa § 18 ods. 4 zákona, ak nie sú súčasťou riadku 100:<xsl:value-of select="/dokument/body/r190"/>
Medzisúčet (r. 110 + r. 120 + r. 130 + r. 140 + r. 150 + r. 160 + r. 170 + r. 180 + r. 190):<xsl:value-of select="/dokument/body/r200"/>

POLOŽKY ZNIŽUJÚCE HOSPODÁRSKY VÝSLEDOK ALEBO ROZDIEL MEDZI PRÍJMAMI A VÝDAVKAMI
Príjmy, ktoré nie sú predmetom dane podľa § 18 ods. 2 zákona, ak sú súčasťou riadku 100:<xsl:value-of select="/dokument/body/r210"/>
Príjmy, ktoré nie sú predmetom dane u daňovníkov nezaložený alebo nezriadených na podnikanie (§ 18 ods. 5 zákona), ak sú súčasťou riadku 100 a nie sú uvedené na riadku 210:<xsl:value-of select="/dokument/body/r220"/>
Príjmy a ostatné položky oslobodené od dane podľa § 19 zákona, ak nie sú súčasťou riadku 100:<xsl:value-of select="/dokument/body/r230"/>
Príjmy nezahrňované do základu dane podľa § 23 ods. 4 písm. a) zákona , z ktorých je daň vyberaná osobitnou sadzbou (§ 36 zákona), vybraním ktorej je daňová povinnosť splnená:<xsl:value-of select="/dokument/body/r240"/>
Rozdiel, o ktorý daňové odpisy hmotného majetku prevyšujú odpisy tohto majetku uplatnené v účtovníctve (tabuľka B - III. časť):<xsl:value-of select="/dokument/body/r250"/>
Sumy podľa § 23 ods. 3 písm. d) a g) zákona, ak neboli prijaté do konca zdaňovacieho obdobia, za ktoré sa priznanie podáva, ak sú súčasťou riadku 100:<xsl:value-of select="/dokument/body/r260"/>
Sumy podľa § 24 ods. 3 zákona a sumy zmluvných pokút, ktoré boli zaplatené v zdaňovacom období, ak nie sú súčasťou riadku 100:<xsl:value-of select="/dokument/body/r270"/>
Úprava (zníženie) základu dane v prípade zrušenia daňovníka likvidáciou alebo zrušením konkurzu (§ 20 ods. 2 a § 23 ods. 12 zákona):<xsl:value-of select="/dokument/body/r280"/>
Ostatné položky nezahrňované do základu dane, znižujúce riadok 100:<xsl:value-of select="/dokument/body/r290"/>
Medzisúčet (r. 210 + r. 220 + r. 230 + r. 240 + r. 250 + r. 260 + r. 270 + r. 280 + r. 290):<xsl:value-of select="/dokument/body/r300"/>

ZÁKLAD DANE ALEBO DAŇOVÁ STRATA
Základ dane alebo daňová strata (r. 100 + r. 200 - r. 300):<xsl:value-of select="/dokument/body/r310"/>
Časť základu dane alebo daňovej straty, preukázanej spoločnosťou, pripadajúca na komplementárov a na spoločníkov verejnej obchodnej spoločnosti:<xsl:value-of select="/dokument/body/r320"/>
Úhrn vyňatých príjmov (základov dane) podliehajúcich zdaneniu v zahraničí:<xsl:value-of select="/dokument/body/r330"/>
Základ dane (+) alebo daňová strata (-) po úprave o položky uvedené na riadkoch 320 a 330 (r. 310 - r.320 - r. 330):<xsl:value-of select="/dokument/body/r400"/>

POLOŽKY ODPOČÍTATEĽNÉ OD ZÁKLADU DANE UVEDENÉHO NA RIADKU 400
Odpočet daňovej straty (tabuľka F - III. časť):<xsl:value-of select="/dokument/body/r410"/>
Hodnota darov podľa § 20 ods. 7 zákona, najviac do výšky 2% z riadku 400 (tabuľka D - III. časť):<xsl:value-of select="/dokument/body/r420"/>
Zaplatený príspevok jednému združeniu právnických osôb, najviac do výšky 0,2 % z objemu zúčtovaných miezd (§ 20 ods. 12 zákona):<xsl:value-of select="/dokument/body/r430"/>
Suma ostatných nákladov na reklamu vymedzených v §34 ods. 1 písm a) zákona, najviac do výšky 1 % z riadku 400 (tabuľka G - III. časť):<xsl:value-of select="/dokument/body/r440"/>
Suma nákladov na reklamné predmety vymedzených v §34 ods. 1 písm b) zákona, najviac do výšky 0,2 % z riadku 400 (tabuľka G - III. časť):<xsl:value-of select="/dokument/body/r450"/>
Ostatné položky odpočítateľné od základu dane neuvedené na riadkoch 410 až 450:<xsl:value-of select="/dokument/body/r460"/>
Úhrn položiek odpočítateľných od základu dane, uvedených na riadkoch 410 až 460, najviac do kladnej sumy na r. 400:<xsl:value-of select="/dokument/body/r470"/>
Základ dane znížený o položky odpočítateľné od základu dane, zaokrúhlené na celé tisícky Sk nadol (r. 400 - r. 470):<xsl:value-of select="/dokument/body/r500"/>

SADZBA DANE A DAŇ PRED UPLATNENÍM ÚĽAV NA DANI A UPLATNENÍM ZÁPOČTU DANE ZAPLATENEJ V ZAHRANIČÍ
Sadzba dane podľa § 21 zákona (v %):<xsl:value-of select="/dokument/body/r510"/>
Daň pred uplatnením úľav na dani (r. 500 x r. 510) / 100:<xsl:value-of select="/dokument/body/r600"/>

ÚĽAVY NA DANI
Oslobodenie od dane na základe § 102 zákona č. 511/19992 Zb. v znení neskorších predpisov, uplatňované na základe<xsl:if test="/dokument/body/r610/text != ''"> <xsl:value-of select="/dokument/body/r610/text"/></xsl:if>:<xsl:value-of select="/dokument/body/r610/suma"/>
Úľava na dani podľa<xsl:if test="/dokument/body/r620/text !=''"> <xsl:value-of select="/dokument/body/r620/text"/></xsl:if>:<xsl:value-of select="/dokument/body/r620/suma"/>
Zníženie dane podľa § 35 ods. 14 a 15 zákona:<xsl:value-of select="/dokument/body/r630"/>
Zníženie dane podľa § 35 ods. 16 a 17 zákona:<xsl:value-of select="/dokument/body/r640"/>
Úhrn úľav na dani, najviac do sumy uvedenej na riadku 600 (r. 610 + r. 620 + r. 630 + r. 640):<xsl:value-of select="/dokument/body/r650"/>
Daň znížená o úhrn úľav na dani (r. 600 - r. 650):<xsl:value-of select="/dokument/body/r700"/>

VÝSLEDNÁ DAŇ PO UPLATNENÍ ZÁPOČTU DANE ZAPLATENEJ V ZAHRANIČÍ
Zápočet dane zaplatenej v zahraničí, najviac do sumy uvedenej na riadku 700 (z riadku 6 tabuľky E - III. časť):<xsl:value-of select="/dokument/body/r710"/>
Daň po úľavách a po zápočte dane uvedenej na riadku 710 zaokrúhlená na celé stovky Sk nahor (r. 700 - r. 710):<xsl:value-of select="/dokument/body/r800"/>

DAŇOVÁ POVINNOSŤ A VÝSLEDNÝ VZŤAH K ŠTÁTNEMU ROZPOČTU
Na daňovú povinnosť za zdaňovacie obdobie bolo v termíne do <xsl:value-of select="/dokument/body/r810/datum"/> preddavkovo uhradené (§ 50 zákona):<xsl:value-of select="/dokument/body/r810/suma"/>
Na daňovú povinnosť za zdaňovacie obdobie bolo v termíne do <xsl:value-of select="/dokument/body/r820/datum"/> preddavkovo zrazené inou fyzickou alebo právnickou osobou (§ 53 zákona):<xsl:value-of select="/dokument/body/r820/suma"/>
Suma preddavkovo vybratej dane z úrokov [§ 36 ods. 2 písm. c) bod 8 zákona]:<xsl:value-of select="/dokument/body/r830"/>
Celkovo preddavkovo uhradená daň (r. 810 + r. 820 + r. 830):<xsl:value-of select="/dokument/body/r840"/>
Daňová povinnosť z r. 800 alebo z r. 830:<xsl:value-of select="/dokument/body/r850"/>
Výsledný vzťah k štátnemu rozpočtu k termínu <xsl:value-of select="/dokument/body/r900/datum"/> Preplatok (-) Nedoplatok (+) (r. 850 - r. 840):<xsl:value-of select="/dokument/body/r900/suma"/>

VZŤAH KU ŠTÁTNEMU ROZPOČTU PO ZOHĽADNENÍ PREDDAVKOVO PLATENEJ DANE
Minimálna výška preddavkovo platenej dane podľa § 21 ods. 4 zákona:<xsl:value-of select="/dokument/body/r901"/>
Vzťah k štátnemu rozpočtu po zohľadnení preddavkovo zaplatenej dane podľa § 21 ods. 4 zákona:<xsl:value-of select="/dokument/body/r902"/>

DAŇ PRE ÚČELY STANOVENIA VÝŠKY PREDDAVKOV NA DAŇ
Daň pre účely stanovenia výšky preddavkov na daň podľa § 50 zákona (r. 600 - r. 620 - r. 630 - r. 640 - r. 710 - r. 830):<xsl:value-of select="/dokument/body/r910"/>

DODATOČNÉ DAŇOVÉ PRIZNANIE
Dátum zistenia vyššej daňovej povinnosti:<xsl:value-of select="/dokument/body/ddp_datum"/>
Posledná známa daňová povinnosť (r. 800 daňového priznania):<xsl:value-of select="/dokument/body/r920"/>
Novo zistená daňová povinnosť (r. 800 dodatočného priznania):<xsl:value-of select="/dokument/body/r930"/>
Zvýšenie (+) alebo zníženie (-) dane (r. 930 - r. 920):<xsl:value-of select="/dokument/body/r940"/>
Posledná známa daňová strata (absolútna hodnota r. 400 daňového priznania):<xsl:value-of select="/dokument/body/r950"/>
Novo zistená daňová strata (absolútna hodnota r. 400 dodatočného priznania):<xsl:value-of select="/dokument/body/r960"/>
Zvýšenie (+) alebo zníženie (-) daňovej straty (r. 960 - r. 950):<xsl:value-of select="/dokument/body/r970"/>

III. ČASŤ - TABUĽKY POMOCNÝCH VÝPOČTOV A DOPLŇUJÚCICH ÚDAJOV

A - POLOŽKY, KTORÉ NIE SÚ DAŇOVÝMI VÝDAVKAMI (K RIADKU 130 II. ČASTI)
Trvalý rozdiel z odpisov uplatňovaných v účtovníctve a limitov odpisov osobných dobravných prostriedkov [§ 24 ods. 2 písm. a) zákona], ak nie je súčasťou riadku 150:<xsl:value-of select="/dokument/body/tab_a/r01"/>
Rozdiel medzi zostatkovou cenou hmotného a nehmotného majetku a nižším príjmom zahŕňaným do základu dane [§ 24 ods. 2 písm. b) zákona] vrátane rozdielu medzi obstarávacou cenou hmotného majetku vylúčeného z odpisovania a nižším príjmom z jeho predaja [§ 24 ods. 2 písm. e) zákona]:<xsl:value-of select="/dokument/body/tab_a/r02"/>
Tvorba rezerv neuznaná ako daňový výdavok nad ráme § 24 ods. 2 písm h) zákona (neuznaná rezerva v nadväznosti na tabuľku C a ďalšie neuznané rezrevy):<xsl:value-of select="/dokument/body/tab_a/r03"/>
Cena obstarania cenných papierov prevyšujúca príjem z predaja [§ 24 ods. 2 písm o) zákona]:<xsl:value-of select="/dokument/body/tab_a/r04"/>
Rozdiel medzi hodnotou alebo cenou obstarania pohľadávky a nižším príjmom plynúcim z jej postúpenia alebo úhrady [§ 24 ods. 2 písm r) zákona]:<xsl:value-of select="/dokument/body/tab_a/r05"/>
Spotreba PHL presahujúca zákonom stanovený limit [§ 24 ods. 2 písm v) zákona]:<xsl:value-of select="/dokument/body/tab_a/r06"/>
Trvalý rozdiel medzi zaúčtovaným nájomným a limitom u osobných dopravných prostriedkov [§ 24 ods. 3 písm f) zákona]:<xsl:value-of select="/dokument/body/tab_a/r07"/>
Odmeny členov štatutárnych orgánov a ďalších orgánov právnických osôb [§ 25 ods. 1 písm d) zákona]:<xsl:value-of select="/dokument/body/tab_a/r08"/>
Výdavky vynaložené na príjmy oslobodené od dane alebo nezahŕňané do základu dane [§ 25 ods. 1 písm i) zákona]:<xsl:value-of select="/dokument/body/tab_a/r09"/>
Manká a škody presahujúce prijaté náhrady [§ 25 ods. 1 písm n) zákona]:<xsl:value-of select="/dokument/body/tab_a/r10"/>
Výdavky na reprezentáciu vrátane reklamných predmetov podľa § 34 ods. 1 písm b) zákona uvedených na r. 2 tabuľky G:<xsl:value-of select="/dokument/body/tab_a/r11"/>
Tvorba opravných položiek podľa § 25 ods. 1 písm v) zákona:<xsl:value-of select="/dokument/body/tab_a/r12"/>
Úroky z úverov a pôžičiek poskytnutých subjektami, ktoré sa zúčastňujú priamo alebo nepriamo na vedení, kontrole alebo majetku príjemcu úveru alebo pôžičky, nezahŕňané do výdavkov podľa § 25:<xsl:value-of select="/dokument/body/tab_a/r13"/>
Odplaty (provízie) za sprostredkovanie s výnimkou provízií podľa § 24 ods. 3 písm. h) a m) zákona:<xsl:value-of select="/dokument/body/tab_a/r14"/>
Príspevky právnickým osobám nad rámec § 24 ods. 3 písm. a) zákona:<xsl:value-of select="/dokument/body/tab_a/r15"/>
Výdavky na reklamu presahujúce rámec § 24 ods. 2 písm u) zákona, vrátane výdavkov na ostatnú reklamu podľa § 34 ods. 1 písm. a) zákona uvedených na r. 1 tabuľky G:<xsl:value-of select="/dokument/body/tab_a/r16"/>
Poskytnuté dary (r. 1 tabuľky D):<xsl:value-of select="/dokument/body/tab_a/r17"/>
Ostatné položky, ktoré nie sú daňovými výdavkami, neuvedené na riadkoch 1až 17:<xsl:value-of select="/dokument/body/tab_a/r18"/>
Úhrn riadkov 1 až 18 (k r. 130 II. časti):<xsl:value-of select="/dokument/body/tab_a/r19"/>

B - ODPISY HMOTNÉHO MAJETKU
Odpisy hmotného majetku podľa § 24 ods. 2 písm. a) zákona:<xsl:value-of select="/dokument/body/tab_b/r01"/>
Účtovné odpisy hmotného investičného majetku:<xsl:value-of select="/dokument/body/tab_b/r02"/>
Odpisy nezahrnuté v daňových výdavkoch z dôvodu prerušenia odpisovania (§ 26 ods. 9 zákona):<xsl:value-of select="/dokument/body/tab_b/r03"/>

C - REZERVA NA OPRAVU HMOTNÉHO MAJETKU
Suma tvorby rezerv na opravu hmotného majetku za zdaňovacie obdobie:<xsl:value-of select="/dokument/body/tab_c/r01"/>
Stav zostatkov rezerv na opravu hmotného majetku na konci zdaňovacieho obdobia:<xsl:value-of select="/dokument/body/tab_c/r02"/>
Úhrn vstupných cien alebo zvýšených vstupných cien majetku, ku ktorému sú rezervy tvorené:<xsl:value-of select="/dokument/body/tab_c/r03"/>

D - PREHĽAD O POSKYTNUTÝCH DAROCH (K RIADKU 420 II. ČASTI)
Celková výška poskytnutých darov:<xsl:value-of select="/dokument/body/tab_d/r01"/>
Suma darov poskytnutých na účely podľa § 20 ods. 7 zákona (časť z hodnoty r. 1):<xsl:value-of select="/dokument/body/tab_d/r02"/>
Dary poskytnuté na financovanie školstva (časť z hodnoty r. 2):<xsl:value-of select="/dokument/body/tab_d/r03"/>
Dary poskytnuté na financovanie kultúry (časť z hodnoty r. 2):<xsl:value-of select="/dokument/body/tab_d/r04"/>
Dary poskytnuté na sociálne a zdravotné účely (časť z hodnoty r. 2):<xsl:value-of select="/dokument/body/tab_d/r05"/>

E - ZÁPOČET DANE ZAPLATENEJ V ZAHRANIČÍ (K RIADKU 710 II. ČASTI)
Základ dane uvedený na riadku 400:<xsl:value-of select="/dokument/body/tab_e/r01"/>
Úhrn príjmov (základov dane) zdanených v zahraničí, pri ktorých je uplatňovaný zápočet (zaokrúhlený na celé koruny nadol):<xsl:value-of select="/dokument/body/tab_e/r02"/>
Pomer príjmov z riadku 2 k základu dane na riadku 1 v % (vypočítaný na dve desatinné miesta) (r. 2 / r. 1) x 100:<xsl:value-of select="/dokument/body/tab_e/r03"/>
Maximálna výška dane zaplatenej v zahraničí, ktorú je možné započítať (zaokrúhlená na celé koruny nahor) (r. 600 II. časti x r. 3) / 100:<xsl:value-of select="/dokument/body/tab_e/r04"/>
Úhrn dane zaplatenej v zahraničí uplatňovanej na zápočet vzťahujúcej sa k príjmom uvedeným na r. 2 (zaokrúhlený na celé koruny nahor):<xsl:value-of select="/dokument/body/tab_e/r05"/>
Výška dane zaplatenej v zahraničí, ktorú je možné započítať (uvedie sa nižšia suma z r. 4 a r. 5):<xsl:value-of select="/dokument/body/tab_e/r06"/>

F - EVIDENCIA A ODPOČET STRATY PODĽA § 34 ZÁKONA Č. 258/1992 ZB. A § 34 ZÁKONA Č. 366/1999 Z. z. (K RIADKU 410 II. ČASTI)<xsl:apply-templates select="/dokument/body/tab_f/cast1"/>
<xsl:apply-templates select="/dokument/body/tab_f/cast2"/>
<xsl:apply-templates select="/dokument/body/tab_f/cast3"/>

G - NÁKLADY NA OSTATNÚ REKLAMU A REKLAMNÉ PREDMETY (K RIADKOM 440 A 450 II. ČASTI)
Náklady vynaložené na ostatnú reklamu podľa § 34 ods. 1 písm. a) zákona:<xsl:value-of select="/dokument/body/tab_g/r01"/>
Náklady vynaložené na reklamné predmety podľa § 34 ods. 1 písm. b) zákona:<xsl:value-of select="/dokument/body/tab_g/r02"/>

H - DOPLŇUJÚCE ÚDAJE
Súčet prevádzkových, finančných a mimoriadnych výnosov:<xsl:value-of select="/dokument/body/tab_h/r01"/>
Súčet prevádzkových, finančných a mimoriadnych nákladov:<xsl:value-of select="/dokument/body/tab_h/r02"/>
Suma zrazenej dane podľa § 53 zákona:<xsl:value-of select="/dokument/body/tab_h/r03"/>
Stav zamestnancov k poslednému dňu zdaňovacieho obdobia:<xsl:value-of select="/dokument/body/tab_h/r04"/>
	</xsl:template>
</xsl:stylesheet>"""
