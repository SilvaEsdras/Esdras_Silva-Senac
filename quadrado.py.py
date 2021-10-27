#2.Classe Quadrado:Crie uma classe que modele um quadrado:
#a.Atributos: Tamanho do lado
#b.Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado():
  def __init__(self, tamanho_do_lado):
    #atributos
    self.tamanho_do_lado = tamanho_do_lado
    
    #Atributos
    #Métodos
  def ladoone(self, lado):
    self.lado = lado

  def lado(self, lado):
    return self.lado

  def area(self):
    return self.tamanho_do_lado * self.tamanho_do_lado

    #Métodos

#tamanho_do_lado = 
object = Quadrado(10)
print(object.area())
