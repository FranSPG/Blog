

a = """alter PROCEDURE [dbo].[F44CPINSPMAYORIGUAL60000KMNORS]
	AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT 'F44CPINSPMAYORIGUAL60000KMNORS' as cuenta,0 as valor
END"""

a = a.split('\n')

rst = []

procedure = a[0][a[0].find('.'):]
procedure = procedure.replace('.', '').replace('[','').replace(']','').strip()

print(procedure)
print(a[0])
newVScript = 10
cont = 0
rst.append("If Existe_Stored_Procerude((\""+ procedure +"\"), dbsConnect) Then ' Si existe lo modifico")
rst.append('vScript = "ALTER PROCEDURE ' + procedure + '"')
rst.append("Else ' Si no existe lo creo")
rst.append('vScript = "CREATE PROCEDURE ' + procedure + '"')
rst.append("End If 'Existe_Stored_Procerude((\""+ procedure +"\"), dbsConnect)")
rst.append(" \n ")
rst.append('vScript = vScript & _ ')

for idx, i in enumerate(a[1:]):
	if (i.strip()):
		if (i == a[-1]):
			rst.append('" ' + i.strip() + ' " ')
		else:	
			if ((cont%newVScript == 0) & (cont>5)):
				rst.append('" ' + i.strip() + ' " ')
				rst.append('vScript = vScript & _ ')
				
			else: rst.append('" ' + i.strip() + ' " & _')
		cont = cont +1

rst.append(" \n ")
rst.append("If Not Operacion_Exitosa((vScript), dbsConnect) Then")
rst.append("Stored_Procedures = False")
rst.append("End If   ' (Not Operacion_Exitosa)")
rst.append(" \n ")

with open('test2.txt', 'a') as f:
    for item in rst:	
        f.write("%s\n" % item)
		
		
#DEBERIA HACER PARA QUE SE SUMEN AL TXT Y NO SE PISE
