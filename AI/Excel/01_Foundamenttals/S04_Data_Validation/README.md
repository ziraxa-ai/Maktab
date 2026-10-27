### خب وارد جلسه چهارم شدیم
ابتدا فایل تمرین را آماده کن

از فایل روز سوم یک نسخه با نام زیر ذخیره کن:

                                                                   
W01_D04_EPC_Validation.xlsx

شیت جدیدی بساز:

```
Lists
```
برای تمرین امروز، جدول اصلی در شیت Calendar این چینش را داشته باشد؛ اگر ساختار قبلی متفاوت است، یک شیت تمرینی جدید بساز:

```
ستون 	عنوان
A 	ProjectID
B 	PackageID
C 	StartDate
D 	ApprovedFinish
E 	ActualDelivery
F 	Status
G 	Quantity
H 	InputCheck
```
ردیف اول عنوان و ردیف دوم اولین رکورد است.

نکته: اعتبارسنجی امروز برای سلول‌های ورودی است. روی ستون‌هایی که خروجی فرمول پاک‌سازی‌اند، انتظار نداشته باش Data Validation نتیجه‌ی محاسبه را مسدود کند.

 ساخت دراپ‌داون وضعیت

در Lists!A1:A5 وارد کن:
```
Status
Pending
In Progress
Delivered
Delayed
```
محدوده را با Ctrl+T به Table تبدیل کن و نامش را بگذار:

```
tblStatus
```
از مسیر زیر یک نام تعریف کن:

```
Formulas → Name Manager → New
```
نام:

```
StatusList
```
مقدار Refers to:

```
=tblStatus[Status]
```
اکنون سلول‌های وضعیت، مثلاً Calendar!F2:F201 را انتخاب کن:

```
Data → Data Validation
```
در تب Settings:
```
    Allow: List
    Source:
```
   ```
=StatusList
```

  **گزینه‌ی In-cell dropdown روشن باشد.**

چرا از نام تعریف‌شده استفاده کردیم؟

ارجاع مستقیم ساخت‌یافته مانند =tblStatus[Status] در کادر Source در همه‌ی محیط‌ها پذیرفته نمی‌شود. نام تعریف‌شده، واسطه‌ی مناسبی است و با گسترش جدول منبع به‌روز می‌شود.

پیام راهنما و پیام خطا
تب Input Message

عنوان:

```
وضعیت قطعه
```
پیام:

   ```
یکی از وضعیت‌های فهرست را انتخاب کنید.
```
این پیام هنگام انتخاب سلول کمک می‌کند؛ خودش محدودیتی اعمال نمی‌کند.
تب Error Alert

گزینه‌ی نمایش هشدار خطا روشن باشد.

    Style: Stop
    Title:

```
وضعیت نامعتبر

    Error message:

   ```
فقط Pending، In Progress، Delivered یا Delayed مجاز است.
