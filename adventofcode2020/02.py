
def readFileLines(file):
    f = open(file);
    data = f.read()
    f.close()
    return data.split("\n")


lines = readFileLines("02.input.txt")
right=0
for line in lines:
    length=len(line)
    x=0
    tracker=0
    rang=""
    rang2=""
    lettertrigger=""
    triggered=0
    
    while x!=length:
        letter=line[x]
        if tracker==0:
            if letter!="-":
                rang=rang+letter
            else:
                tracker=1
        if tracker==1:
            if letter!=" " and letter!="-":
                rang2=rang2+letter
            if letter==" ":
                tracker=2
                rang=int(rang)
                rang2=int(rang2)
        if tracker==2:
            if letter!=" " and letter!=":":
                lettertrigger=letter
            if letter==":":
                tracker=3
        x=x+1
    line=line.replace("-","")
    line=line.replace(":","")
    line=line.replace("1","")
    line=line.replace("2","")
    line=line.replace("3","")
    line=line.replace("4","")
    line=line.replace("5","")
    line=line.replace("6","")
    line=line.replace("7","")
    line=line.replace("8","")
    line=line.replace("9","")
    line=line.replace("0","")
    line=line.replace(" ","")
    if line[rang]==lettertrigger:
        triggered=triggered+1
    if line[rang2]==lettertrigger:
        triggered=triggered+1
    
    print(line)
    if triggered==1:
        right=right+1
        print(right)


