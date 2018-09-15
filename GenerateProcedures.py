text = open("SnapOnVistasConCollate.sql", "r")
a = text.read().split('\n')

rst = []

newVScript = 10
cont = 0
contProcedures = []
contErrores = 0
nombErrores = []
contFunction = 0


for idx, i in enumerate(a):
	i = i.strip()
	if (i.strip()):
		if('PROCEDURE' in [x for x in i.strip().split(' ')]):
			procedure = i[i.find('.'):]
			procedure = procedure[:procedure.find(']')]
			procedure = procedure.replace('.', '').replace('[','')
			contProcedures.append(procedure)
			rst.append("   If Existe_Stored_Procerude((\""+ procedure +"\"), dbsConnect) Then ' Si existe lo modifico")
			rst.append('      vScript = "ALTER PROCEDURE [dbo].[' + procedure + '] "')
			rst.append("   Else ' Si no existe lo creo")
			rst.append('      vScript = "CREATE PROCEDURE [dbo].[' + procedure + '] "')
			rst.append("   End If 'Existe_Stored_Procerude((\""+ procedure +"\"), dbsConnect)")
			rst.append(" \n ")
			rst.append('   vScript = vScript & _ ')
		else:
			if ((i.strip() == 'END') or (i.strip() == 'End')):
				rst.append('   " ' + i.strip() + ' " ')
				rst.append(" \n ")
				rst.append("   If Not Operacion_Exitosa((vScript), dbsConnect) Then")
				rst.append("      Stored_Procedures = False")
				rst.append("   End If   ' (Not Operacion_Exitosa)")
				rst.append(" \n ")
			else:
				if not(('--' in [x for x in i.strip().split(' ')]) or ('/******' in [x for x in i.strip().split(' ')]) or ('QUOTED_IDENTIFIER' in [x for x in i.strip().split(' ')]) or ('ANSI_NULLS' in [x for x in i.strip().split(' ')]) or ('GO' in [x for x in i.strip().split(' ')])):
					aux = i.split('--')					
					if not(len(aux) >1):
						cont = cont +1
						if ((cont%newVScript == 0) & (cont>5)):
							rst.append('   " ' + i.strip() + ' " ')
							rst.append('   vScript = vScript & _ ')
						else: 
							rst.append('   " ' + i.strip() + ' " & _') 
							cont = cont+1	
					if (cont%1500 == 0): rst.append("BREAK FUNCTION")

						
print(cont)
with open('proceduresVB6.txt', 'a') as f:
    for item in rst:
        f.write("%s\n" % item)

with open('nombresProcedures.txt', 'a') as f:
    for item in contProcedures:
        f.write("%s\n" % item)