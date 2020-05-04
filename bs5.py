from bs4 import BeautifulSoup
import requests
import csv                                                                 #BIBLIOTECA PARA ESCRITA DE ARQUIVO CSV
import xlwt                                                                #BIBLIOTECA PARA ESCRITA DE PLANILHA EXCEL


#IDENTIFICAÇÃO DO SITE SENDO TRABALHADO
source = requests.get('https://sobrebarba.com.br/blogs/blog').text

#CRIAÇÃO DE PLANILHA EXCEL
planilha = xlwt.Workbook()
pagina = planilha.add_sheet('Dados')

i = 0                                                                      #CONTADOR QUE VAI SER UTILIZADO NO PREENCHIMENTO DA PLANILHA EXCEL

soup = BeautifulSoup(source,'lxml')
with open('blog_scrape3.csv', 'w') as arquivo_csv:
    escrita_csv = csv.writer(arquivo_csv)                                  #CRIAÇÃO DE OBJETO WRITER (TRANSFORMA DADOS RECEBIDOS EM STRINGS)
    escrita_csv.writerow(['Titulo', 'Sumario', 'Data Publicação'])         #INSERÇÃO DE INFORMAÇÕES STRING NO ARQUIVO CSV

    for div in soup.find_all('div', class_ = 'one-third column alpha article'):
        print("*****************************************************************")
        titulo = div.find('h2', class_ = 'article_title').a.text           #ATRIBUIÇÃO DO ATRIBUTO TITULO QUE VAI SER UTILIZADO PARA PRINTAGEM
        print("Titulo da publicação-> " + titulo)                          #E INSERÇÃO NA PLANILHA E ARQUIVO CSV
        pagina.write(i, 0, 'Titulo')
        pagina.write(i, 1, titulo)
        i += 1

        print() 
        sumario = div.find('div', class_ = 'excerpt').p.text               #ATRIBUIÇÃO DO ATRIBUTO SUMARIO QUE VAI SER UTILIZADO PARA PRINTAGEM
        print("Resumo da publicação-> " + sumario)                         #E INSERÇÃO NA PLANILHA E ARQUIVO CSV
        pagina.write(i, 0, 'Resumo')
        pagina.write(i, 1, sumario)
        i += 1

        datapub = div.find('p', class_ = 'blog_meta').text                 #ATRIBUIÇÃO DO ATRIBUTO DATAPUB QUE VAI SER UTILIZADO PARA PRINTAGEM
        print(datapub)                                                     #E INSERÇÃO NA PLANILHA E ARQUIVO CSV
        pagina.write(i, 0, 'Data de publicação')
        pagina.write(i, 1, datapub)
        i += 1
                                                                          
        escrita_csv.writerow([titulo, sumario, datapub])                   #METODO PARA INSERÇÃO DE DADOS NO ARQUIVO CSV
        i += 1

    for div in soup.find_all('div', class_ = 'one-third column  article'):
                                              

        print("*****************************************************************")
        titulo = div.find('h2', class_ = 'article_title').a.text
        print("Titulo da publicação-> " + titulo)
        pagina.write(i, 0, 'Titulo')
        pagina.write(i, 1, titulo)
        i += 1

        print() 
        sumario = div.find('div', class_ = 'excerpt').p.text
        print("Sumario da publicação-> " + sumario)
        pagina.write(i, 0, 'Resumo')
        pagina.write(i, 1, sumario)
        i += 1

        datapub = div.find('p', class_ = 'blog_meta').text
        print(datapub)
        pagina.write(i, 0, 'Data de publicação')
        pagina.write(i, 1, datapub)
        i += 1

        escrita_csv.writerow([titulo, sumario, datapub])
        i += 1

    for div in soup.find_all('div', class_ = 'one-third column omega article'):


        print("*****************************************************************")
        titulo = div.find('h2', class_ = 'article_title').a.text
        print("Titulo da publicação-> " + titulo)
        pagina.write(i, 0, 'Titulo')
        pagina.write(i, 1, titulo)
        i += 1

        print() 
        sumario = div.find('div', class_ = 'excerpt').p.text
        print("Sumario da publicação-> " + sumario)
        pagina.write(i, 0, 'Resumo')
        pagina.write(i, 1, sumario)
        i += 1

        datapub = div.find('p', class_ = 'blog_meta').text
        print(datapub)
        pagina.write(i, 0, 'Data de publicação')
        pagina.write(i, 1, datapub)
        i += 1

        escrita_csv.writerow([titulo, sumario, datapub])
        i += 1
                                                                                                                                                  
planilha.save('Dados.xls')                                                #DADOS SALVOS NA PLANILHA
print("*****************************************************************")