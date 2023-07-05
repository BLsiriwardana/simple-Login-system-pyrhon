from datetime import datetime
import pyttsx3
engine = pyttsx3.init()
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bihan@2004"
)
my_commands = mydb.cursor()
# my_commands.execute("CREATE DATABASE python_first")
# my_commands.execute("SHOW DATABASES")
my_commands.execute("USE python_first")
# my_commands.execute("drop table user")
# my_commands.execute("CREATE TABLE user (user_id VARCHAR(225), user_password VARCHAR(220), user_name VARCHAR(225),Security_Question VARCHAR(225))")
# my_commands.execute("INSERT INTO user VALUE ('EB2023','Bihan@2004','Bihan Lakshitha', 'Siriwardana')")
# mydb.commit()
# print(my_commands.rowcount, "record inserted.")
my_commands.execute("SELECT user_password,Security_Question FROM user WHERE user_id = 'EB2023'")
result = my_commands.fetchall()
for info in result:
    u_info = {
        'password': info[0],
        's_question': info[1]
    }

print("Hi user ! This is a master system in our company. if your want to access this system type password. if you "
      "forgot password type as 'FORGOT'. ")
password = input("Enter Password :- ")
x = 0
if password == 'FORGOT':
    while True:
        print("\033[1;33;1m SECURITY QUESTION ")
        s_question = input('\033[1;0;1m  Enter your name:-')
        if s_question != u_info['s_question']:
            print("\033[1;31;40m You Can't Access System !")
            engine.say("You Can't Access System ")
            engine.runAndWait()
        else:
            print("\033[1;33;1m You can Reset your password !")
            n_password = input('\033[1;0;1m  Enter your new password:-')
            c_password = input('\033[1;0;1m  Enter Conform your password:-')
            if n_password != c_password:
                print("\033[1;31;40m didn't match your password ! Try again later !")
                engine.say("didn't match your password . Try again later ! ")
                engine.runAndWait()
                break
            else:
                u_info['password'] = c_password
                sql = "UPDATE user SET user_password = %s WHERE user_id = %s"
                value = (c_password, 'EB2023')
                my_commands.execute(sql, value)
                mydb.commit()
                print("\033[1;33;1m successfully changed ! Now you can login to system.")
                engine.say("successfully changed ! Now you can login to system.")
                engine.runAndWait()
                password_again_2 = input("\033[1;0;1m Enter Password :-")
                if password_again_2 == u_info['password']:
                    print('\033[1;32;40m successfully logged ! ')
                    print('\033[1;0;1m hello Sir ! Welcome to system.')
                    engine.say("successfully logged !")
                    engine.runAndWait()
                    engine.say("hello Sir ! Welcome to system.")
                    engine.runAndWait()
                    break
                else:
                    print("\033[1;31;40m You Can't Access System ")
                    break

elif password == u_info['password']:
    print('\033[1;32;40m successfully logged ! ')
    print('\033[1;0;1m hello Sir ! Welcome to system.')
    engine.say("successfully logged !")
    engine.runAndWait()
    engine.say("hello Sir ! Welcome to system.")
    engine.runAndWait()
else:
    x = 1
    while True:
        print("\033[1;31;1m wrong password ! try again ")
        password_again = input("\033[1;0;1m Enter Password :-")
        if password_again == 'FORGOT':
            while True:
                print("\033[1;33;1m SECURITY QUESTION ")
                s_question = input('\033[1;0;1m  Enter your name:-')
                if s_question != u_info['s_question']:
                    print("\033[1;31;40m You Can't Access System !")
                    engine.say("You Can't Access System ")
                    engine.runAndWait()
                else:
                    print("\033[1;33;1m You can Reset your password !")
                    n_password = input('\033[1;0;1m  Enter your new password:-')
                    c_password = input('\033[1;0;1m  Enter Conform your password:-')
                    if n_password != c_password:
                        print("\033[1;31;40m didn't match your password ! Try again later !")
                        engine.say("didn't match your password ! Try again later ! ")
                        engine.runAndWait()
                        break
                    else:
                        u_info['password'] = c_password
                        sql = "UPDATE user SET user_password = %s WHERE user_id = 'EB2023'"
                        value = c_password
                        my_commands.execute(sql, value)
                        mydb.commit()
                        print("\033[1;33;1m successfully changed ! Now you can login to system.")
                        engine.say("successfully changed ! Now you can login to system.")
                        engine.runAndWait()
                        password_again_2 = input("\033[1;0;1m Enter Password :-")
                        if password_again_2 == u_info['password']:
                            print('\033[1;32;40m successfully logged ! ')
                            print('\033[1;0;1m hello Sir ! Welcome to system.')
                            engine.say("successfully logged !")
                            engine.runAndWait()
                            engine.say("hello Sir ! Welcome to system.")
                            engine.runAndWait()
                            break
                        else:
                            print("\033[1;31;40m You Can't Access System ")
                            engine.say("You Can't Access System ")
                            engine.runAndWait()
                            break
            break
        elif password_again == u_info['password']:
            print('\033[1;32;40m successfully logged ! ')
            print('\033[1;0;1m hello Sir ! Welcome to system.')
            engine.say("successfully logged !")
            engine.runAndWait()
            engine.say("hello Sir ! Welcome to system.")
            engine.runAndWait()
            break
        elif x == 3:
            print("\033[1;31;40m You Can't Access System ")
            engine.say("You Can't Access System ")
            engine.runAndWait()
            break
        x = x + 1
