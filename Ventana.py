class Ventana:
    def __init__(self, titulo='', xsup=0, ysup=0, xdown=500, ydown=500):
        self.__titulo= titulo
        if xsup < xdown and ysup < ydown:
            if xsup>=0:
                self.__xsupizq= xsup
            if ysup>=0:
                self.__ysupizq= ysup
            if xdown<=500:
                self.__xdownder= xdown
            if ydown<=500:
                self.__ydownder= ydown
        else:
            print("Valores ingresados incorrectamente")

    def getTitulo(self):
        return self.__titulo

    def alto (self):
        return self.__ydownder-self.__ysupizq

    def ancho(self):
        return self.__xdownder-self.__xsupizq

    def mostrar(self):
        print ("Coordenadas de ventana: x={} y={}, x={} y={}".format(self.__xsupizq,self.__ysupizq,self.__xdownder,self.__ydownder))

    def moverIzquierda (self,desp=1):
        if self.__xdownder-desp<=500 and self.__xsupizq-desp>=0:
            self.__xdownder-=desp
            self.__xsupizq-=desp
        else:
            print ("El desplazamiento no es posible")

    def bajar (self,desp=1):
        if self.__ydownder+desp<=500 and self.__ysupizq+desp>=0:
            self.__ydownder+=desp
            self.__ysupizq+=desp
        else:
            print ("El desplazamiento no es posible")

    def subir (self,desp=1):
        if self.__ydownder-desp<=500 and self.__ysupizq-desp>=0:
            self.__ydownder-=desp
            self.__ysupizq-=desp
        else:
            print ("El desplazamiento no es posible")