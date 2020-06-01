#!/usr/bin/python3

########################################################
#  Programa desenvolvido para realizar consultas\      #
#  automatizadas no Google para determinadas\          #
#  palavras-chave e bases arbitárias                   #
#                                                      #
#  Desenvolvido por: Moroni Vieira                     #
#  Update 3.0 - 26 Mai 2020                            #
#                                                      #
#  Este script foi desenvolvido para localizar códigos #
#  fonte relacionados a uma lista de autores, essa     #
#  lista foi preparada anteriormente utilizando a      #
#  busca por artigos e retirando os nomes completos dos#
#  autores.                                            #
#                                                      #
#  Biblioteca utilizada disponível em                  #
#  https://github.com/abenassi/Google-Search-API       #
#                                                      #
########################################################

from google import google
import time
import random

###Variavel que define a quantidade de páginas por resultado
num_page=1

###Lista com as bases de busca, pode inserir ou retirar mais fontes
lista1 = ['source code','github','gitlab','sourceforge']

###Funcao de Busca
def BuscaGoogle():

    for i in lista1:
        arqresult=open('arq/v3/'+str(i),'w')
        file = open('lista_autores6','r') 

        for p1 in lista1:
            LerLinhas = file.readlines()
            CountTmp=0
            
            for p2 in LerLinhas:

                p2 = p2.rstrip("\n")
                search_results = google.search("\"" + p1 + "\"" + " and " + "\"" + p2 + "\"",num_page)
                print(p1 + " " + p2 ) 
                for result in search_results:
                    print(result.description,";",result.link)
                    arqresult.write(str(result.description) + ';' + str(result.link) + '\n')

                arqresult.write('#######################################'+p1+', '+p2+'\n')
                
                ####Temporizador para evitar o problema 429 - Too Many Requests 
                ####Foram realizados testes em escale de 10 minutos, a solução foi encontrada
                ####quando a metrica do tempo ficou em 20 minutos
                if (CountTmp < 10):
                    time.sleep(random.randrange(1,60))
                    CountTmp += 1 
                else:
                    time.sleep( 1200 )
                    CountTmp = 0
                        
        arqresult.close()
#
########################
### Módulo principal
#
def main():
    BuscaGoogle()
#
if __name__ == '__main__':
    main()
#
