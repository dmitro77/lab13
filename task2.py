from childClass import Child

childList = (Child(sn="Karakovych Tina", year=2017), Child(sn="Semenko Ivan", year=2016), Child(sn="Bardzo Keka", year=2021))

toSchoolList = []
for child in childList:
    if (6 <= child.getAge() >= 7):
        toSchoolList.append(child)

toKindergardenList = []
for child in childList:
    if (child.getAge() == 3):
        toKindergardenList.append(child)

print("\nTo School: ")
for child in toSchoolList:
    print(child)
    
print("\nTo Kindergraden: ")
for child in toKindergardenList:
    print(child)
