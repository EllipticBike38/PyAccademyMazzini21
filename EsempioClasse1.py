class Student():
    '''qui si definisce il docstring della classe in questo modo'''
    cod_CS='LM-32' 
    # questa è una variabile di classe, comune a tutti gli oggetti di una determinatata classe

    # funzione generatrice dell'oggetto -> COSTRUTTORE
    def __init__(self, nome,cf, mat):
        '''qui si definisce il docstring di un metodo in questo modo'''
        self.nome=nome
        self.cf=cf 
        self.mat=mat 
        self.__hidden=0 #questa variabile che inizia con __ non è accessibile dall'esterno
        #args: self, punta a se stesso, si può chiamare in ogni modo, si usa self per prassi; args[1:]: informazioni necessari per l'istanza del singolo oggetto  
    
    def __str__(self):
        """utilizzato da funzioni come print()"""
        return(self.nome+': '+str(self.mat))
        
    @property
    def getName(self):
        return self.nome
    
