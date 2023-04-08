print("""
        ========================================
           Welcome to Fitness Management System
        ========================================
""")
#Establishing connection and creating database along with required tables
import mysql.connector as ms

pd = str(input("Enter Database Password:"))


cn = ms.connect(host="localhost", user="root", passwd="shibiliyas52")
cur = cn.cursor()
# creating database for fitness
cur.execute("create database if not exists GYMFITNESS")
cur.execute("use GYMFITNESS")

cur.execute("create table if not exists GYMS\
                 (gym_id int(10) primary key,\
                 gym_name varchar(30) not null,\
                 place varchar(30),\
                 rate int(10),\
                 type varchar(10),\
                 phone_no int(10))")


# cur.execute("create table if not exists GYMS\
#                  (gym_id varchar(20) primary key,\
#                  gym_name varchar(30) not null,\
#                  place varchar(150),\
#                  rate varchar(10),\
#                  type varchar(20)),\
#                  phone_no varchar(10))")
cur.execute("create table if not exists MEMBERS\
                (m_id varchar(20) primary key,\
                name VARCHAR(50),\
                address VARCHAR(50),\
                age int(10),\
                mobile int(10),\
                gym_name VARCHAR(30))")
cur.execute("create table if not exists PAYMENTS\
                (username VARCHAR(20),\
                pay_id varchar(20) primary key,\
                amount varchar(20),\
                gym_name varchar(20))")
cur.execute("create table if not exists TRAINERS\
                 (name varchar(20) primary key,\
                 gym varchar(10),\
                 city varchar(10),\
                 age int(10),\
                 mobile_no int(10),\
                 salary int(10))")


# creating table for storing the username and password of the new member
cur.execute("create table if not exists users\
                 (username varchar(30) primary key,\
                  password varchar(30) default'000')")


def sign_up():
    print("""

            ============================================
            !!!!!!!Please enter new member details!!!!!!!!
            ============================================
                                                """)
    u = input("Enter New User Name!!:")
    p = input("Enter password (Combination of Letters, Digits etc.):")
    # ENTERING THE ENTERED VALUE TO THE USER_DATA TABLE
    cur.execute("insert into users values('" + u + "','" + p + "')")
    cn.commit()
    print("""
        ========================================================
        !!!!!!!!Congratulations!!!, New User Created...!!!!!!!!
        ========================================================
                                            """)


def login():
    # Login with username and password

    print("""
                ==========================================================
                !!!!!!!!  {{Loginwith username and password }}  !!!!!!!!!!
                ===========================================================
                                                    """)
    un = input("Username!!:")
    ps = input("Password!!:")
    pid = 0
    cur.execute("select password from users where username='" + un + "'")
    rec = cur.fetchall()
    for i in rec:
        a = list(i)
        if a[0] == str(ps):
            while (True):
                # Menu for Administrative Tasks
                print("""
                            1.Admin Tasks
                            2.Members (Join and Remove)
                            3.Sign Out

                                                        """)
                 # prompt message for the task from user
                a = int(input("Enter your choice:"))
                # Admin tasks
                if a == 1:
                    print("""
                                1. Show Details
                                2. Add new member
                                3. Delete existing member
                                4. Exit
                                                         """)
                    b = int(input("Enter your choice:"))
                    # Showing details of GYM, TRAINERS
                    if b == 1:
                        print("""
                                    1. GYM
                                    2. TRAINERS
                                    3. Members
                                                     """)


                         # Prompt Message for users to show details
                        c = int(input("ENTER YOUR CHOICE:"))
                        # See the details of GYMS
                        if c == 1:
                            cur.execute("select * from GYMS")
                            rec = cur.fetchall()
                            for i in rec:
                                b = 0
                                v = list(i)
                                k = ["gym_id", "gym_name", "place", "rate", "type","phone_no"]
                                d = dict(zip(k, v))
                                for i in d:
                                    print(i, ":", d[i])
                                print()

                         # See the details of Trainers
                        elif c == 2:
                                cur.execute("select * from TRAINERS")
                                rec = cur.fetchall()
                                for i in rec:
                                    v = list(i)
                                    k = [ "name", "gym", "city", "age", "mobile_no", "salary"]
                                    d = dict(zip(k, v))
                                    for i in d:
                                        print(i, ":", d[i])
                                    print()
