y = 1
while y :
    if y == 1 :
       print("################################################################################") 
       print("#                     please select oil and price                              #")
       print("#                                                                              #")
       print("#             1.Gasoline 95 ราคา 29.16 BAHT                                    #")
       print("#             2.Gasoline 91 ราคา 25.30 BAHT                                    #")
       print("#             3.Gasohol 91 ราคา 21.68 BAHT                                     #")
       print("#             4.Gasohol E20 ราคา 20.2 BAHT                                     #")
       print("#             5.Gasohol 95 ราคา 21.2 BAHT                                      #")
       print("#             6.Diesel ราคา 21.1 BAHT                                          #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("################################################################################")

       a = (input('select oil and price : '))
       while not(a in "1,2,3,4,5,6") :
          a = (input('select oil and price : '))
       print("################################################################################") 
       print("#                               select function                                #")
       print("#                     1.เปลี่ยนเงินเป็นลิตร                                         #")
       print("#                     2.เปลี่ยนลิตรเป็นเงิน                                         #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("#                                                                              #")
       print("################################################################################")
 

       b = (input("select function :" ))
       
       if "1" in b :
          x = input("จำนวนเงิน: ")
          x = float(x)
       elif "2" in b :
          y = input("จำนวนลิตร: ")
          y = float(y)
       else :
          print("eror")
       k = 0

       if "1" in b :
                 if "1" in a :
                      k= k+(x/29.15)
                      print('Ans','%.2f' %k,'ลิตร')
                 elif  '2' in a  :
                        k = k+(x/25.30)
                        print('Ans','%.2f' %k,'ลิตร')
                 elif  '3' in a  :
                        k = k+(x/21.68)
                        print('Ans','%.2f' %k,'ลิตร')
                 elif  '4' in a  :
                        k = k+(x/20.2)
                        print('Ans','%.2f' %k,'ลิตร')
                 elif  '5' in a  :
                        k = k+(x/21.2)
                        print('Ans','%.2f' %k,'ลิตร')
                 elif  '6' in a  :
                        k = k+(m1/21.1)
                        print('Ans','%.2f' %k,'ลิตร')
                 else :
                      print('Invalid information, please Enter again.')
       elif '2' in b :
                  if '1' in b :
                      k = k+(y*29.15)
                      print('ราคาน้ำมัม =',k,'บาท')
                  elif '2' in b  :
                        k = k+(y*25.30)
                        print('ราคาน้ำมัน =',k,'บาท')
                  elif '3' in b  :
                        k = k+(y*21.68)
                        print('ราคา น้ำมัน =',k,'บาท')
                  elif '4' in b :
                        k = k+(y*20.2)
                        print('ราคา น้ำมัน =',k,'บาท')
                  elif '5' in b  :
                        k = k+(y*21.2)
                        print('ราคา น้ำมัน =',k,'บาท')
                  elif '6' in b  :
                        k = k+(y*21.1)
                        print('ราคา น้ำมัน =',k,'บาท')

                  else :
                      print('Invalid information, please Enter again.')
       x = int(input("กด 1 เพื่อเริ่มใหม่  กด 0 เพื่อออก :   "))
       y = x
    elif y == 0 :
     break
      
