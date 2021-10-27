#3.Classe Retangulo:Crie uma classe que modele um retangulo:
#a.Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)#b.Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#c.Crie um programaque utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo():
  def __init__(self, comprimento, largura):
    #atributos
    self.comprimento = comprimento
    self.largura = largura

    #Atributos
    #Métodos
  def comprimento(self, comprimento):
    self.comprimento = comprimento

  def largura(self, largura):
    self.largura = largura

  def comprimentoone(self):
    return self.comprimento

  def larguraone(self):
    return self.largura


  def area(self):
    return self.comprimento * self.largura

  def perimetro(self):
      return (2 * self.comprimento) + (2 * self.largura)

    #Métodos

comprimento = float(input('Informe o valor do comprimento: '))
largura = float(input('Informe o valor da largura: '))
object = Retangulo(comprimento,largura)
print("A area é: ", object.area())
print("O perimetro é: ", object.perimetro())


#M² = base x altura (duas dimensões do piso). Veja um exemplo para calcular a metragem: 1 – Piso com medida de 45 x 45 cm, ou 0,45m x 0,45 m (o segredo é sempre utilizar a mesma unidade de medida, tudo em centímetros ou tudo em metro).