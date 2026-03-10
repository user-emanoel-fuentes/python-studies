# Importação dos pacotes necessários:
import pyautogui as pa
import time

# Variáveis de ambiente:
link_drive = 'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga'
export_folder = (2028,282)
download_file = (3656,292)
path_file = r'/home/emanoel-fuentes/Downloads/Vendas - Dez.xlsx'

# Controle de fluxo:
pa.PAUSE = 1.5

# Carrega o link do drive dentro do navegador:
time.sleep(5)
pa.press('win')
time.sleep(3)
pa.write('chrome')
pa.press('enter')
time.sleep(2)
pa.hotkey('ctrl', 'shift', 'n') # Abre jánela anônima
pa.write(link_drive)
pa.press('enter')
time.sleep(5)

# Navega até o arquivo a ser baixado e baixa:
pa.click(export_folder,clicks=2) # Clica na pasta de exportação
time.sleep(2)
pa.click(download_file)
time.sleep(10)
pa.press('enter')
time.sleep(5)
pa.hotkey('ctrl', 'w') # Fecha a janela do navegador

# Análise do arquivo baixado:
import pandas

spreadsheet = pandas.read_excel(path_file)
# print(spreadsheet)
faturamento = spreadsheet["Valor Final"].sum()
qtd_produto = spreadsheet["Quantidade"].sum()
# tabela = spreadsheet[["Quantidade", "Valor Unitário", "Valor Final"]]
print(faturamento, qtd_produto)

pa.press('win')
time.sleep(3)
pa.write('chrome')
time.sleep(1)
pa.press('enter')
time.sleep(2)
pa.hotkey('ctrl', 't')
time.sleep(1)
pa.write('https://mail.google.com/')
pa.press('enter')
time.sleep(8)
pa.click(x=2014, y=192)
time.sleep(2)
pa.click(x=3280, y=522)
pa.write('worknoel.cardoso@gmail.com')
pa.press('enter')
time.sleep(2)
pa.press('tab')
time.sleep(1)
pa.write('Relatório de vendas')
pa.press('tab')
time.sleep(1)
pa.write('Segue o relatório de vendas do dia. \n')
pa.write(f"Faturamento: R${faturamento:,.1f}\nQuantidade de produtos vendidos: {qtd_produto}")
pa.click(x=3212, y=1049)
print("Email enviado com sucesso!")
