from selenium import webdriver
from selenium.webdriver.firefox.options import  Options
class EXTRACTION:
    def __init__(self,URL,QUERY,COLUMNS):
        self.url=URL
        self.fa_en_dic = fa_dic = {
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
        option=Options()
        option.add_argument('-headless')
        self.driver=webdriver.Firefox(firefox_options=option)
        # self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.get(self.url)
        self.query=QUERY
        self.is_closed=True
        self.columns=COLUMNS
        self.namad_id_dic={
' وهنر '    :    ' 60783654574662426 ',
' رمپنا '    :    ' 67126881188552864 ',
' رنيك '    :    ' 33854964748757477 ',
' رتكو '    :    ' 3823243780502959 ',
' تابا '    :    ' 51459202425114449 ',
' هاي وب '    :    ' 43362635835198978 ',
' اوان '    :    ' 69847139870135237 ',
' رافزا '    :    ' 68941822863885255 ',
' مرقام '    :    ' 23838634016123354 ',
' رتاپ '    :    ' 41048299027409941 ',
' رانفور '    :    ' 40505767672724777 ',
' سپ '    :    ' 71856634742001725 ',
' آپ '    :    ' 55254206302462116 ',
' ركيش '    :    ' 27952969918967492 ',
' تاپكيش '    :    ' 50002340308486819 ',
' پرداخت '    :    ' 59607545337891226 ',
' مفاخر '    :    ' 4247709727327181 ',
' سيستم '    :    ' 47749661205825616 ',
' افرا '    :    ' 52792903131341205 ',
' فن آوا '    :    ' 55201604487356053 ',
' مداران '    :    ' 65999092673039059 ',
' خبازرس '    :    ' 19310456400689867 ',
' ثاخت '    :    ' 17800036702302776 ',
' ثتران '    :    ' 20926459161497908 ',
' ثفارس '    :    ' 30852391633490755 ',
' وساخت '    :    ' 25514780181345713 ',
' ثنوسا '    :    ' 32845891587040106 ',
' كيسون '    :    ' 49953653111442595 ',
' ثغرب '    :    ' 17939384202383793 ',
' ثپرديس '    :    ' 53999651992586159 ',
' ثمسكن '    :    ' 3863538898378476 ',
' ثامان '    :    ' 66456062140680461 ',
' ثباغ '    :    ' 68909035712962732 ',
' ثنور '    :    ' 63315013743060811 ',
' آ س پ '    :    ' 17617474823279712 ',
' وآذر '    :    ' 1358190916156744 ',
' ثاباد '    :    ' 59612098290740355 ',
' ثرود '    :    ' 18883380772506226 ',
' كرمان '    :    ' 50792786683910016 ',
' ثجوان '    :    ' 30507152381699953 ',
' ثشرق '    :    ' 6043384171800349 ',
' ثنظام '    :    ' 45066064863062755 ',
' وثخوز '    :    ' 40043919653526083 ',
' ثقزوي '    :    ' 12965822877128721 ',
' ثشاهد '    :    ' 63481599728522324 ',
' ثعمرا '    :    ' 15726796686853780 ',
' وتوس '    :    ' 68117765376081366 ',
' ثتوسا '    :    ' 47702059190622416 ',
' ثنام '    :    ' 831325835570803 ',
' ثاصفا '    :    ' 7503669593172728 ',
' ثاژن '    :    ' 40650252484299134 ',
' ثعتما '    :    ' 64707090254488560 ',
' ثزاگرس '    :    ' 28854105556435129 ',
' ثباغ2 '    :    ' 36817024791726552 ',
' تملت '    :    ' 11129387075131725 ',
' فرابورس '    :    ' 58741071099161284 ',
' لوتوس '    :    ' 59142194115401696 ',
' بورس '    :    ' 60523145697836739 ',
' كالا '    :    ' 44549439964296944 ',
' اميد '    :    ' 18599703143458101 ',
' كبورس '    :    ' 37366608481858080 ',
' اكالا '    :    ' 49869693814643443 ',
' نبورس '    :    ' 60095061789823130 ',
' تكالا '    :    ' 67612261115225625 ',
' ميهن '    :    ' 26543014712914772 ',
' ملت '    :    ' 13611044044646901 ',
' آسيا '    :    ' 51106317433079213 ',
' پارسيان '    :    ' 9481703061634967 ',
' اتكام '    :    ' 46772701938567445 ',
' دانا '    :    ' 48511238766369097 ',
' البرز '    :    ' 70270965300262393 ',
' وحكمت '    :    ' 12777578088653944 ',
' ما '    :    ' 29860265627578401 ',
' وسرمد '    :    ' 43291783149314349 ',
' اتكاي '    :    ' 39751275523025334 ',
' بپاس '    :    ' 51971068201094874 ',
' وحافظ '    :    ' 5128151910501174 ',
' نوين '    :    ' 59866041653103343 ',
' وسين '    :    ' 56591881518499520 ',
' بنو '    :    ' 37114514127305200 ',
' آرمان '    :    ' 38738476064699383 ',
' واحيا '    :    ' 17284166795866794 ',
' ولشرق '    :    ' 31078457170311964 ',
' وثنو '    :    ' 44986797317463049 ',
' ولانا '    :    ' 66830065858417081 ',
' وثوق '    :    ' 59839275647597021 ',
' وسنا '    :    ' 24662567615903665 ',
' وآتوس '    :    ' 17269972595370241 ',
' ومشان '    :    ' 35369183060321179 ',
' وارس '    :    ' 53686258677793038 ',
' همراه '    :    ' 68635710163497089 ',
' حخزر '    :    ' 28253678449273505 ',
' حاريا '    :    ' 56798822689379375 ',
' حكشتي '    :    ' 60610861509165508 ',
' حريل '    :    ' 5564768007356822 ',
' حفارس '    :    ' 35424116338766901 ',
' توريل '    :    ' 37389789764168256 ',
' حتوكا '    :    ' 22260326095996531 ',
' حآسا '    :    ' 44625249840480397 ',
' حسينا '    :    ' 1625149423498289 ',
' حپترو '    :    ' 16369313804633525 ',
' حپارسا '    :    ' 917857106093847 ',
' حرهشا '    :    ' 30443839313522574 ',
' حسير '    :    ' 13281937213456378 ',
' ولساپا '    :    ' 45174198424472334 ',
' ولپارس '    :    ' 48241092863917835 ',
' ولصنم '    :    ' 71744682148776880 ',
' وايران '    :    ' 3149396562827132 ',
' وليز '    :    ' 20946530370469828 ',
' ولبهمن '    :    ' 48287670503317419 ',
' ولملت '    :    ' 11403770140000603 ',
' ولغدر '    :    ' 23086515493897579 ',
' دي '    :    ' 44818950263583523 ',
' وملل '    :    ' 24644999329120295 ',
' وسينا '    :    ' 45050389997905274 ',
' سامان '    :    ' 38179358042686391 ',
' ونوين '    :    ' 47302318535715632 ',
' وپست '    :    ' 22087269603540841 ',
' وخاور '    :    ' 47333458678352378 ',
' وآيند '    :    ' 46830341954511303 ',
' سمايه '    :    ' 43913530989262989 ',
' وزمين '    :    ' 19954896371640204 ',
' سامان4 '    :    ' 30842146318343974 ',
' صبا '    :    ' 45392752356003555 ',
' وساپا '    :    ' 37614886280396031 ',
' وخارزم '    :    ' 7395271748414592 ',
' ومهان '    :    ' 58964593134314938 ',
' وصنعت '    :    ' 57309221039930244 ',
' وبيمه '    :    ' 11773403764702778 ',
' وسپه '    :    ' 2328862017676109 ',
' آريان '    :    ' 6506179926371994 ',
' وتوسم '    :    ' 17528249960294496 ',
' وپويا '    :    ' 24785665268004766 ',
' وسبحان '    :    ' 43283802997035462 ',
' وتوصا '    :    ' 2944500421562364 ',
' سرچشمه '    :    ' 35948133957468680 ',
' وآوا '    :    ' 22490169030401337 ',
' وبوعلي '    :    ' 28328710198554144 ',
' وسكاب '    :    ' 11258722998911897 ',
' پرديس '    :    ' 15039949673085566 ',
' وصنا '    :    ' 46982154647719707 ',
' واتي '    :    ' 33541897671561960 ',
' وبهمن '    :    ' 18063426072758458 ',
' وملت '    :    ' 10055255678920880 ',
' گوهران '    :    ' 65018804181564924 ',
' واعتبار '    :    ' 47841327496247362 ',
' وگستر '    :    ' 43951910415124966 ',
' وشمال '    :    ' 9761381741308262 ',
' اعتلا '    :    ' 36773155987365094 ',
' وجامي '    :    ' 57600064931636077 ',
' سدبير '    :    ' 64341992373049080 ',
' وكادو '    :    ' 56717416662584054 ',
' فلات '    :    ' 60633055620418060 ',
' معيار '    :    ' 50580753680043015 ',
' ونيكي '    :    ' 25336820825905643 ',
' وبرق '    :    ' 61298636307861167 ',
' سنوين '    :    ' 36995197800118822 ',
' سمگا '    :    ' 46741025610365786 ',
' گكوثر '    :    ' 66599109405217136 ',
' گشان '    :    ' 70391097626818082 ',
' گكيش '    :    ' 44665761767777759 ',
' كگاز '    :    ' 62346804681275278 ',
' كهمدا '    :    ' 67206358287598044 ',
' كسرا '    :    ' 4614779520007780 ',
' كقزوي '    :    ' 63499217872110599 ',
' كتوكا '    :    ' 65671173927025645 ',
' كاذر '    :    ' 49353447565507376 ',
' كمرجان '    :    ' 50633804639547462 ',
' كپشير '    :    ' 57639364758870873 ',
' سفاسي '    :    ' 34721884030854211 ',
' كساپا '    :    ' 28325731560106431 ',
' كخاك '    :    ' 16405556680571453 ',
' كمينا '    :    ' 54263829393913132 ',
' كسرام '    :    ' 20560887114747719 ',
' كفرآور '    :    ' 49627523909849331 ',
' كفرا '    :    ' 23837844039713715 ',
' سفارود '    :    ' 4686607974846832 ',
' سايرا '    :    ' 62558705479545830 ',
' سپرمي '    :    ' 27668158733246204 ',
' كابگن '    :    ' 10654052153538617 ',
' كايتا '    :    ' 45608932669358493 ',
' سبزوا '    :    ' 611986653700161 ',
' سشرق '    :    ' 26997316501080743 ',
' ستران '    :    ' 30829203706095076 ',
' سپاها '    :    ' 35669480110084448 ',
' سصوفي '    :    ' 13227300125161435 ',
' سخوز '    :    ' 41974758296041288 ',
' ساوه '    :    ' 32347247706508046 ',
' سيدكو '    :    ' 37281199178613855 ',
' سمازن '    :    ' 33808206014018431 ',
' سدور '    :    ' 27218386411183410 ',
' ساروم '    :    ' 15949743338644220 ',
' سكرد '    :    ' 65321970913593427 ',
' سرود '    :    ' 11964419322927535 ',
' سجام '    :    ' 20034264486679145 ',
' سخاش '    :    ' 4470657233334072 ',
' سهگمت '    :    ' 41284516796232939 ',
' سبهان '    :    ' 32525655729432562 ',
' سكرما '    :    ' 15472396110662150 ',
' سفار '    :    ' 41227201752535311 ',
' سغرب '    :    ' 52220424531578944 ',
' سشمال '    :    ' 6757220448540984 ',
' سفارس '    :    ' 15521712617204216 ',
' سقاين '    :    ' 60654872678917533 ',
' سباقر '    :    ' 24807173016704795 ',
' سنير '    :    ' 14231831499205396 ',
' سيلام '    :    ' 14617104402836487 ',
' سفانو '    :    ' 4528607775462304 ',
' سهرمز '    :    ' 29747059672582491 ',
' سبجنو '    :    ' 66295665969375744 ',
' سدشت '    :    ' 27000326841257664 ',
' ساربيل '    :    ' 34890845654517313 ',
' سخواف '    :    ' 55959112038778737 ',
' ساروج '    :    ' 44802346787824971 ',
' سلار '    :    ' 61664227282090067 ',
' كحافظ '    :    ' 32257753560585502 ',
' كلوند '    :    ' 32678431934327184 ',
' كسعدي '    :    ' 29122854902865456 ',
' كترام '    :    ' 24085906177899789 ',
' كپارس '    :    ' 9698674686691945 ',
' كساوه '    :    ' 25001509088465005 ',
' كهرام '    :    ' 25631699615003698 ',
' افق '    :    ' 49502666250908008 ',
' بميلا '    :    ' 16553062355259729 ',
' بالاس '    :    ' 8646067353086740 ',
' خصدرا '    :    ' 2318736941376687 ',
' شگويا '    :    ' 5987841496184505 ',
' فارس '    :    ' 25244329144808274 ',
' تاپيكو '    :    ' 22560050433388046 ',
' شيران '    :    ' 35796086458096255 ',
' پارسان '    :    ' 23441366113375722 ',
' آريا '    :    ' 55127657985997520 ',
' شكلر '    :    ' 62177651435283872 ',
' نوري '    :    ' 19040514831923530 ',
' شاراك '    :    ' 7711282667602555 ',
' جم '    :    ' 32357363984168442 ',
' شلعاب '    :    ' 39116664428676213 ',
' زاگرس '    :    ' 13235547361447092 ',
' كلر '    :    ' 1822787329898392 ',
' شبصير '    :    ' 68517032834363488 ',
' شيراز '    :    ' 38568786927478796 ',
' شغدير '    :    ' 21607242972640064 ',
' شپديس '    :    ' 20562694899904339 ',
' شفارا '    :    ' 16673205196919832 ',
' پاكشو '    :    ' 62786156501584862 ',
' شوينده '    :    ' 3493306453706327 ',
' شفارس '    :    ' 43781018754867729 ',
' شفن '    :    ' 65122215875355555 ',
' كرماشا '    :    ' 38437201078089290 ',
' شپاكسا '    :    ' 11622051128546106 ',
' شپارس '    :    ' 61102694810476197 ',
' شپترو '    :    ' 71957984642204570 ',
' شسينا '    :    ' 30974710508383145 ',
' جم پيلن '    :    ' 27096851668435724 ',
' شگل '    :    ' 44153164692325703 ',
' خراسان '    :    ' 43552974795606067 ',
' شتوكا '    :    ' 38555056423456635 ',
' شجم '    :    ' 49244604018250364 ',
' قرن '    :    ' 39610074039667804 ',
' پترول '    :    ' 69143674941561637 ',
' شصفها '    :    ' 18346219759153870 ',
' شخارك '    :    ' 70934270174405743 ',
' شدوص '    :    ' 40611478183231802 ',
' شاملا '    :    ' 16959429956899455 ',
' شكربن '    :    ' 27308217070238237 ',
' ساينا '    :    ' 64298008532791199 ',
' شرنگي '    :    ' 40025799067544201 ',
' فسا '    :    ' 318005355896147 ',
' جهرم '    :    ' 49674915481184052 ',
' داراب '    :    ' 27299841173245405 ',
' شگامرن '    :    ' 1050751214677134 ',
' بركت '    :    ' 34557241988629814 ',
' دزهراوي '    :    ' 8915450910866216 ',
' والبر '    :    ' 57944184894703821 ',
' دسانكو '    :    ' 47348197320716810 ',
' داوه '    :    ' 5305844922895340 ',
' دكوثر '    :    ' 23353689102956991 ',
' ريشمك '    :    ' 6478064539164167 ',
' دبالك '    :    ' 71510396252618330 ',
' دتوليد '    :    ' 18093681647131179 ',
' دجابر '    :    ' 33406621820337161 ',
' درهآور '    :    ' 13243992182070788 ',
' دامين '    :    ' 50100062518826135 ',
' تيپيكو '    :    ' 29758477602878557 ',
' دكپسول '    :    ' 52382684379473036 ',
' دتماد '    :    ' 34641719089573667 ',
' درازك '    :    ' 22255783119783047 ',
' دفارا '    :    ' 56550776668133562 ',
' دعبيد '    :    ' 49054891736433700 ',
' ددام '    :    ' 66450490505950110 ',
' دابور '    :    ' 61332057061846617 ',
' دسبحان '    :    ' 5866848234665627 ',
' دشيمي '    :    ' 33603212156438463 ',
' دالبر '    :    ' 60451823714332895 ',
' پخش '    :    ' 12638840758449459 ',
' شفا '    :    ' 36899214178084525 ',
' دسينا '    :    ' 11432067920374603 ',
' داسوه '    :    ' 12387472624849835 ',
' دتوزيع '    :    ' 66726992874614788 ',
' كاسپين '    :    ' 28431095903407567 ',
' وپخش '    :    ' 7183333492448248 ',
' دكيمي '    :    ' 20024911381434086 ',
' كي بي سي '    :    ' 62977319271289925 ',
' دارو '    :    ' 67988012428906654 ',
' هجرت '    :    ' 5317427172344706 ',
' دلر '    :    ' 4384288570322406 ',
' دپارس '    :    ' 70474983732269112 ',
' دروز '    :    ' 40262275031537922 ',
' دحاوي '    :    ' 43374709930371268 ',
' دفرا '    :    ' 18303237082155264 ',
' دقاضي '    :    ' 64289770858657141 ',
' دلقما '    :    ' 29247915161590165 ',
' دشيري '    :    ' 63084741752814852 ',
' شتهران '    :    ' 31049085025064185 ',
' غگل '    :    ' 22299894048845903 ',
' غسالم '    :    ' 28672095850798501 ',
' غپينو '    :    ' 18401147983387689 ',
' غشهداب '    :    ' 33611155027418901 ',
' غگيلا '    :    ' 57300230097485720 ',
' تبرك '    :    ' 53204330224889981 ',
' غنوش '    :    ' 48619517949257749 ',
' غمارگ '    :    ' 52975109254504632 ',
' غشهد '    :    ' 20487994977117557 ',
' غپاك '    :    ' 34032872653290886 ',
' غالبر '    :    ' 24303422207378456 ',
' وبشهر '    :    ' 13937270451301973 ',
' غشان '    :    ' 31791737198597563 ',
' غچين '    :    ' 44850033148208596 ',
' غمينو '    :    ' 5516102131364383 ',
' غديس '    :    ' 3492952121304423 ',
' غبشهر '    :    ' 42387718866026650 ',
' غشاذر '    :    ' 59921975187856916 ',
' غويتا '    :    ' 37842793167868642 ',
' غپونه '    :    ' 33736447482634583 ',
' بهپاك '    :    ' 12746730665870442 ',
' خودكفا '    :    ' 22956708386610464 ',
' غگلستا '    :    ' 64843936383937546 ',
' غبهنوش '    :    ' 17059960254855208 ',
' غبهار '    :    ' 71666521540545716 ',
' غشصفا '    :    ' 61506294208022391 ',
' غصينو '    :    ' 31316784129157162 ',
' غپآذر '    :    ' 45518744711972166 ',
' غدام '    :    ' 2254054929817435 ',
' غگلپا '    :    ' 14312030900097668 ',
' غمهرا '    :    ' 6131290133202745 ',
' غشوكو '    :    ' 51294484197536070 ',
' غنيلي '    :    ' 21426277483799140 ',
' غدشت '    :    ' 2434703913394836 ',
' غگز '    :    ' 57551382352708199 ',
' بجهرم '    :    ' 33629260529503413 ',
' دماوند '    :    ' 66142616039907394 ',
' بكهنوج '    :    ' 7628308021169118 ',
' وهور '    :    ' 25215182208950217 ',
' مبين '    :    ' 27922860956133067 ',
' بفجر '    :    ' 46178280540110577 ',
' گواهي ظرفيت '    :    ' 16559249748626171 ',
' شستا '    :    ' 2400322364771558 ',
' وغدير '    :    ' 26014913469567886 ',
' وبانك '    :    ' 48010225447410247 ',
' واميد '    :    ' 52232388263291380 ',
' قثابت '    :    ' 44967158778304588 ',
' قشكر '    :    ' 35964395659427029 ',
' قهكمت '    :    ' 14398278072324784 ',
' قلرست '    :    ' 56820995669577571 ',
' قزوين '    :    ' 15259343650667588 ',
' قمرو '    :    ' 43342306308122676 ',
' قجام '    :    ' 28230238564334914 ',
' قچار '    :    ' 23600798892801694 ',
' قشهد '    :    ' 37631109616997982 ',
' قنيشا '    :    ' 63380098535169030 ',
' قپيرا '    :    ' 67030488744129337 ',
' قصفها '    :    ' 40411537531154482 ',
' قنقش '    :    ' 3050342257199174 ',
' قاروم '    :    ' 10831074117626896 ',
' خگستر '    :    ' 48990026850202503 ',
' خزاميا '    :    ' 2589887561569709 ',
' خمحركه '    :    ' 39436183727126211 ',
' خپارس '    :    ' 42354736493447489 ',
' ختوقا '    :    ' 70289374539527245 ',
' ورنا '    :    ' 7385624172574740 ',
' خريخت '    :    ' 12752224677923341 ',
' خوساز '    :    ' 31879190587976736 ',
' خشرق '    :    ' 63915926161403347 ',
' خفنر '    :    ' 28033133021443774 ',
' خاهن '    :    ' 7483280423474368 ',
' ختراك '    :    ' 22903901709044823 ',
' ختور '    :    ' 50185721305191887 ',
' خكمك '    :    ' 19257295292088310 ',
' خزر '    :    ' 32821908911812078 ',
' خديزل '    :    ' 38084304113529336 ',
' خكاوه '    :    ' 64842837716888827 ',
' خموتور '    :    ' 57273529732791251 ',
' خنصير '    :    ' 17834623106317041 ',
' خمحور '    :    ' 7457232989848872 ',
' تشتاد '    :    ' 66127247173352975 ',
' خچرخش '    :    ' 33783140337377394 ',
' خفناور '    :    ' 58180284328186631 ',
' خپويش '    :    ' 4758266259250794 ',
' خعمرا '    :    ' 6433335428452486 ',
' خليبل '    :    ' 50117925085549635 ',
' لكما '    :    ' 45641540066710190 ',
' لپيام '    :    ' 793710053482057 ',
' بترانس '    :    ' 46752599569017089 ',
' بموتو '    :    ' 22086876724551482 ',
' بالبر '    :    ' 62952165421099192 ',
' بنيرو '    :    ' 20453828618330936 ',
' بسويچ '    :    ' 47377315952751604 ',
' بشهاب '    :    ' 69454539056549106 ',
' نيرو '    :    ' 39481233087768672 ',
' بكاب '    :    ' 70219663893822560 ',
' بايكا '    :    ' 23891830829322971 ',
' بتك '    :    ' 54369290104873523 ',
' تكمبا '    :    ' 30719054967088301 ',
' تايرا '    :    ' 19298748452450329 ',
' لابسا '    :    ' 63363116407864462 ',
' تپمپي '    :    ' 43062880954780884 ',
' لسرما '    :    ' 55897939403232751 ',
' وتوشه '    :    ' 54676885047867737 ',
' لبوتان '    :    ' 30650426998863332 ',
' لخانه '    :    ' 56006915451245411 ',
' تمحركه '    :    ' 15826229869421585 ',
' لخزر '    :    ' 65414507129586385 ',
' تكشا '    :    ' 62258804563636993 ',
' لازما '    :    ' 50368344235826302 ',
' تفيرو '    :    ' 45062188442385800 ',
' فاراك '    :    ' 20865316761157979 ',
' چدن '    :    ' 12329519546621752 ',
' فبيرا '    :    ' 49399017998386087 ',
' فاما '    :    ' 34673681828119297 ',
' فجام '    :    ' 30765727085936322 ',
' فنرژي '    :    ' 63965059137798192 ',
' فلامي '    :    ' 25286509736208688 ',
' فبستم '    :    ' 4159532151694984 ',
' فجوش '    :    ' 64485827086284311 ',
' فولاد '    :    ' 46348559193224090 ',
' ذوب '    :    ' 9211775239375291 ',
' فروي '    :    ' 29974853866926823 ',
' وسديد '    :    ' 41713045190742691 ',
' فخوز '    :    ' 28864540805361867 ',
' ارفع '    :    ' 59266699437480384 ',
' كاوه '    :    ' 60350996279289099 ',
' هرمز '    :    ' 70498485598181604 ',
' فروس '    :    ' 54419429862704331 ',
' فاسمين '    :    ' 66701874099226162 ',
' ميدكو '    :    ' 24018878640527909 ',
' فسازان '    :    ' 12874072841236826 ',
' فباهنر '    :    ' 66772024744156373 ',
' فلوله '    :    ' 48623320733330408 ',
' فرآور '    :    ' 408934423224097 ',
' وتوكا '    :    ' 47232550823972469 ',
' فسرب '    :    ' 54277068923045214 ',
' فوكا '    :    ' 66514709341259550 ',
' فجر '    :    ' 41302553376174581 ',
' فولاژ '    :    ' 40808043719554948 ',
' فنفت '    :    ' 59342912854668427 ',
' فمراد '    :    ' 18004480270695404 ',
' فخاس '    :    ' 4733285133017464 ',
' زنگان '    :    ' 67170215467608124 ',
' فافزا '    :    ' 66021783818850713 ',
' فاهواز '    :    ' 44296315953738727 ',
' فپنتا '    :    ' 68488673556087148 ',
' فسديد '    :    ' 20966291817819448 ',
' فماك '    :    ' 35445515321658835 ',
' ماديرا '    :    ' 15917865009187760 ',
' پيزد '    :    ' 32784604551756178 ',
' پلاسك '    :    ' 57722642338781674 ',
' پكرمان '    :    ' 23214828924506640 ',
' پاسا '    :    ' 63580313877463104 ',
' پكوير '    :    ' 7235435095059069 ',
' پسهند '    :    ' 10120557300120078 ',
' پدرخش '    :    ' 24079409192818584 ',
' پلاست '    :    ' 52593789542874668 ',
' پلوله '    :    ' 29316948750916349 ',
' شتران '    :    ' 51617145873056483 ',
' شپنا '    :    ' 7745894403636165 ',
' شبريز '    :    ' 48753732042176709 ',
' شسپا '    :    ' 49188729526980541 ',
' شنفت '    :    ' 14073782708315535 ',
' ونفت '    :    ' 33931218652865616 ',
' شراز '    :    ' 33683240001985963 ',
' شرانل '    :    ' 44013656953678055 ',
' شزنگ '    :    ' 65490886290565185 ',
' چافست '    :    ' 23936607891892333 ',
' چكاوه '    :    ' 24254843881948059 ',
' چفيبر '    :    ' 64358061873294912 ',
' وملي '    :    ' 41796741644273824 ',
' نتوس '    :    ' 22950683624908253 ',
' نمرينو '    :    ' 30231789123900526 ',
' نشار '    :    ' 49129081625829210 ',
' كماسه '    :    ' 67690708346979840 ',
' ومعادن '    :    ' 58931793851445922 ',
' كاما '    :    ' 4942127026063388 ',
' كگل '    :    ' 35700344742885862 ',
' كچاد '    :    ' 18027801615184692 ',
' تاصيكو '    :    ' 23293437377896568 ',
' كبافق '    :    ' 43256212620530446 ',
' كروي '    :    ' 22787503301679573 ',
' كنور '    :    ' 20411759370751096 ',
' كمنگنز '    :    ' 50341528161302545 ',
' كدما '    :    ' 3623921205367364 ',
' حفاري '    :    ' 28809886765682162 ',
' كشرق '    :    ' 42690477960659940 ',
' كپرور '    :    ' 22941065011246116 ',
' كطبس '    :    ' 8977369674477111 ',
' زكوثر '    :    ' 42599305106713939 ',
' تليسه '    :    ' 41781090739318251 ',
' سيمرغ '    :    ' 28450080638096732 ',
' آبين '    :    ' 9987529074833218 ',
' زفكا '    :    ' 5427792638736934 ',
' زبينا '    :    ' 54482686501491508 ',
' زگلدشت '    :    ' 10024128313803797 ',
' زشگزا '    :    ' 26259366519412975 ',
' زقيام '    :    ' 71290297158948749 ',
' زمگسا '    :    ' 5054819322815158 ',
' زماهان '    :    ' 4507558419857064 ',
' زدشت '    :    ' 25180702353416009 ',
' زشريف '    :    ' 26547785441834730 ',
' آينده '    :    ' 17933573078185644 ',
' زپارس '    :    ' 33420285433308219 ',
}
    def exit_diver(self):
        self.driver.quit()

    def saveidstoxml(self,operate_number,value_number):
        if(operate_number==0):
            self.driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click()
            self.driver.find_element_by_css_selector(
                'div[onclick="mw.Settings.ShowKala=1-mw.Settings.ShowKala;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # بورس کالا
            self.driver.find_element_by_css_selector(
                'div[onclick="mw.Settings.ShowSandoogh=1-mw.Settings.ShowSandoogh;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # صندوق سرمایه گذاری
            self.driver.find_element_by_css_selector(
                'div[onclick="mw.Settings.ShowAti=1-mw.Settings.ShowAti;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # آتی
            self.driver.find_element_by_css_selector(
                'div[onclick="mw.Settings.ShowEkhtiarForoush=1-mw.Settings.ShowEkhtiarForoush;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # اختیار معامله
            self.driver.find_element_by_css_selector(
                'div[onclick="mw.Settings.ShowOraghMosharekat=1-mw.Settings.ShowOraghMosharekat;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # اوراق بدهی
            self.driver.find_element_by_css_selector(
                'div[onclick="mw.Settings.ShowHaghTaghaddom=1-mw.Settings.ShowHaghTaghaddom;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # حق تقدم
            self.driver.find_element_by_css_selector(
                'div[onclick="mw.Settings.ShowHousingFacilities=1-mw.Settings.ShowHousingFacilities;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # تسهیلات مسکن
            self.driver.find_element_by_css_selector(
                'div[onclick="mw.Settings.ShowPayeFarabourse=1-mw.Settings.ShowPayeFarabourse;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # فرابورس پایه
            self.driver.find_element_by_css_selector(
                'div[onclick="mw.Settings.LoadClientType=1-mw.Settings.LoadClientType;mw.SaveParams();HideAllWindow();mw.LoadClientType();"]').click()  # حقیقی حقوقی
            self.driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click()  # تنظیمات
            self.driver.find_element_by_css_selector('div.awesome.tra').click()  # همه نماد ها
            self.driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click()  # تنظیمات
            self.driver.find_element_by_css_selector(
                'div[onclick="mw.Settings.LoadInstHistory=1-mw.Settings.LoadInstHistory;mw.SaveParams();HideAllWindow();mw.LoadInstHistory();"]').click()  # تاریخچه قیمت ها
            namad = list(dict.fromkeys(self.driver.find_elements_by_css_selector('div[class="{c}"]')))
            # گرفتن اسامی ایدی ها
            # print('namad_id_dic={')
            # for target in namad:
            #     print("'", target.find_element_by_css_selector('a.inst').text, "'", '   :   ', "'",
            #           target.get_attribute('id'), "',")
            # print('}')
            #
            # input()
            import xml.etree.cElementTree as ET
            tree = ET.parse('namd_name_ids.xml')
            root = tree.getroot()
            id_name_dic = {}
            id_list = []
            for child in root:
                id_name_dic[child.attrib.get('id')] = child.attrib.get('name')
                id_list.append(child.attrib.get('id'))
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
            self.driver.quit()
            tree = ET.ElementTree(root)
            tree.write("namd_name_ids.xml")
        else:
            if(self.is_closed==True):
                self.driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click()
                self.driver.find_element_by_css_selector(
                    'div[onclick="mw.Settings.ShowKala=1-mw.Settings.ShowKala;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # بورس کالا
                self.driver.find_element_by_css_selector(
                    'div[onclick="mw.Settings.ShowSandoogh=1-mw.Settings.ShowSandoogh;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # صندوق سرمایه گذاری
                self.driver.find_element_by_css_selector(
                    'div[onclick="mw.Settings.ShowAti=1-mw.Settings.ShowAti;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # آتی
                self.driver.find_element_by_css_selector(
                    'div[onclick="mw.Settings.ShowEkhtiarForoush=1-mw.Settings.ShowEkhtiarForoush;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # اختیار معامله
                self.driver.find_element_by_css_selector(
                    'div[onclick="mw.Settings.ShowOraghMosharekat=1-mw.Settings.ShowOraghMosharekat;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # اوراق بدهی
                self.driver.find_element_by_css_selector(
                    'div[onclick="mw.Settings.ShowHaghTaghaddom=1-mw.Settings.ShowHaghTaghaddom;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # حق تقدم
                self.driver.find_element_by_css_selector(
                    'div[onclick="mw.Settings.ShowHousingFacilities=1-mw.Settings.ShowHousingFacilities;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # تسهیلات مسکن
                self.driver.find_element_by_css_selector(
                    'div[onclick="mw.Settings.ShowPayeFarabourse=1-mw.Settings.ShowPayeFarabourse;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # فرابورس پایه
                self.driver.find_element_by_css_selector(
                    'div[onclick="mw.Settings.LoadClientType=1-mw.Settings.LoadClientType;mw.SaveParams();HideAllWindow();mw.LoadClientType();"]').click()  # حقیقی حقوقی
                self.driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click()  # تنظیمات
                self.driver.find_element_by_css_selector('div.awesome.tra').click()  # همه نماد ها
                self.driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click()  # تنظیمات
                self.driver.find_element_by_css_selector('div[onclick="mw.Settings.LoadInstHistory=1-mw.Settings.LoadInstHistory;mw.SaveParams();HideAllWindow();mw.LoadInstHistory();"]').click()  # تاریخچه قیمت ها
                self.driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click()  # تنظیمات
                str_pach = "('#SectorList')"
                elem = self.driver.find_element_by_css_selector(
                    'select[onchange="mw.Settings.ViewMode=3;mw.Settings.SectorNo=$' + str_pach.replace(' ',
                                                                                                        "") + '.val();mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.RemoveAllData();mw.RenderData();"]').find_element_by_css_selector(
                    'option[value=' + '"' + str(value_number) + '"]')  # انتخاب گروه
                file_name = elem.text
                elem.click()
            else:
                self.driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click()  # تنظیمات
                str_pach = "('#SectorList')"
                elem = self.driver.find_element_by_css_selector(
                    'select[onchange="mw.Settings.ViewMode=3;mw.Settings.SectorNo=$' + str_pach.replace(' ',
                                                                                                        "") + '.val();mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.RemoveAllData();mw.RenderData();"]').find_element_by_css_selector(
                    'option[value=' + '"' + str(value_number) + '"]')  # انتخاب گروه
                file_name = elem.text
                elem.click()
            self.is_closed=False
            namad = list(dict.fromkeys(self.driver.find_elements_by_css_selector('div[class="{c}"]')))
            print("Groups's   "  + file_name +"   namad has been save ...")
            return (self.per_to_en(file_name),namad)
    def extractalldata(self):
            elements = self.driver.find_elements_by_css_selector('div[class="{c}"]')
            data = {}
            count=len(self.columns)
            for elem in elements:
                try:
                    self.driver.implicitly_wait(30)
                    str = elem.find_element_by_css_selector('a.inst').text
                    list_str = list(str)
                    is_four_or_two_exist=False
                    for mem in list_str:
                        if(mem=='4'):
                            is_four_or_two_exist=True
                        if(mem=='2'):
                            is_four_or_two_exist=True
                    if(is_four_or_two_exist==False):
                        if (count == 3):
                            id = 'tb_' + elem.get_attribute('id')
                            self.driver.implicitly_wait(30)
                            cfield0 = elem.find_element_by_css_selector('div[class="t0c ch{_cfield0}"]').text
                            self.driver.implicitly_wait(30)
                            cfield1 = elem.find_element_by_css_selector('div[class="t0c ch{_cfield1}"]').text
                            self.driver.implicitly_wait(30)
                            cfield2 = elem.find_element_by_css_selector('div[class="t0c ch{_cfield2}"]').text
                            self.driver.implicitly_wait(30)

                            if id not in data:
                                data[id] = {self.columns[0]: cfield0, self.columns[1]: cfield1,
                                            self.columns[2]: cfield2, 'date': self.gettime()}
                            else:
                                data[id].update(
                                    {self.columns[0]: cfield0, self.columns[1]: cfield1, self.columns[2]: cfield2,
                                     'date': self.gettime()})
                        elif (count == 2):
                            id = 'tb_' + elem.get_attribute('id')
                            self.driver.implicitly_wait(30)
                            cfield0 = elem.find_element_by_css_selector('div[class="t0c ch{_cfield0}"]').text
                            self.driver.implicitly_wait(30)
                            cfield1 = elem.find_element_by_css_selector('div[class="t0c ch{_cfield1}"]').text
                            self.driver.implicitly_wait(30)
                            if id not in data:
                                data[id] = {self.columns[0]: cfield0, self.columns[1]: cfield1, 'date': self.gettime()}
                            else:
                                data[id].update(
                                    {self.columns[0]: cfield0, self.columns[1]: cfield1, 'date': self.gettime()})
                        elif (count == 1):
                            id = 'tb_' + elem.get_attribute('id')
                            self.driver.implicitly_wait(30)
                            cfield0 = elem.find_element_by_css_selector('div[class="t0c ch{_cfield0}"]').text
                            self.driver.implicitly_wait(30)
                            if id not in data:
                                data[id] = {self.columns[0]: cfield0, 'date': self.gettime()}
                            else:
                                data[id].update(
                                    {self.columns[0]: cfield0, 'date': self.gettime()})
                        else:
                            print('wanted data must not be greater than 3')
                            break
                    else:
                        print('there is a namad that have 4 or 2 :',str)
                except:pass
#                   print('Error from frst...')
            return data

    def extractalldata_Bear(self):
        elements = self.driver.find_elements_by_css_selector('div[class="{c}"]')
        data = {}
        count = len(self.columns)
        for elem in elements:
            try:
                self.driver.implicitly_wait(30)
                if (count == 3):
                    id = 'tb_' + elem.get_attribute('id')
                    self.driver.implicitly_wait(30)
                    cfield0 = elem.find_element_by_css_selector('div[class="t0c ch{_cfield0}"]').text
                    self.driver.implicitly_wait(30)
                    cfield1 = elem.find_element_by_css_selector('div[class="t0c ch{_cfield1}"]').text
                    self.driver.implicitly_wait(30)
                    cfield2 = elem.find_element_by_css_selector('div[class="t0c ch{_cfield2}"]').text
                    self.driver.implicitly_wait(30)

                    if id not in data:
                        data[id] = {self.columns[0]: cfield0, self.columns[1]: cfield1,
                                    self.columns[2]: cfield2, 'date': self.gettime()}
                    else:
                        data[id].update(
                            {self.columns[0]: cfield0, self.columns[1]: cfield1, self.columns[2]: cfield2,
                             'date': self.gettime()})
                elif (count == 2):
                    id = 'tb_' + elem.get_attribute('id')
                    self.driver.implicitly_wait(30)
                    cfield0 = elem.find_element_by_css_selector('div[class="t0c ch{_cfield0}"]').text
                    self.driver.implicitly_wait(30)
                    cfield1 = elem.find_element_by_css_selector('div[class="t0c ch{_cfield1}"]').text
                    self.driver.implicitly_wait(30)
                    if id not in data:
                        data[id] = {self.columns[0]: cfield0, self.columns[1]: cfield1, 'date': self.gettime()}
                    else:
                        data[id].update(
                            {self.columns[0]: cfield0, self.columns[1]: cfield1, 'date': self.gettime()})
                elif (count == 1):
                    id = 'tb_' + elem.get_attribute('id')
                    self.driver.implicitly_wait(30)
                    cfield0 = elem.find_element_by_css_selector('div[class="t0c ch{_cfield0}"]').text
                    self.driver.implicitly_wait(30)
                    if id not in data:
                        data[id] = {self.columns[0]: cfield0, 'date': self.gettime()}
                    else:
                        data[id].update(
                            {self.columns[0]: cfield0, 'date': self.gettime()})
                else:
                    print('wanted data must not be greater than 3')
                    break
            except:
                pass
        #                   print('Error from frst...')
        return data

    def extractdata(self,idlist):
            elements = self.driver.find_element_by_css_selector('div[class="{c}"]')
            data = {}
            count=len(self.columns)
            try:
                element=self.driver.find_element_by_xpath("/html/body/div[@class='MainContainer']/form/div[@id='display']/div[@id='main']")
                if (count == 3):
                    for id in idlist:
                        cfield0 = element.find_element_by_css_selector('div[id="'+id+'"]').find_element_by_css_selector('div[class="t0c ch{_cfield0}"]').text
                        cfield1 = element.find_element_by_css_selector('div[id="'+id+'"]').find_element_by_css_selector('div[class="t0c ch{_cfield1}"]').text
                        cfield2 = element.find_element_by_css_selector('div[id="'+id+'"]').find_element_by_css_selector('div[class="t0c ch{_cfield2}"]').text
                        name=element.find_element_by_css_selector('div[id="'+id+'"]').find_element_by_css_selector('a[target="'+id+'"]').text
                        if id not in data:
                            data[id] = {'name':name,self.columns[0]: cfield0, self.columns[1]: cfield1,
                                        self.columns[2]: cfield2, 'date': self.gettime()}
                        else:
                            data[id].update(
                                {'name':name,self.columns[0]: cfield0, self.columns[1]: cfield1, self.columns[2]: cfield2,
                                 'date': self.gettime()})

                elif (count == 2):
                    for id in idlist:
                        cfield0 = element.find_element_by_css_selector('div[id="'+id+'"]').find_element_by_css_selector('div[class="t0c ch{_cfield0}"]').text
                        cfield1 = element.find_element_by_css_selector('div[id="'+id+'"]').find_element_by_css_selector('div[class="t0c ch{_cfield1}"]').text
                        if id not in data:
                            data[id] = {self.columns[0]: cfield0, self.columns[1]: cfield1, 'date': self.gettime()}
                        else:
                            data[id].update(
                                {self.columns[0]: cfield0, self.columns[1]: cfield1,
                                 'date': self.gettime()})

                elif (count == 1):
                    for id in idlist:
                        cfield0 = element.find_element_by_css_selector('div[id="'+id+'"]').find_element_by_css_selector('div[class="t0c ch{_cfield0}"]').text
                        if id not in data:
                            data[id] = {self.columns[0]: cfield0, 'date': self.gettime()}
                        else:
                            data[id].update(
                                {self.columns[0]: cfield0,
                                 'date': self.gettime()})

                else:
                    print('wanted data must not be greater than 3')
            except:
                print('Error from frst...')
            return data
    def addCfield0(self,cfield):
        # print('has been ADded ...')
        self.columns.append(cfield)
    def subtrac_cfield(self,c):
        # print('has been removed ...')
        self.columns.remove(c)

    def dosettingforextraction(self):
        self.driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click()  # بورس کالا
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.ShowKala=1-mw.Settings.ShowKala;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # بورس کالا
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.ShowSandoogh=1-mw.Settings.ShowSandoogh;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # صندوق سرمایه گذاری
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.ShowAti=1-mw.Settings.ShowAti;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # آتی
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.ShowEkhtiarForoush=1-mw.Settings.ShowEkhtiarForoush;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # اختیار معامله
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.ShowOraghMosharekat=1-mw.Settings.ShowOraghMosharekat;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # اوراق بدهی
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.ShowHaghTaghaddom=1-mw.Settings.ShowHaghTaghaddom;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # حق تقدم
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.ShowHousingFacilities=1-mw.Settings.ShowHousingFacilities;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # تسهیلات مسکن
        # self.driver.find_element_by_css_selector('div[onclick = "mw.Settings.ShowSaham=1-mw.Settings.ShowSaham;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # بورس
        # self.driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click()
        self.driver.find_element_by_css_selector('div[onclick="mw.Settings.ShowPayeFarabourse=1-mw.Settings.ShowPayeFarabourse;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # فرابورس پایه


        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.LoadClientType=1-mw.Settings.LoadClientType;mw.SaveParams();HideAllWindow();mw.LoadClientType();"]').click()  # حقیقی حقوقی
        self.driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click()  # تنظیمات
        self.driver.find_element_by_css_selector('div.awesome.tra').click()  # همه نماد ها
        # driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click()# تنظیمات
        self.driver.find_element_by_css_selector('a[onclick="mw.ShowTemplateWindow()"]').click()  # قالب شخصی
        # driver.find_element_by_css_selector('div[onclick="mw.changeTemplate(11)"]').click()# شخصی
        self.driver.find_element_by_css_selector('div[onclick="mw.BuildTemplate()"]').click()  # قالب شخصی ساخت
        self.driver.find_element_by_css_selector('select[id="Col0_Data"]').find_element_by_css_selector(
            'option[value="0"]').click()  # انتخاب نام نماد
        self.driver.find_element_by_css_selector('select[id="Col1_Data"]').find_element_by_css_selector(
            'option[value="24"]').click()  # انتخاب cfield0
        self.driver.find_element_by_css_selector('select[id="Col2_Data"]').find_element_by_css_selector(
            'option[value="25"]').click()  # انتخاب cfield1
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('select[id="Col3_Data"]').find_element_by_css_selector('option[value="26"]').click()  # انتخاب cfield2
        self.driver.find_element_by_css_selector('a[href="javascript:mw.SaveTemplate()"]').click()  # تایید
        self.driver.find_element_by_css_selector('a[onclick="mw.QueryWindow()"]').click()  # پنجره فیلتر
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.QueryWindowNewFilter();mw.QueryWindowFilterNames()"]').click()  # جدید فیلتر
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.SelectFilter(0);mw.ShowSettings();mw.SaveParams();mw.QueryWindowFilterNames()"]').click()  # 0 فیلتر
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.QueryWindowNewFilter();mw.QueryWindowFilterNames()"]').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('textarea[id="InputFilterCode"]').clear()  # پاک کردن متن
        self.driver.find_element_by_css_selector('textarea[id="InputFilterCode"]').click()  # وارد کردن متن
        self.driver.find_element_by_css_selector('textarea[id="InputFilterCode"]').send_keys(self.query)
        self.driver.find_element_by_css_selector('div[onclick="mw.QueryWindowSaveFilter()"]').click()  # ثبت فیلتر
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('div[class="popup_close"]').click()  # خارج شدن از فیلتر
        self.driver.find_element_by_css_selector('a[onclick="mw.ShowTemplateWindow()"]').click()  # قالب شخصی
        self.driver.find_element_by_css_selector('div[onclick="mw.changeTemplate(11)"]').click()  # شخصی
        self.driver.find_element_by_css_selector('div[class="popup_close"]').click()  # خارج شدن از شخصی سازی
        print(f'data are ready to extract for inserting into {self.columns}')
    def newsetting(self,key):
        #bourse
        if(key==0):
            self.driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click() #main-setting
            self.driver.find_element_by_css_selector('div[onclick="mw.Settings.ShowPayeFarabourse=1-mw.Settings.ShowPayeFarabourse;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # فرابورس پایه
            self.driver.find_element_by_css_selector('div[onclick="mw.Settings.Market=1;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.RemoveAllData();mw.RenderData();"]').click()  # بورس
            #self.driver.find_element_by_css_selector('div[class="popup_close"]').click()  # exit main-setting
        #fara-bourse
        elif(key==1):
            self.driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click() #main-setting
            self.driver.find_element_by_css_selector('div[onclick="mw.Settings.ShowPayeFarabourse=1-mw.Settings.ShowPayeFarabourse;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # فرابورس پایه
            #self.driver.find_element_by_css_selector('div[onclick = "mw.Settings.ShowSaham=1-mw.Settings.ShowSaham;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # بورس
            self.driver.find_element_by_css_selector('div[onclick="mw.Settings.Market=2;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.RemoveAllData();mw.RenderData();"]').click()  # بورس
            #self.driver.find_element_by_css_selector('div[class="popup_close"]').click()  # exit main-setting
        else:pass
    def newstringfilter(self,query,COLUMNS):
        self.columns = COLUMNS
        print(f'new data are ready to extract for inserting into {self.columns}')
        self.driver.find_element_by_css_selector('a[onclick="mw.QueryWindow()"]').click()  # پنجره فیلتر
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.QueryWindowNewFilter();mw.QueryWindowFilterNames()"]').click()  # جدید فیلتر
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.SelectFilter(0);mw.ShowSettings();mw.SaveParams();mw.QueryWindowFilterNames()"]').click()  # 0 فیلتر
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.QueryWindowNewFilter();mw.QueryWindowFilterNames()"]').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('textarea[id="InputFilterCode"]').clear()  # پاک کردن متن
        self.driver.find_element_by_css_selector('textarea[id="InputFilterCode"]').click()  # وارد کردن متن
        self.driver.find_element_by_css_selector('textarea[id="InputFilterCode"]').send_keys(query)
        self.driver.find_element_by_css_selector('div[onclick="mw.QueryWindowSaveFilter()"]').click()  # ثبت فیلتر
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('div[class="popup_close"]').click()  # خارج شدن از فیلتر
        self.driver.find_element_by_css_selector('a[onclick="mw.ShowTemplateWindow()"]').click()  # قالب شخصی
        self.driver.find_element_by_css_selector('div[onclick="mw.changeTemplate(11)"]').click()  # شخصی
        self.driver.find_element_by_css_selector('div[class="popup_close"]').click()  # خارج شدن از شخصی سازی
    def gettime(self):
        import datetime
        date = str(datetime.datetime.now().year) + '/' + str(datetime.datetime.now().month) + '/' + str(
            datetime.datetime.now().day)
        return  date




    def dosettingforextraction_namad(self):
        self.driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click()  # بورس کالا
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.ShowKala=1-mw.Settings.ShowKala;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # بورس کالا
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.ShowSandoogh=1-mw.Settings.ShowSandoogh;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # صندوق سرمایه گذاری
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.ShowAti=1-mw.Settings.ShowAti;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # آتی
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.ShowEkhtiarForoush=1-mw.Settings.ShowEkhtiarForoush;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # اختیار معامله
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.ShowOraghMosharekat=1-mw.Settings.ShowOraghMosharekat;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # اوراق بدهی
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.ShowHaghTaghaddom=1-mw.Settings.ShowHaghTaghaddom;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # حق تقدم
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.ShowHousingFacilities=1-mw.Settings.ShowHousingFacilities;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # تسهیلات مسکن
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.ShowPayeFarabourse=1-mw.Settings.ShowPayeFarabourse;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();"]').click()  # فرابورس پایه
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.LoadInstStat=1-mw.Settings.LoadInstStat;mw.SaveParams();HideAllWindow();mw.LoadInstStat();"]').click()  # آمار کلیدی
        self.driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click()
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.LoadInstHistory=1-mw.Settings.LoadInstHistory;mw.SaveParams();HideAllWindow();mw.LoadInstHistory();"]').click()  # تاریخچه قیمت ها
        self.driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click()
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.Settings.LoadClientType=1-mw.Settings.LoadClientType;mw.SaveParams();HideAllWindow();mw.LoadClientType();"]').click()  # حقیقی حقوقی
        self.driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click()  # تنظیمات
        self.driver.find_element_by_css_selector('div.awesome.tra').click()  # همه نماد ها
        # driver.find_element_by_css_selector('a#id1.TopIcon.MwIcon.MwSetting').click()# تنظیمات
        self.driver.find_element_by_css_selector('a[onclick="mw.ShowTemplateWindow()"]').click()  # قالب شخصی
        # driver.find_element_by_css_selector('div[onclick="mw.changeTemplate(11)"]').click()# شخصی
        self.driver.find_element_by_css_selector('div[onclick="mw.BuildTemplate()"]').click()  # قالب شخصی ساخت
        self.driver.find_element_by_css_selector('select[id="Col0_Data"]').find_element_by_css_selector(
            'option[value="0"]').click()  # انتخاب نام نماد
        self.driver.find_element_by_css_selector('select[id="Col1_Data"]').find_element_by_css_selector(
            'option[value="24"]').click()  # انتخاب cfield0
        self.driver.find_element_by_css_selector('select[id="Col2_Data"]').find_element_by_css_selector(
            'option[value="25"]').click()  # انتخاب cfield1
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('select[id="Col3_Data"]').find_element_by_css_selector('option[value="26"]').click()  # انتخاب cfield2
        self.driver.find_element_by_css_selector('a[href="javascript:mw.SaveTemplate()"]').click()  # تایید
        self.driver.find_element_by_css_selector('a[onclick="mw.QueryWindow()"]').click()  # پنجره فیلتر
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.QueryWindowNewFilter();mw.QueryWindowFilterNames()"]').click()  # جدید فیلتر
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.SelectFilter(0);mw.ShowSettings();mw.SaveParams();mw.QueryWindowFilterNames()"]').click()  # 0 فیلتر
        self.driver.find_element_by_css_selector(
            'div[onclick="mw.QueryWindowNewFilter();mw.QueryWindowFilterNames()"]').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('textarea[id="InputFilterCode"]').clear()  # پاک کردن متن
        self.driver.find_element_by_css_selector('textarea[id="InputFilterCode"]').click()  # وارد کردن متن
        self.driver.find_element_by_css_selector('textarea[id="InputFilterCode"]').send_keys(self.query)
        self.driver.find_element_by_css_selector('div[onclick="mw.QueryWindowSaveFilter()"]').click()  # ثبت فیلتر
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('div[class="popup_close"]').click()  # خارج شدن از فیلتر
        self.driver.find_element_by_css_selector('a[onclick="mw.ShowTemplateWindow()"]').click()  # قالب شخصی
        self.driver.find_element_by_css_selector('div[onclick="mw.changeTemplate(11)"]').click()  # شخصی
        self.driver.find_element_by_css_selector('div[class="popup_close"]').click()  # خارج شدن از شخصی سازی
        print(f'data are ready to extract for inserting into {self.columns}')

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