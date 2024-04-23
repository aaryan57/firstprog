data = [
["sunny","hot","high","false","no"],
["sunny","hot","high","true","no"],
["overcast","hot","high","false","yes"],
["rain","mild","high","false","yes"],
["rain","cool","normal","false","yes"],
["rain","cool","normal","true","no"],
["overcast","cool","normal","true","yes"],
["sunny","mild","high","false","no"],
["sunny","cool","normal","false","yes"],
["rain","mild","normal","false","yes"],
["sunny","mild","normal","true","yes"],
["overcast","mild","high","true","yes"],
["overcast","hot","normal","false","yes"],
["rain","mild","high","true","no"]
]

def predict(string):
    fy=sy=ty=cy=yes=0
    fn=sn=tn=cn=no=0
    size=len(data)
    for row in data:
        outlook, temprature, humidity, windy, prob = row[0], row[1], row[2], row[3], row[4]
        if(prob=="yes"):
            yes+=1
            if(outlook==string[0]):
                fy+=1
            if(temprature==string[1]):
                sy+=1
            if(humidity==string[2]):
                ty+=1
            if(windy==string[3]):
                cy+=1
        else:
            no+=1
            if (outlook == string[0]):
                fn += 1
            if (temprature == string[1]):
                sn += 1
            if (humidity == string[2]):
                tn += 1
            if (windy == string[3]):
                cn += 1
    fy=fy/yes
    sy=sy/yes
    ty=ty/yes
    cy=cy/yes
    yes=yes/size
    fn=fn/no
    sn=sn/no
    cn=cn/no
    tn=tn/no
    no=no/size
    yess=yes*fy*sy*ty*cy
    noo=no*fn*tn*sn*cn

    print("p ",yess)
    print("p",noo)
    if yess>noo:
        print("yes")
    else:
        no

string=input("enter string")
string=string.split()
predict(string)









