import math

class Figura ():
    def __init__(self):
        pass

    def perimetro(self):
        return 'La figura no tiene perímetro'

    def area(self):
        return 'La figura no tiene área'

class Cuadrado(Figura):
    def __init__ (self, lado):
        self.lado = lado
    def dame_perimetro(self):
        return 4 * self.lado
    def dame_area(self):
        return self.lado**2

class Rectangulo(Figura):
    def __init__ (self, base,altura):
        self.base = base
        self.altura = altura
    def dame_perimetro(self):
        return 2 * self.base + 2 * self.altura
    def dame_perimetro(self):
        return base * altura

class Circulo(Figura):
    def __init__(self,radio):
        self.radio = radio
    def dame_perimetro(self):
        return 2 * math.pi * self.radio
    def dame_area(self):
        return math.pi * self.radio

class Elipse(Figura):
    def __init__(self, semieje_mayor , semieje_menor):
        self.semieje_mayor = semieje_mayor
        self.semieje_menor = semieje_menor
    def dame_perimetro(self):
        return ((self.semieje_mayor**2 + self.semieje_menor**2)/2)**(1/2)*2*math.pi
    def dame_area(self):
        return math.pi * self.semieje_mayor * self.semieje_menor



cuadrado = Cuadrado(5)
print (cuadrado.dame_perimetro(),cuadrado.dame_area())
circulo = Circulo (float(input ('Radio del círculo: ')))
print (circulo.dame_perimetro(),circulo.dame_area())
elipse = Elipse (float(input ('Semieje mayor:  ')), float(input('Semieje menor: ')))
print (elipse.dame_perimetro(),elipse.dame_area())
