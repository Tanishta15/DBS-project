import mysql.connector
from prettytable import PrettyTable
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prarths@0103",
    database="dbs_proj")
cursor = conn.cursor()
#for the faculty table
def insert_faculty(name, id):
    cursor.execute('''INSERT INTO FACULTY(NAME, ID) VALUES (%s, %s)''', (name, id))
    conn.commit()
def delete_faculty(name):
    cursor.execute('''DELETE FROM FACULTY WHERE NAME = %s''', (name,))
    conn.commit()
def view_faculty():
    cursor.execute('''SELECT * FROM FACULTY''')
    result=cursor.fetchall()
    table = PrettyTable()
    table.field_names = [i[0] for i in cursor.description]
    for row in result:
        table.add_row(row)
    print(table)
#for the club table
def insert_club(club_name, year_of_formation, domain, tech_nontech, core_committee, faculty):
    year_of_formation = int(year_of_formation)
    cursor.execute('''INSERT INTO CLUB(CLUB_NAME, YEAR_OF_FORMATION, DOMAIN, TECH_NONTECH, CORE_COMMITTEE, FACULTY) VALUES (%s, %s, %s, %s, %s, %s)''', (club_name, year_of_formation, domain, tech_nontech, core_committee, faculty))
    conn.commit()
def delete_club(club_name):
    cursor.execute('''DELETE FROM CLUB WHERE CLUB_NAME = %s''', (club_name,))
    conn.commit()
def view_club():
    cursor.execute('''SELECT * FROM CLUB''')
    result=cursor.fetchall()
    table = PrettyTable()
    table.field_names = [i[0] for i in cursor.description]
    for row in result:
        table.add_row(row)
    print(table)
#for the members table
def insert_clubmember(reg_no, name, learners_id, year, department):
    cursor.execute('''INSERT INTO CLUB_MEMBERS(REG_NO, NAME, LEARNERS_ID, YEAR, DEPARTMENT) VALUES (%s, %s, %s, %s, %s)''', (reg_no, name, learners_id, year, department))
    conn.commit()
def delete_clubmember(reg_no):
    cursor.execute('''DELETE FROM CLUB_MEMBERS WHERE REG_NO = %s''', (reg_no,))
    conn.commit()
def view_clubmember():
    cursor.execute('''SELECT * FROM CLUB_MEMBERS''')
    result=cursor.fetchall()
    table = PrettyTable()
    table.field_names = [i[0] for i in cursor.description]
    for row in result:
        table.add_row(row)
    print(table)
#for the event table
def insert_event(event_name, club_name, date, time, venue, participation_fee):
    cursor.execute('''INSERT INTO EVENT(EVENT_NAME, CLUB_NAME, DATE, TIME, VENUE, PARTICIPATION_FEE) VALUES(%s, %s, %s, %s, %s, %s)''', (event_name, club_name, date, time, venue, participation_fee))
    conn.commit()
def delete_event(event_name):
    cursor.execute('''DELETE FROM EVENT WHERE EVENT_NAME = %s''', (event_name,))
    conn.commit()
def view_event():
    cursor.execute('''SELECT * FROM EVENT''')
    result=cursor.fetchall()
    table = PrettyTable()
    table.field_names = [i[0] for i in cursor.description]
    for row in result:
        table.add_row(row)
    print(table)
#for the attendance table
def insert_attendance(reg_no, event_name, date, time):
    cursor.execute('''INSERT INTO ATTENDANCE(REG_NO, EVENT_NAME, DATE, TIME) VALUES(%s, %s, %s, %s)''', (reg_no, event_name, date, time))
    conn.commit()
def delete_attendance(reg_no, event_name):
    cursor.execute('''DELETE FROM ATTENDANCE WHERE REG_NO = %s AND EVENT_NAME = %s''', (reg_no, event_name))
    conn.commit()
def view_attendance():
    cursor.execute('''SELECT * FROM ATTENDANCE''')
    result=cursor.fetchall()
    table = PrettyTable()
    table.field_names = [i[0] for i in cursor.description]
    for row in result:
        table.add_row(row)
    print(table)

