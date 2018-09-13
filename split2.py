
text = open("SnapOnVistas.sql", "r")
a = text.read().split('\n')

rst = []



#procedure = a[0][a[0].find('.'):]
#procedure = procedure.replace('.', '').replace('[','').replace(']','').strip()

#print(procedure)
#print(a[0])
newVScript = 10
cont = 0
#rst.append('vScript = "ALTER PROCEDURE ' + procedure + '"')
#rst.append("Else ' Si no existe lo creo")
#rst.append('vScript = "CREATE PROCEDURE ' + procedure + '"')
#rst.append("End If 'Existe_Stored_Procerude((\""+ procedure +"\"), dbsConnect)")
#rst.append(" \n ")
#rst.append('vScript = vScript & _ ')

for idx, i in enumerate(a):
	cont = 0
	if (i.strip()):
		if not(('--' in [x for x in i.strip().split(' ')]) or ('/******' in [x for x in i.strip().split(' ')]) or ('-' in [x[x.find('-')] for x in i])):
			print(i)
			if('PROCEDURE' in [x for x in i.strip().split(' ')]):
				procedure = i[i.find('.'):]
				procedure = procedure.replace('.', '').replace('[','').replace(']','').strip()
				print(procedure)
				rst.append("If Existe_Stored_Procerude((\""+ procedure +"\"), dbsConnect) Then ' Si existe lo modifico")
				rst.append('vScript = "ALTER PROCEDURE ' + procedure + '"')
				rst.append("Else ' Si no existe lo creo")
				rst.append('vScript = "CREATE PROCEDURE ' + procedure + '"')
				rst.append("End If 'Existe_Stored_Procerude((\""+ procedure +"\"), dbsConnect)")
				rst.append(" \n ")
				rst.append('vScript = vScript & _ ')
			else:
				if (i == 'END'):
					rst.append('" ' + i.strip() + ' " ')
					rst.append(" \n ")
					rst.append("If Not Operacion_Exitosa((vScript), dbsConnect) Then")
					rst.append("Stored_Procedures = False")
					rst.append("End If   ' (Not Operacion_Exitosa)")
					rst.append(" \n ")
				else:
					if not(('--' in [x for x in i.strip().split(' ')]) & ('/******' in [x for x in i.strip().split(' ')])):
						if ((cont%newVScript == 0) & (cont>5)):

								rst.append('" ' + i.strip() + ' " ')
								rst.append('vScript = vScript & _ ')

						else: rst.append('" ' + i.strip() + ' " & _')
		cont = cont +1



with open('test2.txt', 'a') as f:
    for item in rst:
        f.write("%s\n" % item)


#DEBERIA HACER PARA QUE SE SUMEN AL TXT Y NO SE PISE
