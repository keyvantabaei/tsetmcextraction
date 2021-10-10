import pymysql
from pymysql import Error
class DB:
    def __init__(self,host,user,passw,db):
        try:
            self.password=passw
            self.username=user
            self.hostname=host
            self.id_for_insert=0
            self.dbname=db
            self.columns=['ID','bou_tval_B','lbuy_tval_bou_B','lsell_tval_bou_B','i_buy_tval_bou_B','i_sell_tval_bou_B','n_buy_tval_bou_B','n_sell_tval_bou_B','i_findow_bou_M','n_findow_bou_M','bou_tno_M','bou_tvol_B','i_buy_count_bou_K','i_sell_count_bou_K','n_buy_count_bou_K','n_sell_count_bou_K','namad_positive_bou_count','fbou_tval_B','lbuy_tval_fbou_B','lsell_tval_fbou_B','i_buy_tval_fbou_B','i_sell_tval_fbou_B','n_buy_tval_fbou_B','n_sell_tval_fbou_B','i_findow_fbou_M','n_findow_fbou_M','fbou_tno_M','fbou_tvol_B','i_buy_count_fbou_K','i_sell_count_fbou_K','n_buy_count_fbou_K','n_sell_count_fbou_K','namad_positive_fbou_count','date']
            self.mydb = pymysql.connect(host=self.hostname, user=self.username, passwd=self.password, database=self.dbname)
            self.cursor = self.mydb.cursor()
            print(f'has been connected to database {self.dbname}')
        except Error as error:print(error)
        finally:
            pass


    #################################### TABLES ###########################
    def showtables(self):
        try:
            self.cursor.execute(f'SHOW TABLES IN {self.dbname}')
            result = self.cursor.fetchall()
            for i in range(len(result)):
                print(result[i])
            print(f'''{self.dbname}'s tables has been shown ... ''')
            return True,result
        except Error as error:
            print(error)
            return False
        finally:
            pass
    def gettables(self):
        try:
            self.cursor.execute(f'SHOW TABLES IN {self.dbname}')
            result = self.cursor.fetchall()
            return result
        except Error as error:
            print(error)
            return False
        finally:
            pass
    def deletetable(self,tablelist):
        try:
            for tablename in tablelist:
              self.cursor.execute(f'DROP Table {tablename}')
              print(f'table {tablename} from {self.dbname} has been deleted ...')
            return True
        except Error as error:
            print(error,'Or recieved tables may has not sent as list')
            return False
        finally:
            pass
    def addtable(self,tablecolumndic):
        try:
            for table in tablecolumndic:
                columnstring=''
                str=' VARCHAR(100),'
                for i in range(len(tablecolumndic[table])):
                    if(i==0):columnstring+='('+tablecolumndic[table][i]+str
                    elif(i==len(tablecolumndic[table])-1):columnstring+=tablecolumndic[table][i]+' VARCHAR(100)'+')'
                    else:columnstring+=tablecolumndic[table][i]+str
                str=f"CREATE TABLE {table} {columnstring}"
                self.cursor.execute(str)
                print(f'table {table} has been created with columns: {tablecolumndic[table]}')
            return True
        except Error as error:
            return False
        finally:
            pass
    #################################### TABLES ###########################


    #################################### COLUMNS ###########################
    def showcolumns(self,tablelist):
        try:
            for table in tablelist:
                if(self.istablesexist(table)):
                  self.cursor.execute(f"SHOW columns FROM {table} IN {self.dbname}")
                  columns = self.cursor.fetchall()
                  print('table: ',table,'  columns:  ',columns)
                else:print(f'table {table} dose not exist in database {self.dbname}')
            return True
        except Error as error:
            print(error,'Or recieved tables may has not sent as list')
            return False
    def getcolumns(self,tablelist):
        try:
            resultdic={}
            tables=self.gettables()
            for table in tablelist:
                tableid=(table,)
                if tableid in tables:
                  self.cursor.execute(f"SHOW columns FROM {table} IN {self.dbname}")
                  columns = self.cursor.fetchall()
                  resultdic[table]=columns
                else:pass
            return resultdic
        except Error as error:
            pass
            return False
    def deletecolumn(self,tablecolumnsdic):
        try:
            for table in tablecolumnsdic:
              if(self.istablesexist(table)):
                  for column in tablecolumnsdic[table]:
                      if (self.iscolumnexist({table:column})):
                          self.cursor.execute(f"ALTER TABLE {table} DROP {column}")
                          print(f'column {column} has been dropped from table {table}')
                      else:print(f'there is no column {column} in table {table}')
              else:print(f'there is no table {table} in database {self.dbname}')
            return True
        except Error as error:
            print(error)
            return False
        finally:
            pass
    def addcolumn(self,tablecolumnsdic):
        try:
            for table in tablecolumnsdic:
                if(self.istablesexist(table)):
                    columns = tablecolumnsdic[table]
                    if(self.iscolumnexist({table:columns})):
                        columnsname=''
                        if(len(columns)!=1):
                            for i in range(len(columns)):
                                if (i == 0):
                                    columnsname = '(' + columns[i] + ' VARCHAR(100),'
                                elif (i == len(columns)-1):
                                    columnsname += columns[i] + ' VARCHAR(100)' + ')'
                                else:
                                    columnsname += columns[i] + ' VARCHAR(100),'
                        else:columnsname='('+columns[0]+' VARCHAR(100))'
                        if(columnsname!=''):
                            self.cursor.execute(f"ALTER TABLE {table} ADD {columnsname}")
                            print(f'columns {columns} has been added into table {table}.')
                    else: print(f'you had have at least one of these columns: {columns} since befor in table {table}.')
                else:print(f'there is no table {table} in database {self.dbname}')
            return True
        except Error as error:
            print(error)
    #################################### COLUMNS ###########################

    #################################### DATA ###########################
    def insertdata(self,data):
        import datetime
        date =  str(datetime.datetime.now().year) + '/' + str(datetime.datetime.now().month) + '/' + str(
            datetime.datetime.now().day)
        try:
            for tb in data:
                self.find_id(tb)
                columnslist = []
                valueslist = []
                tablename=tb
                columnvaluedic=data[tb]
                columns=[]
                for columnkey in columnvaluedic:
                    columns.append(columnkey)
                if (self.istablesexist(tablename)):
                    if (self.iscolumnexist({tablename: columns})==False):
                        if( self.isitrepeated({tablename: {'date': date}})==False): #today date
                            columnnames = ''
                            values = ''
                            i = 1
                            for column in columnvaluedic:
                                if (i == 1):
                                    i += 1
                                    columnslist.append(column)
                                    valueslist.append("'" + columnvaluedic[column] + "'")
                                else:
                                    columnslist.append(',' + column)
                                    valueslist.append(",'" + columnvaluedic[column] + "'")
                            columnnames = '(' + ''.join(columnslist) +',ID'+ ')'
                            values = '(' + ''.join(valueslist) + ','+str(self.id_for_insert)+')'
                            query = f'INSERT INTO {tablename} {columnnames} VALUES {values}'
                            self.cursor.execute(
                                query)  # columns_example='(column1,column2)' #values_example='(values1,values2)'
                            self.mydb.commit()
                            print(f'data {values} has been inserted into columns: {columnnames} tablename: {tablename}')
                        else:
                            for column in columnvaluedic:
                                    columnslist.append(column)
                                    valueslist.append( columnvaluedic[column])
                            strbegin = f"UPDATE {tablename} SET "
                            strmiddle = ''
                            for i in range(len(columnslist)):
                                if (i != len(columns) - 1):
                                    strmiddle += columnslist[i] + "='" + valueslist[i] + "',"
                                else:
                                    strmiddle += columnslist[i] + "='" + valueslist[i] + "'"
                            strend = f" WHERE date = '{date}'" #today
                            query=strbegin+strmiddle+strend
                            self.cursor.execute(query)  # columns_example='(column1,column2)' #values_example='(values1,values2)'
                            self.mydb.commit()
                            print(f'data {valueslist} blong to columns {columnslist} has been updated at table {tablename}')
                    else:
                        print(f'there is no column {columns} in table {tablename}')
                else:
                    print(f'there is no table {tablename} in database {self.dbname}')
        except Error as error:
            print(error)
    def getdata(self,columntables):
        datadic = {}
        for table in columntables:
            if (self.istablesexist(table)):
                columnlist = columntables[table]
                columnlistcout = len(columnlist)
                if (self.iscolumnexist({table: columnlist})==False):
                    if (columnlistcout > 0):
                        for column in columnlist:
                            self.cursor.execute(f"SELECT {column} FROM {table}")
                            rows = self.cursor.fetchall()
                            datalist=()
                            for row in rows:
                                datalist += row
                                datadic[column]=datalist
                    else:
                        self.cursor.execute(f"SELECT * FROM {table}")
                        rows = self.cursor.fetchall()
                        for row in rows: datadic[table] = row
                        print(f'all data column in table {table} has been shown .')
                else:
                    print(f'there are/is no column(s) : {columnlist}  in table {table}')
            else:
                print(f'there is no table {table} in database {self.dbname}')
                print(datadic)
        return datadic
    #################################### DATA ###########################

    def deletedatabase(self):
        try:
            self.cursor.execute(f'DROP DATABASE {self.dbname}')
            print(f'database {self.dbname} has been deleted ...')
            return True
        except Error as error:
            print(error)
            return False
        finally:
            pass
    def istablesexist(self,tablename):
        tables=self.gettables()
        table=(tablename,)
        if table in tables:
            return  True
        else:
            print(tablename, ' is not exisst so it has created ...')
            self.addtable({table: self.columns})
            return True
    def iscolumnexist(self,tablecolumndic):     # recieved : dict(tablenme:columnnamelist}
        for table in tablecolumndic:
            columnsdic = self.getcolumns([table,])
            columnlist = tablecolumndic[table]
            for column in columnlist:
                c=(column, 'varchar(100)', 'YES', '', None, '')
                if c in columnsdic[table]:
                    return  False
                else:pass
        return True
    def isitrepeated(self,tablecolumnvaluedic):
        for table in tablecolumnvaluedic:
            for column in tablecolumnvaluedic[table]:
                data = self.getdata({table:[column,]})
                if(data!={}):
                    for date in data:
                        if tablecolumnvaluedic[table][column] in data[column]:
                            return True
                        else:
                            return False
                else:
                    return  False
    def deletedata(self,tablename,date):
        try:
            self.cursor.execute(f"DELETE FROM {tablename} WHERE date IS NULL")
            self.mydb.commit()
            print(f'Data ROW from table : {tablename} has been deleted ...')
            return True
        except Error as error:
            print(error)
            return False
        finally:
            pass

    def find_id(self,tb_target):
        columns=self.getcolumns([tb_target])
        columnlist=[]
        if(self.istablesexist(tb_target)==True):
            for column_tuple in columns[tb_target]:
                columnlist.append(column_tuple[0])
            table_column_dic = {tb_target: columnlist}
            id_list = []
            data = self.getdata(table_column_dic)
            try:
                id_list = list(data['ID'])
            except:
                pass
            max = 0
            from decimal import Decimal
            if (len(id_list) > 0):
                for id in id_list:
                    if (max < Decimal(id)):
                        max = Decimal(id)
                self.id_for_insert = max + 1
            else:
                self.id_for_insert = 0


