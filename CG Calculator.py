shapes=['Circle','Rectangle','Triangle','Ishape','Cshape','Lshape','Tshape' ]
print(shapes)
x=input("Select object: ")

if x=='Circle':
    input("Enter radius: ")
    print("CG of circle is (0,0)")
    
elif x=='Rectangle':
    l=input("Enter length: ")
    b=input("Enter width: ")
    y="{:.2f}".format((float(l)/2, float(b)/2))
    print("CG of rectangle is ", y)
    
elif x=='Triangle':
    b=input("Enter base: ")
    h=input("Enter hieght: ")
    y="{:.2f}".format((float(b)/3,float(h)/3))
    print("CG of Triangle is ", y)   

elif x== 'Ishape':
    h=input("Enter hieght: ")
    b1=input("Enter width of base, b1: ")
    b2=input("Enter width of top face, b2: ")
    b3=input("Enter width of mid-face, t3: ")
    t1=input("Enter thickness, t1: ")
    t2=input('Enter thickness, t2: ')
    a1=float(b1)*float(t1)
    a2=float(b2)*float(t2)    
    a3=(float(h)-float(t1)-float(t2))*float(b3)
    y1=float(t1)/2
    y2=float(h)-(float(t2)/2)
    y3=(float(h)-float(t1)-float(t2))/2+(float(t1))    
    x="{:.2f}".format(float(b1)/2)
    y="{:.2f}".format(((a1*y1)+(a2*y2)+(a3*y3))/(a1+a2+a3))
    print("CG of Ishape is ", (x,y))

elif x=='Cshape':
    h=input("Enter hieght: ")
    b1=input("Enter base, b1: ")
    b2=input("Enter base, b2: ")
    t1=input("Enter thickness, t1: ")
    t2=input("Enter thickness, t2: ")
    t3=input("Enter thickness, t3: ")
    a1=(float(b1)-float(t3))*float(t1)
    a2=(float(b2)-float(t3))*float(t2)
    a3=float(h)*float(t3)    
    y1=float(t1)/2
    y2=float(h)-(float(t2)/2)
    y3=float(h)/2
    x1=(float(b1)-float(t3))/2+(float(t3))
    x2=(float(b2)-float(t3))/2+(float(t3))
    x3=float(t3)/2
    x="{:.2f}".format(((a1*x1)+(a2*x2)+(a3*x3))/(a1+a2+a3))
    y="{:.2f}".format(((a1*y1)+(a2*y2)+(a3*y3))/(a1+a2+a3))
    print("CG of Cshape is ", (x,y))

elif x=='Lshape':   
     h=input("Enter hieght,h : ")
     b=input("Eneter base length, b: ")
     t1=input("Enter thickness t1: ")
     t2=input("Enter thickness t2: ")
     a1=float(h)*(float(t1))
     a2=(float(b)-float(t1))*float(t2)
     x1=float(t1)/2
     x2=(float(b)-float(t1))/2 + (float(t1))
     y1=float(h)/2
     y2=float(t2)/2
     x="{:.2f}".format(((a1*x1)+(a2*x2))/(a1+a2))
     y="{:.2f}".format(((a1*y1)+(a2*y2))/(a1+a2))
     print("CG of L shape is ", (x,y))