def CRUD_op():
    while True:
        print("-----MENU-----")
        print("1. FACULTY\n2. CLUB\n3. CLUB MEMBERS\n4. EVENT\n5. ATTENDANCE\n6. VIEW TABLES\n7. EXIT\n")
        table_ch = input("ENTER YOUR CHOICE: ")

        if table_ch == '1':#faculty
            print("----FACULTY----")
            print("1. INSERT\n2. DELETE\n3. GO BACK\n")
            ch = input("ENTER YOUR CHOICE: ")
            if ch == '1':
                name = input("ENTER FACULTY'S NAME: ")
                id = input("ENTER THE ID NUMBER: ")
                insert_faculty(name, id)
                print("DATA ENTRY SUCCESSFUL")
            elif ch == '2':
                name = input("ENTER THE NAME TO BE DELETED: ")
                delete_faculty(name)
                print("DATA HAS BEEN DELETED")
            elif ch == '3':
                break
            else:
                print("INVALID OPTIONS")

        elif table_ch == '2':#club
            print("----CLUB----")
            print("1. INSERT\n2. DELETE\n3. GO BACK\n")
            ch = input("ENTER YOUR CHOICE: ")
            if ch == '1':
                club_name = input("ENTER THE CLUB'S NAME: ")
                year = input("ENTER THE YEAR OF FORMATION: ")
                domain = input("ENTER DOMAIN: ")
                tech_nontech = input("ENTER IF TECH OR NONTECH: ")
                core_committee = input("ENTER THE CORE MEMBERS: ")
                faculty = input("ENTER THE FACULTY INCHARGE: ")
                insert_club(club_name, year, domain, tech_nontech, core_committee, faculty)
                print("DATA ENTRY SUCCESSFUL")
            elif ch == '2':
                club_name = input("ENTER THE CLUB'S NAME TO BE DELETED: ")
                delete_club(club_name)
                print("DATA HAS BEEN DELETED")
            elif ch == '3':
                continue
            else:
                print("INVALID OPTIONS")

        elif table_ch == '3':#club members
            print("----CLUB MEMBERS----")
            print("1. INSERT\n2. DELETE\n3. GO BACK\n")
            ch = input("ENTER YOUR CHOICE: ")
            if ch == '1':
                reg_no = input("ENTER YOUR REGISTRATION NUMBER: ")
                name = input("ENTER YOUR NAME: ")
                learners_id = input("ENTER YOUR LEARNER'S ID: ")
                year = input("ENTER WHICH YEAR: ")
                department = input("ENTER WHICH DEPARTMENT: ")
                insert_clubmember(reg_no, name, learners_id, year, department)
                print("DATA ENTRY SUCCESSFUL")
            elif ch == '2':
                reg_no = input("ENTER THE REGISTRATION NUMBER TO BE DELETED: ")
                delete_clubmember(reg_no)
                print("DATA HAS BEEN DELETED")
            elif ch == '3':
                continue
            else:
                print("INVALID OPTIONS")

        elif table_ch == '4':#event
            print("----EVENT----")
            print("1. INSERT\n2. DELETE\n3. GO BACK\n")
            ch = input("ENTER YOUR CHOICE: ")
            if ch == '1':
                event_name = input("ENTER THE EVENT'S NAME: ")
                club_name = input("ENTER THE CLUB'S NAME: ")
                date = input("ENTER DATE: ")#yyyy-mm-dd
                time = input("ENTER TIME: ")
                venue = input("ENTER VENUE: ")
                fee = input("ENTER FEE: ")
                insert_event(event_name, club_name, date, time, venue, fee)
                print("DATA ENTRY SUCCESSFUL")
            elif ch == '2':
                event_name = input("ENTER THE EVENT'S NAME TO BE DELETED: ")
                delete_event(event_name)
                print("DATA HAS BEEN DELETED")
            elif ch == '3':
                continue
            else:
                print("INVALID OPTIONS")

        elif table_ch == '5':#attendance
            print("----ATTENDANCE----")
            print("1. INSERT\n2. DELETE\n3. GO BACK\n")
            ch = input("ENTER YOUR CHOICE: ")
            if ch == '1':
                reg_no = input("ENTER YOUR REGISTRATION NUMBER: ")
                event_name = input("ENTER THE EVENT NAME: ")
                date = input("ENTER DATE: ")#yyyy-mm-dd
                time = input("ENTER TIME: ")
                insert_attendance(reg_no, event_name, date, time)
                print("DATA ENTRY SUCCESSFUL")
            elif ch == '2':
                reg_no = input("ENTER THE REGISTRATION NUMBER: ")
                event_name = input("ENTER THE CLUB'S NAME TO BE DELETED: ")
                delete_attendance(reg_no, event_name)
                print("DATA HAS BEEN DELETED")
            elif ch == '3':
                continue
            else:
                print("INVALID OPTIONS")

        elif table_ch == '6':#viewing table
            print("----VIEW----")
            print("1. FACULTY\n2. CLUB\n3. CLUB MEMBERS\n4. EVENT\n5. ATTENDANCE\n6. GO BACK\n")
            ch=input("ENTER YOUR CHOICE: ")
            
            if ch=='1':
                view_faculty()
            elif ch=='2':
                view_club()
            elif ch=='3':
                view_clubmember()
            elif ch=='4':
                view_event()
            elif ch=='5':
                view_attendance()
            elif ch=='6':
                continue
            else:
                print("INVALID CHOICE")
            
        elif table_ch=='7':#exit
            break

        else:
            print("INVALID CHOICE")

CRUD_op()
cursor.close()
conn.close()