import random
import pyfiglet

def total():
    import mysql.connector as a
    mycon = a.connect(host='localhost', user='root', passwd='password', database='project')
    cursor = mycon.cursor()
    query = 'update fees set total=tuitionfeesemester1+tuitionfeesemester2+transportfeesemester1+transportfeesemester2'
    cursor.execute(query)
    mycon.commit()
    mycon.close()


def noavailnopickupanddroppoints():
    import mysql.connector as a
    mycon = a.connect(host='localhost', user='root', passwd='password', database='project')
    cursor = mycon.cursor()
    query = 'select * from transport'
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        if row[2] in ['NULL', 'Null', 'null', 'no', 'NO', 'No']:
            query1 = 'update transport set pickup=NULL,droppoint=NULL where grno=%s'
            cursor.execute(query1, (row[0],))

    mycon.close()


def noavailnofees(grno):
    import mysql.connector as a
    mycon = a.connect(host='localhost', user='root', passwd='password', database='project')
    cursor = mycon.cursor()
    query1 = 'select * from transport where grno=%s'
    data1 = (grno,)
    cursor.execute(query1, data1)
    data = cursor.fetchall()
    for row in data:
        if row[2] in ('null', 'Null', 'NULL', 'NO', 'no', 'No','n','N'):
            query2 = 'update fees set transportfeesemester1=0,transportfeesemester2=0,status3=0,status4=0'
            cursor.execute(query2)
            mycon.commit()


def check(n):
    import mysql.connector as a
    mycon = a.connect(host='localhost', user='root', passwd='password', database='project')
    cursor = mycon.cursor()
    query = 'select * from student'
    cursor.execute(query)
    data = cursor.fetchall()
    toggle = 1
    for row in data:
        if row[0] == n:
            toggle = 2
            break
    if toggle == 1:
        print("THE ADMISSION NUMBER IS INCORRECT".center(110,'-'))
        print("PLEASE TRY AGAIN OR REGISTER A NEW STUDENT".center(110,'-'))
        main()


def admissionnumber():
    string = ''
    for a in range(0, 5):
        string += str(random.randint(1, 9))
    str1 = int(string)
    import mysql.connector as a
    mycon = a.connect(host='localhost', user='root', passwd='password', database='project')
    cursor = mycon.cursor()
    query = 'select * from student'
    cursor.execute(query)
    data = cursor.fetchall()
    toggle = 1
    for row in data:
        if row[0] == str1:
            toggle = 2
            break
    mycon.close()
    if toggle == 1:
        return str1
    if toggle == 2:
        admissionnumber()


area = ['Sardar Patel Stadium', 'Orchird Park', 'Star Bazaar', 'Lotus School', 'Rose Wood', 'Aarohi Complex',
        'Gala Aria', 'Girdhar Nagar', 'Safal Parisar', 'Applewoods', 'Science City Circle', 'Iscon Flower',
        'Satellite Centre',
        'Reliance Fresh Bodakdev', 'Nalanda Complex', 'Vejalpur Police Station', 'Dhar Nidhar BRTS', 'Venus Park',
        'Ramdev Temple Vastrapur', 'Suncity',
        'Orchid Elegance', 'Jhansi Ki Rani Statue', 'Akshar Jyot', 'Panchavati Cross Road', 'Vishal Tower',
        'Indraprasth', 'Gala Swings']


