from lxml import etree

doc = etree.parse('206974-0-agenda-eventos-culturales-100.xml')
xml = etree.tostring(doc,pretty_print=True ,xml_declaration=True, encoding="utf-8")

raiz = doc.getroot()

#<atributo nombre="TITULO-ACTIVIDAD">
#VI Muestra de Teatro Latina</atributo>

#<atributo nombre="HORA-EVENTO">19:00</atributo>

actividades=[]
temact=[]

bloque=raiz.findall('contenido')
for contenido in bloque:
	for contenidos in contenido[1]:
		if contenidos.attrib["nombre"]=="TITULO":
			temact.append(contenidos.text)
		if contenidos.attrib["nombre"]=="HORA-EVENTO":
			temact.append(contenidos.text)

	actividades.append(temact)

	temact=[]

print(actividades)