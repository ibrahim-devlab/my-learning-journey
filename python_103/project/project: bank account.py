


# المتطلبات:
# قم بكتابة برنامج يمثل حساب المستخدم في البنك، بحيث يقوم بالتالي:
# عندما يتم إنشاء مستخدم يقوم بتهيئة رصيده البنكي وإعطائه القيمة صفر
# يستطيع المستخدم إيداع نقوده عن طريق زيادة رصيده البنكي
# يستطيع المستخدم السحب عن طريق خصم رصيده البنكي
# يستطيع المستخدم الاستعلام عن رصيده عن طريق الوصول لقية رصيده الحالي
# يتم إظهار جملة طباعة عند السحب أو الإيداع مع التاريخ والوقت عند حدوث تلك العملية

# مثال:
# إيداع 2000 ريال: تم إيداع 2000 ريال لرصيدك البنكي في يوم الخميس، 10 يونيو 2021، الساعة 4:45 am
# خصم 150 ريال: تم خصم 150 ريال من رصيدك البنكي في يوم الثلاثاء، 9 فبراير 2021، الساعة 9:15 pm

from accs_manage import get_acc
from password_check import passcheck
i = 1
while (i < 2):

    try:
        inpu = int(input("enter 1 to get to your account, enter 2 to create an account.: "))
        if inpu == 1 or inpu == 2:
            i += 1
    except ValueError:
        print("enter a correct value")

if inpu == 2:
    acc_nasb = input("enter your nasb: ")
    
    password = (input("enter a 4 digits password: "))
    pas = passcheck(password)
    if pas == 0:
        print("invalid password: the password should be only 4 digits!.")

else:
    card = input("Enter your name or your account number: ")
    print(get_acc(card))