def divide_karo():
    print("--- Division Calculator ---")
    
    # 1. TRY: Yahan wo code likhte hain jisme error aane ka chance ho
    try:
        num1 = int(input("Pehla number dalein: "))
        num2 = int(input("Dusra number (divisor) dalein: "))
        
        result = num1 / num2
        
    # 2. EXCEPT: Agar koi specific error aati hai, toh program crash hone ki jagah ye chalega
    except ValueError:
        print("❌ Error: Kripya sirf numbers hi dalein, ABCD nahi!")
        
    except ZeroDivisionError:
        print("❌ Error: Kisi bhi number ko 0 se divide nahi kiya ja sakta!")
        
    except Exception as e:
        print(f"❌ Koi anjaan error aa gayi: {e}")
        
    # 3. ELSE: Agar 'try' block mein KOI ERROR NAHI aati hai, tab ye chalega
    else:
        print(f"✅ Success! Aapka answer hai: {result}")
        
    # 4. FINALLY: Ye block HAMESHA chalega, chahe error aaye ya na aaye
    finally:
        print("--- Calculation Process Khatam Hua ---\n")

# Function ko call kar rahe hain
divide_karo()