def vs(n):
    import mysql.connector as a
    mycon = a.connect(host='localhost', user='root', passwd='password', database='project')
    cursor = mycon.cursor()
    query = 'select * from student where class=%s'
    cursor.execute(query, (n,))
    data = cursor.fetchall()
    print('%10s' % 'Admission number', '%10s' % 'Name', '%10s' % 'Class', '%10s' % 'Section', '%10s' % 'Roll Number',
          '%10s' % 'Course', '%10s' % 'Phone Number', '%10s' % 'Alternate Phone Number', '%10s' % 'Birthdate',
          '%10s' % 'Gender', '%10s' % 'Father Name', '%10s' % 'Mother Name', '%10s' % 'Area',
          '%10s' % 'Detailed location',
          '%10s' % 'Avail Transport', '%10s' % 'Email-id', '%10s' % 'Adhar Number', '%10s' % 'Sibling Info.')
    for row in data:
        print('%10s' % row[0], '%10s' % row[1], '%10s' % row[2], '%10s' % row[3],
              '%10s' % row[4], '%10s' % row[5], '%10s' % row[6], '%10s' % row[7],
              '%10s' % row[8], '%10s' % row[9], '%10s' % row[10], '%10s' % row[11], '%10s' % row[12],
              '%10s' % row[13], '%10s' % row[14], '%10s' % row[15], '%10s' % row[16], '%10s' % row[17])


def vss(n):
    import mysql.connector as a
    mycon = a.connect(host='localhost', user='root', passwd='password', database='project')
    cursor = mycon.cursor()
    query = 'select * from student where grno=%s'
    cursor.execute(query, (n,))
    data = cursor.fetchall()
    print('%10s' % 'Admission number', '%10s' % 'Name', '%10s' % 'Class', '%10s' % 'Section', '%10s' % 'Roll Number',
          '%10s' % 'Course', '%10s' % 'Phone Number', '%10s' % 'Alternate Phone Number', '%10s' % 'Birthdate',
          '%10s' % 'Gender', '%10s' % 'Father Name', '%10s' % 'Mother Name', '%10s' % 'Area',
          '%10s' % 'Detailed location',
          '%10s' % 'Avail Transport', '%10s' % 'Email-id', '%10s' % 'Adhar Number', '%10s' % 'Sibling Info.')
    for row in data:
        print('%10s' % row[0], '%10s' % row[1], '%10s' % row[2], '%10s' % row[3],
              '%10s' % row[4], '%10s' % row[5], '%10s' % row[6], '%10s' % row[7],
              '%10s' % row[8], '%10s' % row[9], '%10s' % row[10], '%10s' % row[11], '%10s' % row[12],
              '%10s' % row[13], '%10s' % row[14], '%10s' % row[15], '%10s' % row[16], '%10s' % row[17])


from getpass import getpass


def login():
    user = 'SASadmin'

    password = '12345'
    u = input("PLEASE ENTER THE USER ID TO SIGN-IN: ")
    p = getpass("PLEASE ENTER THE PASSWORD(Not displayed because of security reasons): ")

    if u != user or p != password:
        print('INCORRECT ID OR PASSWORD'.center(110, '*'))
        login()
    else:
        main()