#Add detais into Fitness
                        elif b == 2:
                                print("""

                                                                    1. Gym
                                                                    2. Trainer

                                c = int(input("Enter your choice:"))                                                                            """)
                                # New Gym details
                                if c==1:
                                  # Prompt messages for Gym details
                                  gym_id = input("Enter the gym id:")
                                  gym_name = input("Enter name of GYM:")
                                  place = input("Enter place:")
                                  rate = input("Enter the rate:")
                                  type = input("Enter type of gym.:")
                                  phone_no = input("Enter phone number:")
                                  cur.execute(
                                      "insert into GYM values('" + gym_id + "','" + gym_name + "','" + place + "','" + rate + "','" + type + "','" + phone_no + "')")
                                elif c == 2:
                                    # Prompt messages for Trainer details
                                    name = input("Enter name of Trainer:")
                                    gym = input("Enter GYM:")
                                    age = input("Enter age:")
                                    city = input("Enter city Trainer belongs to:")
                                    mno = input("Enter 10 digit mobile no.:")
                                    sal = input("Enter Salary of Trainer:")
                                    # Insert values into trainers table
                                    cur.execute(
                                        "insert into Trainers values('" + name + "','" + gym + "','" + age + "','" + city + "','" + mno + "','" + sal + "')")
                                    cn.commit()
                                    print("New Trainer details has been added successfully. ")

                             # Menu for delete data
                                elif b == 3:
                                    print("""
                                                                1. GYM
                                                                2. Trainers

                                                                                                            """)
                                    c = int(input("Enter your choice:"))
                                     # deleting Gym details
                                    if c == 1:
                                        name = input("Enter Gym name to delete:")
                                        cur.execute("select * from GYMS where gym_name='" + gym_name + "'")
                                        rec = cur.fetchall()
                                        print(rec)
                                        p = input("you really wanna delete this data? (y/n):")
                                        if p == "y":
                                            cur.execute("delete from gyms where gym_name='" + gym_name + "'")
                                            cn.commit()
                                            print("The requested gym has been deleted successfully")
                                        else:
                                            print("Error in deletion....")


                                    # deleting trainer details
                                    elif c == 2:
                                        name = input("Enter name of trainer:")
                                        cur.execute("select * TRAINERS where name='" + name + "'")
                                        rec = cur.fetchall()
                                        print(rec)
                                        p = input("Are you really wanna delete this data? (y/n):")
                                        if p == "y":
                                            cur.execute("delete from TRAINERS where name='" + name + "'")
                                            cn.commit()
                                            print("Trainer has been deleted successfully.")
                                        else:
                                            print("Error in deletion")

                                elif b == 4:
                                    print("Thank you! See you again! Have nice Day!")
                                    break

                                    # entering the patient details table
                elif a == 2:

                                    print("""
                                                                1. Show Members record
                                                                2. Admit new Member
                                                                3. Remove Member
                                                                4. Exit
                                                                                                  """)
                                    b = int(input("ENTER YOUR CHOICE:"))
                                    # showing the existing details of member
                                    # See the details of member
                                    if b == 1:
                                        cur.execute("select * from MEMBERS")
                                        rec = cur.fetchall()
                                        for i in rec:
                                            b = 0
                                            v = list(i)
                                            k = ["Name", "Address", "Age", "City", "mobile_no","gym-name"]
                                            d = dict(zip(k, v))
                                            for i in d:
                                                print(i, ":", d[i])
                                    # Admit a new member
                                    elif b == 2:
                                                m_id = m_id + 1
                                                name = str(input("Enter name of member: "))
                                                age = str(input("Enter age: "))
                                                city = str(input("Enter City: "))
                                                mn = str(input("Enter Mobile no.: "))
                                                cur.execute("select name from GYM")
                                                rec = cur.fetchall()
                                                print(rec)
                                                gm = str(input("Enter gymnanme to be recommended:"))
                                                cur.execute("insert into member values('" + str(m_id) + "','" + str(
                                                    name) + "','" + str(
                                                    mn) + "','" + str(age) + "','" + str(city) + "','" + str(gm) + "')")
                                                cn.commit()
                                    print("""
                                                                    ====================================
                                                                    !!!!!!!New Member admitted!!!!!!
                                                                    ====================================
                                                                                    """)
                                # remove a member
                elif b == 3:
                                    name = input("Enter the name of member to remove:")
                                    cur.execute("select * from MEMBERS where name='" + name + "'")
                                    rec = cur.fetchall()
                                    print(rec)
                                    amount = input("Amount paid (y/n):")
                                    if amount == "y":
                                        cur.execute("delete from MEMBERS where name like'%" + name + "%'")
                                        cn.commit()
                                    elif amount == "n":
                                        print("Please pay your pending  amount to avoid member from a gym patient.")
                                    else:
                                        print("payment status is unknown....")
                        # if user wants to exit
                elif b == 4:
                            break
             ###SIGN OUT
        elif a == 3:
                            break

def change_pass():
                                cur.execute("select username from users")
                                rec = cur.fetchall()
                                for i in rec:
                                    v = list(i)
                                    k = ["USERNAME"]
                                    d = dict(zip(k, v))
                                print(d)
                                u = input("Enter username to change password from above:")
                                if u in d.values():
                                    pd = input("Enter New Password:")
                                    pd1 = input("Renter New Password again:")
                                    if pd == pd1:
                                        cur.execute("update users set password='" + pd + "'where username='" + u + "'")
                                        cn.commit()
                                        print("Password Changed Successfully.")
                                    else:
                                        print("Password did not match...")
                                else:
                                    print("Username not found")

 # Main Menu
r = 0
while r != 4:
    print("""
                    1. Sign Up (New User)
                    2. Log In
                    3. Change Password
                    4. Exit
                                                        """)

    r = int(input("Enter your choice:"))
    # New User Registration
    if r == 1:
        sign_up()
    elif r == 2:
        login()
    elif r == 3:
          change_pass()
    elif r == 4:
        print("Thank you for using FITNESS App, Have a nice day!")
        break
