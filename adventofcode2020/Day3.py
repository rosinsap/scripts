f = open("Day3input.txt", "r")
inpu=f.read()
f.close
inpu=inpu.split("\n")
x=1
at=0
bonkedtrees=0
while x!=len(inpu):
    current=inpu[x]
    at=at+3
    if at>30:
        at=at-31
    if current[at]=="#":
        bonkedtrees=bonkedtrees+1
    x=x+1
print(bonkedtrees,"right 3 down 1")
x=1
at=0
bonkedtrees=0
while x!=len(inpu):
    current=inpu[x]
    at=at+1
    if at>30:
        at=at-31
    if current[at]=="#":
        bonkedtrees=bonkedtrees+1
    x=x+1
print(bonkedtrees,"right 1 down 1")
x=1
at=0
bonkedtrees=0
while x!=len(inpu):
    current=inpu[x]
    at=at+5
    if at>30:
        at=at-31
    if current[at]=="#":
        bonkedtrees=bonkedtrees+1
    x=x+1
print(bonkedtrees,"right 5 down 1")
x=1
at=0
bonkedtrees=0
while x!=len(inpu):
    current=inpu[x]
    at=at+7
    if at>30:
        at=at-31
    if current[at]=="#":
        bonkedtrees=bonkedtrees+1
    x=x+1
print(bonkedtrees,"right 7 down 1")
x=2
at=0
bonkedtrees=0
while x!=len(inpu)-1:
    current=inpu[x]
    at=at+1
    if at>30:
        at=at-31
    if current[at]=="#":
        bonkedtrees=bonkedtrees+1
    x=x+2
print(bonkedtrees,"right 1 down 2")