اتصال متریال به پایگاه قیمت با XLOOKUP و INDEX/MATCH

امروز یک بخش مهم از داشبورد EPC را می‌سازیم:

    کد متریال هر ردیف BOQ را به پایگاه قیمت متصل کنیم؛ بدون انتخاب قیمت اشتباه، پنهان‌کردن کدهای ناموجود یا کندکردن فایل.

نکته: VLOOKUP هنوز کاربرد دارد، اما XLOOKUP محدودیت‌هایی مثل جستجوی صرفاً راست‌رو و شماره‌ستون ثابت را برطرف می‌کند.

سازگاری: XLOOKUP در Microsoft 365، Excel 2021 و نسخه‌های جدیدتر موجود است؛ در Excel 2016 و 2019 از INDEX/MATCH استفاده کن.

فرمول‌ها با , نوشته شده‌اند؛ اگر اکسل تو نیاز دارد، آن را با ; جایگزین کن.
بخش روز — ۲ ساعت آموزش و تمرین
زمان 	موضوع
۲۰ دقیقه 	ساخت جدول‌ها و جستجوی دقیق
۲۵ دقیقه 	مدیریت پیدا نشدن و کلیدهای تکراری
۲۰ دقیقه 	جستجو از آخر به اول
۲۵ دقیقه 	جستجوی تقریبی و دودویی
۲۰ دقیقه 	INDEX/MATCH
۱۰ دقیقه 	تست و مرور
۱. آماده‌سازی جدول‌های تمرین

در شیت PriceDB داده‌های زیر را وارد کن و با Ctrl+T به Table تبدیل کن.

نام جدول:

                                                                    text
tblPrices

MaterialCode 	MaterialName 	Unit 	Currency 	UnitPrice
MAT-001 	Steel Plate 	kg 	USD 	2.5
MAT-002 	Cement Bag 	bag 	USD 	6
MAT-003 	Power Cable 	m 	USD 	4.2
MAT-004 	Control Valve 	ea 	USD 	85
MAT-005 	Cable Tray 	m 	USD 	12
MAT-006 	Pipe 	m 	USD 	18

در شیت BOQ جدول زیر را با نام tblBOQ بساز:
LineID 	MaterialCode 	Qty
B001 	MAT-003 	100
B002 	MAT-001 	500
B003 	MAT-004 	4
B004 	MAT-999 	10
B005 	MAT-002 	200
B006 	MAT-006 	30

این پایگاه تمرینی، برای هر کد فقط یک قیمت جاری، یک واحد و یک ارز دارد. در پروژه واقعی این فرض را باید بررسی کنیم.
۲. ساختار XLOOKUP

                                                                    excel
=XLOOKUP(lookup_value,lookup_array,return_array,[if_not_found],[match_mode],[search_mode])

آرگومان 	وظیفه
lookup_value 	چه مقداری را پیدا کنم؟
lookup_array 	در کدام ستون جستجو کنم؟
return_array 	نتیجه را از کدام ستون برگردانم؟
if_not_found 	اگر تطبیقی نبود، چه برگردانم؟
match_mode 	تطبیق دقیق، تقریبی یا wildcard
search_mode 	جهت و روش جستجو
اولین اتصال قیمت

در ستون جدید UnitPrice جدول BOQ:

                                                                    excel
=XLOOKUP([@MaterialCode],tblPrices[MaterialCode],tblPrices[UnitPrice],"NOT_FOUND",0,1)

معنی:

    کد متریال همین ردیف را بخوان؛
    در ستون کد پایگاه قیمت جستجو کن؛
    قیمت متناظر را برگردان؛
    اگر پیدا نشد، NOT_FOUND بنویس؛
    فقط تطبیق دقیق؛
    از اول به آخر جستجو کن.

نتیجه:
MaterialCode 	UnitPrice
MAT-003 	4.2
MAT-001 	2.5
MAT-004 	85
MAT-999 	NOT_FOUND
MAT-002 	6
MAT-006 	18

تفاوت مهم با VLOOKUP: پیش‌فرض XLOOKUP تطبیق دقیق است. بااین‌حال، در فرمول‌های آموزشی و حساس، نوشتن صریح 0 خوانایی را بیشتر می‌کند.
