from bs4 import BeautifulSoup
import requests
import csv
import xlwt
# arquivo_csv = open('blog_scrape.csv', 'w')


source = requests.get('https://sobrebarba.com.br/blogs/blog').text

planilha = xlwt.Workbook()
pagina = planilha.add_sheet('Dados')
# pagina.write(0, 0, 'Titulo')
# pagina.write(1, 0, 'Resumo')
# pagina.write(2, 0, 'Data de publicação')
# planilha.save('Dados.xls')


i = 0

soup = BeautifulSoup(source,'lxml')
with open('blog_scrape3.csv', 'w') as arquivo_csv:
    escrita_csv = csv.writer(arquivo_csv)
    escrita_csv.writerow(['Titulo', 'Sumario', 'Data Publicação'])
    
    for div in soup.find_all('div', class_ = 'one-third column alpha article'):
        print("*****************************************************************")
        titulo = div.find('h2', class_ = 'article_title').a.text
        print("Titulo da publicação-> " + titulo)
        pagina.write(i, 0, 'Titulo')
        pagina.write(i, 1, titulo)
        i += 1

        print() 
        sumario = div.find('div', class_ = 'excerpt').p.text
        print("Resumo da publicação-> " + sumario)
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

planilha.save('Dados.xls')
print("*****************************************************************")