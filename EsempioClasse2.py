class Animale():
    def __init__(self,nome, n_zampe, famiglia, n_occhi, vola):
        self.nome=nome
        self.__n_zampe=n_zampe
        self.__famiglia=famiglia
        self.__n_occhi=n_occhi
        self.__vola=vola
    
    #get
    def getZampe(self):
        return self.__n_zampe
    def getFam(self):
        return self.__famiglia    
    def getEyes(self):
        return self.__n_occhi
    def getFly(self):
        return self.__vola
    
    def __str__(self):
        return self.nome+':'+'\n\t zampe: '+str(self.__n_zampe)+'\n\t famiglia: '+self.__famiglia+'\n\t occhi: '+str(self.__n_occhi) +'\n\t vola: '+str(self.__vola)
    


