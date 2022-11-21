class Config(): 
    def __init__(self):
        self.DBNAME = "vendas.db"
        self.SCREENCACHE = "scache.bin"
        
    def getDatabaseName(self):
        return self.DBNAME

    def getSreenCacheName(self):
        return self.SCREENCACHE