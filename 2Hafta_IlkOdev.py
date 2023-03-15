students = ["Simge İsik", "Hazal Ates", "Mert Cardak"]

print("**********************")
#öğrenci ekleme 
students.append("Melike Çardak")
print(students)

print("**********************")
#öğrenci silme
students.pop(2)
print(students)

print("**********************")
#listeye birden fazla ögrenci ekleme
students.extend(["Eymen Cinar", "Onur Karaca", "Oguzhan Karaca"])
print(students)

print("**********************")
#tüm ögrencileri tek tek yazdıran
for i in range(len(students)):
    print(students[i])
    
print("**********************")    
#Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
print("Student number: ",students.index("Simge İsik")," || ","Student name:",students[0])
print("Student number: ",students.index("Hazal Ates")," || ","Student name:",students[1])
print("Student number: ",students.index("Melike Çardak")," || ","Student name:",students[2])


print("**********************")    
#birden çok öğrenciyi silmeyi mümkün kılan 
def removeStudents():
    number = int(input("Kaç kişiyi silmek istersiniz? :"))
    newList = []
    i = 0
    while i < number:
        removedStudent = input("Silinmesini istediğiniz öğrencinin adı : ")
        i += 1
        newList.append(removedStudent)
        for student in students:
            if student in newList:
                students.remove(student)
    print(students)

removeStudents()
