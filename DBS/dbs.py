import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prarths@0103",
    database="dbs_proj")
cursor=conn.cursor()

def insert_faculty(name,id):
    cursor.execute('''INSERT INTO FACULTY(NAME,ID) VALUES (%s,%s)''',(name,id))
    conn.commit()
def insert_club(club_name,year_of_formation,domain,tech_nontech,core_committe,faculty):
    cursor.execute('''INSERT INTO CLUB(CLUB_NAME,YEAR_OF_FORMATION,DOMAIN,TECH_NONTECH,CORE_COMMITEE,FACULTY) VALUES (%s,%s,%s,%s,%s,%s)''',(club_name,year_of_formation,domain,tech_nontech,core_committe,faculty))
    conn.commit()
def insert_clubmem(reg_no,name,learners_id,year,department):
    cursor.execute('''INSERT INTO CLUB_MEMBERS(REG_NO,NAME,LEARNERS_ID,YEAR,DEPARTMENT) VALUES (%s,%s,%s,%s,%s)''',(reg_no,name,learners_id,year,department))
    conn.commit()
def insert_event(event_name,club_name,date,time,venue,participation_fee):
    cursor.execute('''INSERT INTO EVENT(EVENT_NAME,CLUB_NAME,DATE,TIME,VENUE,PARTICIPATION_FEE) VALUES(%s,%s,%s,%s,%s,%s)''',(event_name,club_name,date,time,venue,participation_fee))
    conn.commit()
def insert_attendance(reg_no,event_name,date,time):
    cursor.execute('''INSERT INTO ATTENDANCE(REG_NO,EVENT_NAME,DATE,TIME) VALUES(%s,%s,%s,%s)''',(reg_no,event_name,date,time))
    conn.commit()

def CRUD_op():
    while True:
        print("-----MENU-----")
        print("1. FACULTY\n2. CLUB\n3. CLUB MEMBERS\n4. EVENT\n5. ATTENDANCE\n6. EXIT\n")
        ch=input("ENTER YOUR CHOICE")

        if ch=='1':
            name=input("ENTER FACULTY'S NAME:\n")
            id=input("ENTER THE ID NUMBER:\n")
            insert_faculty(name,id)
            print("DATA ENTRY SUCCESSFUL\n")

        elif ch=='2':
            club_name=input("ENTER THE CLUB'S NAME:\n")
            year=input("ENTER THE YEAR OF FORMATION\n")
            domain=input("ENTER DOMAIN:\n")
            type=input("ENTER IF TECH OR NONTECH:\n")
            core_committee=input("ENTER THE CORE MEMBERS:\n")
            faculty=input("ENTER THE FACULTY INCHARGE:\n")
            cursor.execute("SELECT NAME FROM FACULTY")
            existing_faculty_names = [row[0] for row in cursor.fetchall()]
            print("Existing Faculty Names:", existing_faculty_names)

            # Check if the faculty exists in the FACULTY table before inserting into the CLUB table
            if faculty in existing_faculty_names:
                insert_club(club_name, year, domain,type, core_committee, faculty)
            else:
                print("Error: Faculty doesn't exist. Please add faculty first.")
            
        elif ch=='3':
            reg_no=input("ENTER YOUR REGISTRATION NUMBER:\n")
            name=input("ENTER YOUR NAME:\n")
            learners_id=input("ENTER YOUR LEARNER'S ID:\n")
            year=input("ENTER WHICH YEAR:\n")
            department=input("ENTER WHICH DEPARTMENT:\n")
            insert_clubmem(reg_no,name,learners_id,year,department)
            print("DATA ENTRY SUCCESSFUL")
        elif ch=='4':
            event_name=input("ENTER THE EVENT'S NAME:\n")
            club_name=input("ENTER THE CLUB'S NAME:\n")
            date=input("ENTER DATE:\n")
            time=input("ENTER TIME:\n")
            venue=input("ENTER VENUE:\n")
            fee=input("ENTER FEE:\n")
            insert_club(event_name,club_name,date,time,venue,fee)
            print("DATA ENTRY SUCCESSFUL")
        elif ch=='5':
            reg_no=input("ENTER YOUR REGISTRATION NUMBER:\n")
            event_name=input("ENTER THE EVENT NAME:\n")
            date=input("ENTER DATE:\n")
            time=input("ENTER TIME:\n")
        elif ch=='6':
            break
        else:
            print("INVALID CHOICE")

CRUD_op()
cursor.close()
conn.close()