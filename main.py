
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Database Connection
try:
    mydb = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )

    mycursor = mydb.cursor()

    print("Connected to MySQL Database successfully!\n")

except mysql.connector.Error as e:
    print("Error while connecting to MySQL:", e)
    exit()



# Add Study Record Function

def add_record():
    try:
        subject = input("Enter Subject Name: ")

        topics = input(
            "Enter Topics/Chapters (separated by commas): "
        ).split(",")

        study_date = input("Enter Date (YYYY-MM-DD): ")

        for t in topics:
            topic = t.strip()

            hours = float(
                input("Enter Hours Studied for '" + topic + "': ")
            )

            remarks = input("Enter Remarks for '" + topic + "': ")

            query = """INSERT INTO study
            (subject, topic, hours, date, remarks)
            VALUES (%s, %s, %s, %s, %s)"""

            data = (subject, topic, hours, study_date, remarks)

            mycursor.execute(query, data)
            mydb.commit()

        print("\nAll Topics Added Successfully!\n")

    except ValueError:
        print("Invalid input! Please enter a numeric value for hours.\n")

    except mysql.connector.Error as e:
        print("Database Error:", e)


# View All Study Records

def view_records():
    try:
        mycursor.execute("SELECT * FROM study")
        records = mycursor.fetchall()

        if len(records) == 0:
            print("No records found.\n")

        else:
            print("\n--- Study Records ---")

            for row in records:
                print(
                    f"ID: {row[0]}, "
                    f"Subject: {row[1]}, "
                    f"Topic: {row[2]}, "
                    f"Hours: {row[3]}, "
                    f"Date: {row[4]}, "
                    f"Remarks: {row[5]}"
                )

            print()

    except mysql.connector.Error as e:
        print("Database Error:", e)


# Update Study Record

def update_record():
    try:
        rid = int(input("Enter Record ID to Update: "))

        new_hours = float(input("Enter New Hours: "))

        new_remarks = input("Enter New Remarks: ")

        query = "UPDATE study SET hours=%s, remarks=%s WHERE id=%s"

        data = (new_hours, new_remarks, rid)

        mycursor.execute(query, data)
        mydb.commit()

        if mycursor.rowcount == 0:
            print("No such record found.\n")
        else:
            print("Record Updated Successfully!\n")

    except ValueError:
        print("Invalid input! Please enter numeric values.\n")

    except mysql.connector.Error as e:
        print("Database Error:", e)


# Delete Study Record

def delete_record():
    try:
        rid = int(input("Enter Record ID to Delete: "))

        query = "DELETE FROM study WHERE id=%s"

        data = (rid,)

        mycursor.execute(query, data)
        mydb.commit()

        if mycursor.rowcount == 0:
            print("Record not found.\n")
        else:
            print("Record Deleted Successfully!\n")

    except ValueError:
        print("Invalid input! Please enter a valid record ID.\n")

    except mysql.connector.Error as e:
        print("Database Error:", e)


# Search Records by Subject

def search_by_subject():
    try:
        sub = input("Enter Subject to Search: ")

        query = "SELECT * FROM study WHERE subject=%s"

        data = (sub,)

        mycursor.execute(query, data)
        records = mycursor.fetchall()

        if len(records) == 0:
            print("No records found for this subject.\n")

        else:
            print("\n--- Search Results ---")

            for row in records:
                print(
                    f"ID: {row[0]}, "
                    f"Subject: {row[1]}, "
                    f"Topic: {row[2]}, "
                    f"Hours: {row[3]}, "
                    f"Date: {row[4]}, "
                    f"Remarks: {row[5]}"
                )

            print()

    except mysql.connector.Error as e:
        print("Database Error:", e)


# Calculate Total Study Hours by Subject

def total_hours():
    try:
        query = "SELECT subject, SUM(hours) FROM study GROUP BY subject"

        mycursor.execute(query)
        result = mycursor.fetchall()

        if len(result) == 0:
            print("No records found.\n")

        else:
            print("\n--- Total Study Hours by Subject ---")

            for row in result:
                print("Subject:", row[0], "| Total Hours:", row[1])

            print()

    except mysql.connector.Error as e:
        print("Database Error:", e)


# Export Study Records to Text File

def export_to_file():
    try:
        mycursor.execute("SELECT * FROM study")
        records = mycursor.fetchall()

        if len(records) == 0:
            print("No data to export.\n")

        else:
            f = open("study_report.txt", "w")

            for row in records:
                f.write(
                    "ID: " + str(row[0]) +
                    ", Subject: " + str(row[1]) +
                    ", Topic: " + str(row[2]) +
                    ", Hours: " + str(row[3]) +
                    ", Date: " + str(row[4]) +
                    ", Remarks: " + str(row[5]) + "\n"
                )

            f.close()

            print("Data exported to 'study_report.txt' successfully!\n")

    except mysql.connector.Error as e:
        print("Database Error:", e)


# Main Menu Loop

while True:

    print("========== STUDY TRACKER MENU ==========")
    print("1. Add Study Record")
    print("2. View All Records")
    print("3. Update a Record")
    print("4. Delete a Record")
    print("5. Search by Subject")
    print("6. View Total Hours by Subject")
    print("7. Export All Records to File")
    print("8. Exit")
    print("========================================")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        add_record()

    elif choice == '2':
        view_records()

    elif choice == '3':
        update_record()

    elif choice == '4':
        delete_record()

    elif choice == '5':
        search_by_subject()

    elif choice == '6':
        total_hours()

    elif choice == '7':
        export_to_file()

    elif choice == '8':
        print("Exiting Study Tracker. Goodbye!")
        mycursor.close()
        mydb.close()
        break

    else:
        print("Invalid Choice! Please try again.\n")

