# EduManage – School Management System

EduManage is a simple and user-friendly School Management System built using **Python and Streamlit**. It provides a centralized dashboard to manage student registrations, teacher records, and academic grades through a clean and interactive web interface.

## Features

- **Dashboard:** View total students, teachers, grade entries, and average marks.
- **Student Management:** Register students and view student records.
- **Teacher Management:** Register teachers and manage teacher information.
- **Grade Management:** Add and update students' subject-wise marks.
- **Student Records:** View individual student profiles and academic performance.
- **Teacher Records:** Access teacher details and assigned subjects.
- **Data Persistence:** Automatically save and retrieve records using JSON.
- **Interactive UI:** Easy-to-use dashboard with sidebar navigation and organized sections.

## Tech Stack

- **Python** – Core programming language
- **Streamlit** – Web application and user interface
- **JSON** – Data storage
- **Pathlib** – File and database handling

## Project Structure

```text
EduManage/
│
├── app.py
├── school_data.json
└── README.md
```

`school_data.json` is created automatically when data is saved for the first time.

## Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/sourabh-76/edumanage-school-management-system.git
```

**2. Navigate to the project directory**

```bash
cd EduManage
```

**3. Install the required library**

```bash
pip install streamlit
```

**4. Run the application**

```bash
streamlit run app.py
```

The application will open in your default web browser.

## Data Storage

EduManage uses a JSON file (`school_data.json`) to store student and teacher information.

- Student details and academic grades are stored locally.
- Teacher information is saved in the same database.
- Existing records are loaded automatically when the application starts.

## Future Improvements

- Admin login and authentication
- Student and teacher record editing and deletion
- Attendance management
- Report generation and PDF export
- Database integration

## Author

**Sourabh Singh Rawat**

B.Tech – Artificial Intelligence & Machine Learning

---

If you find this project useful, consider giving the repository a ⭐ on GitHub!
