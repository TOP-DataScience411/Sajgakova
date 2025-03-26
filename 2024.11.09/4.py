err_book = {}

while True:
    line = input().strip()
    if not line: 
        break
        
    key, name = line.split()
    err_book[name] = key  

search_name = input().strip()

if search_name in err_book:
    print(err_book[search_name])  
else:
    print("! value error !")
    
    
#C:\Git\Sajgakova\2024.11.09>python 4.py
#1004 ER_CANT_CREATE_FILE
#    1005 ER_CANT_CREATE_TABLE
#    1006 ER_CANT_CREATE_DB
#    1007 ER_DB_CREATE_EXISTS
#    1008 ER_DB_DROP_EXISTS
#    1010 ER_DB_DROP_RMDIR
#    1016 ER_CANT_OPEN_FILE
#    1022 ER_DUP_KEY

#ER_CANT_CREATE_DB
#1006



#C:\Git\Sajgakova\2024.11.09>python 4.py
#4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
#    4108 ER_GIPK_COLUMN_EXISTS
#    4111 ER_DROP_PK_COLUMN_TO_DROP_GIPK
#    4113 ER_DA_EXPIRE_LOGS_DAYS_IGNORED
#    4114 ER_CTE_RECURSIVE_NOT_UNION

#ER_CANT_OPEN_FILE
#! value error !