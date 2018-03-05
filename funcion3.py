from lxml import etree

doc = etree.parse('206974-0-agenda-eventos-culturales-100.xml')
xml = etree.tostring(doc,pretty_print=True ,xml_declaration=True, encoding="utf-8")

raiz = doc.getroot()


busqueda=input("Dime el distrito que desee ver sus activades: ")
busqueda1=busqueda.upper()

listado=[]

bloque=raiz.findall('contenido')
for contenido in bloque:
	for contenidos in contenido[1]:
		if contenidos.attrib["nombre"]=="TITULO":
			listadotemp=contenidos.text
		for contenidos1 in contenidos:
			if contenidos1.attrib["nombre"]=="DISTRITO":
				if busqueda1 == contenidos1.text:
					listado.append(listadotemp)
					listadotemp=()
				else:
					listadotemp=()


if len(listado) >= 1:
	print(listado)
	print('El numero total de actividades para la busqueda es: %i' % (len(listado)))
else:
	print('Error no se ha encontrado ninguna actividad en la localidad deseada.')