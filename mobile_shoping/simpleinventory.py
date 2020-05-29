from datetime import datetime
##import random



def banner():
    print("*************************************")
    print("\tMy Mobiles Shop")
    print("*************************************")
    print("\t1.Show All Products")
    print("\t2.Buy Product")
    print("\t3.Add Products")
    print("\t4.Exit")
    print("**************************************")

def display_all():
    print("SNO\tProduct\t\tIn Stock\tRate")
    for item in all_products:
        print("%d\t%s\t%d\t\t%s" %(int(item[0]), item[1], int(item[2]), item[3]))

def order_summary(product, name,qty):
    print("***********************************************")
    print("\t\tClix Mobiles Shop")
    print("***********************************************")
##    dt=datetime.now()
##    dt=dt.strftime('%D')
##    print("Order Summary\tDate:%s" %dt)
    global price
    global pricegst
    print("Customer Name: %s" %name)
    print("Product Name: %s" %(item[1]))
    rate=item[3]
    rate=int(rate[0:-1])
    price=rate*qty
    pricegst=price+price*0.18
    price=str(price)+'$'
   
    print("Price: %s" %(price))
    
    print("***********************************************")
    print("\t\tTotal Bill Amount: %s" %(pricegst))

def generate_bill(product, name):
    print("***********************************************")
    print("\t\tClix Mobiles Shop")
    print("***********************************************")
    global price
    global pricegst
    dt=datetime.now()
    dt=dt.strftime('%D')
    print("Bill:%s \tDate:%s" %(dt+'A', dt))
    print("Customer Name: %s" %(name))
    print("Product Name: %s" %(item[1]))
    print("Price: %s" %(price))
    print("***********************************************")
    print("\t\tTotal Bill Amount: %s" %(pricegst))
    
prod_ids=[]
file=open('inventory.csv','r')
products=[]
for line in file:
    products.append(line.strip())
all_products=[]
for i in range(len(products)):
    all_products.append(products[i].split(','))
try:
    
    while True:
        banner()
        choice = int(input())
        if choice == 1:
            display_all()
        elif choice == 2:
            display_all()
            prod_id = int(input("Enter the Product ID: "))
            for i in all_products:
                prod_ids.append(int(i[0]))
            if prod_id in prod_ids:
                item=all_products[prod_id-1]
                qty=int(input('How many? \n to check out press q')) 
                if qty=='q' or qty=='Q':
                    break
                if qty>int(item[2]):
                    print('out of stock')
                    continue
                name = input("Customer Name: ")
                order_summary(item, name,qty)
                cnf = input("Confirm the Order(Y/N)")
                if cnf == 'Y' or cnf=='y':
                    item[2]=int(item[2])
                    item[2] -= qty
                    generate_bill(item, name)
                    print("Thanks For shopping with Us")
                else:
                    print("Continue Exploring the shop")
            else:
                print('Not available')
                break
        elif choice == 3:
            username = input("Enter Admin UserID: ")
            password = input("Enter the Password: ")
            if username == "Admin" and password == "password":
                file=open('inventory.csv','a')
                prod = []
                prod.append(len(all_products)+1)
                prod.append(input("Enter the Product Name: "))
                prod.append(int(input("Quantity: ")))
                prod.append(input("Rate: ")+'$')
                all_products.append(prod)
                line=''
                line+=str(prod[0])+','+prod[1]+','+str(prod[2])+','+prod[3]
                file.write(line)
            else:
                print("Incorrect username and password")
        else:
            print("GoodBye!!")
            break

except:
    print('seed file not found')
finally:
    file.close()
