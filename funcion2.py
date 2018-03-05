from lxml import etree

doc = etree.parse('206974-0-agenda-eventos-culturales-100.xml')
xml = etree.tostring(doc,pretty_print=True ,xml_declaration=True, encoding="utf-8")

raiz = doc.getroot()

contador = 0

busqueda=input("Dime el distrito que desee contabilizar: ")
busqueda1=busqueda.upper()


bloque=raiz.findall('contenido')
for contenido in bloque:
	for contenidos in contenido[1]:
		for contenidos1 in contenidos:
			if contenidos1.attrib["nombre"]=="DISTRITO":
				if busqueda1 == contenidos1.text:
					contador=contador+1

if contador >= 1:
	print('Existen %d eventos en %s.' % (contador,busqueda))
else:
	print('Error, la busqueda no ha dado ningun resultado.')