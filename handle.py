import USERCONTROL
import timeit
start = timeit.default_timer()





sanat_list=[
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
# fa_en_dic = fa_dic = {
#     '1': ['آ', 'ا'],
#     '2': 'ب',
#     '3': 'ث',
#     '4': 'د',
#     '5': 'ی',
#     '6': 'ف',
#     '7': 'ل',
#     '8': 'گ',
#     '9': ['ح', 'ه'],
#     'I': 'ی',
#     'V': 'ج',
#     'W': 'ک',
#     'K': 'ل',
#     'P': 'م',
#     'O': 'ن',
#     'Q': 'پ',
#     'R': ['ق', 'غ'],
#     'S': 'ر',
#     'T': ['س', 'ص'],
#     'U': ['ت', 'ط'],
#     'G': 'و',
#     'H': 'ک',
#     'L': 'خ',
#     'Z': ['ز', 'ض', 'ظ', 'ذ'],
# }
# def per_to_en(str):
#     res=''
#     for c in str:
#         for en in fa_en_dic:
#             if(c==fa_dic[en] or c in fa_en_dic[en] ):
#                 res+=en
#             if(c==en):
#                 try:res+=fa_en_dic[en]
#                 except:res+=fa_en_dic[en][0]
#     print(res)
# per_to_en(sanat_list[0])
# input()
#
# import os
# arr = os.listdir('Groups')
# names=[]
# for name in arr:
#     names.append(name.replace('.xml',''))
# print(names)
# for name in names:
#     print(name)

# input()
# import EXT
#
# ext_motor = EXT.EXTRACTION('http://www.tsetmc.com/Loader.aspx?ParTree=15131F', '', [])
# ext_motor.update_groups()





# import math
# distance_dic={
#     'AB':2,'AC':3,'AF':4,'AD':5,'AG':7,
#     'BF':3,'BC':6,'BG':2,'BD':1,
#     'CF':2,'CG':7,'CD':10,
#     'FG':4,'FD':3,
#     'GD':4
#     }
# KT=math.pow(10,-5)
# C_reduce=0

def plot():
    import ANALYZER
    import NAMADMANAGER
    analyzer = ANALYZER.ANALYZER()
    namad_manager = NAMADMANAGER.NAMADMANAGER()
    #
    data = analyzer.get_time_and_value('tsetmc', 'نسبت صف خرید/فروش به ارزش بازار')
    analyzer.plot(data,['نسبت ارزش صف خرید بورس به ارزش بورس', 'نسبت ارزش صف فروش بورس به ارزش بورس', 'نسبت ارزش صف خرید فرابورس به ارزش فرابورس', 'نسبت ارزش صف فروش فرابورس به ارزش فرابورس',
     'نسبت ارزش صف خرید بازار به ارزش بازار', 'نسبت ارزش صف فروش بازار به ارزش بازار'],'نسبت صف خرید/فروش به ارزش بازار', u'زمان', u'درصد')


    data = analyzer.get_time_and_value('tsetmc', 'میانگین ارزش خرید/ فروش حقوقی بازار')
    analyzer.plot(data,['میانگین ارزش خرید بورس', 'میانگین ارزش فروش بورس', 'میانگین ارزش خرید فرابورس', 'میانگین ارزش فروش فرابورس',
     'میانگین ارزش خرید بازار', 'میانگین ارزش فروش بازار'],'میانگین ارزش خرید/ فروش حقوقی بازار', u'زمان', u'میانگین ارزش(میلیارد تومان)')
    # #
    # #
    data = analyzer.get_time_and_value('tsetmc', 'میانگین ارزش خرید/ فروش حقیقی بازار')
    analyzer.plot(data,['میانگین ارزش خرید بورس', 'میانگین ارزش فروش بورس', 'میانگین ارزش خرید فرابورس', 'میانگین ارزش فروش فرابورس',
     'میانگین ارزش خرید بازار', 'میانگین ارزش فروش بازار'], 'میانگین ارزش خرید/ فروش حقیقی بازار', u'زمان', u'میانگین ارزش(میلیون تومان)')
    # #
    data = analyzer.get_time_and_value('tsetmc', 'میانگین حجم معامله شده به ازای هر کد بورسی')
    analyzer.plot(data, ['بورس','فرابورس', 'بازار'], 'میانگین حجم معامله شده به ازای هر کد بورسی', u'زمان', u'میانگین حجم معامله شده به ازای هر کد بورسی(هزار)')
    # #

    data=analyzer.get_time_and_value('tsetmc','اختلاف صف خرید بورس و فرابورس')
    analyzer.plot(data,['بورس','فرابورس','بازار'],'اختلاف صف خرید بورس و فرابورس',u'زمان',u'ارزش (میلیارد تومان)')

    data=analyzer.get_time_and_value('tsetmc','ارزش بازار بورس و فرابورس')
    analyzer.plot(data,['بورس','فرابورس','بازار'],'ارزش بازار بورس و فرابورس',u'زمان',u'ارزش (میلیارد تومان)')


    data=analyzer.get_time_and_value('tsetmc','تعداد سهام پایانی مثبت بازار بورس و فرابورس')
    analyzer.plot(data,['بورس','فرابورس','بازار'],'تعداد سهام پایانی مثبت بازار بورس و فرابورس',u'زمان',u'تعداد')

    # data=analyzer.get_time_and_value('tsetmc','18093681647131179')
    # analyzer.plot(data,['حقوقی','حقیقی'],'دتولید',u'زمان',u'(میلیون تومان)اختلاف سرانه')
    data=analyzer.get_time_and_value('tsetmc','69090868458637360')
    analyzer.plot(data,['حقوقی','حقیقی'],'دیران',u'زمان',u'(میلیون تومان)اختلاف سرانه')
    data=analyzer.get_time_and_value('tsetmc','24085906177899789')
    analyzer.plot(data,['حقوقی','حقیقی'],'کترام',u'زمان',u'(میلیون تومان)اختلاف سرانه')
    data=analyzer.get_time_and_value('tsetmc',namad_manager.convert_namad_to_id('وتعاون'))
    analyzer.plot(data,['حقوقی','حقیقی'],'وتعاون',u'زمان',u'(میلیون تومان)اختلاف سرانه')
    data=analyzer.get_time_and_value('tsetmc','66450490505950110')
    analyzer.plot(data,['حقوقی','حقیقی'],'ددام',u'زمان',u'(میلیون تومان)اختلاف سرانه')
    # #

    data=analyzer.get_time_and_value('tsetmc','مواد و محصولات دارويي')
    analyzer.plot(data,['حقوقی','حقیقی'],'مواد و محصولات دارويي',u'زمان',u'خروج نقدینگی(میلیون تومان)')

    data=analyzer.get_time_and_value('tsetmc','كاشي و سراميك')
    analyzer.plot(data,['حقوقی','حقیقی'],'كاشي و سراميك',u'زمان',u'خروج نقدینگی(میلیون تومان)')

    data=analyzer.get_time_and_value('tsetmc','جریان نقدینگی بازار')
    analyzer.plot(data,['حقوقی','حقیقی'],u'جریان نقدینگی بازار',u'زمان',u'(میلیون تومان)خروج نقدینگی')

    data=analyzer.get_time_and_value('tsetmc','جریان نقدینگی بورس و فرایورس')
    analyzer.plot(data,['حقیقی بورس','حقیقی فرابورس','حقوقی بورس','حقوقی فرابورس'],u'جریان نقدینگی بورس و فرایورس',u'زمان',u'بورس و فرایورس خروج نقدینگی(میلیون تومان)')

    data=analyzer.get_time_and_value('tsetmc','جریان نقدینگی بورس')
    analyzer.plot(data,['حقیقی بورس','حقوقی بورس'],u'جریان نقدینگی بورس',u'زمان',u'بورس خروج نقدینگی(میلیون تومان)')

    data=analyzer.get_time_and_value('tsetmc','جریان نقدینگی فرابورس')
    analyzer.plot(data,['حقوقی فرابورس','حقیقی فرابورس'],u'جریان نقدینگی فرابورس',u'زمان',u'(میلیون تومان)بورس خروج نقدینگی')
    #
def intro():
    import ANALYZER
    analyzer = ANALYZER.ANALYZER()
    analyzer.CHOOSE()
    input()
# plot()
# intro()
# input()
# # sanat namad (s)
# out=analyzer.show_namad_in_sanat( 'مواد و محصولات دارويي')
# for data in out:
#     analyzer.plot(data[0],['حقیقی','حقوقی'],data[1],u'زمان',u'(میلیون تومان)اختلاف سرانه')
# input()
# for mem in sanat_list:
#     data = analyzer.get_time_and_value('tsetmc',mem)
#     analyzer.plot(data, ['حقیقی', 'حقوقی'], mem, u'زمان', u'خروج نقدینگی(میلیون تومان)')
#
# input()


# file1 = open(r"D:\extractionapp\indicators\rsi.txt","r")
# str=''
# for line in file1.readlines():
#     str+=line
# print(str)
# input()

# #
import NAMADMANAGER
# # import CALCULATOR
# # # cal=CALCULATOR.CAL()
# # # # cal.insert_data_into_namad_tables({'tb_10024128313803797':{'rsi':'12'},})
# namad_manager=NAMADMANAGER.NAMADMANAGER()
# namad_manager.createnamadtales()
# # # namad_manager.deletetables()
# # # # namad_manager.delete_a_table_by_name('ومهان')
# # # # namad_manager.add_a_table_by_name('ومهان')
# namad_manager.update_tables()
# namad_manager.update_group()
# input('this is the beginning of a huge victory ...')


# import DB
# db=DB.DB('127.0.0.1','root', '', 'tsetmc_db')
# print(db.gettables())
# print(db.getcolumns(['tsetmc']))
# db.deletedata('tsetmc','s')
# db.find_id('tsetmc')
# print(db.id_for_insert)
# input()
# tablecolumn_dic={}
# tables=db.gettables()
# print(len(tables))
# for tb in tables:
#     if(tb[0]!='tsetmc'):pass
#     else:
#         table=str(tb[0])
#         tablecolumn_dic[table]=['pcp',]
#         db.deletedata(table,'')
#         # print(db.getdata({table:['ID']}))
#         # db.deletecolumn(tablecolumn_dic)
#         # db.deletedata(table,'2020/8/4')
#         # db.deleteco(   tablecolumn_dic )
#         # db.addcolumn(tablecolumn_dic)
#         tablecolumn_dic.clear()
#         # db.addcol(tablecolumn_dic)
# # # for tb in db.gettables():
# # #     if(tb=='tsetmc'):pass
# # #     else:
# # #         db.deletedata(tb[0], 2)
# # # db.deletedata('tsetmc','date')
# # # db.insertdata(dict(tsetmc=dict(bou_tval_B='14980.3',lbuy_tval_bou_B='5779.3',lsell_tval_bou_B='3222',i_buy_tval_bou_B='12661.8',i_sell_tval_bou_B='10663.5',n_buy_tval_bou_B='2318.5',n_sell_tval_bou_B='4316.8',i_findow_bou_M='-2798',n_findow_bou_M='-173441.3',bou_tno_M='1.7',bou_tvol_B='8.1',i_buy_count_bou_K='1059.6',i_sell_count_bou_K='395.1',n_buy_count_bou_K='1.4',n_sell_count_bou_K='1.4',namad_positive_bou_count='110',fbou_tval_B='5112.5',lbuy_tval_fbou_B='2046.4',lsell_tval_fbou_B='646',i_buy_tval_fbou_B='4478.6',i_sell_tval_fbou_B='4202.6',n_buy_tval_fbou_B='634',n_sell_tval_fbou_B='910.1',i_findow_fbou_M='1173.1',n_findow_fbou_M='-94811.1',fbou_tno_M='0.7',fbou_tvol_B='2.4',i_buy_count_fbou_K='334.6',i_sell_count_fbou_K='253.5',n_buy_count_fbou_K='0.5',n_sell_count_fbou_K='0.5',namad_positive_fbou_count='131',date='2020/7/26')))
# # # db.deletetable(['tsetmc',])
# # # data=db.getdata(dict(tsetmc=['bou_tval_B','lbuy_tval_bou_B','lsell_tval_bou_B','i_buy_tval_bou_B','i_sell_tval_bou_B','n_buy_tval_bou_B','n_sell_tval_bou_B','i_findow_bou_M','n_findow_bou_M','bou_tno_M','bou_tvol_B','i_buy_count_bou_K','i_sell_count_bou_K','n_buy_count_bou_K','n_sell_count_bou_K','namad_positive_bou_count','fbou_tval_B','lbuy_tval_fbou_B','lsell_tval_fbou_B','i_buy_tval_fbou_B','i_sell_tval_fbou_B','n_buy_tval_fbou_B','n_sell_tval_fbou_B','i_findow_fbou_M','n_findow_fbou_M','fbou_tno_M','fbou_tvol_B','i_buy_count_fbou_K','i_sell_count_fbou_K','n_buy_count_fbou_K','n_sell_count_fbou_K','namad_positive_fbou_count','date']))
# # # db.addtable(dict(tsetmc=['ID','bou_tval_B','lbuy_tval_bou_B','lsell_tval_bou_B','i_buy_tval_bou_B','i_sell_tval_bou_B','n_buy_tval_bou_B','n_sell_tval_bou_B','i_findow_bou_M','n_findow_bou_M','bou_tno_M','bou_tvol_B','i_buy_count_bou_K','i_sell_count_bou_K','n_buy_count_bou_K','n_sell_count_bou_K','namad_positive_bou_count','fbou_tval_B','lbuy_tval_fbou_B','lsell_tval_fbou_B','i_buy_tval_fbou_B','i_sell_tval_fbou_B','n_buy_tval_fbou_B','n_sell_tval_fbou_B','i_findow_fbou_M','n_findow_fbou_M','fbou_tno_M','fbou_tvol_B','i_buy_count_fbou_K','i_sell_count_fbou_K','n_buy_count_fbou_K','n_sell_count_fbou_K','namad_positive_fbou_count','date']))
# #
# input('that is end ....')





# #
# import EXEL
# exec =EXEL.EXEL()
# exec.save_all_data_to_exel()
# input()



# import EXT
# import datetime
# def KFB_tval():
#
#  extractionmotor2 = EXT.EXTRACTION('http://www.tsetmc.com/Loader.aspx?ParTree=15131F','true==function(){a=0;b=0;b=(po1)*(qo1);(cfield0)=b;(cfield1)=(tval);a=a+(pd1)*(qd1);(cfield2)=a;if(1==1){return true;}else{returnfalse;}}()',['findow', 'tval', 'val_buy'])
#  extractionmotor2.dosettingforextraction()
#  #extractionmotor2.newstringfilter('true==function(){(cfield0)=(qd1)*(pd1);(cfield1)=( ((ct).Buy_I_Volume/(ct).Buy_CountI) - ((ct).Sell_I_Volume/(ct).Sell_CountI) )*(pc);(cfield2)=( ((ct).Buy_N_Volume/(ct).Buy_CountN) - ((ct).Sell_N_Volume/(ct).Sell_CountN) )*(pc);if(1==1){return true;}else{return false;}}()',['lbuy_tval_B','i_findow_M','n_findow_M'])
#  while (1 == 1):
#   data = extractionmotor2.extractalldata()
#   tval=0
#   findow=0
#   val_buy=0
#   from decimal import Decimal
#   for table in data:
#       if(data[table]['tval'].isdigit()): tval = tval + Decimal(data[table]['tval'])
#       if(data[table]['findow'].isdigit()): findow = findow + Decimal(data[table]['findow'])
#       if(data[table]['val_buy'].isdigit()): val_buy = val_buy + Decimal(data[table]['val_buy'])
#   print('Arzesh SafForosh =',findow/10000000000,'B  Arzesh Moamelat=',tval/10000000000,'B   Arzesh SafKharid=',val_buy/10000000000,'B    Time:',datetime.datetime.now().time())
#
#
# KFB_tval()



























# usser=USERCONTROL.USER({
# 'ورود-خروج نقدینگی حقیقی بورس(میلیون تومان)':'ON',
# 'ورود-خروج نقدینگی حقوقی بورس(میلیون تومان)':'ON',
# 'ورود-خروج نقدینگی حقیقی فرابورس(میلیون تومان)':'ON',
# 'ورود-خروج نقدینگی حقوقی فرابورس(میلیون تومان)':'ON',
# })
# usser.extract_namad_data()
# input()






usser=USERCONTROL.USER({
'ارزش  بورس':'ON',
'تعداد معاملات بورس':'ON',
'برایند اختلاف سرانه حقیقی بورس':'ON',
'حجم معاملات بورس':'ON',
'تعداد خریدار حقیقی بورس':'ON',
'برایند اختلاف سرانه حقوقی بورس':'ON',
'تعداد خریدار حقوقی بورس':'ON',
'تعداد فروشنده حقوقی بورس':'ON',
'ارزش خرید حقیقی بورس':'ON',
'تعداد فروشنده حقیقی بورس':'ON',
'ارزش فروش حقیقی بورس':'ON',
'ارزش فروش حقوقی بورس':'ON',
'ارزش صف خرید بورس':'ON',
'ارزش صف فروش بورس':'ON',
'تعداد سهام پایانی مثبت بورس':'ON',
'ارزش فرابورس':'ON',
'تعداد معاملات فرابورس':'ON',
'برایند اختلاف سرانه حقوقی فرابورس':'ON',
'حجم معاملات فرابورس':'ON',
'تعداد خریدار حقیقی فرابورس':'ON',
'برایند اختلاف سرانه حقیقی فرابورس':'ON',
'تعداد خریدار حقوقی فرابورس':'ON',
'تعداد فروشنده حقوقی فرابورس':'ON',
'ارزش خرید حقیقی فرابورس':'ON',
'تعداد فروشنده حقیقی فرابورس':'ON',
'ارزش فروش حقیقی فرابورس':'ON',
'ارزش فروش حقوقی فرابورس':'ON',
'ارزش صف خرید فرابورس':'ON',
'ارزش صف فروش فرابورس':'ON',
'تعداد سهام پایانی مثبت فرابورس':'ON',
'ارزش خرید حقوقی فرابورس':'ON',
'ارزش خرید حقوقی بورس':'ON',
})
usser.extrac()
import NAMADMANAGER
namad_manager=NAMADMANAGER.NAMADMANAGER()
namad_manager.createnamadtales()
usser.extract_namad_data()
stop = timeit.default_timer()
print('Running Time: ', round((stop - start)/60) , ' Min')
import os
os.system('shutdown -s')



































