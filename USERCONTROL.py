class USER:
    def __init__(self,OPTIONS):
        self.dictionary={
            'bou_tval_B':'ارزش  بورس',
            'bou_tno_M': 'تعداد معاملات بورس',
            'bou_tvol_B':'حجم معاملات بورس',
            'n_findow_bou_M':'برایند اختلاف سرانه حقوقی بورس',
            'i_buy_count_bou_K':'تعداد خریدار حقیقی بورس',
            'n_buy_count_bou_K':'تعداد خریدار حقوقی بورس',
            'n_sell_count_bou_K':'تعداد فروشنده حقوقی بورس',
            'i_buy_tval_bou_B':'ارزش خرید حقیقی بورس',
            'i_findow_bou_M':'برایند اختلاف سرانه حقیقی بورس',
            'i_sell_count_bou_K':'تعداد فروشنده حقیقی بورس',
            'i_sell_tval_bou_B':'ارزش فروش حقیقی بورس',
            'n_sell_tval_bou_B':'ارزش فروش حقوقی بورس',
            'lbuy_tval_bou_B':'ارزش صف خرید بورس',
            'lsell_tval_bou_B':'ارزش صف فروش بورس',
            'namad_positive_bou_count':'تعداد سهام پایانی مثبت بورس',
            'fbou_tval_B':'ارزش فرابورس',
            'fbou_tno_M': 'تعداد معاملات فرابورس',
            'fbou_tvol_B': 'حجم معاملات فرابورس',
            'n_findow_fbou_M': 'برایند اختلاف سرانه حقوقی فرابورس',
            'i_buy_count_fbou_K': 'تعداد خریدار حقیقی فرابورس',
            'n_buy_count_fbou_K': 'تعداد خریدار حقوقی فرابورس',
            'n_sell_count_fbou_K': 'تعداد فروشنده حقوقی فرابورس',
            'i_buy_tval_fbou_B': 'ارزش خرید حقیقی فرابورس',
            'i_findow_fbou_M': 'برایند اختلاف سرانه حقیقی فرابورس',
            'i_sell_count_fbou_K': 'تعداد فروشنده حقیقی فرابورس',
            'i_sell_tval_fbou_B': 'ارزش فروش حقیقی فرابورس',
            'n_sell_tval_fbou_B': 'ارزش فروش حقوقی فرابورس',
            'lbuy_tval_fbou_B': 'ارزش صف خرید فرابورس',
            'lsell_tval_fbou_B': 'ارزش صف فروش فرابورس',
            'namad_positive_fbou_count': 'تعداد سهام پایانی مثبت فرابورس',
            'n_buy_tval_fbou_B':'ارزش خرید حقوقی فرابورس',
            'n_buy_tval_bou_B':'ارزش خرید حقوقی بورس',
            'i_subtrac_ave_bou_M':'ورود-خروج نقدینگی حقیقی بورس(میلیون تومان)',
            'n_subtrac_ave_bou_M': 'ورود-خروج نقدینگی حقوقی بورس(میلیون تومان)',
            'i_subtrac_ave_fbou_M': 'ورود-خروج نقدینگی حقیقی فرابورس(میلیون تومان)',
            'n_subtrac_ave_fbou_M': 'ورود-خروج نقدینگی حقوقی فرابورس(میلیون تومان)',


        }
        self.columns_header_for_exel_persian_and_file_name=[]
        self.options_dic=self.translate_options(OPTIONS)
        print(self.options_dic , 'options has been saved .')
        #syntax_dic
        self.syntax_repo={
            'bou_tval_B':['(tval)',],
            'bou_tno_M': ['(tno)',],
            'bou_tvol_B':['(tvol)',],
            'n_findow_bou_M':['((ct).Buy_N_Volume/(ct).Buy_CountN)*(pc)','-((ct).Sell_N_Volume/(ct).Sell_CountN)*(pc)',],
            'i_buy_count_bou_K':['(ct).Buy_CountI',],
            'n_buy_count_bou_K':['(ct).Buy_CountN',],
            'n_sell_count_bou_K':['(ct).Sell_CountN',],
            'i_buy_tval_bou_B':['((ct).Buy_I_Volume)*(pc)',],
            'i_findow_bou_M':['((ct).Buy_I_Volume/(ct).Buy_CountI)*(pc)','-((ct).Sell_I_Volume/(ct).Sell_CountI)*(pc)',],
            'i_sell_count_bou_K':[' (ct).Sell_CountI',],
            'i_sell_tval_bou_B':['((ct).Sell_I_Volume)*(pc)',],
            'n_sell_tval_bou_B':['((ct).Sell_N_Volume)*(pc)',],
            'lbuy_tval_bou_B':['(qd1)*(pd1)',],
            'lsell_tval_bou_B':['(po1)*(qo1)',],
            'namad_positive_bou_count':['(pcp)',],
            'fbou_tval_B': ['(tval)', ],
            'fbou_tno_M': ['(tno)', ],
            'fbou_tvol_B': ['(tvol)', ],
            'n_findow_fbou_M': ['((ct).Buy_N_Volume/(ct).Buy_CountN)*(pc)',
                               '-((ct).Sell_N_Volume/(ct).Sell_CountN)*(pc)', ],
            'i_buy_count_fbou_K': ['(ct).Buy_CountI', ],
            'n_buy_count_fbou_K': ['(ct).Buy_CountN', ],
            'n_sell_count_fbou_K': ['(ct).Sell_CountN', ],
            'i_buy_tval_fbou_B': ['((ct).Buy_I_Volume)*(pc)', ],
            'i_findow_fbou_M': ['((ct).Buy_I_Volume/(ct).Buy_CountI)*(pc)',
                               '-((ct).Sell_I_Volume/(ct).Sell_CountI)*(pc)', ],
            'i_sell_count_fbou_K': [' (ct).Sell_CountI', ],
            'i_sell_tval_fbou_B': ['((ct).Sell_I_Volume)*(pc)', ],
            'n_sell_tval_fbou_B': ['((ct).Sell_N_Volume)*(pc)', ],
            'lbuy_tval_fbou_B': ['(qd1)*(pd1)', ],
            'lsell_tval_fbou_B': ['(po1)*(qo1)', ],
            'namad_positive_fbou_count': ['(pcp)', ],
            'n_buy_tval_fbou_B':['((ct).Buy_N_Volume)*(pc)',],
            'n_buy_tval_bou_B': ['((ct).Buy_N_Volume)*(pc)', ],
            'i_subtrac_ave_bou_M':['((ct).Buy_I_Volume/(ct).Buy_CountI)*(pc)',
                               '-((ct).Sell_I_Volume/(ct).Sell_CountI)*(pc)', ],
            'n_subtrac_ave_bou_M':['((ct).Buy_N_Volume/(ct).Buy_CountN)*(pc)',
                               '-((ct).Sell_N_Volume/(ct).Sell_CountN)*(pc)', ],
            'i_subtrac_ave_fbou_M': ['((ct).Buy_I_Volume/(ct).Buy_CountI)*(pc)',
                                    '-((ct).Sell_I_Volume/(ct).Sell_CountI)*(pc)', ],
            'n_subtrac_ave_fbou_M': ['((ct).Buy_N_Volume/(ct).Buy_CountN)*(pc)',
                                    '-((ct).Sell_N_Volume/(ct).Sell_CountN)*(pc)', ],

        }
        self.query_box={}
        self.true_options_list=[]
        self.sepereted_bou_options_dic={}
        self.sepereted_fbou_options_dic={}
        self.bou_options_dic={}
        self.fbou_options_dic={}
        self.indicators_dic=self.make_indicator_path_and_column_dic({
            r'\macdhisto-rsi-pc': ['macd_minus_signal', 'rsi14', 'pc'],
            r'\isaraneh':['i_saraneh_M',],r'\nsaraneh':['n_saraneh_M',],

                                                                     r'\momentum14-bolingerbands':['momentum14','bollinger_bands'],
                                                                     })
        self.indicator_query_dic={}
        self.namad_data_list=[]

    def make_indicator_path_and_column_dic(self,data):
        import os
        script_path = os.getcwd()
        result_dic={}
        for name in data:
            print('indicator :',name, ' has added for extracting into namad tables ...')
            result_dic[script_path+r'\indicators' + name + '.txt'] = data[name]
        return result_dic
    def sum_tuples(self,t1, t2):
        l1 = list(t1)
        l2 = list(t2)
        resultlist = []
        for i in range(len(l1)):
            try:
                resultlist.append(l1[i] + l2[i])
            except:resultlist.append('NONE')
        return tuple(resultlist)
    def check_true_options(self):
        count=0
        for option_subject in self.options_dic:
            if(self.options_dic[option_subject]=='ON'):
                self.true_options_list.append(option_subject)
                print(option_subject,' has been choosed for extraction . . .')
                count+=1
            else:pass
        print('total :' ,count)
    def filter_syntax_repo(self,target):
        syntax=''
        for syntax in self.syntax_repo:
            if(target==syntax):
                return self.syntax_repo[syntax]
            else:
                pass
    def middle_syntax_maker(self,target):
        syntax=[]
        # if(self.filter_syntax_repo(target)==False):
        #     print(target, ' dose not exist in syntax repo .')
        #     return False
        # else:
        syntax = self.filter_syntax_repo(target)
        return syntax
    def sync_middle_and_target(self):
        began_filter_query='true==function(){'
        end_filter_query="if(1==1){return true;}else{return false;}}()"
        #(18)[(18).length-1]!='2')
        middel_syntax=''
        self.check_true_options()
        for target in self.true_options_list:
            middel_syntax = self.middle_syntax_maker(target)
            if middel_syntax is not None:
                print('Syntax : ', '"', middel_syntax, '"', ' has been added for ',target,' ...')
                self.add_to_query_box(target, middel_syntax)
        self.seperate_bou_fbou_options()
    def add_to_query_box(self,target,query):
        self.query_box[target] = query
        print(query, 'query and ', target, ' target hase been added to query_box ...')
    def seperate_bou_fbou_options(self):
        for target in self.query_box:
            if(('fbou' in target)==True):
                self.sepereted_fbou_options_dic[target]=self.query_box[target]
            else:
                self.sepereted_bou_options_dic[target]=self.query_box[target]
        self.combine_bou_fbou_options()
    def combine_bou_fbou_options(self):
        fbou_count=0
        fbou_target_list=[]
        fbou_middelquery_list=[]
        bou_count=0
        bou_target_list=[]
        bou_middelquery_list=[]
        iterate=0
        bou_sepereted_list=self.adjust_targets(self.sepereted_bou_options_dic)
        for target in bou_sepereted_list:
            iterate += 1
            if(target[0]=='None'):
                bou_count += 2
            else:
                bou_target_list.append(target[0])
                bou_middelquery_list.append(self.query_box[target[0]])
                bou_count += 1
            if(bou_count>=3 or iterate== len(bou_sepereted_list)):
                self.bou_options_dic[tuple(bou_target_list)] =self.make_query(bou_middelquery_list)
                bou_count = 0
                bou_middelquery_list.clear()
                bou_target_list.clear()
        iterate=0
        fbou_sepereted_list=self.adjust_targets(self.sepereted_fbou_options_dic)
        for target in fbou_sepereted_list:
            iterate += 1
            if(target[0]=='None'):
                fbou_count += 2
            else:
                fbou_target_list.append(target[0])
                fbou_middelquery_list.append(self.query_box[target[0]])
                fbou_count += 1
            if(fbou_count>=3 or iterate== len(fbou_sepereted_list)):
                self.fbou_options_dic[tuple(fbou_target_list)] =self.make_query(fbou_middelquery_list)
                fbou_count = 0
                fbou_middelquery_list.clear()
                fbou_target_list.clear()
    def make_query(self,query_list):
        began_query='true==function(){'
        end_query='if(1==1){return true;}else{return false;}}()'
        middle_query=''
        i=0
        for str_syn in query_list:
            if(len(str_syn)==1):
                str0 = '(cfield' + str(i) + ')='
                middle_query = middle_query + str0 + str_syn[0] + ';'
                i+=1
            else:
                for str_value in str_syn:
                    str0 = '(cfield' + str(i) + ')='
                    middle_query = middle_query + str0 + str_value + ';'
                    i += 1
        return  began_query+middle_query+end_query
    def adjust_targets(self,targetdic):
        index=0
        index_list=[]
        adjusting_list = [[k, v] for k, v in targetdic.items()]
        manipulating_list=adjusting_list
        for target in adjusting_list:
            if (target[0] == 'n_findow_fbou_M' or target[0] == 'i_findow_fbou_M' or target[0] == 'n_findow_bou_M' or target[0] == 'i_findow_bou_M' or target[0] == 'i_subtrac_ave_bou_M' or target[0] == 'n_subtrac_ave_bou_M' or target[0] == 'i_subtrac_ave_fbou_M' or target[0] == 'n_subtrac_ave_fbou_M'or target[0] == 'i_subtrac_ave_M' or target[0] == 'n_subtrac_ave_M'):
                index += 1
                index_list.append(index)
            else:
                index+=1
        c=0
        for i in index_list:
            i=i+c*2
            manipulating_list.insert(i - 1, ['None', 'None'])
            manipulating_list.insert(i + 1, ['None', 'None'])
            c+=1
        print(targetdic, ' has been adjusted as : ', manipulating_list)
        return manipulating_list
    def check_findow_for_ext(self,list_key):
        check_key = False
        if 'n_findow_fbou_M' in list_key:
            check_key = True
            findow_index = list_key.index('n_findow_fbou_M')
        elif 'i_findow_fbou_M' in list_key:
            check_key = True
            findow_index = list_key.index('i_findow_fbou_M')
        elif 'i_findow_bou_M' in list_key:
            check_key = True
            findow_index = list_key.index('i_findow_bou_M')
        elif 'n_findow_bou_M' in list_key:
            check_key = True
            findow_index = list_key.index('n_findow_bou_M')
        elif 'n_subtrac_ave_fbou_M' in list_key:
            check_key = True
            findow_index = list_key.index('n_subtrac_ave_fbou_M')
        elif 'i_subtrac_ave_fbou_M' in list_key:
            check_key = True
            findow_index = list_key.index('i_subtrac_ave_fbou_M')
        elif 'n_subtrac_ave_bou_M' in list_key:
            check_key = True
            findow_index = list_key.index('n_subtrac_ave_bou_M')
        elif 'i_subtrac_ave_bou_M' in list_key:
            check_key = True
            findow_index = list_key.index('i_subtrac_ave_bou_M')
        elif 'n_saraneh_M' in list_key:
            check_key = True
            findow_index = list_key.index('n_saraneh_M')
        elif 'i_saraneh_M' in list_key:
            check_key = True
            findow_index = list_key.index('i_saraneh_M')
        else:
            check_key = False
        if (check_key == True):
            name = list_key[findow_index]
            list_key.pop(findow_index)
            list_key.insert(findow_index, name + '_part2')
            list_key.insert(findow_index, name + '_part1')
        else:
            pass
        return list_key
    def print_query_target(self):
        count=0
        for key in self.bou_options_dic:
            print(key,' : ',self.bou_options_dic[key])
            count+=1
        for key in self.fbou_options_dic:
            print(key,' : ',self.fbou_options_dic[key])
            count+=1
        print('totat constructed string-query-filter is : ',count)
    def Convert_list_to_dic(self,list_target):
        dic={}
        for li in list_target:
            dic[li[0]]=li[1]
        return dic
    def translate_options(self,options):
        option_list=[[k, v] for k, v in options.items()]
        dictionary_list=[[k, v] for k, v in self.dictionary.items()]
        for key_per in option_list:
            for key_en in dictionary_list:
                if(key_en[1]==key_per[0]):
                    self.columns_header_for_exel_persian_and_file_name.append(key_per[0])
                    key_per[0] = key_en[0]
                else:pass
        return self.Convert_list_to_dic(option_list)
    def save_to_exel(self):
        import EXEL
        exel_handle=EXEL.EXEL()
        exel_handle.save_all_data_to_exel()
    def read_filter_query_from_file(self):
        str_query=''
        for indicator_file in self.indicators_dic:
            str_query=''
            indicator=open(indicator_file,"r")
            for line in indicator:
                str_query+=line
            self.indicator_query_dic.update({str_query: self.indicators_dic[indicator_file]})
    def add_to_data_list(self,data):
        exist_namad_list=[]
        for namad in self.namad_data_list:
            try:exist_namad_list.append(namad[0])
            except:pass
        print(data)
        for namad in data:
            values = [(k, v) for k, v in data[namad].items()]
            if namad in exist_namad_list:
                for i in range(0,len(self.namad_data_list),1):
                    if (namad == self.namad_data_list[i][0]):
                        self.namad_data_list[i][1]+= values
                        print('data :',values,'  for namad : ',namad,'has added to data list ...')
            else:
                self.namad_data_list.append([namad, values])
    def convert_list_to_dic(self,lst):
        tb_list_data=[]
        namad_data_tuple=()
        namad_data_list=[]
        data_dic={}
        for namad_data in lst:
            namad_data_tuple=tuple(namad_data[1])
            for data in namad_data[1]:
                tb_list_data.append(data)
            namad_data_list.append((namad_data[0],tuple(tb_list_data)))
            tb_list_data.clear()
        namad_data_tuple=tuple(namad_data_list)
        namad_data_tuple=tuple(namad_data_tuple)
        for mem in namad_data_tuple:
            data_dic.update(dict({mem[0]:dict((x, y) for x, y in mem[1])}))
        print('namad_data are ready :   ',data_dic)
        return data_dic


    def extrac(self):
        self.sync_middle_and_target()
        self.print_query_target()
        # self.read_filter_query_from_file()
        import EXT
        import CALCULATOR
        import DB
        db=DB.DB('127.0.0.1', 'root', '', 'tsetmc_db')
        caculator=CALCULATOR.CAL()
        ext_motor= EXT.EXTRACTION('http://www.tsetmc.com/Loader.aspx?ParTree=15131F','',[])
        print('Connected to TSETMC ...')
        ext_motor.dosettingforextraction_namad()
        print('General settings are done ...')
        # #****************************** NAMADS **********************************
        #
        # for query in self.indicator_query_dic:
        #     columns=list(self.indicator_query_dic[query])
        #     ext_motor.newstringfilter(query,self.check_findow_for_ext(columns))
        #     data =ext_motor.extractalldata()
        #     columns=list(self.indicator_query_dic[query])+['date',]
        #     if 'n_saraneh_M' in columns:
        #         result = caculator.sum_for_namad(data, columns)
        #         data.update(result)
        #     elif 'i_saraneh_M' in columns:
        #         result = caculator.sum_for_namad(data, columns)
        #         data.update(result)
        #     self.add_to_data_list(data)
        # data=self.convert_list_to_dic(self.namad_data_list)
        # caculator.insert_data_into_namad_tables(data)
        # #************************************************************************
        #************** BOURSE *******************
        ext_motor.newsetting(0)
        print('BOURSE settings are done ...')
        for key in self.bou_options_dic:
            list_key=list(key)
            ext_motor.newstringfilter(str(self.bou_options_dic[key]),self.check_findow_for_ext(list_key))
            data=ext_motor.extractalldata()
            list_key=list(key)+['date',]
            data=caculator.sum(data,list_key)
            db.insertdata(dict(tsetmc=data))
        #************** FARA-BOURSE **************
        ext_motor.newsetting(1)
        print('FARA-BOURSE settings are done ...')
        for key in self.fbou_options_dic:
            list_key=list(key)
            ext_motor.newstringfilter(str(self.fbou_options_dic[key]),self.check_findow_for_ext(list_key))
            data=ext_motor.extractalldata()
            list_key=list(key)+['date',]
            data=caculator.sum(data,list_key)
            db.insertdata(dict(tsetmc=data))
        self.save_to_exel()
    def extract_namad_data(self):
        self.read_filter_query_from_file()
        import EXT
        import CALCULATOR
        caculator=CALCULATOR.CAL()
        ext_motor= EXT.EXTRACTION('http://www.tsetmc.com/Loader.aspx?ParTree=15131F','',[])
        print('Connected to TSETMC ...')
        ext_motor.dosettingforextraction_namad()
        print('General settings are done ...')
        #****************************** NAMADS **********************************

        for query in self.indicator_query_dic:
            columns=list(self.indicator_query_dic[query])
            ext_motor.newstringfilter(query,self.check_findow_for_ext(columns))
            data =ext_motor.extractalldata()
            columns=list(self.indicator_query_dic[query])+['date',]
            if 'n_saraneh_M' in columns:
                result = caculator.sum_for_namad(data, columns)
                data.update(result)
            elif 'i_saraneh_M' in columns:
                result = caculator.sum_for_namad(data, columns)
                data.update(result)
            self.add_to_data_list(data)
        data=self.convert_list_to_dic(self.namad_data_list)
        caculator.insert_data_into_namad_tables(data)
        #************************************************************************
    def Bear(self):
        data_i=0
        import EXT
        import timeit
        from decimal import Decimal
        ext_motor= EXT.EXTRACTION('http://www.tsetmc.com/Loader.aspx?ParTree=15131F','(cfield0)=(qo1)*(pmin)/10000000000;(cfield0)>20&&(po1)==(tmin) && (qo1)!=0',['lsell_tval'])
        print('Connected to TSETMC ...')
        ext_motor.dosettingforextraction()
        while(1==1):
            start = timeit.default_timer()
            data_f = ext_motor.extractalldata_Bear()
            if(data_i==0):
                data_i=data_f
                data_f = 0
            else:
                # for key in data_i:
                #     print(Decimal(0.25)*Decimal(data_i[key]['lsell_tval']))
                # input()
                shared_items = {k: data_f[k] for k in data_f if k in data_i and Decimal(data_f[k]['lsell_tval']) < Decimal(0.7)*Decimal(data_i[k]['lsell_tval'])}
                if(len(shared_items)>0):
                    import winsound
                    frequency = 1500  # Set Frequency To 2500 Hertz
                    duration = 1000  # Set Duration To 1000 ms == 1 second
                    winsound.Beep(frequency, duration)
                    print(shared_items)
                data_i = data_f
                data_f = 0
            stop = timeit.default_timer()
            print('Running Time: ', round((stop - start)), ' Sec')