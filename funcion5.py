from lxml import etree

doc = etree.parse('206974-0-agenda-eventos-culturales-100.xml')
xml = etree.tostring(doc,pretty_print=True ,xml_declaration=True, encoding="utf-8")

raiz = doc.getroot()

busqueda=input("¿Desea ver el listado de actividades gratuitas o de pago?: ")
busqueda1=busqueda.upper()

contadorG=0
contadorP=0

if busqueda1 == "GRATUITAS" or busqueda1 == "GRATIS":
	contadorG=1
if busqueda1 == "PAGO" or busqueda1 == "COSTE":
	contadorP=1
elif busqueda1 != "PAGO" or busqueda1 != "COSTE" or busqueda1 != "GRATUITAS" or busqueda1 != "GRATIS":
	print("Error el dato introducido no coincide.")


listado=[]

contador = 0

if contadorG == 1:

	bloque1=raiz.findall('contenido/atributos/atributo')
	for contenido1 in bloque1:
		if contenido1.attrib["nombre"]=="TITULO":
			listtemp=contenido1.text
		if contenido1.attrib["nombre"]=="GRATUITO":
			if contenido1.text == "1":
				listado.append(listtemp)
				listtemp=()
			else:
				listtemp=()

if contadorP == 1:

	bloque1=raiz.findall('contenido/atributos/atributo')
	for contenido1 in bloque1:
		if contenido1.attrib["nombre"]=="TITULO":
			listtemp=contenido1.text
		if contenido1.attrib["nombre"]=="GRATUITO":
			if contenido1.text == "0":
				listado.append(listtemp)
				listtemp=()
			else:
				listtemp=()

print(" ")
print("Estas son las actividades de tipo: %s encontradas: " % (busqueda1))
print(" ")
print(listado)
print(" ")
print("Total actividades encontradas: %d" % (len(listado)))