import qrcode
links_produtos = {"produto1": "123456", "produto2": "123456", "produto3": "123456", "produto4": "123456"}

for produto in links_produtos:
    #print(produto)
    #print(links_produtos[produto])
    link = links_produtos[produto]
    image_qrcode = qrcode.make(link)
    image_qrcode.save(f"qrcode_(produto).jpg")