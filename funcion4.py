from lxml import etree

doc = etree.parse('206974-0-agenda-eventos-culturales-100.xml')
xml = etree.tostring(doc,pretty_print=True ,xml_declaration=True, encoding="utf-8")

raiz = doc.getroot()

busqueda=input("Dime la actividad que desee buscar: ")
busqueda1=busqueda.upper()

listado=[]

contador = 0



bloque=raiz.findall('contenido')
for contenido in bloque:
	for contenidos in contenido[1]:
		if contenidos.attrib["nombre"]=="TITULO":
			if contenidos.text == busqueda:
				contador=1
		
		if contador == 1:
			if contenidos.attrib["nombre"]=="TIPO":
				tipo=contenidos.text
				contador=0

tipo1 = tipo.split("/")
tipo1 = tipo1[3:]

print("El tipo de actividad que busca es: %s" % (tipo1))

bloque1=raiz.findall('contenido/atributos/atributo')
for contenido1 in bloque1:
	if contenido1.attrib["nombre"]=="TITULO":
		listtemp=contenido1.text
	if contenido1.attrib["nombre"]=="TIPO":
		if contenido1.text == tipo:
			listado.append(listtemp)
			listtemp=()
		else:
			listtemp=()

#Aceites esenciales y aromaterapia
#Actividades 8 de Marzo en el Distrito de Villa de Vallecas

print("Estas son actividades del mismo tipo que la buscada: ")
print(listado)