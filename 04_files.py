
file = open('/home/marins/Área de Trabalho/PUC Minas - Pós Graduação/Unidade 1 - Introdução a programação/02_Data_Structures_and_Loops/04_files.txt', 'r') 

for line in file:
    list = line.split()
    print(list)

file.close()


listOfMaterials = ['pen', 'book', 'pencil', 'journal']

fileMaterials = open('/home/marins/Área de Trabalho/PUC Minas - Pós Graduação/Unidade 1 - Introdução a programação/02_Data_Structures_and_Loops/materials.txt', 'w')

for item in listOfMaterials:
    fileMaterials.write(item + '\n')

fileMaterials.close()