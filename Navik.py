# import timeit
import time
from decimal import Decimal
import sys


def Beep(frequency,duration):
    import winsound
    winsound.Beep(frequency, duration)
def delta(data0,data1,namad,op):
    f=0
    i=0
    try:
        i=Decimal(data0[namad][op])
        f=Decimal(data1[namad][op])
    except:pass
    return f-i;
def NAVIK(time_delay):
    import EXT
    import NAMADMANAGER
    namad_manager = NAMADMANAGER.NAMADMANAGER()
    namad_list = [namad_manager.convert_namad_to_id('خصدرا')]
    id1=namad_manager.convert_namad_to_id('حفارس');
    id2=namad_manager.convert_namad_to_id('خبهمن')
    ext_motor = EXT.EXTRACTION('http://www.tsetmc.com/Loader.aspx?ParTree=15131F',
                               'true==function(){(cfield1)=(ct).Buy_CountI;(cfield0)=(tval);if (1 == 1){return true;}else {return false;}}()',
                               ['Value', 'No.Buy'])  # ,'date'])
    ext_motor.dosettingforextraction()
    # dot='.'
    while (1 == 1):
        data0 = ext_motor.extractdata(namad_list)
        time.sleep(time_delay)
        data1 = ext_motor.extractdata(namad_list)
        for namad in namad_list:
            delta_NoBuy = delta(data0, data1, namad, 'No.Buy')
            delta_Value = delta(data0, data1, namad, 'Value')
            if (delta_NoBuy != 0):
                signal = delta_Value / delta_NoBuy
                signal = signal / 10000000000
                if (signal >= 0.1):
                    Beep(1000, 1000)
                    print(namad)
                    print('No.Buy :', delta_NoBuy)
                    print('Buy Value Average per person :',signal , ' B')
                    print('_______________________________________________________________________________')

NAVIK(3)