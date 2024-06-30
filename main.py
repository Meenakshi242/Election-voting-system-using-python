import mysql.connector
import datetime
import smtplib
 
try:
    mydb= mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="project_1"
        )
    mycursor = mydb.cursor()
except:
    print("error connecting to database")    

def email_sending(user_name,receiver_email):
    try:
        s=smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        s.login("meena2003dummy@gmail.com","qjvy qcqc tefx psbd")
        message=(f"Subject:Successfully voted\n\n")
        message+=(f"Thanks for your voting {user_name}")
        s.sendmail("meena2003dummy@gmail.com",receiver_email,message)
        s.quit()
        print(f"Email sent successfully to {receiver_email}")
    except:
        print("mail not sent")

def main():
    user_name=input("enter your name : ")
    receiver_email=input("enter your mail id :")
    try:
        mycursor.execute("SELECT id, name FROM candidates")
        candidates = mycursor.fetchall()
        for candidate in candidates:
            print(f"{candidate[0]}. {candidate[1]}")

        while True:
            try:
                candidate_id = int(input("Enter the candidate number you want to vote for (or 0 to exit): "))
                if candidate_id == 0:
                    break
                mycursor.execute("UPDATE candidates SET votes = votes + 1 WHERE id = %s", (candidate_id,))
                mydb.commit()
                print("vote counted successfully")
                print(f"Thanks for your voting {user_name}")
            except ValueError:
                print("Please enter a valid candidate number.")
            except mysql.connector.Error as err:
                print(f"Error: {err}")

            f=open("details.txt","a")

            x=datetime.datetime.now()

            f.write("ELECTION VOTING DETAILS\n\n")
            f.write(f"Name :{user_name} \n")
            f.write(f"Time : {x}\n")
            f.write("Thanks for your voting\n")
            f.write("---------------------------------\n\n")

            email_sending(user_name, receiver_email)

    except mysql.connector.Error as err:
        print(f"error connecting to mysql:{err}")
    
    finally:
        mydb.close()
        print("MySQL connection closed.")
main()


    



