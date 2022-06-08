
from barcode import EAN13
from barcode.writer import Imagewriter

codigos_produtos = {'Feijão': '551746511111', 'Arroz': '665887111111', 'Macarrao': '667588711111', 'Azeite':' 998562111111'}

for produto in codigos_produtos:
    #print(produto)
    #print(codigos_produtos{produto})
    codigo = (codigos_produtos[produto])
    codigo_barra = EAN13(codigo, writer = Imagewriter())
    codigo_barra.save
    (f"codigo_barra_{produto}")