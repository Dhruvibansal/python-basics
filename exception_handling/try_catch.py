while(1):
  try:
    a=int (input("enter any number"))
    b=int (input("enter any number"))
    ch = input()
  except ValueError:
    print('something fishy')
    continue
  finally:
    try:
      if ch=='+':
        print(a+b)
      elif ch== '-':
        print(a-b)
      elif ch== '*':
        print(a*b)
      elif ch== '/':
        print(a/b) 
      else:
        print('something fishy')
    except:
      print('biee')
    if a==100:
      break