def main():
    print(pyfiglet.figlet_format("SHANTI ASIATIC SCHOOL,AHMEDABAD", font="digital", justify="center", width=110))
    print("1. STUDENT DEPARTMENT".center(110, '-'))
    print("2. TRANSPORT".center(110, '-'))
    print("3. FEES".center(110, '-'))
    print("4. EXIT".center(110, '-'))
    print()
    ch = int(input("PLEASE ENTER THE VALID CHOICE: "))
    if ch == 1:
        print(pyfiglet.figlet_format("STUDENT DEPARTMENT", font='digital', justify='center', width=110))

        print('1. VIEW STUDENTS'.center(110, '-'))
        print('2. MODIFY STUDENT DETAILS'.center(110, '-'))
        print('3. REGISTER A NEW STUDENT'.center(110, '-'))
        print('4. EXIT'.center(110, '-'))
        ch1 = int(input("Please enter the valid choice:"))
        if ch1 == 1:
            
            print(pyfiglet.figlet_format('VIEW STUDENT', font='digital', justify='center', width=110))
            print('1. VIEW SINGLE STUDENT'.center(110, '-'))
            print('2. VIEW A CLASS'.center(110, '-'))
            print('3. EXIT'.center(110, '-'))
            print()
            ch2 = int(input("PLEASE ENTER A VALID CHOICE: "))
            print()
            if ch2 == 1:
                grno = int(input("PLEASE ENTER THE ADMISSION NUMBER OF THE WARD:"))
                check(grno)
                vss(grno)
                main()
            elif ch2 == 2:
                classvalue = int(input("PLEASE ENTER THE CLASS(9/10/11/12):  "))
                vs(classvalue)
                main()
            elif ch2 == 3:
                main()

            else:
                print("INVALID CHOICE".center(110, '-'))
                main()

        elif ch1 == 2:
            grno = int(input("PLEASE ENTER THE ADMISSION NUMBER NUMBER OF THE WARD: "))
            check(grno)
            vss(grno)
            d1 = {1: 'section', 2: 'rollno', 3: 'course', 4: 'phoneno', 5: 'alternatephoneno', 6: 'area',
                  7: 'detailedlocation', 8: 'availtransport', 9: 'emailid',
                  10: 'adharno', 11: 'siblinginfo'}
            print()
            print("WHAT DO YOU WISH TO UPDATE?".center(110, '-'))
            
            print("1.SECTION".center(110,' '))
            print("2.ROLL NUMBER".center(110,' '))
            print('3.COURSE'.center(110,' '))
            print('4.PHONE NUMBER'.center(110,' '))
            print('5.ALTERNATE PHONENUMBER'.center(110,' '))
            print('6.AREA'.center(110,' '))
            print('7.DETAILED LOCATION'.center(110,' '))
            print('8.AVAIL TRANSPORT'.center(110,' '))
            print('9.EMAIL-ID'.center(110,' '))
            print('10.AADHAR NUMBER'.center(110,' '))
            print('11.SIBLING INFO'.center(110,' '))
            c1 = int(input("Please enter the valid choice: "))
            if c1 in [1,3,4,5,6,7,8,9,10,11]:
                print()
                new=input("PLEASE ENTER THE NEW MODIFIED VALUE: ")
            else:
                print()
                new=int(input("PLEASE INPUT THE REQUIRED MODIFIED VALUE(in numbers):  "))
            import mysql.connector as a
            mycon = a.connect(host='localhost', user='root', passwd='password', database='project')
            cursor = mycon.cursor()
            query = 'update student set j=%s where grno=%s'.replace('j',d1[c1])
            data = (new, grno)
            cursor.execute(query, data)
            mycon.commit()
            print()
            print("THE DATA HAS BEEN SUCCESSFULLY UPDATED IN THE STUDENT DEPARTMENT".center(110,' '))
            mycon.close()

            if c1 in [1, 6, 7, 8]:
                import mysql.connector as a
                mycon = a.connect(host='localhost', user='root', passwd='password', database='project')
                cursor = mycon.cursor()
                query = 'update transport set j=%s where grno=%s'.replace('j',d1[c1])
                data = (new, grno)
                cursor.execute(query, data)
                mycon.commit()
                print("THE DATA HAS BEEN SUCCESSFULLY UPDATED IN THE TRANSPORT DEPARTMENT".center(110,' '))
                mycon.close()
            

            noavailnofees(grno)
            noavailnopickupanddroppoints()
            total()
            main()









        elif ch1 == 3:

            d2 = {9: 60000, 10: 60000, 11: 80000, 12: 80000}
            print()
            print("SOME OF THE INFORMATION CANNOT BE CHANGED LATER".center(110,'*'))
            print("PLEASE FILL THE DETAILS CAREFULLY".center(110,'*'))
            print()

            print("BASIC INFO".center(110, '-'))
            print('*  ---------------  REQUIRED FIELD')
            grno = admissionnumber()
            name = input("Please enter the name of the ward*: ")
            classno = int(input("Please enter the class(9/10/11/12)*: "))
            section = input('Please enter the section of the ward(A/B/C/D/E/F/G/H)*: ')
            rollno = int(input("Please enter the roll number(1-30)*: "))
            course = input("Please enter the course chosen by the student(PCM,PCMB,HUMANITIES,COMMERCE)*:")
            print('COMMUNICATIONS'.center(110, '-'))
            phoneno = input("Please enter a valid phone number*: ")
            alternatephoneno = input("Please enter an aletrnate phone number(input NULL elsewise): ")
            by = input("Please enter the birth year of the ward(YYYY)*: ")
            bm = input("Please enter the birth month of the ward(MM)*: ")
            bd = input("Please enter the birthdate of the ward(DD)*: ")
            dateofbirth = by + '-' + bm + '-' + bd
            gender = input("Please enter the gender of the person(M/F)*: ")
            fathername = input("Please enter the name of the father of the ward*: ")
            mothername = input("Please enter the name of the mother of the ward*:")
            print("THESE ARE THE AREAS NEAR THE SCHOOL".center(110, '-'))
            for a in area:
                print(a.center(110, '-'))
            print()
            area2 = input("Please enter the area of the ward for the list above*: ")
            detailedarea = input("Please enter the detailed area of the student*: ")
            emailid = input("Please enter the email of the ward*: ")
            print('DOCUMENTS'.center(110,'-'))
            aadharnumber = input("Please enter the aadhar number of the ward*: ")
            sibling = input("Do you wish to enter the class of your sibling(if any)(if not,then enter 'NULL': ")
            transport = input("Do you wish to avail transport?(YES/NULL)(If not then enter 'NULL'): ")
            if transport.lower == 'yes':
                transport = 'YES'
                print()
                print("Please register in the transport department after this.........")

            import mysql.connector as a
            mycon = a.connect(host='localhost', user='root', passwd='password', database='project')
            cursor = mycon.cursor()
            query1 = 'insert into student values(%s,"%s",%s,"%s",%s,"%s",%s,%s,%s,"%s","%s","%s","%s","%s","%s","%s","%s","%s")'
            query2 = 'insert into transport(grno,name,availtransport,class,section,area,detailedlocation) values(%s,"%s","%s",%s,"%s","%s","%s")'
            data1 = (grno, name, classno, section, rollno, course, phoneno, alternatephoneno, dateofbirth, gender,fathername,mothername, area2, detailedarea, transport, emailid, aadharnumber, sibling)
            data2 = (grno, name, transport, classno, section, area2, detailedarea)
            print(data1)
            print(data2)
            cursor.execute(query1, data1)
            mycon.commit()
            print()
            print("The student has been successfully registered".center(110,' '))
            print("THE ADMISSION NUMBER OF THE STUDENT REGISTERED".center(110,'-'))
            print(pyfiglet.figlet_format(str(grno),font='digital',justify='center',width=110))
            print()
            
            cursor.execute(query2, data2)
            mycon.commit()
            print("TRANSPORT DEPARTMENT HAS BEEN UPDATED.PLEASE CHECK AFTER THIS".center(110, '-'))
            query3 = 'insert into fees(grno,tuitionfeesemester1,status1,tuitionfeesemester2,status2,total,status5) values(%s,%s,"Not Paid",%s,"Not Paid",%s,"Not Paid")'
            z=d2[classno] + d2[classno]
            data3 = (grno, d2[classno], d2[classno],z)
            cursor.execute(query3, data3)
            mycon.commit()
            print("FEES DEPARTMENT HAS BEEN UPDATED,PLEASE CHECK AFTER THIS.".center(110, '-'))

            mycon.close()
            noavailnofees(grno)
            noavailnopickupanddroppoints()
            total()
            main()







        elif ch1 == 4:
            main()
        else:
            print("INVALID CHOICE".center(110, '-'))
            main()
    elif ch == 2:

        print(pyfiglet.figlet_format("TRANSPORTATION DEPARTMENT", font='digital', justify='center', width=110))
        print("1. VIEW DETAILS".center(110, '-'))
        print("2. REGISTER FOR TRANSPORT FACILITIES".center(110, '-'))
        print("3. MODIFY PICKUP/DROP POINTS".center(110, '-'))
        print("4. EXIT".center(110, '-'))

        c7 = int(input("PLEASE ENTER THE VALID CHOICE: "))
        if c7 == 1:
            grno = int(input("PLEASE ENTER THE ADMISSION NUMBER OF THE WARD: "))
            check(grno)

            import mysql.connector as a
            mycon = a.connect(host='localhost', user='root', passwd='password', database='project')
            cursor = mycon.cursor()
            query = 'select * from transport where grno=%s'
            cursor.execute(query, (grno,))
            data = cursor.fetchall()
            print('%10s' % 'Admission number', '%10s' % 'Name', '%10s' % 'Availing Transport', '%10s' % 'Class',
                  '%10s' % 'Section',
                  '%10s' % 'Area', '%10s' % 'Detailed Location', '%10s' % 'Pickup Point', '%10s' % 'Drop Point')
            for row in data:
                print('%10s' % row[0], '%10s' % row[1], '%10s' % row[2], '%10s' % row[3],
                      '%10s' % row[4], '%10s' % row[5], '%10s' % row[6], '%10s' % row[7],
                      '%10s' % row[8])
            main()

        elif c7 == 2:
            grno = int(input("PLEASE ENTER THE ADMISSION NUMBER OF THE WARD: "))
            check(grno)

            import mysql.connector as a
            mycon = a.connect(host='localhost', user='root', passwd='password', database='project')
            cursor = mycon.cursor()
            query = 'select * from transport where grno=%s'
            cursor.execute(query, (grno,))
            data = cursor.fetchall()
            print('%10s' % 'Admission number', '%10s' % 'Name', '%10s' % 'Availing Transport', '%10s' % 'Class',
                  '%10s' % 'Section',
                  '%10s' % 'Area', '%10s' % 'Detailed Location', '%10s' % 'Pickup Point', '%10s' % 'Drop Point')
            y = 0
            for row in data:
                print('%10s' % row[0], '%10s' % row[1], '%10s' % row[2], '%10s' % row[3],
                      '%10s' % row[4], '%10s' % row[5], '%10s' % row[6], '%10s' % row[7],
                      '%10s' % row[8])
                y = row[5]

            mycon.close()
            print()

            ans = input("Are the fields 'AVAILING TRANSPORT','AREA','DETAILED LOCATION' displaying correct information?(y/n): ")
            if ans.lower() == 'y':
                d3 = {'Sardar Patel Stadium': 17500, 'Orchird Park': 15000, 'Star Bazaar': 15000, 'Lotus School': 16100,
                      'Rose Wood': 16000, 'Aarohi Complex': 13600,
                      'Gala Aria': 13600, 'Girdhar Nagar': 18500, 'Safal Parisar': 15000, 'Applewoods': 7500,
                      'Science City Circle': 15000, 'Iscon Flower': 14000, 'Satellite Centre': 16300,
                      'Reliance Fresh Bodakdev': 16100, 'Nalanda Complex': 16000, 'Vejalpur Police Station': 15300,
                      'Dhar Nidhar BRTS': 16700, 'Venus Park': 15000, 'Ramdev Temple Vastrapur': 17000,
                      'Suncity': 15000,
                      'Orchid Elegance': 12000, 'Jhansi Ki Rani Statue': 16500, 'Akshar Jyot': 16400,
                      'Panchavati Cross Road': 18500, 'Vishal Tower': 16500, 'Indraprasth': 15500, 'Gala Swings': 13700}
                print()
                pickup = input("PLEASE ENTER THE PICKUP POINT: ")
                droppoint = input("PLEASE ENTER THE DROP POINT: ")
                import mysql.connector as a
                mycon = a.connect(host='localhost', user='root', passwd='password', database='project')
                cursor = mycon.cursor()
                query = 'update transport set pickup="%s",droppoint="%s" where grno=%s'
                data = (pickup, droppoint, grno)
                cursor.execute(query, data)
                mycon.commit()
                print("The Pickup And Drop Points have been updated.".center(110,'-'))
                print("PLEASE NOTE THAT THE TRANSPORT FEES ARE NON REFUNDABLE".center(110,'-'))
                
                if y not in d3.keys():
                    query2 = 'update fees set transportfeesemester1=%s,transportfeesemester2=%s,status3="Not Paid",status4="Not Paid" where grno=%s'
                    data2 = (18000, 18000, grno)
                else:
                    query2 = 'update fees set transportfeesemester1=j,transportfeesemester2=j,status3="Not Paid",status4="Not Paid" where grno=%s'.replace('j',d3[y])
                    data2 = (grno,)
                cursor.execute(query2, data2)
                mycon.commit()
                total()
                print("THE FEES DEPARTMENT HAS BEEN MODIFIED.PLEASE CHECK AFTER THIS.".center(110,'-'))
                total()
                main()







                
            else:
                print('Please do the necessary changes in the Student Department first.Only then can you register for using '
                    'transport facilities of Shanti Asiatic School'.center(110,' '))
                total()
                main()
            
            
        elif c7 == 3:

            grno = int(input("PLEASE ENTER THE ADMISSION NUMBER OF THE WARD: "))
            check(grno)

            import mysql.connector as a
            mycon = a.connect(host='localhost', user='root', passwd='password', database='project')
            cursor = mycon.cursor()
            query = 'select * from transport where grno=%s'
            cursor.execute(query, (grno,))
            data = cursor.fetchall()
            print('%10s' % 'Admission number', '%10s' % 'Name', '%10s' % 'Availing Transport', '%10s' % 'Class',
                  '%10s' % 'Section',
                  '%10s' % 'Area', '%10s' % 'Detailed Location', '%10s' % 'Pickup Point', '%10s' % 'Drop Point')
            for row in data:
                print('%10s' % row[0], '%10s' % row[1], '%10s' % row[2], '%10s' % row[3],
                      '%10s' % row[4], '%10s' % row[5], '%10s' % row[6], '%10s' % row[7],
                      '%10s' % row[8])
            mycon.close()
            print()

            ans = input("Are the fields 'Availing Transport','Area','Detailed Location' displaying correct information AND are you registered with pickup/drop points already?(y/n): ")
            if ans.lower() == 'n':
                print()
                print("THEN YOU NEED TO GO TO THE STUDENT DEPARTMENT AND MODIFY THE NECESSARY DETAILS [or] REGISTER WITH TRANSPORT DEPARTMENT".center(110,' '))
                print()
                print("ONLY THEN CAN YOU CHANGE THE PICKUP/DROP POINTS".center(110,' '))
                total()
                main()
            else:
                pickup = input("Please enter the new Pickup Point: ")
                droppoint = input("Please enter the new Drop Point: ")
                import mysql.connector as a
                mycon = a.connect(host='localhost', user='root', passwd='password', database='project')
                cursor = mycon.cursor()
                query = 'update transport set pickup="%s",droppoint="%s" where grno=%s'
                data = (pickup, droppoint, grno)
                cursor.execute(query, data)
                print("The Pickup And Drop Points have been updated.".center(110,' '))
                total()
                main()



        elif c7 == 4:
            main()
        else:
            print('INVALID CHOICE'.center(110, '-'))
            main()


    elif ch == 3:

        print(pyfiglet.figlet_format("FEES DEPARTMENT", font='digital', justify='center', width=110))
        print("1. VIEW DETAILS".center(110, '-'))
        print("2. UPDATE DETAILS".center(110, '-'))
        print("3. EXIT".center(110, '-'))

        ans = int(input("PLEASE ENTER THE CORRECT CHOICE: "))
        if ans == 1:
            grno = int(input("PLEASE ENTER THE ADMSSION NUMBER OF THE WARD: "))
            check(grno)

            import mysql.connector as a
            mycon = a.connect(host='localhost', user='root', passwd='password', database='project')
            cursor = mycon.cursor()
            query = 'select * from fees where grno=%s'
            cursor.execute(query, (grno,))
            data = cursor.fetchall()
            print('%10s' % 'Admission number', '%10s' % 'Tuition Fee(Semester1)', '%10s' % 'Status-1',
                  '%10s' % 'Tuition Fee(Semester-2)',
                  '%10s' % 'Status-2',
                  '%10s' % 'Transport Fee(Semester-1)', '%10s' % 'Status-3', '%10s' % 'Transport Fee(Semester-2)',
                  '%10s' % 'Status-4', '%10s' % 'Total',
                  '%10s' % 'Status-5')
            for row in data:
                print('%10s' % row[0], '%10s' % row[1], '%10s' % row[2], '%10s' % row[3],
                      '%10s' % row[4], '%10s' % row[5], '%10s' % row[6], '%10s' % row[7],
                      '%10s' % row[8], '%10s' % row[9], '%10s' % row[10])
            mycon.close()
            main()


        elif ans == 2:
            grno = int(input("PLEASE ENTER THE ADMISSION NUMBER OF THE WARD: "))
            check(grno)

            import mysql.connector as a
            mycon = a.connect(host='localhost', user='root', passwd='password', database='project')
            cursor = mycon.cursor()
            query = 'select * from fees where grno=%s'
            cursor.execute(query, (grno,))
            data = cursor.fetchall()
            print('%10s' % 'Admission number', '%10s' % 'Tuition Fee(Semester1)', '%10s' % 'Status-1',
                  '%10s' % 'Tuition Fee(Semester-2)',
                  '%10s' % 'Status-2',
                  '%10s' % 'Transport Fee(Semester-1)', '%10s' % 'Status-3', '%10s' % 'Transport Fee(Semester-2)',
                  '%10s' % 'Status-4', '%10s' % 'Total',
                  '%10s' % 'Status-5')
            for row in data:
                print('%10s' % row[0], '%10s' % row[1], '%10s' % row[2], '%10s' % row[3],
                      '%10s' % row[4], '%10s' % row[5], '%10s' % row[6], '%10s' % row[7],
                      '%10s' % row[8], '%10s' % row[9], '%10s' % row[10])
            mycon.close()
            
            
            print('1.Status-1'.center(110,' '))
            print('2.Status-2'.center(110,' '))
            print('3.Status-3'.center(110,' '))
            print('4.Status-4'.center(110,' '))
            print('5.Status-5'.center(110,' '))

            d5 = {1: 'status1', 2: 'status2', 3: 'status3', 4: 'status4', 5: 'status5'}
            import mysql.connector as a
            mycon = a.connect(host='localhost', user='root', passwd='password', database='project')
            cursor = mycon.cursor()
            

            ans = int(input("Please enter the field to be updated: "))
            value = input("Enter the new value of the Field(PAID/NOT PAID): ")
            query4 = 'update fees set x=%s where grno=%s'.replace('x', d5[ans])
            data3 = [value, grno]
            cursor.execute(query4, data3)
            mycon.commit()
            print("The changes have been saved.".center(110,' '))
            total()
            main()




        elif ans == 3:
            main()
        else:
            print("INVALID CHOICE".center(110, '-'))
            main()

    elif ch == 4:
        print(pyfiglet.figlet_format('THANK YOU FOR BEING WITH US',font='digital',justify='center',width=110))

    else:
        print('INVALID CHOICE'.center(110, '-'))
        main()


login()
