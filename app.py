import streamlit as st
import json
from pathlib import Path

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="EduManage | School Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

DB = Path("school_data.json")

# =====================================================
# DATABASE FUNCTIONS
# =====================================================

def load_data():
    if DB.exists():
        try:
            with open(DB, "r") as file:
                content = json.load(file)
                return {
                    "student": content.get("student", []),
                    "teachers": content.get("teachers", [])
                }
        except (json.JSONDecodeError, OSError):
            st.error("Database could not be loaded.")

    return {"student": [], "teachers": []}


data = load_data()


def save_data():
    with open(DB, "w") as file:
        json.dump(data, file, indent=4)


def valid_email(email):
    parts = email.strip().split("@")
    return len(parts) == 2 and bool(parts[0]) and "." in parts[1]


def page_header(title, description):
    st.markdown(
        f"""
        <div class="page-header">
            <h1>{title}</h1>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def metric_card(title, value, icon, color):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-top">
                <span>{title}</span>
                <div class="metric-icon" style="background:{color}20;color:{color}">
                    {icon}
                </div>
            </div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def empty_message(message):
    st.markdown(
        f'<div class="empty-state">{message}</div>',
        unsafe_allow_html=True
    )


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

/* Main application */

.stApp {
    background: #F5F7FB;
    color: #18243A;
    font-family: 'Inter', sans-serif;
}

.block-container {
    padding-top: 2.2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

/* Sidebar */

[data-testid="stSidebar"] {
    background: #17243B;
    border-right: none;
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 2rem;
}

[data-testid="stSidebar"] * {
    color: #E8EDF7;
}

.brand {
    font-size: 25px;
    font-weight: 800;
    letter-spacing: -1px;
    color: white;
    margin-bottom: 2px;
}

.brand span {
    color: #65A5FF;
}

.brand-sub {
    font-size: 12px;
    color: #A4B2C9;
    margin-bottom: 30px;
}

.sidebar-label {
    color: #8C9CB7;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-bottom: 10px;
}

/* Page header */

.page-header {
    margin-bottom: 28px;
}

.page-header h1 {
    color: #17243B;
    font-size: 30px;
    font-weight: 750;
    letter-spacing: -1px;
    margin-bottom: 5px;
}

.page-header p {
    color: #8793A6;
    font-size: 14px;
    margin-top: 0;
}

/* Metrics */

.metric-card {
    background: white;
    padding: 22px;
    border: 1px solid #E9EDF4;
    border-radius: 13px;
    min-height: 125px;
    box-shadow: 0 3px 12px rgba(20, 35, 60, 0.025);
    margin-bottom: 12px;
}

.metric-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #7D899B;
    font-size: 13px;
    font-weight: 600;
}

.metric-icon {
    height: 38px;
    width: 38px;
    border-radius: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 17px;
}

.metric-value {
    font-size: 30px;
    font-weight: 750;
    color: #17243B;
    margin-top: 13px;
}

/* Section headings */

.section-heading {
    font-size: 18px;
    font-weight: 700;
    color: #17243B;
    margin-top: 12px;
    margin-bottom: 15px;
}

/* Forms */

[data-testid="stForm"] {
    background: white;
    padding: 24px;
    border: 1px solid #E9EDF4;
    border-radius: 13px;
}

[data-testid="stTextInput"] label,
[data-testid="stNumberInput"] label,
[data-testid="stSelectbox"] label {
    color: #36445B;
    font-size: 13px;
    font-weight: 600;
}

.stTextInput input,
.stNumberInput input {
    border-radius: 8px;
    background: #FAFBFD;
    border-color: #E2E7EF;
}

.stTextInput input:focus {
    border-color: #3979EB;
}

/* Buttons */

.stButton button,
.stFormSubmitButton button {
    border-radius: 8px;
    font-weight: 600;
    min-height: 40px;
}

.stFormSubmitButton button[kind="primary"] {
    background: #2869DC;
    border: none;
}

.stFormSubmitButton button[kind="primary"]:hover {
    background: #1D56BA;
}

/* Tabs */

.stTabs [data-baseweb="tab-list"] {
    gap: 20px;
    border-bottom: 1px solid #E3E8F0;
}

.stTabs [data-baseweb="tab"] {
    color: #718096;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    color: #2869DC !important;
}

/* Dataframes */

[data-testid="stDataFrame"] {
    border: 1px solid #E9EDF4;
    border-radius: 10px;
    overflow: hidden;
}

/* Empty state */

.empty-state {
    background: white;
    border: 1px dashed #D5DDE9;
    border-radius: 12px;
    padding: 35px;
    text-align: center;
    color: #8995A7;
    font-size: 14px;
}

/* Divider */

hr {
    border-color: #E7EBF2;
}

/* Alerts */

[data-testid="stAlert"] {
    border-radius: 9px;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# SIDEBAR NAVIGATION
# =====================================================

with st.sidebar:

    st.markdown(
        '<div class="brand">Edu<span>Manage</span></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="brand-sub">SCHOOL ADMINISTRATION PORTAL</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-label">MAIN MENU</div>',
        unsafe_allow_html=True
    )

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Students",
            "Teachers",
            "Grade Management",
            "Student Records",
            "Teacher Records"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown(
        """
        <div style="font-size:12px;color:#9BAAC0;line-height:1.8">
            <b>EduManage Portal</b><br>
            Version 2.0.0<br>
            School Management System
        </div>
        """,
        unsafe_allow_html=True
    )


# =====================================================
# DASHBOARD
# =====================================================

if page == "Dashboard":

    page_header(
        "Dashboard",
        "Overview of your school's students, teachers and academic performance."
    )

    total_students = len(data["student"])
    total_teachers = len(data["teachers"])

    all_marks = [
        mark
        for student in data["student"]
        for mark in student.get("grades", {}).values()
    ]

    average = sum(all_marks) / len(all_marks) if all_marks else 0

    total_subjects = sum(
        len(student.get("grades", {}))
        for student in data["student"]
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("Total Students", total_students, "S", "#3979EB")

    with c2:
        metric_card("Total Teachers", total_teachers, "T", "#16A47B")

    with c3:
        metric_card("Grade Entries", total_subjects, "G", "#9564D8")

    with c4:
        metric_card("Average Marks", f"{average:.1f}%", "A", "#E39A38")

    st.markdown("<br>", unsafe_allow_html=True)

    left, right = st.columns([1.6, 1])

    with left:

        st.markdown(
            '<div class="section-heading">Recently Registered Students</div>',
            unsafe_allow_html=True
        )

        if data["student"]:

            recent = data["student"][-5:][::-1]

            st.dataframe(
                [
                    {
                        "Student Name": s["name"],
                        "Roll Number": s["roll_no"],
                        "Email": s["email"]
                    }
                    for s in recent
                ],
                use_container_width=True,
                hide_index=True
            )

        else:
            empty_message("No student records available yet.")

    with right:

        st.markdown(
            '<div class="section-heading">School Overview</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="metric-card">
                <p style="color:#8490A2;font-size:13px">Registered Students</p>
                <h2 style="color:#17243B">{total_students}</h2>
                <hr>
                <p style="color:#8490A2;font-size:13px">Registered Teachers</p>
                <h2 style="color:#17243B">{total_teachers}</h2>
                <hr>
                <p style="color:#8490A2;font-size:13px">Academic Grade Entries</p>
                <h2 style="color:#17243B">{total_subjects}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )


# =====================================================
# STUDENT MANAGEMENT
# =====================================================

elif page == "Students":

    page_header(
        "Student Management",
        "Register new students and manage student information."
    )

    tab1, tab2 = st.tabs(["Register Student", "Student List"])

    with tab1:

        st.markdown("### New Student Registration")

        with st.form("student_form"):

            col1, col2 = st.columns(2)

            with col1:
                name = st.text_input("Full Name", placeholder="Enter student name")
                age = st.number_input("Age", 1, 100, 18)

            with col2:
                roll_no = st.text_input("Roll Number", placeholder="Enter roll number")
                email = st.text_input("Email Address", placeholder="example@gmail.com")

            submit = st.form_submit_button(
                "Register Student",
                type="primary",
                use_container_width=True
            )

            if submit:

                if not all([name.strip(), roll_no.strip(), email.strip()]):
                    st.error("Please complete all fields.")

                elif not valid_email(email):
                    st.error("Please enter a valid email address.")

                elif any(s["roll_no"].lower() == roll_no.strip().lower()
                         for s in data["student"]):
                    st.error("This roll number is already registered.")

                else:
                    data["student"].append({
                        "name": name.strip(),
                        "age": age,
                        "email": email.strip(),
                        "roll_no": roll_no.strip(),
                        "grades": {}
                    })

                    save_data()
                    st.success("Student registered successfully!")
                    st.rerun()

    with tab2:

        st.markdown("### All Students")

        if data["student"]:

            search = st.text_input(
                "Search by name or roll number",
                placeholder="Search students..."
            )

            filtered = [
                s for s in data["student"]
                if search.lower() in s["name"].lower()
                or search.lower() in s["roll_no"].lower()
            ]

            st.dataframe(
                [
                    {
                        "Name": s["name"],
                        "Age": s["age"],
                        "Roll Number": s["roll_no"],
                        "Email": s["email"]
                    }
                    for s in filtered
                ],
                use_container_width=True,
                hide_index=True
            )

            st.caption(f"Showing {len(filtered)} of {len(data['student'])} students")

        else:
            empty_message("No students registered. Add your first student above.")


# =====================================================
# TEACHER MANAGEMENT
# =====================================================

elif page == "Teachers":

    page_header(
        "Teacher Management",
        "Register and manage your school's teaching staff."
    )

    tab1, tab2 = st.tabs(["Register Teacher", "Teacher List"])

    with tab1:

        st.markdown("### New Teacher Registration")

        with st.form("teacher_form"):

            col1, col2 = st.columns(2)

            with col1:
                name = st.text_input("Full Name", placeholder="Enter teacher name")
                age = st.number_input("Age", 18, 100, 25)

            with col2:
                emp_id = st.text_input("Employee ID", placeholder="Enter employee ID")
                email = st.text_input("Email Address", placeholder="example@gmail.com")

            subject = st.text_input(
                "Teaching Subject",
                placeholder="e.g. Mathematics"
            )

            submit = st.form_submit_button(
                "Register Teacher",
                type="primary",
                use_container_width=True
            )

            if submit:

                if not all([name.strip(), emp_id.strip(), email.strip(), subject.strip()]):
                    st.error("Please complete all fields.")

                elif not valid_email(email):
                    st.error("Please enter a valid email address.")

                elif any(t["emp_id"].lower() == emp_id.strip().lower()
                         for t in data["teachers"]):
                    st.error("This employee ID is already registered.")

                else:

                    data["teachers"].append({
                        "name": name.strip(),
                        "age": age,
                        "email": email.strip(),
                        "emp_id": emp_id.strip(),
                        "subject": subject.strip()
                    })

                    save_data()
                    st.success("Teacher registered successfully!")
                    st.rerun()

    with tab2:

        st.markdown("### All Teachers")

        if data["teachers"]:

            search = st.text_input(
                "Search by name or employee ID",
                placeholder="Search teachers..."
            )

            filtered = [
                t for t in data["teachers"]
                if search.lower() in t["name"].lower()
                or search.lower() in t["emp_id"].lower()
            ]

            st.dataframe(
                [
                    {
                        "Name": t["name"],
                        "Age": t["age"],
                        "Employee ID": t["emp_id"],
                        "Subject": t["subject"],
                        "Email": t["email"]
                    }
                    for t in filtered
                ],
                use_container_width=True,
                hide_index=True
            )

            st.caption(f"Showing {len(filtered)} of {len(data['teachers'])} teachers")

        else:
            empty_message("No teachers registered yet.")


# =====================================================
# GRADE MANAGEMENT
# =====================================================

elif page == "Grade Management":

    page_header(
        "Grade Management",
        "Add and update academic marks for registered students."
    )

    if not data["student"]:

        empty_message("Register a student first to manage grades.")

    else:

        student_options = {
            f'{s["name"]} ({s["roll_no"]})': s["roll_no"]
            for s in data["student"]
        }

        with st.form("grade_form"):

            selected = st.selectbox(
                "Select Student",
                list(student_options.keys())
            )

            col1, col2 = st.columns(2)

            with col1:
                subject = st.text_input(
                    "Subject",
                    placeholder="e.g. Mathematics"
                )

            with col2:
                marks = st.number_input(
                    "Marks Obtained",
                    min_value=0,
                    max_value=100,
                    value=0
                )

            submit = st.form_submit_button(
                "Save Grade",
                type="primary",
                use_container_width=True
            )

            if submit:

                if not subject.strip():
                    st.error("Please enter a subject name.")

                else:

                    roll = student_options[selected]

                    for s in data["student"]:

                        if s["roll_no"] == roll:
                            s["grades"][subject.strip()] = marks
                            break

                    save_data()
                    st.success("Grade saved successfully!")
                    st.rerun()

        st.markdown("### Existing Grade Records")

        selected_roll = student_options[selected]

        student = next(
            s for s in data["student"]
            if s["roll_no"] == selected_roll
        )

        grades = student.get("grades", {})

        if grades:

            st.dataframe(
                [
                    {"Subject": sub, "Marks": mark}
                    for sub, mark in grades.items()
                ],
                use_container_width=True,
                hide_index=True
            )

        else:
            empty_message("No grades available for this student.")


# =====================================================
# STUDENT RECORDS
# =====================================================

elif page == "Student Records":

    page_header(
        "Student Records",
        "View individual student profiles and academic performance."
    )

    if not data["student"]:

        empty_message("No student records found.")

    else:

        options = {
            f'{s["name"]} | {s["roll_no"]}': s["roll_no"]
            for s in data["student"]
        }

        selected = st.selectbox("Select Student", list(options.keys()))
        roll = options[selected]

        student = next(
            s for s in data["student"]
            if s["roll_no"] == roll
        )

        grades = student.get("grades", {})

        avg = sum(grades.values()) / len(grades) if grades else 0

        st.markdown("---")

        st.subheader(student["name"])
        st.caption(f"Student ID: {student['roll_no']}")

        c1, c2, c3 = st.columns(3)

        with c1:
            metric_card("Age", student["age"], "A", "#3979EB")

        with c2:
            metric_card("Subjects", len(grades), "S", "#16A47B")

        with c3:
            metric_card("Average Marks", f"{avg:.1f}%", "M", "#9564D8")

        st.markdown("### Personal Information")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Full Name**")
            st.write(student["name"])

            st.write("**Roll Number**")
            st.write(student["roll_no"])

        with col2:
            st.write("**Email Address**")
            st.write(student["email"])

            st.write("**Age**")
            st.write(student["age"])

        st.markdown("### Academic Performance")

        if grades:

            st.dataframe(
                [
                    {"Subject": sub, "Marks": mark}
                    for sub, mark in grades.items()
                ],
                use_container_width=True,
                hide_index=True
            )

            st.bar_chart(grades)

        else:
            empty_message("No academic records available yet.")


# =====================================================
# TEACHER RECORDS
# =====================================================

elif page == "Teacher Records":

    page_header(
        "Teacher Records",
        "View individual teacher profiles and assigned subjects."
    )

    if not data["teachers"]:

        empty_message("No teacher records found.")

    else:

        options = {
            f'{t["name"]} | {t["emp_id"]}': t["emp_id"]
            for t in data["teachers"]
        }

        selected = st.selectbox("Select Teacher", list(options.keys()))

        emp_id = options[selected]

        teacher = next(
            t for t in data["teachers"]
            if t["emp_id"] == emp_id
        )

        st.markdown("---")

        st.subheader(teacher["name"])
        st.caption(f"Employee ID: {teacher['emp_id']}")

        c1, c2 = st.columns(2)

        with c1:
            metric_card("Age", teacher["age"], "A", "#3979EB")

        with c2:
            metric_card("Teaching Subject", teacher["subject"], "S", "#16A47B")

        st.markdown("### Personal Information")

        st.write("**Full Name:**", teacher["name"])
        st.write("**Employee ID:**", teacher["emp_id"])
        st.write("**Email:**", teacher["email"])
        st.write("**Age:**", teacher["age"])
        st.write("**Subject:**", teacher["subject"])

st.markdown("""
<style>
.stApp,
[data-testid="stAppViewContainer"] {
    background-color: #0B1220 !important;
}

.stTextInput input,
.stNumberInput input {
    background-color: #202E43 !important;
    color: white !important;
    -webkit-text-fill-color: white !important;
    caret-color: #60A5FA !important;
}

.stTextInput input::placeholder,
.stNumberInput input::placeholder {
    color: #94A3B8 !important;
    -webkit-text-fill-color: #94A3B8 !important;
}

[data-testid="stForm"] {
    background-color: #17243A !important;
    border: 1px solid #293A53 !important;
}

</style>
""", unsafe_allow_html=True)


# ===== FINAL TEXT VISIBILITY FIX =====

st.markdown("""
<style>

/* Main headings */
h1, h2, h3, h4, h5, h6,
.page-header h1,
.section-heading {
    color: #F8FAFC !important;
    -webkit-text-fill-color: #F8FAFC !important;
}

/* All normal text */
p, span, label, li,
.stMarkdown,
.stMarkdown p,
.stMarkdown span {
    color: #DCE6F3;
}

/* Page descriptions */
.page-header p,
.stCaption,
[data-testid="stCaptionContainer"] {
    color: #AFC0D5 !important;
}

/* Form labels */
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stTextArea label,
[data-testid="stWidgetLabel"] p {
    color: #E2EAF5 !important;
    -webkit-text-fill-color: #E2EAF5 !important;
}

/* Typed input text */
.stTextInput input,
.stNumberInput input,
.stTextArea textarea,
[data-baseweb="input"] input {
    background-color: #202E43 !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    caret-color: #60A5FA !important;
    border: 1px solid #526780 !important;
}

/* Placeholder */
input::placeholder,
textarea::placeholder {
    color: #A9B9CC !important;
    -webkit-text-fill-color: #A9B9CC !important;
    opacity: 1 !important;
}

/* Number input controls */
[data-testid="stNumberInput"] button {
    background: #293B55 !important;
    color: #FFFFFF !important;
}

/* Select box */
[data-baseweb="select"] *,
[data-baseweb="select"] input {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    color: #C5D2E3 !important;
}

.stTabs [aria-selected="true"] {
    color: #60A5FA !important;
}

/* Radio navigation */
[data-testid="stRadio"] label {
    color: #E2EAF5 !important;
}

/* Metrics */
.metric-top {
    color: #C1CDDD !important;
}

.metric-value {
    color: #FFFFFF !important;
}

/* Tables */
[data-testid="stDataFrame"] {
    color: #FFFFFF !important;
}

/* Alerts */
[data-testid="stAlert"] p {
    color: inherit !important;
}

/* Keep primary buttons readable */
.stButton button,
.stFormSubmitButton button {
    color: #FFFFFF !important;
}

/* Form background */
[data-testid="stForm"] {
    background: #17243A !important;
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: #E2EAF5;
}

</style>
""", unsafe_allow_html=True)


# ===== FORCE DARK DASHBOARD CARDS =====

st.markdown("""
<style>

/* All custom metric cards */
div.metric-card {
    background: #17243A !important;
    background-color: #17243A !important;
    border: 1px solid #344761 !important;
    border-radius: 14px !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.15) !important;
}

/* Metric card labels */
div.metric-card .metric-top,
div.metric-card .metric-top span,
div.metric-card p {
    color: #C5D3E5 !important;
    -webkit-text-fill-color: #C5D3E5 !important;
}

/* Metric numbers */
div.metric-card .metric-value,
div.metric-card h2 {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    font-weight: 750 !important;
}

/* Overview card separators */
div.metric-card hr {
    border-color: #344761 !important;
}

/* Ensure dashboard background remains dark */
.stApp,
[data-testid="stAppViewContainer"],
.main {
    background-color: #0B1220 !important;
}

</style>
""", unsafe_allow_html=True)
