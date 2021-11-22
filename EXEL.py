from random import random
import DB
import CALCULATOR
import pandas as pd
class EXEL:
    def __init__(self,):pass
    def save_all_data_to_exel(self):
        db = DB.DB('127.0.0.1', 'root', '', 'tsetmc_db')
        caculator=CALCULATOR.CAL()
        data=db.getdata(dict(tsetmc=['ID','bou_tval_B','lbuy_tval_bou_B','lsell_tval_bou_B','i_buy_tval_bou_B','i_sell_tval_bou_B','n_buy_tval_bou_B','n_sell_tval_bou_B','i_findow_bou_M','n_findow_bou_M','bou_tno_M','bou_tvol_B','i_buy_count_bou_K','i_sell_count_bou_K','n_buy_count_bou_K','n_sell_count_bou_K','namad_positive_bou_count','fbou_tval_B','lbuy_tval_fbou_B','lsell_tval_fbou_B','i_buy_tval_fbou_B','i_sell_tval_fbou_B','n_buy_tval_fbou_B','n_sell_tval_fbou_B','i_findow_fbou_M','n_findow_fbou_M','fbou_tno_M','fbou_tvol_B','i_buy_count_fbou_K','i_sell_count_fbou_K','n_buy_count_fbou_K','n_sell_count_fbou_K','namad_positive_fbou_count','date']))
        data=caculator.TSE_CAL(data)
        print(data)
        self.data=data
        self.data['ارزش  بورس (میلیارد تومان)'] = self.data.pop('bou_tval_B')
        self.data['ارزش فرابورس (میلیارد تومان)'] = self.data.pop('fbou_tval_B')

        del self.data['i_sell_tval_fbou_B'] #= self.data.pop('i_sell_tval_fbou_B')
        del self.data['i_buy_tval_fbou_B'] #= self.data.pop('i_buy_tval_fbou_B')
        del self.data['n_sell_tval_fbou_B'] #= self.data.pop('n_sell_tval_fbou_B')
        del self.data['n_buy_tval_fbou_B'] #= self.data.pop('n_buy_tval_fbou_B')

        del self.data['i_sell_tval_bou_B'] #= self.data.pop('i_sell_tval_bou_B')
        del self.data['i_buy_tval_bou_B'] #= self.data.pop('i_buy_tval_bou_B')
        del self.data['n_sell_tval_bou_B'] #= self.data.pop('n_sell_tval_bou_B')
        del self.data['n_buy_tval_bou_B'] #= self.data.pop('n_buy_tval_bou_B')

        self.data['برایند اختلاف سرانه حقیقی بورس (میلیون تومان)'] = self.data.pop('i_findow_bou_M')
        self.data['برایند اختلاف سرانه حقوقی بورس (میلیون تومان)'] = self.data.pop('n_findow_bou_M')
        self.data['برایند اختلاف سرانه حقیقی فرابورس (میلیون تومان)'] = self.data.pop('i_findow_fbou_M')
        self.data['برایند اختلاف سرانه حقوقی فرابورس (میلیون تومان)'] = self.data.pop('n_findow_fbou_M')

        del self.data['bou_tno_M']# = self.data.pop('bou_tno_M')
        del self.data['fbou_tno_M'] #= self.data.pop('fbou_tno_M')

        del self.data['bou_tvol_B'] #= self.data.pop('bou_tvol_B')
        del self.data['fbou_tvol_B'] #= self.data.pop('fbou_tvol_B')

        del self.data['n_buy_count_fbou_K'] #= self.data.pop('n_buy_count_fbou_K')
        del self.data['i_buy_count_fbou_K'] #= self.data.pop('i_buy_count_fbou_K')
        del self.data['i_sell_count_fbou_K']# = self.data.pop('i_sell_count_fbou_K')
        del self.data['n_sell_count_fbou_K'] #= self.data.pop('n_sell_count_fbou_K')

        del self.data['n_buy_count_bou_K']# = self.data.pop('n_buy_count_bou_K')
        del self.data['i_buy_count_bou_K']# = self.data.pop('i_buy_count_bou_K')
        del self.data['i_sell_count_bou_K']# = self.data.pop('i_sell_count_bou_K')
        del self.data['n_sell_count_bou_K'] #= self.data.pop('n_sell_count_bou_K')

        del self.data['lbuy_tval_fbou_B']# = self.data.pop('lbuy_tval_fbou_B')
        del self.data['lsell_tval_fbou_B'] #= self.data.pop('lsell_tval_fbou_B')

        del self.data['lbuy_tval_bou_B']# = self.data.pop('lbuy_tval_bou_B')
        del self.data['lsell_tval_bou_B'] #= self.data.pop('lsell_tval_bou_B')

        del self.data['namad_positive_bou_count'] #= self.data.pop('namad_positive_bou_count')
        del self.data['namad_positive_fbou_count']# = self.data.pop('namad_positive_fbou_count')

        self.data['تاریخ'] = self.data.pop('date')
        self.data['ID'] = self.data.pop('ID')
        print(data)
        df = pd.DataFrame(self.data, columns=['ID',
                                              'ارزش  بورس (میلیارد تومان)',
                                              # 'ارزش صف خرید بورس(میلیارد تومان)',
                                              # 'ارزش صف فروش بورس(میلیارد تومان)' ,
                                              # 'ارزش خرید حقیقی بورس (میلیارد تومان)',
                                              # 'ارزش فروش حقیقی بورس (میلیارد تومان)',
                                              # 'ارزش خرید حقوقی بورس (میلیارد تومان)',
                                              # 'ارزش فروش حقوقی بورس (میلیارد تومان)',
                                              'برایند اختلاف سرانه حقیقی بورس (میلیون تومان)',
                                              'برایند اختلاف سرانه حقوقی بورس (میلیون تومان)',
                                              # 'تعداد معاملات بورس (میلیون)' ,
                                              # 'حجم معاملات بورس (میلیارد)',
                                              # 'تعداد خریدار حقیقی بورس(هزار)',
                                              # 'تعداد فروشنده حقیقی بورس(هزار)',
                                              # 'تعداد خریدار حقوقی بورس(هزار)',
                                              # 'تعداد فروشنده حقوقی بورس(هزار)',
                                              # 'تعداد سهام پایانی مثبت بورس',
                                              'ارزش فرابورس (میلیارد تومان)',
                                              # 'ارزش صف خرید فرابورس(میلیارد تومان)',
                                              # 'ارزش صف فروش فرابورس(میلیارد تومان)',
                                              # 'ارزش خرید حقیقی فرابورس (میلیارد تومان)',
                                              # 'ارزش فروش حقیقی فرابورس (میلیارد تومان)',
                                              # 'ارزش خرید حقوقی فرابورس (میلیارد تومان)',
                                              # 'ارزش فروش حقوقی فرابورس (میلیارد تومان)',
                                              'برایند اختلاف سرانه حقیقی فرابورس (میلیون تومان)',
                                              'برایند اختلاف سرانه حقوقی فرابورس (میلیون تومان)',
                                              # 'تعداد معاملات فرابورس (میلیون)',
                                              # 'حجم معاملات فرابورس (میلیارد)',
                                              # 'تعداد خریدار حقیقی فرابورس(هزار)',
                                              # 'تعداد فروشنده حقیقی فرابورس(هزار)',
                                              # 'تعداد خریدار حقوقی فرابورس(هزار)',
                                              # 'تعداد فروشنده حقوقی فرابورس(هزار)',
                                              # 'تعداد سهام پایانی مثبت فرابورس',
                                              'ارزش کل بازار',
                                              # 'ارزش صف خرید بازار',
                                              # 'ارزش صف فروش بازار',
                                              # 'خرید کل حقیقی',
                                              # 'فروش کل حقیقی',
                                              # 'خرید کل حقوقی',
                                              # 'فروش کل حقوقی',
                                              'ورود/خروج نقدینگی',
                                              'برایند اختلاف سرانه حقیقی',
                                              'برایند اختلاف سرانه حقوقی',
                                              'تاریخ'])

        import os
        script_path = os.getcwd()
        try:os.mkdir(script_path+r'\result')
        except:pass
        df.to_excel(script_path + r'\result\KALAGH.xlsx', index=False, header=True)
        print(' اطلاعات ذخیره شد')
        os.startfile(script_path + r'\result\KALAGH.xlsx')
        # try:
        #     df.to_excel(script_path + r'\result\KALAGH.xlsx', index=False, header=True)
        #     print(' اطلاعات ذخیره شد')
        #     os.startfile(script_path + r'\result\KALAGH.xlsx')
        # except:
        #     print(' فایل اکسل باز است. اطلاعات ذخیره نشد')
    def save_sorted_data(self,data,filename):
        column=[]
        for key in data:
            column.append(key)
        #df = pd.DataFrame(self.data, columns=['ورود/خروج نقدینگی حقیقی بورس(میلیون تومان)','ورود/خروج نقدینگی حقیقی فرابورس(میلیون تومان)','ورود/خروج نقدینگی حقوقی بورس(میلیون تومان)' ,'ورود/خروج نقدینگی حقوقی فرابورس(میلیون تومان)','تاریخ'])
        df = pd.DataFrame(data, columns=column)

        import os
        script_path = os.getcwd()
        try:os.mkdir(script_path+r'\result')
        except:pass
        try:
            df.to_excel(script_path + '\\result\\' + filename + '.xlsx', index=False, header=True)
            print(' اطلاعات ذخیره شد')
            os.startfile(script_path + '\\result\\' + filename + '.xlsx')
        except:
            print(' فایل اکسل باز است. اطلاعات ذخیره نشد')
    def save_all_data_to_exel2(self):
        db = DB.DB('127.0.0.1', 'root', '', 'tsetmc_db')
        caculator = CALCULATOR.CAL()
        data = db.getdata(dict(
            tsetmc=['ID', 'bou_tval_B', 'lbuy_tval_bou_B', 'lsell_tval_bou_B', 'i_buy_tval_bou_B', 'i_sell_tval_bou_B',
                    'n_buy_tval_bou_B', 'n_sell_tval_bou_B', 'i_findow_bou_M', 'n_findow_bou_M', 'bou_tno_M',
                    'bou_tvol_B', 'i_buy_count_bou_K', 'i_sell_count_bou_K', 'n_buy_count_bou_K', 'n_sell_count_bou_K',
                    'namad_positive_bou_count', 'fbou_tval_B', 'lbuy_tval_fbou_B', 'lsell_tval_fbou_B',
                    'i_buy_tval_fbou_B', 'i_sell_tval_fbou_B', 'n_buy_tval_fbou_B', 'n_sell_tval_fbou_B',
                    'i_findow_fbou_M', 'n_findow_fbou_M', 'fbou_tno_M', 'fbou_tvol_B', 'i_buy_count_fbou_K',
                    'i_sell_count_fbou_K', 'n_buy_count_fbou_K', 'n_sell_count_fbou_K', 'namad_positive_fbou_count',
                    'date']))
        data = caculator.TSE_CAL(data)
        print(data)
        self.data = data
        self.data['ارزش  بورس (میلیارد تومان)'] = self.data.pop('bou_tval_B')
        self.data['ارزش فرابورس (میلیارد تومان)'] = self.data.pop('fbou_tval_B')

        self.data['ارزش فروش حقیقی فرابورس (میلیارد تومان)'] = self.data.pop('i_sell_tval_fbou_B')
        self.data['ارزش خرید حقیقی فرابورس (میلیارد تومان)'] = self.data.pop('i_buy_tval_fbou_B')
        self.data['ارزش فروش حقوقی فرابورس (میلیارد تومان)'] = self.data.pop('n_sell_tval_fbou_B')
        self.data['ارزش خرید حقوقی فرابورس (میلیارد تومان)'] = self.data.pop('n_buy_tval_fbou_B')

        self.data['ارزش فروش حقیقی بورس (میلیارد تومان)'] = self.data.pop('i_sell_tval_bou_B')
        self.data['ارزش خرید حقیقی بورس (میلیارد تومان)'] = self.data.pop('i_buy_tval_bou_B')
        self.data['ارزش فروش حقوقی بورس (میلیارد تومان)'] = self.data.pop('n_sell_tval_bou_B')
        self.data['ارزش خرید حقوقی بورس (میلیارد تومان)'] = self.data.pop('n_buy_tval_bou_B')

        self.data['برایند اختلاف سرانه حقیقی بورس (میلیون تومان)'] = self.data.pop('i_findow_bou_M')
        self.data['برایند اختلاف سرانه حقوقی بورس (میلیون تومان)'] = self.data.pop('n_findow_bou_M')
        self.data['برایند اختلاف سرانه حقیقی فرابورس (میلیون تومان)'] = self.data.pop('i_findow_fbou_M')
        self.data['برایند اختلاف سرانه حقوقی فرابورس (میلیون تومان)'] = self.data.pop('n_findow_fbou_M')

        self.data['تعداد معاملات بورس (میلیون)'] = self.data.pop('bou_tno_M')
        self.data['تعداد معاملات فرابورس (میلیون)'] = self.data.pop('fbou_tno_M')

        self.data['حجم معاملات بورس (میلیارد)'] = self.data.pop('bou_tvol_B')
        self.data['حجم معاملات فرابورس (میلیارد)'] = self.data.pop('fbou_tvol_B')

        self.data['تعداد خریدار حقوقی فرابورس(هزار)'] = self.data.pop('n_buy_count_fbou_K')
        self.data['تعداد خریدار حقیقی فرابورس(هزار)'] = self.data.pop('i_buy_count_fbou_K')
        self.data['تعداد فروشنده حقیقی فرابورس(هزار)'] = self.data.pop('i_sell_count_fbou_K')
        self.data['تعداد فروشنده حقوقی فرابورس(هزار)'] = self.data.pop('n_sell_count_fbou_K')

        self.data['تعداد خریدار حقوقی بورس(هزار)'] = self.data.pop('n_buy_count_bou_K')
        self.data['تعداد خریدار حقیقی بورس(هزار)'] = self.data.pop('i_buy_count_bou_K')
        self.data['تعداد فروشنده حقیقی بورس(هزار)'] = self.data.pop('i_sell_count_bou_K')
        self.data['تعداد فروشنده حقوقی بورس(هزار)'] = self.data.pop('n_sell_count_bou_K')

        self.data['ارزش صف خرید فرابورس(میلیارد تومان)'] = self.data.pop('lbuy_tval_fbou_B')
        self.data['ارزش صف فروش فرابورس(میلیارد تومان)'] = self.data.pop('lsell_tval_fbou_B')

        self.data['ارزش صف خرید بورس(میلیارد تومان)'] = self.data.pop('lbuy_tval_bou_B')
        self.data['ارزش صف فروش بورس(میلیارد تومان)'] = self.data.pop('lsell_tval_bou_B')

        self.data['تعداد سهام پایانی مثبت بورس'] = self.data.pop('namad_positive_bou_count')
        self.data['تعداد سهام پایانی مثبت فرابورس'] = self.data.pop('namad_positive_fbou_count')

        self.data['تاریخ'] = self.data.pop('date')
        self.data['ID'] = self.data.pop('ID')
        print(data)
        import xlsxwriter
        import os
        script_path = os.getcwd()
        try:
            os.mkdir(script_path + r'\result')
        except:
            pass
        try:
            workbook = xlsxwriter.Workbook('KALAGH.xlsx')
            print(' اطلاعات ذخیره شد')
            os.startfile(script_path + r'\result\KALAGH.xlsx')
        except:
            print(' فایل اکسل باز است. اطلاعات ذخیره نشد')

        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'ID')
        worksheet.write('B1', 'ارزش  بورس (میلیارد تومان)')
        worksheet.write('C1', 'ارزش صف خرید بورس(میلیارد تومان)')
        worksheet.write('D1', 'ارزش صف فروش بورس(میلیارد تومان)')
        worksheet.write('E1', 'اارزش خرید حقیقی بورس (میلیارد تومان)')
        worksheet.write('F1', 'ارزش فروش حقیقی بورس (میلیارد تومان)')
        worksheet.write('G1', 'ارزش خرید حقوقی بورس (میلیارد تومان)')
        worksheet.write('H1', 'ارزش فروش حقوقی بورس (میلیارد تومان)')
        worksheet.write('I1', 'برایند اختلاف سرانه حقیقی بورس (میلیون تومان)')
        worksheet.write('J1', 'برایند اختلاف سرانه حقوقی بورس (میلیون تومان)')
        worksheet.write('K1', 'تعداد معاملات بورس (میلیون)')
        worksheet.write('L1', 'حجم معاملات بورس (میلیارد)')
        worksheet.write('M1', 'تعداد خریدار حقیقی بورس(هزار)')
        worksheet.write('N1',  'تعداد فروشنده حقیقی بورس(هزار)')
        worksheet.write('O1', 'تعداد خریدار حقوقی بورس(هزار)')
        worksheet.write('P1', 'تعداد فروشنده حقوقی بورس(هزار)')
        worksheet.write('Q1', 'تعداد سهام پایانی مثبت بورس')
        worksheet.write('R1',  'ارزش فرابورس (میلیارد تومان)')
        worksheet.write('S1', 'ارزش صف خرید فرابورس(میلیارد تومان)')
        worksheet.write('T1',  'ارزش صف فروش فرابورس(میلیارد تومان)')
        worksheet.write('U1',  'ارزش خرید حقیقی فرابورس (میلیارد تومان)')
        worksheet.write('V1',   'ارزش فروش حقیقی فرابورس (میلیارد تومان)')
        worksheet.write('W1', 'ارزش خرید حقوقی فرابورس (میلیارد تومان)')
        worksheet.write('X1', 'ارزش فروش حقوقی فرابورس (میلیارد تومان)')
        worksheet.write('Y1', 'برایند اختلاف سرانه حقیقی فرابورس (میلیون تومان)')
        worksheet.write('Z1', 'برایند اختلاف سرانه حقوقی فرابورس (میلیون تومان)')
        worksheet.write('AA1', 'تعداد معاملات فرابورس (میلیون)')
        worksheet.write('AB1', 'حجم معاملات فرابورس (میلیارد)')
        worksheet.write('AC1',   'تعداد خریدار حقیقی فرابورس(هزار)')
        worksheet.write('AD1', 'تعداد فروشنده حقیقی فرابورس(هزار)')
        worksheet.write('AE1', 'تعداد خریدار حقوقی فرابورس(هزار)')
        worksheet.write('AF1',  'تعداد فروشنده حقوقی فرابورس(هزار)')
        worksheet.write('AG1',  'تعداد سهام پایانی مثبت فرابورس')
        worksheet.write('AH1',  'ارزش کل بازار')
        worksheet.write('AI1', 'ارزش صف خرید بازار')
        worksheet.write('AJ1', 'ارزش صف فروش بازار')
        worksheet.write('AK1', 'خرید کل حقیقی')
        worksheet.write('AL1',  'فروش کل حقیقی')
        worksheet.write('AM1',  'خرید کل حقوقی')
        worksheet.write('AN1',  'فروش کل حقوقی')
        worksheet.write('AO1',  'ورود/خروج نقدینگی')
        worksheet.write('AP1',  'برایند اختلاف سرانه حقیقی')
        worksheet.write('AQ1', 'برایند اختلاف سرانه حقوقی')
        worksheet.write('AR1', 'تاریخ')
        cl=1
        for header in data:
            cl=10
            for i in range(0, len(data[header])):
                worksheet.write(i+1, cl, data[header][i])
            cl = cl + 1
        workbook.close()



