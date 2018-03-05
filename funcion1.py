from lxml import etree

doc = etree.parse('206974-0-agenda-eventos-culturales-100.xml')
xml = etree.tostring(doc,pretty_print=True ,xml_declaration=True, encoding="utf-8")

raiz = doc.getroot()

#contenido = raiz[1]
#tipo = contenido[0]
#tipo = tipo.text
#print(tipo)

#<atributo nombre="TITULO-ACTIVIDAD">
#VI Muestra de Teatro Latina</atributo>

#<atributo nombre="HORA-EVENTO">19:00</atributo>

actividades=[]
temact=[]

for i in range(1,(len(raiz))):

	contenido=raiz[i]
	
	#elemento = contenido[0]
	atributos = contenido[1]
	atributos1 = atributos[1]
	
	#texto = elemento.text
	texto1 = atributos1.text
	
	#print(texto1)

	temact.append(texto1)
	actividades.append(temact)

	atributos3 = atributos[6]

	for attr,value in atributos3.items():
		hora=(attr,value)
		hora=hora[1]
		hora=hora.split('-')
		hora=hora[0]

		if hora == 'HORA':
			texto3 = atributos3.text
			temact.append(texto3)

	temact=[]

print(actividades)