import ANALYZER
import NAMADMANAGER

analyzer = ANALYZER.ANALYZER()
namad_manager = NAMADMANAGER.NAMADMANAGER()
# print(analyzer.getdata())
data=analyzer.getdata()
tableslist=[]
for namad in data:
    if(not bool(data[namad])==str("True")):
        tableslist.append(namad)
print(tableslist)
# print("asdasd")
# input("adasd")
#
# data = analyzer.get_time_and_value('tsetmc', 'نسبت صف خرید/فروش به ارزش بازار')
# analyzer.plot(data,['نسبت ارزش صف خرید بورس به ارزش بورس', 'نسبت ارزش صف فروش بورس به ارزش بورس', 'نسبت ارزش صف خرید فرابورس به ارزش فرابورس', 'نسبت ارزش صف فروش فرابورس به ارزش فرابورس',
#  'نسبت ارزش صف خرید بازار به ارزش بازار', 'نسبت ارزش صف فروش بازار به ارزش بازار'],'نسبت صف خرید/فروش به ارزش بازار', u'زمان', u'درصد')


# data = analyzer.get_time_and_value('tsetmc', 'میانگین ارزش خرید/ فروش حقوقی بازار')
# analyzer.plot(data,['میانگین ارزش خرید بورس', 'میانگین ارزش فروش بورس', 'میانگین ارزش خرید فرابورس', 'میانگین ارزش فروش فرابورس',
#  'میانگین ارزش خرید بازار', 'میانگین ارزش فروش بازار'],'میانگین ارزش خرید/ فروش حقوقی بازار', u'زمان', u'میانگین ارزش(میلیارد تومان)')
# #
# #
# data = analyzer.get_time_and_value('tsetmc', 'میانگین ارزش خرید/ فروش حقیقی بازار')
# analyzer.plot(data,['میانگین ارزش خرید بورس', 'میانگین ارزش فروش بورس', 'میانگین ارزش خرید فرابورس', 'میانگین ارزش فروش فرابورس',
#  'میانگین ارزش خرید بازار', 'میانگین ارزش فروش بازار'], 'میانگین ارزش خرید/ فروش حقیقی بازار', u'زمان', u'میانگین ارزش(میلیون تومان)')
# #
# data = analyzer.get_time_and_value('tsetmc', 'میانگین حجم معامله شده به ازای هر کد بورسی')
# analyzer.plot(data, ['بورس','فرابورس', 'بازار'], 'میانگین حجم معامله شده به ازای هر کد بورسی', u'زمان', u'میانگین حجم معامله شده به ازای هر کد بورسی(هزار)')
# #

# data=analyzer.get_time_and_value('tsetmc','اختلاف صف خرید بورس و فرابورس')
# analyzer.plot(data,['بورس','فرابورس','بازار'],'اختلاف صف خرید بورس و فرابورس',u'زمان',u'ارزش (میلیارد تومان)')

# data = analyzer.get_time_and_value('tsetmc', 'ارزش بازار بورس و فرابورس')
# analyzer.plot(data, ['بورس', 'فرابورس', 'بازار'], 'ارزش بازار بورس و فرابورس', u'زمان', u'ارزش (میلیارد تومان)')

# data=analyzer.get_time_and_value('tsetmc','تعداد سهام پایانی مثبت بازار بورس و فرابورس')
# analyzer.plot(data,['بورس','فرابورس','بازار'],'تعداد سهام پایانی مثبت بازار بورس و فرابورس',u'زمان',u'تعداد')

# data=analyzer.get_time_and_value('tsetmc','18093681647131179')
# analyzer.plot(data,['حقوقی','حقیقی'],'دتولید',u'زمان',u'(میلیون تومان)اختلاف سرانه')
# data=analyzer.get_time_and_value('tsetmc','69090868458637360')
# analyzer.plot(data,['حقوقی','حقیقی'],'دیران',u'زمان',u'(میلیون تومان)اختلاف سرانه')
# data=analyzer.get_time_and_value('tsetmc','24085906177899789')
# analyzer.plot(data,['حقوقی','حقیقی'],'کترام',u'زمان',u'(میلیون تومان)اختلاف سرانه')
# data=analyzer.get_time_and_value('tsetmc',namad_manager.convert_namad_to_id('وتعاون'))
# analyzer.plot(data,['حقوقی','حقیقی'],'وتعاون',u'زمان',u'(میلیون تومان)اختلاف سرانه')
data = analyzer.get_time_and_value('tsetmc', '26824673819862694')
analyzer.plot(data, ['حقوقی', 'حقیقی'], 'خبهمن', u'زمان', u'(میلیون تومان)اختلاف سرانه')
# #

# data=analyzer.get_time_and_value('tsetmc','مواد و محصولات دارويي')
# analyzer.plot(data,['حقوقی','حقیقی'],'مواد و محصولات دارويي',u'زمان',u'خروج نقدینگی(میلیون تومان)')
#
# data=analyzer.get_time_and_value('tsetmc','كاشي و سراميك')
# analyzer.plot(data,['حقوقی','حقیقی'],'كاشي و سراميك',u'زمان',u'خروج نقدینگی(میلیون تومان)')
data = analyzer.get_time_and_value('tsetmc', '70934270174405743')
analyzer.plot(data, ['حقوقی', 'حقیقی'], 'شخارک', u'زمان', u'(میلیون تومان)اختلاف سرانه')

data = analyzer.get_time_and_value('tsetmc', '35424116338766901')
analyzer.plot(data, ['حقوقی', 'حقیقی'], 'حفارس', u'زمان', u'(میلیون تومان)اختلاف سرانه')

# data = analyzer.get_time_and_value('tsetmc', 'جریان نقدینگی بازار')
# analyzer.plot(data, ['حقوقی', 'حقیقی'], u'جریان نقدینگی بازار', u'زمان', u'(میلیون تومان)خروج نقدینگی')
#
# data = analyzer.get_time_and_value('tsetmc', 'جریان نقدینگی بورس و فرایورس')
# analyzer.plot(data, ['حقیقی بورس', 'حقیقی فرابورس', 'حقوقی بورس', 'حقوقی فرابورس'], u'جریان نقدینگی بورس و فرایورس',
#               u'زمان', u'بورس و فرایورس خروج نقدینگی(میلیون تومان)')

# data=analyzer.get_time_and_value('tsetmc','جریان نقدینگی بورس')
# analyzer.plot(data,['حقیقی بورس','حقوقی بورس'],u'جریان نقدینگی بورس',u'زمان',u'بورس خروج نقدینگی(میلیون تومان)')
#
# data=analyzer.get_time_and_value('tsetmc','جریان نقدینگی فرابورس')
# analyzer.plot(data,['حقوقی فرابورس','حقیقی فرابورس'],u'جریان نقدینگی فرابورس',u'زمان',u'(میلیون تومان)بورس خروج نقدینگی')
#