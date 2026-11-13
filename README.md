# Study Tracker Management System

A command-line application built using Python and MySQL to help students record, manage, and monitor their study activities.

## About the Project

The Study Tracker Management System allows students to maintain records of their study sessions, organize topics by subject, and calculate their total study hours.

Originally developed as a Class 12 board practical project and subsequently updated to improve database connectivity and configuration management.

## Features

- **Add Study Records:** Add subjects, multiple topics, study hours, dates, and remarks.
- **View All Records:** Display all saved study entries.
- **Update Records:** Modify study hours and remarks using a record ID.
- **Delete Records:** Delete a selected study record.
- **Search by Subject:** Find records belonging to a particular subject.
- **Calculate Total Study Hours:** View the total hours spent on each subject.
- **Export Records:** Export all study records into a text file.

## Technologies Used

- Python
- MySQL
- mysql-connector-python
- python-dotenv

## Project Structure

```text
Study-Tracker-Management-System/
│
├── main.py
├── test_mysql.py
├── requirements.txt
├── .gitignore
├── README.md
│
└── .env  (local configuration - not uploaded)
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ananyasinghkriti-prog/Study-Tracker-Management-System.git
```

### 2. Navigate to the Project Directory

```bash
cd Study-Tracker-Management-System
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure MySQL Database

Make sure MySQL is installed and running.

Create the database:

```sql
CREATE DATABASE study_tracker;
```

Select the database:

```sql
USE study_tracker;
```

Create the required table:

```sql
CREATE TABLE study (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subject VARCHAR(100) NOT NULL,
    topic VARCHAR(255) NOT NULL,
    hours FLOAT NOT NULL,
    date DATE NOT NULL,
    remarks TEXT
);
```

### 5. Configure Environment Variables

Create a `.env` file in the project directory and add your own MySQL credentials:

```env
MYSQL_HOST=127.0.0.1
MYSQL_USER=your_mysql_username
MYSQL_PASSWORD=your_mysql_password
MYSQL_DATABASE=study_tracker
```

**Security Note:** The `.env` file is excluded through `.gitignore`. Never upload or share your database credentials.

### 6. Run the Application

```bash
python main.py
```

## Application Menu

```text
========== STUDY TRACKER MENU ==========

1. Add Study Record
2. View All Records
3. Update a Record
4. Delete a Record
5. Search by Subject
6. View Total Hours by Subject
7. Export All Records to File
8. Exit

========================================
```

## Learning Outcomes

Working on this project helped me practise:

- Python programming and problem-solving.
- Connecting Python with a MySQL database.
- Performing CRUD (Create, Read, Update, Delete) operations.
- Writing SQL queries for searching and data aggregation.
- Handling user input and exceptions.
- Managing application configuration using environment variables.
- Exporting database records into text files.

## Future Improvements

- Develop a web-based interface.
- Add graphical representations of study statistics.
- Introduce additional study analytics.
- Improve the overall user experience.

## Author

**Ananya Singh**

B.Tech Computer Science and Engineering Student

[GitHub Profile](https://github.com/ananyasinghkriti-prog)

[View Repository](https://github.com/ananyasinghkriti-prog/Study-Tracker-Management-System)
