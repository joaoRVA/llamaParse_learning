import os
import re
from io import StringIO

import pandas as pd


def analisa_tab(texto):
    # Padrão para identificar tabelas em Markdown

    regras_regex = re.compile(r"(\|(?:[^\n]*\|\n)+\|(?:[-: ]*\|)+(?:\n\|[^\n]*\|)*)", re.MULTILINE)
    tabelas = regras_regex.findall(texto)
    return tabelas

def transformar_markdown_excel(texto, num_pag):
    lista_tabelas = analisa_tab(texto)

    if len(lista_tabelas) > 0:
        #ler a tabela
        for i, texto_tabela in enumerate(lista_tabelas):
            tabela = pd.read_csv(StringIO(texto_tabela), sep="|", encoding="utf-8", engine="python")
            tabela = tabela.dropna(how="all", axis=0)
            tabela = tabela.dropna(how="all", axis=1)
        #salvar ela no excel
            tabela.to_excel(f"tabelas/Pagina{num_pag}Tabela{i+1}.xlsx", index=False)

lista_pdf = os.listdir("paginas_pdf")

for i, pagina in enumerate(lista_pdf):

    with open(f"paginas_pdf/{pagina}", "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()
    num_pag = i + 1
    transformar_markdown_excel(texto, num_pag)