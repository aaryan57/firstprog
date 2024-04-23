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
    size=len(data)
    Fy=Sy=Ty=Cy=yess=0
    Fn=Sn=Tn=Cn=no=0
    for row in data:
        outlook,temprature,humidity,windy,prob=row[0],row[1],row[2],row[3],row[4]
        if(prob=="yes"):
            yess+=1
            if(outlook==string[0]):
                Fy+=1
            if (temprature == string[1]):
                Sy += 1
            if (humidity == string[2]):
                Ty += 1
            if (windy == string[3]):
                Cy += 1
        else:
            no+=1
            if (outlook == string[0]):
                Fn += 1
            if (temprature == string[1]):
                Sn += 1
            if (humidity == string[2]):
                Tn += 1
            if (windy == string[3]):
                Cn += 1

    Fy=Fy/yess
    Sy=Sy/yess
    Ty=Ty/yess
    Cy=Cy/yess
    yess=yess/size
    Fn=Fn/no
    Sn=Sn/no
    Tn=Tn/no
    Cn=Cn/no
    no=no/size

    pYes=yess*Fy*Sy*Ty*Cy
    pNo=no*Fn*Sn*Tn*Cn

    print("pYes=",pYes)
    print("pNo=",pNo)
    if(pYes>pNo):
        print("yes")
    else:
        print("no")

string=input("enter the string")
string=string.split(' ')
print(string)
predict(string)

