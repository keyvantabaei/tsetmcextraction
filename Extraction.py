import  USERCONTROL
import timeit
start = timeit.default_timer()

usser=USERCONTROL.USER({
'ارزش  بورس':'ON',
# 'تعداد معاملات بورس':'OFF',
'برایند اختلاف سرانه حقیقی بورس':'ON',
# 'حجم معاملات بورس':'OFF',
# 'تعداد خریدار حقیقی بورس':'OFF',
'برایند اختلاف سرانه حقوقی بورس':'ON',
# 'تعداد خریدار حقوقی بورس':'OFF',
# 'تعداد فروشنده حقوقی بورس':'OFF',
'ارزش خرید حقیقی بورس':'ON',
# 'تعداد فروشنده حقیقی بورس':'OFF',
'ارزش فروش حقیقی بورس':'ON',
# 'ارزش فروش حقوقی بورس':'ON',
# 'ارزش صف خرید بورس':'ON',
# 'ارزش صف فروش بورس':'ON',
# 'تعداد سهام پایانی مثبت بورس':'ON',
'ارزش فرابورس':'ON',
# 'تعداد معاملات فرابورس':'OFF',
'برایند اختلاف سرانه حقوقی فرابورس':'ON',
# 'حجم معاملات فرابورس':'OFF',
# 'تعداد خریدار حقیقی فرابورس':'OFF',
'برایند اختلاف سرانه حقیقی فرابورس':'ON',
# 'تعداد خریدار حقوقی فرابورس':'OFF',
# 'تعداد فروشنده حقوقی فرابورس':'OFF',
'ارزش خرید حقیقی فرابورس':'ON',
# 'تعداد فروشنده حقیقی فرابورس':'OFF',
'ارزش فروش حقیقی فرابورس':'ON',
# 'ارزش فروش حقوقی فرابورس':'ON',
# 'ارزش صف خرید فرابورس':'ON',
# 'ارزش صف فروش فرابورس':'ON',
# 'تعداد سهام پایانی مثبت فرابورس':'OFF',
# 'ارزش خرید حقوقی فرابورس':'ON',
# 'ارزش خرید حقوقی بورس':'ON',
})
usser.extrac()
import NAMADMANAGER
namad_manager=NAMADMANAGER.NAMADMANAGER()
# namad_manager.deletetables()
# namad_manager.createnamadtales()
# namad_managerana.createnamadtales()
# namad_manager.createnamadtales()
usser.extract_namad_data()
stop = timeit.default_timer()
print('Running Time: ', round((stop - start)/60) , ' Min')
import os
# os.system('shutdown -s')