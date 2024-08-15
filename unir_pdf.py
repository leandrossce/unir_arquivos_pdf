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
    # Loop para garantir que o diretório e o nome do arquivo de saída sejam válidos
    while True:
        # Solicita ao usuário o diretório contendo os PDFs
        diretorio = input("Digite o caminho do diretório contendo os PDFs: ")
        
        if not os.path.isdir(diretorio):
            print("Diretório inválido. Por favor, tente novamente.")
            continue
        
        # Solicita ao usuário o caminho e nome do arquivo de saída
        arquivo_saida = input("Digite o caminho e nome do arquivo de saída (ex: C:\\Users\\leandro\\Downloads\\consolidado.pdf): ")
        
        # Verifica se o arquivo de saída termina com '.pdf'
        if not arquivo_saida.lower().endswith('.pdf'):
            print("O nome do arquivo de saída deve terminar com '.pdf'. Por favor, tente novamente.")
            continue
        
        # Verifica se o diretório do arquivo de saída existe
        diretorio_saida = os.path.dirname(arquivo_saida)
        
        if not os.path.exists(diretorio_saida):
            criar_diretorio = input(f"O diretório '{diretorio_saida}' não existe. Deseja criá-lo? (s/n): ").lower()
            if criar_diretorio == 's':
                os.makedirs(diretorio_saida)
                print(f"Diretório '{diretorio_saida}' criado com sucesso.")
            else:
                print("Por favor, forneça um caminho de saída válido.")
                continue
        
        # Se todos os inputs forem válidos, sai do loop
        break

    # Chama a função com o diretório e o arquivo de saída fornecidos pelo usuário
    unir_pdfs([diretorio], arquivo_saida)
