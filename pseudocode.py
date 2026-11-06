def assignmentGrade(avg):
    if avg >= 80:
        print("A")
    else:
        if avg >= 70:
            print("B")
        else:
            if avg >= 60:
                print("C")
            else:
                if avg >= 50:
                    print("D")
                else:
                    print("F")
    
    return 

def calcAttendance(id):
    present = 18
    total = 20
    
    return present / total * 100

def calcAverage(id):
    pass
    
    return 65

def checkLogin():
    print("Username and password")
    user = input()
    pwd = input()
    ok = user == "admin" and pwd == "1234"
    
    return ok

def findStudent(id):
    pass
    
    return id > 0 && id <= 100

def loadData():
    print("Data loaded")

def markAttendance():
    print("Enter class and data")
    className = input()
    dataText = input()
    numStudents = int(input())
    i = i
    totalDays = 0
    daysPresent = 0
    while i <= numStudents:
        status = input()
    while status != "P" and status != "A":
        print("Enter P or A")
        status = input()
    totalDays = totalDays + 1
    if status == "P":
        daysPresent = daysPresent + 1
    i = i + 1
    saveAttendence()

def saveAttendence():
    print("Attendence saved")

def saveData():
    print("Datasaved")

def studentSummary():
    print("Enter student ID")
    studentID = int(input())
    found = findStudent(studentID)
    if found == True:
        attendancePct = calcAttendance(studentID)
        average = calcAverage(studentID)
        grade = assignGrade(average)
    else:
        print("No student found")
    if attendancePct < 75 or average < 50:
        print("ALERT: at risk")
    print("Student " + str(studentID) + " Attendance " + str(attendancePct) + "% Average " + str(average) + " Grade " + grade)

# Main
choice = 0
loadData()
loginOk = checkLogin()
if loginOk == True:
    while choice != 3:
        pass
else:
    print("Access denied")
print("1 Mark Attendance, 2 Student Summary, 3 Exit")
choice = int(input())
if choice == 1:
    markAttendance()
else:
    if choice == 2:
        studentSummary()
    else:
        saveData()
print("Goodbye")
