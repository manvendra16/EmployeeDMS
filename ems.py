import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     database='ems',
                                     user='root',
                                     password='mannu123')

def npersonal():
    print("Enter Employee details below: ")
    n = input("Name: ").capitalize()
    c = input("City: ").capitalize()
    d = input("D.O.B: ")
    p = input("Phone: ")
    ec = input("Ecode: ")
    data = (n, c, d, p, ec)
    sql = 'insert into personal values(%s,%s,%s,%s,%s)'
    a = connection.cursor()
    a.execute(sql, data)
    connection.commit()
    print("Saved Successfully")
    main()


def personal():
    sql = "select * from personal"
    a = connection.cursor()
    a.execute(sql)
    d = a.fetchall()
    for i in d:
        print(i)
    main()


def noffice():
    print("Enter Employee details below: ")
    ec = input("Employee Code: ")
    n = input("Name: ").capitalize()
    j = input("Date of Joining: ")
    bp = input("Basic Salary: ")
    ps = input("Post: ").capitalize()
    data = (ec, n, j, ps, bp)
    sql = 'insert into office values(%s,%s,%s,%s,%s)'
    a = connection.cursor()
    a.execute(sql, data)
    connection.commit()
    print("Saved Successfully")
    main()


def office():
    sql = "select * from office"
    a = connection.cursor()
    a.execute(sql)
    d = a.fetchall()
    for i in d:
        print(i)
    main()


def nsalary():
    ec = input("Employee Code: ")
    v = (ec,)
    sql = "select Basic_Pay from office where Ecode = %s"
    a = connection.cursor()
    a.execute(sql, v)
    bs = a.fetchone()
    print("Enter Employee details below: ")
    n = input("Name: ").capitalize()
    y = input("Years: ")
    m = input("Months: ")
    wd = int(input("Working Days: "))
    td = int(input("Total Working Days: "))
    fp = bs[0]/td*wd
    data = (ec, n, y, m, wd, fp)
    sql = 'insert into salary values(%s,%s,%s,%s,%s,%s)'
    a = connection.cursor()
    a.execute(sql, data)
    connection.commit()
    print("Saved Successfully")
    main()


def salary():
    sql = "select * from salary"
    a = connection.cursor()
    a.execute(sql)
    d = a.fetchall()
    for i in d:
        print(i)
    main()

def personalDetails():
    print("""
    1. Add New Employee Personal Details
    2. Display Employee's Personal Details""")
    choice = int(input("Enter your choice: "))
    while True:
        if choice == 1:
            npersonal()
        elif choice == 2:
            personal()
        else:
            print("PLEASE ENTER CORRECT CHOICE!!")
            main()
        main()

def officeDetails():
    print("""
    1. Add New Employee Office Details
    2. Display Employee's Office Details""")
    choice = int(input("Enter your choice: "))
    while True:
        if choice == 1:
            noffice()
        elif choice == 2:
            office()
        else:
            print("PLEASE ENTER CORRECT CHOICE!!")
            main()
        main()

def salaryRecords():
    print("""
    1. Add Salary Details of Employee
    2. Display Salary Details of Employee""")
    choice = int(input("Enter your choice: "))
    while True:
        if choice == 1:
            nsalary()
        elif choice == 2:
            salary()
        else:
            print("PLEASE ENTER CORRECT CHOICE!!")
            main()
        main()

def main():
    print("""
    1. Personal Details
    2. Office Details
    3. Salary Records
    4. Exit""")
    choice1 = int(input("Enter your choice: "))
    while True:
        if choice1 == 1:
            personalDetails()
        elif choice1 == 2:
            officeDetails()
        elif choice1 == 3:
            salaryRecords()
        elif choice1 == 4:
            print("Bye! Exiting...")
            exit(0)
        else:
            print("PLEASE ENTER CORRECT CHOICE!!")
            main()


main()
