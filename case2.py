import pandas as pd
filename = "IBOVDia_10-06-21.csv"
data=pd.read_csv(filename, delimiter=";", decimal=',', encoding='latin1', skiprows=1, index_col='Código')[:-2]

sorted_data = data.sort_values('Part. (%)', ascending=False) #fazer sem declarar novo objeto antes, mostrar que o método é conservativo, não altera o objeto mas sim um clone
print(sorted_data)

pass_data_to_excel = input("Create new csv file with data? y/n \n")

if pass_data_to_excel.upper() == 'Y':
    sorted_data.to_csv('case2_output.csv', encoding='latin1', decimal=',', sep=';') #Explicar sem encoding, sem decimal, sem sep principalmente. Mostrar como sep faz quebrar.
    print('Excel file saved.')
else:
    print('Finished program without saving excel file.')