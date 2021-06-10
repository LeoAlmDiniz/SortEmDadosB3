import pandas as pd
url = 'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=IBOV&idioma=pt-br'
data=pd.read_html(url, decimal=',', thousands='.', index_col= 'Código')[0][:-1] #puxar sem o [0] e sem o [:-1] antes, explicar que começa vindo como lista, dps transformamos em df

sorted_data = data.sort_values('Part. (%)', ascending=False) #fazer sem declarar novo objeto antes, mostrar que o método é conservativo, não altera o objeto mas sim um clone
print(sorted_data)

pass_data_to_excel = input("Create new xlsx file with data? y/n \n")

if pass_data_to_excel.upper() == 'Y':
    sorted_data.to_excel('case1_output.xlsx') #Fazer pra csv e pra excel. Explicar a diferença entre os dois.
    print('Excel file created.')
else:
    print('Finished program without saving excel file.')

