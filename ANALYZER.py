class ANALYZER:
    def __init__(self):
        self.fa_en_dic = {
            '1': ['آ', 'ا'],
            '2': 'ب',
            '3': 'ث',
            '4': 'د',
            '5': 'ی',
            '6': 'ف',
            '7': 'ل',
            '8': 'گ',
            '9': ['ح', 'ه'],
            'I': 'ی',
            'V': 'ج',
            'W': 'ک',
            'K': 'ل',
            'P': 'م',
            'O': 'ن',
            'Q': 'پ',
            'R': ['ق', 'غ'],
            'S': 'ر',
            'T': ['س', 'ص'],
            'U': ['ت', 'ط'],
            'G': 'و',
            'H': 'ک',
            'L': 'خ',
            'Z': ['ز', 'ض', 'ظ', 'ذ'],
        }
        import DB
        db = DB.DB('127.0.0.1', 'root', '123456', 'tsetmc_db')
        self.namad_ids_dic=self.read_namad_ids()
        self.db=db
        self.sanat_name=[
    'زراعت و خدمات وابسته',
    'جنگلداري و ماهيگيري',
    'استخراج زغال سنگ',
    'استخراج نفت گاز و خدمات جنبي جز اکتشاف',
'استخراج کانه هاي فلزي',
'استخراج ساير معادن',
'حذف شده- فرآورده‌هاي غذايي و آشاميدني',
'منسوجات',
'دباغي، پرداخت چرم و ساخت انواع پاپوش',
'محصولات چوبي',
'محصولات كاغذي',
'انتشار، چاپ و تکثير',
'فراورده هاي نفتي، كك و سوخت هسته اي',
'حذف شده-مواد و محصولات شيميايي',
'لاستيك و پلاستيك',
'توليد محصولات كامپيوتري الكترونيكي ونوري',
'فلزات اساسي',
'ساخت محصولات فلزي',
'ماشين آلات و تجهيزات',
'ماشين آلات و دستگاه‌هاي برقي',

'ساخت دستگاه‌ها و وسايل ارتباطي',
'ابزارپزشکي، اپتيکي و اندازه‌گيري',
'خودرو و ساخت قطعات',
'ساير تجهيزات حمل و نقل',
'مبلمان و مصنوعات ديگر',
'قند و شكر',
'شرکتهاي چند رشته اي صنعتي',
'عرضه برق، گاز، بخاروآب گرم',
'جمع آوري، تصفيه و توزيع آب',
'محصولات غذايي و آشاميدني به جز قند و شكر',
'مواد و محصولات دارويي',
'محصولات شيميايي',
'پيمانكاري صنعتي',
'تجارت عمده فروشي به جز وسايل نقليه موتور',
'خرده فروشي،باستثناي وسايل نقليه موتوري',
'كاشي و سراميك',
'تجارت عمده وخرده فروشي وسائط نقليه موتور',
'حمل و نقل هوايي',
'انبارداري و حمايت از فعاليتهاي حمل و نقل',
'سيمان، آهك و گچ',
'ساير محصولات كاني غيرفلزي',
'هتل و رستوران',
'سرمايه گذاريها',
'بانكها و موسسات اعتباري',
'ساير واسطه گريهاي مالي',
'اوراق حق تقدم استفاده از تسهيلات مسكن',
'حمل ونقل، انبارداري و ارتباطات',
'حمل و نقل آبي',
'فعاليت هاي پشتيباني و كمكي حمل و نقل',
'مخابرات',
'واسطه‌گري‌هاي مالي و پولي',
'بيمه وصندوق بازنشستگي به جزتامين اجتماعي',
'فعاليتهاي كمكي به نهادهاي مالي واسط',
'صندوق سرمايه گذاري قابل معامله',
'اوراق تامين مالي',
'انبوه سازي، املاك و مستغلات',
'فعاليت مهندسي، تجزيه، تحليل و آزمايش فني',
'رايانه و فعاليت‌هاي وابسته به آن',
'اطلاعات و ارتباطات',
'خدمات فني و مهندسي',
'اوراق بهادار مبتني بر دارايي فكري',
'فعالبت هاي اجاره و ليزينگ',
'فعاليت پشتيباني اجرائي اداري وحمايت كسب',
'فعاليت هاي هنري، سرگرمي و خلاقانه',
   'فعاليتهاي فرهنگي و ورزشي' ,
'گروه اوراق غيرفعال',

]
        self.target=[
            'rsi14',
            'macd_minus_signal',
            'momentum14',
            'bollinger_bands',
            'pc',
            'buy_sell_power_ratio',
            'i_money_fluence_B',
            'bou_tval_B',
            'lbuy_tval_bou_B',
            'lsell_tval_bou_B',
            'i_buy_tval_bou_B',
            'i_sell_tval_bou_B',
            'n_buy_tval_bou_B',
            'n_sell_tval_bou_B',
            'i_findow_bou_M',
            'n_findow_bou_M',
            'bou_tno_M',
            'bou_tvol_B',
            'i_buy_count_bou_K',
            'i_sell_count_bou_K',
            'n_buy_count_bou_K',
            'n_sell_count_bou_K',
            'namad_positive_bou_count',
            'fbou_tval_B',
            'lbuy_tval_fbou_B',
            'lsell_tval_fbou_B',
            'i_buy_tval_fbou_B',
            'i_sell_tval_fbou_B',
            'n_buy_tval_fbou_B',
            'n_sell_tval_fbou_B',
            'i_findow_fbou_M',
            'n_findow_fbou_M',
            'fbou_tno_M',
            'fbou_tvol_B',
            'i_buy_count_fbou_K',
            'i_sell_count_fbou_K',
            'n_buy_count_fbou_K',
            'n_sell_count_fbou_K',
            'namad_positive_fbou_count'

        ]
        self.data={}
    def getdata(self):
        result_dic={}
        tables = self.db.gettables()
        for table in tables:
            table_column_dic=self.db.getcolumns(table)
            column_list=[]
            for column in table_column_dic[table[0]]:
                column_list.append(column[0])
            data=self.db.getdata({table[0]:column_list})
            result_dic.update({table[0]:data})
        return result_dic
    def get_data_one_table(self,table):
        result_dic={}
        table_column_dic = self.db.getcolumns([table,])
        column_list = table_column_dic[table]
        columns=[]
        for col in column_list:
            columns.append(col[0])
        data = self.db.getdata({table: columns})
        result_dic.update({table: data})
        return result_dic
    def to_int(self,list):
        from decimal import Decimal
        result=[]
        for mem in list:
            if mem is not None:
               result.append(Decimal(mem))
        return result
    def AVE(self):
        data=self.getdata()
        ave=0
        ave_tuple=[]
        for table in data:
            columns_dic=data[table]
            data_tuple = []
            for column in columns_dic:
                if column in self.target:
                    ave=sum(self.to_int(columns_dic[column]))/len(columns_dic[column])
                    data_tuple.append((column,ave))
            data_tuple=tuple(data_tuple)
            ave_tuple.append((table,data_tuple))
        ave_tuple=tuple(ave_tuple)
        for table in ave_tuple:
            print(table)
    def MACD(self):
        result_list=[]
        from decimal import Decimal
        for table in self.data:
            if(table!='tsetmc'):
                for column in self.data[table]:
                    if(column=='macd_minus_signal'):
                        for macd_value in self.data[table][column]:
                            try:
                                macd=Decimal(macd_value)
                                if (macd > -5 and macd < 5):
                                    result_list.append(table)
                            except:pass
            else:pass
        return result_list
    def RSI(self):
        result_list=[]
        from decimal import Decimal
        for table in self.data:
            if(table!='tsetmc'):
                for column in self.data[table]:
                    if(column=='rsi14'):
                        for rsi_value in self.data[table][column]:
                            try:
                                rsi=Decimal(rsi_value)
                                if ( rsi > 25 and rsi < 35):
                                    result_list.append(table)
                            except:pass
            else:pass
        return result_list
    def Bolinger_Bands(self):
        result_list=[]
        from decimal import Decimal
        for table in self.data:
            if(table!='tsetmc'):
                for column in self.data[table]:
                    if(column=='bollinger_bands'):
                        for rsi_value in self.data[table][column]:
                            try:
                                rsi=Decimal(rsi_value)
                                if (rsi > 0 and rsi < 1500 ):
                                    result_list.append(table)
                            except:pass
            else:pass
        return result_list
    def CHOOSE(self):
        self.data=self.getdata()
        rsi_list=self.RSI()
        macd_list=self.MACD()
        bolinger_band_list=self.Bolinger_Bands()
        list1=list(set(rsi_list) & set(macd_list) & set(bolinger_band_list))
        result_list=[]
        for str in list1:
            result_list.append(str.replace("tb_", ""))
        file1 = open("NamadRecommended.txt", "w", encoding="utf-8")
        for id in result_list:
            file1.write(self.convert_id_to_name(id) + "\n")
            # print(self.convert_id_to_name(id),'             ',id)
        file1.close()
        # import os
        # script_path = os.getcwd()
        # os.startfile(script_path + r'\NamadRecommended.txt')
    def convert_id_to_name(self, id):
        result_name = 0
        for nn in self.namad_ids_dic:
            if (self.namad_ids_dic[nn] == id):
                result_name = nn
        return result_name
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
        print('name and ids has been read : ',result_dic)
        return result_dic
    def plot(self,data,legend_names,title,xlab,ylab):
        import matplotlib.pyplot as plt
        from matplotlib.ticker import FuncFormatter
        xlable = self.to_persian(xlab)
        ylable = self.to_persian(ylab)
        title = self.to_persian(title)
        from matplotlib.dates import date2num
        date1=date2num(list(data[0]))
        ax = plt.subplot(111)
        # list1=[mem - 500000 for mem in date_values_tuple[1]]
        width=0.1
        alien=-2*width
        colors=['r','b','g','y','cyan','black']
        print(data)

        for i in range(0,len(data[1]),1):
            plt.bar(date1+alien, data[1][i], width=width, color=colors[i], label=self.to_persian(legend_names[i]))
            alien+=width
        ax.xaxis_date()

        ax.set_axisbelow(True)

        # Turn on the minor TICKS, which are required for the minor GRID
        ax.minorticks_on()

        # Customize the major grid
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        # Customize the minor grid
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        # ax.grid(zorder=0)
        # ax.bar(range(len(y)), y, width=0.3, align='center', color='skyblue', zorder=3)
        plt.xlabel(xlable, fontweight='bold')
        plt.ylabel(ylable, fontweight='bold')
        plt.title(title, fontweight='bold')
        plt.legend()
        plt.show()
    def to_persian(self,str):
        import arabic_reshaper
        from bidi.algorithm import get_display
        str = arabic_reshaper.reshape(str)
        str = get_display(str)
        return str
    def str_to_date(self,date_list):
        import datetime
        import TAGHVIM
        from decimal import Decimal
        date_ass=''
        date_result=[]
        for date in date_list:
            res_part=''
            date_list=[]
            for c in date:
                if(c!='/'):
                    res_part+=c
                else:
                    date_list.append(res_part)
                    res_part=''
            date_list.append(res_part)
            cal = TAGHVIM.gregorian_to_jalali(int(date_list[0]), int(date_list[1]), int(date_list[2]))
            x = datetime.datetime(cal[0],cal[1] ,cal[2] )
            date_result.append(x)
        return tuple(date_result)
    def sum_corrosponding(self,list1,list2):
        result_list=[]
        from decimal import Decimal
        for i in range(0,len(list1),1):
            try:val1=Decimal(list1[i])
            except:val1=0
            try:val2=Decimal(list2[i])
            except:val2=0
            res=val1+val2
            result_list.append(res)
        return result_list
    def divide_corrosponding(self,list_vol,list_tno,c):
        result_list=[]
        from decimal import Decimal
        for i in range(0,len(list_vol),1):
            try:vol=Decimal(list_vol[i])
            except:val1=0
            try:tno=Decimal(list_tno[i])*c
            except:val2=0
            res=round(vol/tno,1)
            result_list.append(res)
        return result_list
    def sell_buy_per_tval_corrosponding(self,sellorbuy,tval):
        result_list=[]
        from decimal import Decimal
        for i in range(0,len(sellorbuy),1):
            try:vol=Decimal(sellorbuy[i])
            except:val1=0
            try:tno=Decimal(tval[i])
            except:val2=0
            res=round((vol/tno)*100,1)
            result_list.append(res)
        return result_list
    def get_time_and_value(self,table,column):
        data={}
        date=[]
        values=[]
        #values
        # time
        if(column=='جریان نقدینگی بازار'):
            print(column,' bar chart is loading ...')
            data=self.get_data_one_table(table)
            date = self.str_to_date(data[table]['date'])
            value_list1 = data['tsetmc']['n_findow_fbou_M']
            value_list2 = data['tsetmc']['n_findow_bou_M']
            value_list3 = data['tsetmc']['i_findow_fbou_M']
            value_list4 = data['tsetmc']['i_findow_bou_M']
            values_n = self.sum_corrosponding(value_list2, value_list1)
            values_i = self.sum_corrosponding(value_list3, value_list4)
            values=[values_n,values_i]
        elif(column=='جریان نقدینگی بورس'):
            print(column,' bar chart is loading ...')
            data=self.get_data_one_table(table)
            date = self.str_to_date(data[table]['date'])
            values=[self.to_decimal(data['tsetmc']['i_findow_bou_M']),self.to_decimal(data['tsetmc']['n_findow_bou_M'])]
        elif(column=='جریان نقدینگی فرابورس'):
            print(column,' bar chart is loading ...')
            data=self.get_data_one_table(table)
            date = self.str_to_date(data[table]['date'])
            values=[self.to_decimal(data['tsetmc']['i_findow_fbou_M']),self.to_decimal(data['tsetmc']['n_findow_fbou_M'])]
        elif (column == 'جریان نقدینگی بورس و فرایورس'):
            print(column,' bar chart is loading ...')
            data=self.get_data_one_table(table)
            date = self.str_to_date(data[table]['date'])
            value_list1 =self.to_decimal( data['tsetmc']['n_findow_fbou_M'])
            value_list2 = self.to_decimal(data['tsetmc']['n_findow_bou_M'])
            value_list3 = self.to_decimal(data['tsetmc']['i_findow_fbou_M'])
            value_list4 = self.to_decimal(data['tsetmc']['i_findow_bou_M'])
            values=[value_list4,value_list3,value_list2,value_list1]
        elif (column == 'اختلاف صف خرید بورس و فرابورس'):
            print(column,' bar chart is loading ...')
            data=self.get_data_one_table(table)
            date = self.str_to_date(data[table]['date'])
            value_list1 =self.to_decimal( data['tsetmc']['lbuy_tval_bou_B'])
            value_list2 = self.to_decimal(data['tsetmc']['lbuy_tval_fbou_B'])
            value_list3 = self.to_decimal(data['tsetmc']['lsell_tval_bou_B'])
            value_list4 = self.to_decimal(data['tsetmc']['lsell_tval_fbou_B'])
            bourse=self.subtrac_corrosponding(value_list1,value_list3)
            fara_bourse=self.subtrac_corrosponding(value_list2,value_list4)
            values=[bourse,fara_bourse,self.sum_corrosponding(bourse,fara_bourse)]
        elif column in self.sanat_name:
            try:
                print('sanat: ', column, ' bar chart in loading ...')
                import os
                script_path = os.getcwd()
                import xml.etree.cElementTree as ET
                tree = ET.parse(script_path + r'\Groups' + '\\' + self.per_to_en(column) + '.xml')
                root = tree.getroot()
                id_name_dic = {}
                id_list = []
                for child in root:
                    # id_name_dic[child.attrib.get('id')] = child.attrib.get('name')
                    id_list.append(child.attrib.get('id'))
                value_lists_i = []
                value_lists_n = []
                tb_name = ''
                for id in id_list:
                    data = self.get_data_one_table('tb_' + id)
                    tb_name = 'tb_' + id
                    value_lists_i.append(self.to_decimal(data['tb_' + id]['buy_sell_power_ratio']))
                    value_lists_n.append(self.to_decimal(data['tb_' + id]['i_money_fluence_B']))
                date = self.str_to_date(data[tb_name]['date'])
                value_list_i = []
                value_list_n = []
                for v_l_i in value_lists_i:
                    value_list_i = self.sum_corrosponding(v_l_i, value_list_i)
                for v_l_n in value_lists_n:
                    value_list_n = self.sum_corrosponding(v_l_n, value_list_n)
                values = [value_list_i, value_list_n]
            except:print('sanat bar chart Error ... ')
        elif (column == 'تعداد سهام پایانی مثبت بازار بورس و فرابورس'):
            print(column,' bar chart is loading ...')
            data=self.get_data_one_table(table)
            date = self.str_to_date(data[table]['date'])
            value_list2 =self.to_decimal( data['tsetmc']['namad_positive_fbou_count'])
            value_list1 = self.to_decimal(data['tsetmc']['namad_positive_bou_count'])
            values=[value_list1,value_list2,self.sum_corrosponding(value_list2,value_list1)]
        elif (column == 'ارزش بازار بورس و فرابورس'):
            print(column,' bar chart is loading ...')
            data=self.get_data_one_table(table)
            date = self.str_to_date(data[table]['date'])
            value_list2 =self.to_decimal( data['tsetmc']['fbou_tval_B'])
            value_list1 = self.to_decimal(data['tsetmc']['bou_tval_B'])
            values=[value_list1,value_list2,self.sum_corrosponding(value_list2,value_list1)]
        elif column in self.namad_ids_dic.values():
            data=self.get_data_one_table('tb_'+column)
            date = self.str_to_date(data['tb_'+column]['date'])
            print('namad: ',column, ' bar chart in loading ...')
            values=[self.to_decimal(data['tb_'+column]['i_money_fluence_B']),self.to_decimal(data['tb_'+column]['buy_sell_power_ratio'])]
        elif (column == 'میانگین حجم معامله شده به ازای هر کد بورسی'):
            print(column,' bar chart is loading ...')
            data=self.get_data_one_table(table)
            date = self.str_to_date(data[table]['date'])
            fbou_tvol =self.to_decimal( data['tsetmc']['fbou_tvol_B'])
            fbou_tno = self.to_decimal(data['tsetmc']['fbou_tno_M'])
            fbou=self.divide_corrosponding(fbou_tvol,fbou_tno,1)
            bou_tvol =self.to_decimal( data['tsetmc']['bou_tvol_B'])
            bou_tno = self.to_decimal(data['tsetmc']['bou_tno_M'])
            bou=self.divide_corrosponding(bou_tvol,bou_tno,1)
            tse_tvol=self.sum_corrosponding(fbou_tvol,bou_tvol)
            tse_tno=self.sum_corrosponding(fbou_tno,bou_tno)
            tse=self.divide_corrosponding(tse_tvol,tse_tno,1)
            values=[bou,fbou,tse]
        elif (column == 'میانگین ارزش خرید/ فروش حقیقی بازار'):
            print(column,' bar chart is loading ...')
            data=self.get_data_one_table(table)
            date = self.str_to_date(data[table]['date'])
            i_buy_bou =self.to_decimal( data['tsetmc']['i_buy_tval_bou_B'])
            i_buy_fbou = self.to_decimal(data['tsetmc']['i_buy_tval_fbou_B'])
            i_sell_bou = self.to_decimal(data['tsetmc']['i_sell_tval_bou_B'])
            i_sell_fbou = self.to_decimal(data['tsetmc']['i_sell_tval_fbou_B'])

            i_buy_bou_count =self.to_decimal( data['tsetmc']['i_buy_count_bou_K'])
            i_buy_fbou_count = self.to_decimal(data['tsetmc']['i_buy_count_fbou_K'])
            i_sell_bou_count = self.to_decimal(data['tsetmc']['i_sell_count_bou_K'])
            i_sell_fbou_count = self.to_decimal(data['tsetmc']['i_sell_count_fbou_K'])

            i_buy_tse_tval=self.sum_corrosponding(i_buy_bou,i_buy_fbou)
            i_sell_tse_tval=self.sum_corrosponding(i_sell_bou,i_sell_fbou)
            i_buy_tse_count=self.sum_corrosponding(i_buy_bou_count,i_buy_fbou_count)
            i_sell_tse_count=self.sum_corrosponding(i_sell_bou_count,i_sell_fbou_count)

            i_buy_tse=self.divide_corrosponding(i_buy_tse_tval,i_buy_tse_count,1)
            i_sell_tse=self.divide_corrosponding(i_sell_tse_tval,i_sell_tse_count,1)




            bou_sell=self.divide_corrosponding(i_sell_bou,i_sell_bou_count,1)
            bou_buy = self.divide_corrosponding(i_buy_bou, i_buy_bou_count,1)

            fbou_sell=self.divide_corrosponding(i_sell_fbou,i_sell_fbou_count,1)
            fbou_buy = self.divide_corrosponding(i_buy_fbou, i_buy_fbou_count,1)


            values=[bou_buy,bou_sell,fbou_buy,fbou_sell,i_buy_tse,i_sell_tse]
        elif (column == 'میانگین ارزش خرید/ فروش حقوقی بازار'):
            print(column,' bar chart is loading ...')
            data=self.get_data_one_table(table)
            date = self.str_to_date(data[table]['date'])
            i_buy_bou =self.to_decimal( data['tsetmc']['n_buy_tval_bou_B'])
            i_buy_fbou = self.to_decimal(data['tsetmc']['n_buy_tval_fbou_B'])
            i_sell_bou = self.to_decimal(data['tsetmc']['n_sell_tval_bou_B'])
            i_sell_fbou = self.to_decimal(data['tsetmc']['n_sell_tval_fbou_B'])

            i_buy_bou_count =self.to_decimal( data['tsetmc']['n_buy_count_bou_K'])
            i_buy_fbou_count = self.to_decimal(data['tsetmc']['n_buy_count_fbou_K'])
            i_sell_bou_count = self.to_decimal(data['tsetmc']['n_sell_count_bou_K'])
            i_sell_fbou_count = self.to_decimal(data['tsetmc']['n_sell_count_fbou_K'])

            i_buy_tse_tval=self.sum_corrosponding(i_buy_bou,i_buy_fbou)
            i_sell_tse_tval=self.sum_corrosponding(i_sell_bou,i_sell_fbou)
            i_buy_tse_count=self.sum_corrosponding(i_buy_bou_count,i_buy_fbou_count)
            i_sell_tse_count=self.sum_corrosponding(i_sell_bou_count,i_sell_fbou_count)

            i_buy_tse=self.divide_corrosponding(i_buy_tse_tval,i_buy_tse_count,1000)
            i_sell_tse=self.divide_corrosponding(i_sell_tse_tval,i_sell_tse_count,1000)




            bou_sell=self.divide_corrosponding(i_sell_bou,i_sell_bou_count,1000)
            bou_buy = self.divide_corrosponding(i_buy_bou, i_buy_bou_count,1000)

            fbou_sell=self.divide_corrosponding(i_sell_fbou,i_sell_fbou_count,1000)
            fbou_buy = self.divide_corrosponding(i_buy_fbou, i_buy_fbou_count,1000)


            values=[bou_buy,bou_sell,fbou_buy,fbou_sell,i_buy_tse,i_sell_tse]
        elif (column == 'نسبت صف خرید/فروش به ارزش بازار'):
            print(column,' bar chart is loading ...')
            data=self.get_data_one_table(table)
            date = self.str_to_date(data[table]['date'])
            lbuy_tval_bou_B =self.to_decimal( data['tsetmc']['lbuy_tval_bou_B'])
            lbuy_tval_fbou_B = self.to_decimal(data['tsetmc']['lbuy_tval_fbou_B'])
            lsell_tval_bou_B = self.to_decimal(data['tsetmc']['lsell_tval_bou_B'])
            lsell_tval_fbou_B = self.to_decimal(data['tsetmc']['lsell_tval_fbou_B'])
            bou_tval_B = self.to_decimal(data['tsetmc']['bou_tval_B'])
            fbou_tval_B = self.to_decimal(data['tsetmc']['fbou_tval_B'])
            tse_lbuy_B=self.sum_corrosponding(lbuy_tval_bou_B,lbuy_tval_fbou_B)
            tse_lsell_B=self.sum_corrosponding(lsell_tval_bou_B,lsell_tval_fbou_B)
            tse_tval_B=self.sum_corrosponding(bou_tval_B,fbou_tval_B)


            BPV_bou=self.sell_buy_per_tval_corrosponding(lbuy_tval_bou_B,bou_tval_B)
            SPV_bou=self.sell_buy_per_tval_corrosponding(lsell_tval_bou_B,bou_tval_B)
            BPV_fbou=self.sell_buy_per_tval_corrosponding(lbuy_tval_fbou_B,fbou_tval_B)
            SPV_fbou=self.sell_buy_per_tval_corrosponding(lsell_tval_fbou_B,fbou_tval_B)
            BPV_tse=self.sell_buy_per_tval_corrosponding(tse_lbuy_B,tse_tval_B)
            SPV_tse=self.sell_buy_per_tval_corrosponding(tse_lsell_B,tse_tval_B)
            values=[BPV_bou,SPV_bou,BPV_fbou,SPV_fbou,BPV_tse,SPV_tse]




        return (date,values)
    def to_decimal(self,list):
        result_list=[]
        from decimal import Decimal
        for mem in list:
            result_list.append(Decimal(mem))
        return result_list
    def get_sanat_name(self):
        import os
        try:
            arr = os.listdir('Groups')
            names = []
            for name in arr:
                names.append(name.replace('.xml', ''))
            return names
        except:pass
    def per_to_en(self,str):
        res = ''
        for c in str:
            for en in self.fa_en_dic:
                if (c == self.fa_en_dic[en] or c in self.fa_en_dic[en]):
                    res += en
                if (c == en):
                    try:
                        res += self.fa_en_dic[en]
                    except:
                        res += self.fa_en_dic[en][0]
        return res
    def get_id_by_name(self,name):
        try:
            import NAMADMANAGER
            Mn = NAMADMANAGER.NAMADMANAGER()
            return Mn.convert_namad_to_id(name)
        except:pass
    def subtrac_corrosponding(self,list1,list2):
        result_list=[]
        from decimal import Decimal
        for i in range(0,len(list1),1):
            try:val1=Decimal(list1[i])
            except:val1=0
            try:val2=Decimal(list2[i])
            except:val2=0
            res = val1 - val2
            result_list.append(res)
        return result_list
    def show_namad_in_sanat(self,column):
        print('sanat: ', column, ' bar chart in loading ...')
        import os
        script_path = os.getcwd()
        import xml.etree.cElementTree as ET
        tree = ET.parse(script_path + r'\Groups' + '\\' + self.per_to_en(column) + '.xml')
        root = tree.getroot()
        id_name_dic = {}
        id_list = []
        for child in root:
            # id_name_dic[child.attrib.get('id')] = child.attrib.get('name')
            id_list.append(child.attrib.get('id'))
        value_lists_i = []
        value_lists_n = []
        tb_name = ''
        result_list=[]
        import NAMADMANAGER
        namad = NAMADMANAGER.NAMADMANAGER()
        data=[]
        for id in id_list:
            data.clear()
            data = self.get_data_one_table('tb_' + id)
            tb_name = 'tb_' + id
            value_lists_i=self.to_decimal(data['tb_' + id]['buy_sell_power_ratio'])
            value_lists_n=self.to_decimal(data['tb_' + id]['i_money_fluence_B'])
            date = self.str_to_date(data[tb_name]['date'])
            self.plot((date,[value_lists_i,value_lists_n]), ['حقیقی', 'حقوقی'], namad.convert_id_to_name(id), u'زمان',u'سرانه(میلیون تومان)')
        return result_list
    def ReturnDB(self):
        return self.db




