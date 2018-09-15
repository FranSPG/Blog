text = open("vistasSnapon.sql", "r")
a = text.read().split('\n')

rst = []
rst2 = []
newVScript = 10
cont = 0
contViews = []
contErrores = 0
nombErrores = []
contFunction = 0
query = []
view = ''
flag = False



for idx, i in enumerate(a):
	i = i.strip()
	if('create' in [x.lower() for x in i.strip().split(' ')]):
		flag = True
		view = i[i.find('.'):]
		view = view[:view.find(']')]
		view = view.replace('.', '').replace('[','')
		print(view)
		rst.append('If Not Existe_Vista("'+view+'", dbsConnect) Then')
		rst.append('   vScript = " " & _ ')
		continue
	if(('go' in [x.lower() for x in i.strip().split(' ')]) and (flag == True)):
		rst.append("\n")
		rst.append("   If NOT Crear_Vista((\""+ view +"\"), vScript, dbsConnect) Then ")
		rst.append("      Vistas = False")
		rst.append('   End If   \' (Not Crear_Vista("'+view+'")')
		rst.append("End If 'Not Existe_Vista("+view+", dbsConnect)")
		rst.append("\n\n")
		
		flag = False
	
	if flag:
		if (i.strip()):
			if not(('as' in [x.lower() for x in i.strip().split(' ')]) and (len(i.split(' ')) == 1)):
				rst.append('   " '+i+' " & _')

		
with open('viewVB6.txt', 'a') as f:
    for item in rst:
        f.write("%s\n" % item)

