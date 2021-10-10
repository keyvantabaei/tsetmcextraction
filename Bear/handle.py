def Beep(frequency,duration):
    import winsound
    winsound.Beep(frequency, duration)
def FindMax(listdic):
    from decimal import Decimal
    # print(len(listdic))
    maxdic={k:listdic[0][k] for k in listdic[0]}
    listdic.pop(0)
    for dic in listdic:
        for k in dic:
            try:
                if Decimal(dic[k]['lsell_tval']) >= Decimal(maxdic[k]['lsell_tval']):
                    maxdic[k] = dic[k]

            except:pass
    return maxdic
def convert_id_to_name(namad_ids_dic,id):
        result_name=0
        for nn in namad_ids_dic:
            if(namad_ids_dic[nn]==id):
                result_name=nn
        return result_name
def list_check(olddata,newdata,namad_id_dic):
    for oldkey in olddata.keys():
        if oldkey not in newdata.keys():
            print("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            print('\n', "نمادهای زیر از لیست صف های فروش خارج شدند :")
            # namads = {k: 0 for k in olddata.keys() if k not in newdata.keys()}
            # for key in namads:
            Beep(1000, 1000)
            print(convert_id_to_name(namad_id_dic, oldkey), '>>>>>     ')
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

    # if (len(olddata.keys()) > int(len(newdata.keys()))):
    #     # print(olddata_lenght,'   ', int(len(data.keys())))

def Bear(p):
    import sys
    import timeit
    from decimal import Decimal
    import EXT
    print('\nConnecting to TSETMC ...')
    ext_motor = EXT.EXTRACTION('http://www.tsetmc.com/Loader.aspx?ParTree=15131F',
                             '(cfield1)=(ct).Buy_CountI;(cfield0)=(qo1)*(pmin)/10000000000;(cfield0)>2&&(cfield0)<30&&(po1)==(tmin) && (qo1)!=0',
                               ['lsell_tval'])
    print('Settings are being done ...')
    ext_motor.dosettingforextraction()
    namad_id_dic = {}
    import xml.etree.ElementTree as ET
    tree = ET.parse('namd_name_ids.xml')
    root = tree.getroot()
    for child in root:
        namad_id_dic[child.attrib.get('name')] = 'tb_'+child.attrib.get('id')
    olddatalist=[]
    run_time=0
    i=0
    cdata=10
    while (len(olddatalist) < cdata):
        i=i+1
        olddatalist.append(ext_motor.extractalldata_Bear())
        sys.stdout.write("\rCollecting data [%d" % i + "] ...")
        sys.stdout.flush()
    print('  Completed .\n')
    # last_icount_data = {k: 0 for k in olddatalist[cdata-1]}
    min=100
    detected_namad={}
    olddata={}
    maxdata={}
    while (1 == 1):
        start = timeit.default_timer()
        data=ext_motor.extractalldata_Bear()
        # list_check(olddata,data,namad_id_dic)
        olddatalist.append(data)
        maxdata.clear()
        maxdata=FindMax(olddatalist)
        shared_items = {k: data[k] for k in data if k in maxdata and Decimal(data[k]['lsell_tval']) <= Decimal(p) * Decimal(maxdata[k]['lsell_tval'])}
        ave={}
        if (len(shared_items) > 0):
            #####
            ext_motor.addCfield0('icount')
            data = ext_motor.extractalldata_Bear()
            # print('\n', data)
            last_icount_data = {k: Decimal(data[k]['icount']) for k in data}
            data = ext_motor.extractalldata_Bear()
            # maxdata.clear()
            # maxdata = FindMax(olddatalist)
            #####
            for key in shared_items:
                try:
                    a = Decimal(maxdata[key]['lsell_tval']) - Decimal(data[key]['lsell_tval'])
                    # print('data icoount : ',Decimal(data[key]['icount']),'  olddata icount :  ',last_icount_data[key])
                    b = Decimal(data[key]['icount']) - last_icount_data[key]
                    ave[key] = a / b
                except:
                    ave[key] = 0
            for id in shared_items:
                for nn in namad_id_dic:
                    if (namad_id_dic[nn] == id):
                        if (id in detected_namad.keys() and detected_namad[id] > 0):
                            pass
                        else:
                            Beep(1500,1000)
                            ID = id.replace("tb_", "")
                            import webbrowser
                            webbrowser.open('http://www.tsetmc.com/Loader.aspx?ParTree=151311&i=' + ID, new=2)
                            print('\n', nn, ' : نماد', )
                            import datetime
                            print(ave[id], ': (میلیون تومان) خرید به ازای هر کد حقیقی ',
                                  '                 Time :        ', datetime.datetime.now(), '\n',
                                  '********************')
                            detected_namad[id] = cdata
            ext_motor.subtrac_cfield('icount')
        # last_icount_data.clear()
        # try:        last_icount_data={k:Decimal(data[k]['icount']) for k in data}
        # except:pass
        stop = timeit.default_timer()
        ex_time=round(stop - start,2)
        run_time+=ex_time/60
        if ex_time<min:min=ex_time
        sys.stdout.write("\rExtracting Time: %f" % ex_time + " Sec" +  '        Namad NO.: %f' % int(len(data.keys())) + '        Runining Time: '+ str(round(run_time,2)) +' Min' )
        sys.stdout.flush()
        if(ex_time>9.5*min):
            import os,sys
            print('\n\n >> Application restarted .\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            os.system("python handle.py")
            sys.exit()
        for key in detected_namad:
            if(detected_namad[key]>0):
                detected_namad[key]=detected_namad[key]-1
        olddata=data
Bear(0.7)












