print("***********************************************************")
print("      My Mobiles Shop       ")
print("***********************************************************")
n= int(input('1.Show All Products\n2.Buy Product\n3.Add Product\n4.Exit\n'))

SNO=['SNO',1,2,3,4,5]
Product=['Product','SmartPhone','HeadPhones','ScreenGaurd','Chargers','MemoryCards']
In_Stock=['   InStock',20,100,200,100,120]
Price=['Price',2000,3000,50,100,250]
while(1):
    
    if n==1:
        for i in range(len(Product)):
            print(SNO[i],Product[i], In_Stock[i], Price[i],sep='\t')
        n= int(input('1.Show All Products\n2.Buy Product\n3.Add Product\n4.Exit\n'))
    elif n==2:
        a,m,q=input('Enter customer name:'), int(input('Enter the product ID:',)),int(input('Quantity:'))
        if q>In_Stock[m]:
            print('not enough qty')
        print("***********************************************************")  
        print("      My Mobiles Shop Bill     ")
        print("***********************************************************")  
        #k= int(input('1.Customer name\n2.Product ID\n3.Amount\n'))

        print('Cutomer name:', a)
        print('Product ID:', m)
        print('Price:', q*Price[m])
        
        In_Stock[m]=In_Stock[m]-q
        n= int(input('1.Show All Products\n2.Buy Product\n3.Add Product\n4.Exit\n'))
    elif n==3:
        p,i,pr = input('Enter name'),int(input('In_Stock')),int(input('Price'))
        Product.append(p)
        In_Stock.append(i)
        Price.append(pr)
        w=len(SNO)
        SNO.append(w)
        n= int(input('1.Show All Products\n2.Buy Product\n3.Add Product\n4.Exit\n'))
    elif n==4:
        break
