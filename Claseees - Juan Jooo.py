from ssl import HAS_TLSv1_1


class Helado:
    def __init__(self, sabor, agua, cono, color, ricura):
        self.sabor = sabor
        self.agua = agua
        self.cono = cono
        self.color = color
        self.ricura = ricura
    
h1 =Helado("Fresa","Si es de agua","Si tiene cono, no vaso","Rosado","Si está bien pinche rico")

print(h1.ricura)

from ssl import HAS_TLSv1_1


class Banco:
    def __init__(self, Dinero, Seguridad, Personas, Trabajo, Bovedas):
        self.Dinero = Dinero
        self.Seguridad = Seguridad
        self.Personas = Personas
        self.Trabajo = Trabajo
        self.Bovedas = Bovedas
    
h1 = Banco ("Tiene mucho dinero","50 guardias","Hay 160 personas","70 trabajadores","Tiene 4 bovedas de oro")

print(h1.Seguridad)



from ssl import HAS_TLSv1_1


class basquetbolista:
    def __init__(self,vision,salto,fuerza,punteria,Habilidad):
        self.vision = vision
        self.salto = salto
        self.fuerza= fuerza
        self.punteria = punteria 
        self.Habilidad = Habilidad

b1 = basquetbolista ("Tiene buena vision","Salta bastante","si tiene fuerza","Canastea todas","Es un jugador bastante Habilidoso")


print(b1.Habilidad)