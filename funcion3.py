from lxml import etree

doc = etree.parse('206974-0-agenda-eventos-culturales-100.xml')
xml = etree.tostring(doc,pretty_print=True ,xml_declaration=True, encoding="utf-8")

raiz = doc.getroot()


busqueda=input("Dime la localidad que desee ver sus activades: ")
busqueda1=busqueda.upper()

listado=[]

for i in range(1,(len(raiz))):

	contenido=raiz[i]

	atributos = contenido[1]

	for i in range(len(atributos)):
		atributos1=atributos[i]

		for attr,value in atributos1.items():
			locate=(attr,value)

			if locate[1] == 'LOCALIZACION':
				localizacion = atributos1[7]
				texto1 = localizacion.text

				if busqueda1 == texto1:
					atributos1 = atributos[1]
					texto1 = atributos1.text

					listado.append(texto1)

print(listado)