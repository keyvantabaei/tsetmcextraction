import datetime
class CAL:
    def __init__(self):
        print('CALCULATOR OBJ has made ...')
        self.namad_id_dic = self.read_namad_ids()
        self.FILE_NAME=''

    def to_number(self,data):
        from decimal import Decimal
        for key in data:
            valueslist = list(data[key])
            index = 0
            for value in valueslist:
                if (key != 'date'):
                    try:valueslist[index] = Decimal(value)
                    except:pass
                    index += 1
                else:
                    pass
            data[key] = tuple(valueslist)
        return data
    def sum_tuples(self,t1, t2):
        l1 = list(t1)
        l2 = list(t2)
        resultlist = []
        for i in range(len(l1)):
            try:
                resultlist.append(l1[i] + l2[i])
            except:resultlist.append('NONE')
        return tuple(resultlist)
    def subtraction_tuples(self,t1, t2):
        l1 = list(t1)
        l2 = list(t2)
        resultlist = []
        for i in range(len(l1)):
            try:resultlist.append(l1[i] - l2[i])
            except:resultlist.append('NONE')
        return tuple(resultlist)
    def TSE_CAL(self,data):
        print('TSE-CAL is ready for Calculation ...')
        dataNumber = self.to_number(data)
        # *******************************************************
        dataNumber['ارزش کل بازار'] = self.sum_tuples(dataNumber['bou_tval_B'], dataNumber['fbou_tval_B'])
        # *******************************************************
        # ارزش صف های بازار
        sum_lbuy = self.sum_tuples(dataNumber['lbuy_tval_bou_B'], dataNumber['lbuy_tval_fbou_B'])
        sum_lsell = self.sum_tuples(dataNumber['lsell_tval_bou_B'], dataNumber['lsell_tval_fbou_B'])
        dataNumber['ارزش صف خرید بازار'] = sum_lbuy
        dataNumber['ارزش صف فروش بازار'] = sum_lsell
        # *******************************************************
        # خرید کل حقیقی بازار
        sum_buy_I = self.sum_tuples(dataNumber['i_buy_tval_bou_B'], dataNumber['i_buy_tval_fbou_B'])
        # فروش کل حقیقی بازار
        sum_sell_I = self.sum_tuples(dataNumber['i_sell_tval_bou_B'], dataNumber['i_sell_tval_fbou_B'])
        # خرید کل حقوقی بازار
        sum_buy_N = self.sum_tuples(dataNumber['n_buy_tval_bou_B'], dataNumber['n_buy_tval_fbou_B'])
        # فروش کل حقوقی بازار
        sum_sell_N = self.sum_tuples(dataNumber['n_sell_tval_bou_B'], dataNumber['n_sell_tval_fbou_B'])
        dataNumber['خرید کل حقیقی'] = sum_buy_I
        dataNumber['فروش کل حقیقی'] = sum_sell_I
        dataNumber['خرید کل حقوقی'] = sum_buy_N
        dataNumber['فروش کل حقوقی'] = sum_sell_N
        dataNumber['ورود/خروج نقدینگی'] = self.subtraction_tuples(sum_buy_I, sum_sell_I)
        # *******************************************************
        # برایند اختلاف سرانه ها بازار
        sum_findow_i = self.sum_tuples(dataNumber['i_findow_bou_M'], dataNumber['i_findow_fbou_M'])
        sum_findow_n = self.sum_tuples(dataNumber['n_findow_bou_M'], dataNumber['n_findow_fbou_M'])
        dataNumber['برایند اختلاف سرانه حقیقی'] = sum_findow_i
        dataNumber['برایند اختلاف سرانه حقوقی'] = sum_findow_n
        # *******************************************************
        return dataNumber


    def sum(self,data, columns):
        print('new sumation operation for data :',data,' and columns :',columns)
        from decimal import Decimal
        date = str(datetime.datetime.now().year) + '/' + str(datetime.datetime.now().month) + '/' + str(
            datetime.datetime.now().day)
        resultlist = {}
        bou_pos_count=[]
        fbou_pos_count=[]
        for columnname in columns:
            sum = 0
            for namad in data:
                if (columnname == 'namad_positive_fbou_count'):
                    if (Decimal(data[namad][columnname]) >= 0):
                        fbou_pos_count.append(namad)
                        resultlist[columnname] = str(len(fbou_pos_count))
                    else:
                        pass
                elif (columnname == 'namad_positive_bou_count'):
                    if (Decimal(data[namad][columnname]) >= 0):
                        bou_pos_count.append(namad)
                        resultlist[columnname] = str(len(bou_pos_count))
                    else:
                        pass
                elif (columnname == 'i_findow_fbou_M'):
                    if (data[namad][columnname + '_part1'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part1'])
                    if (data[namad][columnname + '_part2'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part2'])
                    resultlist[columnname] = str(round(sum / 10000000, 1))
                elif (columnname == 'n_findow_fbou_M'):
                    if (data[namad][columnname + '_part1'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part1'])
                    if (data[namad][columnname + '_part2'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part2'])
                    resultlist[columnname] = str(round(sum / 10000000, 1))
                elif (columnname == 'i_findow_bou_M'):
                    if (data[namad][columnname + '_part1'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part1'])
                    if (data[namad][columnname + '_part2'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part2'])
                    resultlist[columnname] = str(round(sum / 10000000, 1))
                elif (columnname == 'n_findow_bou_M'):
                    if (data[namad][columnname + '_part1'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part1'])
                    if (data[namad][columnname + '_part2'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part2'])
                    resultlist[columnname] = str(round(sum / 10000000, 1))
                else:
                    if (data[namad][columnname].isdigit()):
                        sum = sum + Decimal(data[namad][columnname])
                    if (columnname == 'bou_tno_M'):
                        resultlist[columnname] = str(round(sum / 1000000, 1))
                    elif (columnname == 'fbou_tno_M'):
                        resultlist[columnname] = str(round(sum / 1000000, 1))
                    elif (columnname == 'fbou_tvol_B'):
                        resultlist[columnname] = str(round(sum / 1000000000, 1))
                    elif (columnname == 'bou_tvol_B'):
                        resultlist[columnname] = str(round(sum / 1000000000, 1))
                    elif (columnname == 'n_sell_count_bou_K'):
                        resultlist[columnname] = str(round(sum / 1000, 1))
                    elif (columnname == 'n_buy_count_bou_K'):
                        resultlist[columnname] = str(round(sum / 1000, 1))
                    elif (columnname == 'i_sell_count_bou_K'):
                        resultlist[columnname] = str(round(sum / 1000, 1))
                    elif (columnname == 'i_buy_count_bou_K'):
                        resultlist[columnname] = str(round(sum / 1000, 1))
                    elif (columnname == 'i_sell_count_fbou_K'):
                        resultlist[columnname] = str(round(sum / 1000, 1))
                    elif (columnname == 'i_buy_count_fbou_K'):
                        resultlist[columnname] = str(round(sum / 1000, 1))
                    elif (columnname == 'n_sell_count_fbou_K'):
                        resultlist[columnname] = str(round(sum / 1000, 1))
                    elif (columnname == 'n_buy_count_fbou_K'):
                        resultlist[columnname] = str(round(sum / 1000, 1))
                    else:
                        resultlist[columnname] = str(round(sum / 10000000000, 1))
        resultlist['date'] = date
        return resultlist

    def sum_for_namad(self, data, columns):
        print('new sumation operation for data :', data, ' and columns :', columns)
        from decimal import Decimal
        date = str(datetime.datetime.now().year) + '/' + str(datetime.datetime.now().month) + '/' + str(
            datetime.datetime.now().day)
        resultlist = {}
        for columnname in columns:
            sum = 0
            for namad in data:
                sum=0
                if (columnname == 'n_saraneh_M'):
                    if (data[namad][columnname + '_part1'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part1'])
                    if (data[namad][columnname + '_part2'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part2'])
                    resultlist[namad] = {columnname: str(round(sum / 10000000, 1))}
                elif (columnname == 'i_saraneh_M'):
                    if (data[namad][columnname + '_part1'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part1'])
                    if (data[namad][columnname + '_part2'] == 'NaN'):
                        pass
                    else:
                        # if(namad=='tb_11773403764702778'):
                        #     print(Decimal(data[namad][columnname + '_part2']),'   ',Decimal(data[namad][columnname + '_part1']),'   ',Decimal(data[namad][columnname + '_part1'])+Decimal(data[namad][columnname + '_part2']))
                        #     input('rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
                        sum = sum + Decimal(data[namad][columnname + '_part2'])
                    resultlist[namad] = {columnname: str(round(sum / 10000000, 1))}
                else:pass
                # result_list.append([namad,round(sum/10000000,1)])
                sum=0
        # for columnname in columns:
        #     sum = 0
        #     for namad in data:
        #         if (columnname == 'n_saraneh_M'):
        #             if (data[namad][columnname + '_part1'] == 'NaN'):
        #                 pass
        #             else:
        #                 sum = sum + Decimal(data[namad][columnname + '_part1'])
        #             if (data[namad][columnname + '_part2'] == 'NaN'):
        #                 pass
        #             else:
        #                 sum = sum + Decimal(data[namad][columnname + '_part2'])
        #             resultlist[namad] ={columnname:str(round(sum / 1117734037647027780000000, 1))}
        #         elif (columnname == 'i_saraneh_M'):
        #             if (data[namad][columnname + '_part1'] == 'NaN'):
        #                 pass
        #             else:
        #                 sum = sum + Decimal(data[namad][columnname + '_part1'])
        #             if (data[namad][columnname + '_part2'] == 'NaN'):
        #                 pass
        #             else:
        #                 sum = sum + Decimal(data[namad][columnname + '_part2'])
        #             resultlist[namad] ={columnname:str(round(sum / 10000000, 1))}
        #         else:pass
        return resultlist

    def insert_data_into_namad_tables(self,data):
        #dadeh haro bebin : rahat mitoni zakhireh koni
        import DB
        db=DB.DB('127.0.0.1','root', '', 'tsetmc_db')
        for namad in data:
            table_name=namad
            values=data[namad]
            db.insertdata({table_name:values})

    def sum_and_sort_for_subtrac_ave(self,data, columns,file_name):
        print('new sumation operation for data :',data,' and columns :',columns)
        columns_persian_index=-1
        self.FILE_NAME=file_name
        print('file name :',self.FILE_NAME,'.xlsx is ready for building ...')
        from decimal import Decimal
        date = str(datetime.datetime.now().year) + '/' + str(datetime.datetime.now().month) + '/' + str(
            datetime.datetime.now().day)
        result_list=[]
        for columnname in columns:
            sum = 0
            for namad in data:
                if (columnname == 'i_subtrac_ave_bou_M'):
                    if (data[namad][columnname + '_part1'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part1'])
                    if (data[namad][columnname + '_part2'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part2'])
                elif (columnname == 'n_subtrac_ave_bou_M'):
                    if (data[namad][columnname + '_part1'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part1'])
                    if (data[namad][columnname + '_part2'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part2'])
                elif (columnname == 'i_subtrac_ave_fbou_M'):
                    if (data[namad][columnname + '_part1'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part1'])
                    if (data[namad][columnname + '_part2'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part2'])
                elif (columnname == 'n_subtrac_ave_fbou_M'):
                    if (data[namad][columnname + '_part1'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part1'])
                    if (data[namad][columnname + '_part2'] == 'NaN'):
                        pass
                    else:
                        sum = sum + Decimal(data[namad][columnname + '_part2'])
                else:pass
                result_list.append([namad,round(sum/10000000,1)])
                sum=0
        self.buble_sort(result_list)
    def buble_sort(self,data):
        ite=len(data)-1
        while(ite>1):
            for i in range(0,ite,1):
                if(data[i][1]<data[i+1][1]):
                    data[i],data[i+1]=data[i+1],data[i]
            ite-=1
        #id into list
        namads=self.replace_namad_id(self.get_namadid(data))
        values=self.get_namadval(data)
        import EXEL
        exel_motor=EXEL.EXEL()
        exel_motor.save_sorted_data({'نماد':namads,self.FILE_NAME:values},self.FILE_NAME)
    def replace_namad_id(self,idlist):
        mani_idlist=[]
        i=0
        for id in idlist:
            for namaid in self.namad_id_dic:
                if(id=='tb_'+self.namad_id_dic[namaid].replace(" ","")):
                    mani_idlist.append(namaid)
            i+=1
        return mani_idlist
    def get_namadid(self,data):
        idlist=[]
        for idvallist in data:
            idlist.append(idvallist[0])
        return idlist
    def get_namadval(self,data):
        idlist=[]
        for idvallist in data:
            idlist.append(idvallist[1])
        return idlist
    def read_namad_ids(self):
        # import EXT
        # ext_motor= EXT.EXTRACTION('http://www.tsetmc.com/Loader.aspx?ParTree=15131F','',[])
        # ext_motor.saveidstoxml()
        result_dic={}
        import xml.etree.ElementTree as ET
        tree = ET.parse('namd_name_ids.xml')
        root = tree.getroot()
        for child in root:
            result_dic[child.attrib.get('name')] = child.attrib.get('id')
        print('name and ids has been saved : ',result_dic)
        return result_dic
