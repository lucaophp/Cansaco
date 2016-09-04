#!/usr/bin/python
# -*- coding: utf-8 -*-
#
"""
  Nome: extrai_atributos.py
  Autor: Hemerson Pistori (pistori@ucdb.br)

  Descricão: Extrai vários atributos de um banco de imagens organizado com uma subpasta para cada classe do banco e gerar um arquivo arff que pode ser utilizado com o weka

  Modo de Usar:


  Coloque seu banco de imagens na pasta 'data' que fica dentro de python-extrai-atributos (veja a organização do banco de exemplo)

  Execute o programa:

  $ python extraiAtributos nome_do_banco_de_imagens ou
  $ python extraiAtributos nome_do_banco_de_imagen pasta_onde_esta_localizado_o_banco
"""

import sys
from arff import Arff
from bancoImagens import BancoImagens
from extratores import Extratores


nomeBancoImagens = 'sojaDrone3C'
nomePastaRaiz = '../data/'

# Testa se o nome foi passado na linha de comando, se não foi, irá abrir o banco de examplos (sojaDrone3C)
if len(sys.argv) > 1:
    nomeBancoImagens = sys.argv[1]
    if len(sys.argv) > 2:
        nomePastaRaiz = sys.argv[2]



print 'Gerando ARFF para o Banco de Imagens ' + nomeBancoImagens + "..."

bancoImagens = BancoImagens(nomeBancoImagens,nomePastaRaiz)
extratores = Extratores()



print 'Localização do Banco ' + bancoImagens.pastaBancoImagens

classes = bancoImagens.classes



print 'Classes Encontradas'
print classes


# Aqui começa a extração de atributos de todas as imagens de cada classe

dados = []
nomesAtributos = []
tiposAtributos = []
valoresAtributos = []

for classe in classes:

    imagens = bancoImagens.imagens_da_classe(classe)

    print "Processando %s imagens da classe %s " % (len(imagens),classe)

    for imagem in imagens:

        nomesAtributos, tiposAtributos, valoresAtributos = extratores.extrai_todos(imagem)

        dados.append(valoresAtributos+[classe])


if len(classes) > 0:

    Arff().cria(bancoImagens.nomeArquivoArff, dados, nomeBancoImagens, nomesAtributos, tiposAtributos, classes)


print 'Arquivo ARFF gerado em ' + bancoImagens.nomeArquivoArff