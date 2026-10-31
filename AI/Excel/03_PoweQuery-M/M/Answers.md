## پاسخ تمرین‌ها (سری اول)
### پاسخ ۱

خروجی:

                                                                    
        20

چون in مقدار Sum را انتخاب کرده است، نه Doubled.
### پاسخ ۲
```                                                                
    let
        Price = 200,
        Quantity = 4,
        Total = Price * Quantity
    in
        Total
```
خروجی:

                                                                    
        800

### پاسخ ۳

```                                                                    
    let
        RawText = "  predictive analytics  ",
        TrimmedText = Text.Trim(RawText),
        FinalText = Text.Upper(TrimmedText)
    in
        FinalText
```
### پاسخ ۴

گام نهایی باید از TrimmedText استفاده کند:

```                                                                    
    let
        RawText = "  AI  ",
        TrimmedText = Text.Trim(RawText),
        FinalText = Text.Upper(TrimmedText)
    in
        FinalText
```
### پاسخ ۵

                                                                    
    let
        UnitPrice = 250,
        Quantity = 4,
        DiscountRate = 0.10,
        GrossAmount = UnitPrice * Quantity,
        DiscountAmount = GrossAmount * DiscountRate,
        NetAmount = GrossAmount - DiscountAmount
    in
        NetAmount

خروجی:

                                                                    
          900 

برای مشاهده مبلغ تخفیف فقط بخش خروجی را تغییر بده:

```                                                                    
    in
        DiscountAmount
```
خروجی:

                                                                  
          100

---

## پاسخ تمرین‌ها(سری دوم) 
پاسخ ۱

                                                                    text
40

سه نام متفاوت داریم؛ اما این سبک نام‌گذاری برای پروژه واقعی مناسب نیست.
پاسخ ۲

الف:

                                                                    text
Sara

ب:

                                                                    text
Clean Name

در اولی به شناسه ارجاع داده‌ایم؛ در دومی متن ثابت برگردانده‌ایم.
پاسخ ۳

                                                                    powerquery
let
    RawName = "  sara  ",
    CleanName = Text.Trim(RawName)
in
    CleanName

سه اصلاح:

    text.trim ← Text.Trim
    rawName ← RawName
    cleanName ← CleanName

خروجی sara است؛ Text.Trim حروف را بزرگ نمی‌کند.
پاسخ ۴

                                                                    powerquery
let
    OriginalAmount = 500,
    DiscountedAmount = OriginalAmount * 0.90
in
    DiscountedAmount

پاسخ ۵

                                                                    powerquery
let
    RawCity1 = "  shiraz ",
    RawCity2 = "SHIRAZ",

    CleanCity1 = Text.Trim(RawCity1),
    CleanCity2 = Text.Trim(RawCity2),

    AreEqual = Comparer.Equals(
        Comparer.OrdinalIgnoreCase,
        CleanCity1,
        CleanCity2
    )
in
    AreEqual

پاسخ ۶

دو تعریف ابتدای پروژه:

                                                                    powerquery
MinimumAge = 40,
TargetCity = "SHIRAZ",

خروجی:
CustomerID 	Name 	Age 	City
3 	Reza 	41 	Shiraz
