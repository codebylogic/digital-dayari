import time
date=time.strftime("%d/%m/%Y")
# टाइम मॉड्यूल का इस्तेमाल करके डायरी में कौन सा डेट को डायरी लिखा है यह पता चलेगा
def dayri():
    print("="*50)
    print("\t    स्वागत है आपका डिजिटल डायरी में ")
    print("="*50)

    while True:
        global ask
        ask=input("लिखने के लिए A पढ़ने के लिए R बंद करने के लिए exit दवाएं: ").lower()

        try:
            if ask=='a':
                a=input("आज का डायरी यहां लिखें: ")
                with open("mydayri.txt", "a") as f:
                    data = f.write(f"\n{date}\n{a}\n")
                print("आपकी डायरी सफलता पूर्वक सेव की गई")

            elif ask=='r':
                with open("mydayri.txt", "r") as f:
                    data = f.read()
                    print(f"आपका डायरी \n {data}")

            elif ask=='exit':
                print("="*50)
                print("\t \t अलविदा !")
                print("="*50)
                break

            else:
                print(" कृपया सिर्फ A,R और exit दबाए: ")

        except:
            print("कृपया सिर्फ A,R और exit दबाए: ")


#lock system
password=input("enter your dayri password: ")
n=3
while True: # sahi password dalne per 
    if (password=='shivam@123'):#password is 'shivam@123'
        dayri()
        if ask=='exit':
            break
    else: # galat password dalne per 
        if n==1:
            print("❎"*25 )
            print("="*50)
            print("\t आप अधिकतम प्रयासों की सीमा पार कर चुके हैं")
            print("="*50)
            print("❎"*25 )
            break
        else:
            n-=1
            print("inviled password")
            password=input("plese enter valid password: ")

    