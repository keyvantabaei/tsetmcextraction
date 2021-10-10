class NAMADMANAGER:
    def __init__(self):
        print('namad-manager is activated ...')
        self.fa_en_dic={
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
        self.sanat_list=sanat_list=[
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
        self.namad_ids_dic = self.read_namad_ids()
        self.columns_list=['ID','rsi14','macd_minus_signal','momentum14','bollinger_bands','pc','i_saraneh_M','n_saraneh_M','date']
        print('columns ',self.columns_list, ' has set ...')
    def createnamadtales(self):
        import DB
        db=DB.DB('127.0.0.1','root', '', 'tsetmc_db')
        self.namad_ids_dic=self.read_namad_ids_for_inserting()
        for namad_name in self.namad_ids_dic:
            table_name='tb_'+self.namad_ids_dic[namad_name]
            table_columns_dic= {table_name:self.columns_list}
            db.addtable(table_columns_dic)
        print('namad tables has created ...')
    def deletetables(self):
        import DB
        db = DB.DB('127.0.0.1', 'root', '', 'tsetmc_db')
        for namad_name in self.namad_ids_dic:
            table_name = 'tb_' + self.namad_ids_dic[namad_name]
            db.deletetable([table_name,])
        print('namad tables has deleted ...')
    def read_namad_ids(self):
        # import EXT
        # ext_motor= EXT.EXTRACTION('http://www.tsetmc.com/Loader.aspx?ParTree=15131F','',[])
        # ext_motor.saveidstoxml(0,0)
        result_dic={}
        import xml.etree.ElementTree as ET
        tree = ET.parse('namd_name_ids.xml')
        root = tree.getroot()
        for child in root:
            result_dic[child.attrib.get('name')] = child.attrib.get('id')
        print('name and ids has been read : ',result_dic)
        return result_dic
    def delete_a_table_by_name(self,name):
        table_id='tb_'+self.convert_namad_to_id(name)
        import DB
        db = DB.DB('127.0.0.1', 'root', '', 'tsetmc_db')
        db.deletetable([table_id,])
        print('table : ',name,' has been deleted by name :',name)
    def delete_a_table_by_id(self,id):
        table_id='tb_'+id
        import DB
        db = DB.DB('127.0.0.1', 'root', '', 'tsetmc_db')
        db.deletetable([table_id,])
        print('table : ',self.convert_id_to_name(id),' has been deleted by id :',id)
    def add_a_table_by_name(self,name):
        table_id='tb_'+self.convert_namad_to_id(name)
        import DB
        db = DB.DB('127.0.0.1', 'root', '', 'tsetmc_db')
        db.addtable({table_id:self.columns_list})
        print('table : ',name,' has been added by name',name)
    def add_a_table_by_id(self,id):
        table_id='tb_'+id
        import DB
        db = DB.DB('127.0.0.1', 'root', '', 'tsetmc_db')
        db.addtable({table_id:self.columns_list})
        print('table : ',self.convert_id_to_name(id),' has been added by id : ',id)
    def convert_namad_to_id(self,namad_name):
        result_id=0
        for nn in self.namad_ids_dic:
            if(nn==namad_name):
                result_id=self.namad_ids_dic[nn]
        print('name :',namad_name,' successfully converted to :',result_id)
        return result_id
    def convert_id_to_name(self,id):
        result_name=0
        for nn in self.namad_ids_dic:
            if(self.namad_ids_dic[nn]==id):
                result_name=nn
        print('id :',id,' successfully converted to :',result_name)
        return result_name
    def update_tables(self):
        import EXT
        ext_motor= EXT.EXTRACTION('http://www.tsetmc.com/Loader.aspx?ParTree=15131F','',[])
        ext_motor.saveidstoxml(0,1)
        result_dic={}
        import xml.etree.ElementTree as ET
        tree = ET.parse('namd_name_ids.xml')
        root = tree.getroot()
        print('namad and its id has been saved into namad_name_ids.xml at application path ...')
        for child in root:
            result_dic[child.attrib.get('name')] = child.attrib.get('id')
        self.createnamadtales()
        print('name and ids has been updated : ',result_dic)
    def savetoexel(self,file_name,namad):
        import xml.etree.cElementTree as ET
        import os
        script_path = os.getcwd()
        try:
            os.mkdir(script_path + r'\Groups')
        except:
            pass
        id_name_dic = {}
        id_list = []
        try:
            tree = ET.parse(script_path + r'\Groups' + '\\' + file_name + ".xml")
            root = tree.getroot()
            for child in root:
                id_name_dic[child.attrib.get('id')] = child.attrib.get('name')
                id_list.append(child.attrib.get('id'))
        except:
            pass

        root = ET.Element("root")
        for _target in namad:
            try:
                name = _target.find_element_by_css_selector('a.inst').text
                ID = _target.get_attribute('id')
                if ID in id_list:
                    pass
                else:
                    id_name_dic[ID] = name
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
        for _ID in id_name_dic:
            doc = ET.SubElement(root, "namad", name=id_name_dic[_ID], id=_ID)
            # ET.SubElement(doc,'id',id=_target.get_attribute('id'))
        tree = ET.ElementTree(root)
        tree.write(script_path + r'\Groups' + '\\' + file_name + ".xml")
    def update_group(self):
        value_list=['01','02','10','11','13','14','15','17','19','20','21','22','23','24','25','26','27','28','29','31','32','33','34','35','36','38','39','40','41','42','43','44','45','46','47','49','50','51','52','53','54','55','56','57','58','59','60','61','63','64','65','66','67','68','69','70','71','72','73','74','76','77','82',
                    90,'93','98']
        import EXT
        ext_motor = EXT.EXTRACTION('http://www.tsetmc.com/Loader.aspx?ParTree=15131F', '', [])
        for value in value_list:
            data=ext_motor.saveidstoxml(1,value)
            self.savetoexel(data[0],data[1])
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
        print(res)
    def read_namad_ids_for_inserting(self):
        import EXT
        ext_motor= EXT.EXTRACTION('http://www.tsetmc.com/Loader.aspx?ParTree=15131F','',[])
        ext_motor.saveidstoxml(0,0)
        result_dic={}
        import xml.etree.ElementTree as ET
        tree = ET.parse('namd_name_ids.xml')
        root = tree.getroot()
        for child in root:
            result_dic[child.attrib.get('name')] = child.attrib.get('id')
        print('name and ids has been read : ',result_dic)
        return result_dic

