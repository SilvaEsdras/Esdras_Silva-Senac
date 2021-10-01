print('Tempo do Download\n')

tamanho_do_arquivo = float(input('Qual o tamanho do Download em Mega? '))
v_do_link = float(input('Qual é a velocidade em Mbps? '))
velocidade_do_download = tamanho_do_arquivo / ( v_do_link / 60)


print('Seu Download termina em: ', velocidade_do_download)