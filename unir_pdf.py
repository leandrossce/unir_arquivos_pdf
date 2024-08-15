import os
from PyPDF2 import PdfMerger

def unir_pdfs(diretorios, arquivo_saida):
    merger = PdfMerger()
    
    # Percorre todos os diretórios e arquivos recursivamente
    for diretorio in diretorios:
        for pasta_atual, _, arquivos in os.walk(diretorio):
            for arquivo in arquivos:
                # Verifica se o arquivo é um PDF
                if arquivo.lower().endswith('.pdf'):
                    caminho_pdf = os.path.join(pasta_atual, arquivo)
                    merger.append(caminho_pdf)
                    print(f'Adicionando: {caminho_pdf}')
    
    # Escreve o PDF unido no arquivo de saída
    merger.write(arquivo_saida)
    merger.close()
    print(f'PDFs unidos em: {arquivo_saida}')

if __name__ == "__main__":
    # Solicita ao usuário o diretório contendo os PDFs
    diretorio = input("Digite o caminho do diretório contendo os PDFs: ")
    
    # Solicita ao usuário o caminho e nome do arquivo de saída
    arquivo_saida = input("Digite o caminho e nome do arquivo de saída (ex: C:\\Users\\leandro\\Downloads\\consolidado.pdf): ")

    # Chama a função com o diretório e o arquivo de saída fornecidos pelo usuário
    unir_pdfs([diretorio], arquivo_saida)
