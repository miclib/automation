from pgconn import PgConn


#instantiation 
pgconn = PgConn("car_portal","postgres","postgres")
#
#sample to print class attributes 
#print ("connecting to database: {} ".format(pgconn.__class__.sqlcode))
#print ("connecting to database: {} ".format(pgconn.__class__.returnCode))
#
print ("Creating connection to database: {}".format(pgconn.dbname))
print ("using user name: {}".format(pgconn.user))
print ("with password: {} ".format(pgconn.password))




