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
