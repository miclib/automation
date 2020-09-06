class PgConn: 

        #class attributes 
        sqlcode = 0                             #SQL code from database operation 
        returnCode = 0                          #Return code from database action           

        def __init__(self, dbname , user , password):
            self.dbname = dbname
            self.user = user 
            self.password = password

        def setDbName (self, dbname):
            self.dbname = dbname

        def setUser (self, user):
            self.user = user  


