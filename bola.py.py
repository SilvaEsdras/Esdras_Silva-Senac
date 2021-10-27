#1.Classe Bola:Crie uma classe que modele uma bola:
#a.Atributos: Cor, circunferência, material
#b.Métodos: trocaCor e mostraCor

class bola():
  def __init__(self, cor, circunferencia, material):
    #atributos
    self.cor = cor
    self.circunferencia = circunferencia
    self.material = material
    #Atributos
    #Métodos
  def trocaCor(self, cor):
    self.cor = cor

  def mostraCor(self):
    return self.cor
    #Métodos
    
cor = input('Qual a cor que voçe deseja?\n')
circunferencia = float(input('Qual a circunferencia?\n'))
material = float(input('Qual o material?\n'))


object = bola("azul", 10, "couro")
print(object.mostraCor())
object.trocaCor("vermelha")
print(object.mostraCor())
