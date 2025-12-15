#Excercise - 3
# Student Marks Processor 
#  Import NumPy library for working with arrays and numerical data
import numpy as np

# ---------- Write data to input file ----------
# Open the file 'student_marks.txt' in write mode
with open("student_marks.txt", "w") as s:
    # Write student registration number, exam marks, and coursework marks
    s.write("ip001,78,82\n")
    s.write("ip002,45,60\n")
    s.write("ip003,90,88\n")
    s.write("ip004,76,89\n")
    s.write("ip005,92,67\n")

# Confirm that data has been written
print("Data written successfully\n")

# ---------- Read and display file ----------
# Open the input file in read mode
with open("student_marks.txt", "r") as s:
    # Read and display the entire file content
    print(s.read())

# Store input and output file names
input_file = "student_marks.txt"
output_file = "results.txt"

try:
    # Create an empty list to store processed student records
    students = []

    # ---------- Read student data ----------
    # Open the input file for reading student records
    with open(input_file, "r") as stu:
        # Loop through each line in the file
        for line in stu:
            # Remove extra spaces/newline and split data by comma
            parts = line.strip().split(",")

            # Validate number of fields in each line
            if len(parts) != 3:
                raise ValueError("Invalid data format in input file.")

            # Unpack student data
            registration_number, exam_marks, coursework_marks = parts

            # Convert marks from string to float
            exam_marks = float(exam_marks)
            coursework_marks = float(coursework_marks)

            # Validate marks range
            if exam_marks < 0 or exam_marks > 100 or coursework_marks < 0 or coursework_marks > 100:
                raise ValueError("Marks must be between 0 and 100.")

            # ---------- Overall marks ----------
            # Calculate overall marks using 70% exam and 30% coursework
            overall_marks = exam_marks * 0.7 + coursework_marks * 0.3

            # ---------- Grade assignment ----------
            # Assign grade based on overall marks
            if overall_marks >= 70:
                grade = "A"
            elif overall_marks >= 60:
                grade = "B"
            elif overall_marks >= 50:
                grade = "C"
            elif overall_marks >= 40:
                grade = "D"
            else:
                grade = "F"

            # Store the student record as a tuple
            students.append(
                (registration_number, exam_marks, coursework_marks, overall_marks, grade)
            )

    # ---------- Structured NumPy array ----------
    # Define data types for each column
    dtype = [
        ("RegNo", "U10"),        # Registration number (string)
        ("Exam", "f4"),         # Exam marks (float)
        ("Coursework", "f4"),   # Coursework marks (float)
        ("Overall", "f4"),      # Overall marks (float)
        ("Grade", "U1")         # Grade (single character)
    ]

    # Convert list of student records into a structured NumPy array
    students_array = np.array(students, dtype=dtype)

    # ---------- Sort by overall marks ----------
    # Sort students by overall marks in descending order
    students_array = np.sort(students_array, order="Overall")[::-1]

    # ---------- Write output file ----------
    # Open the output file in write mode
    with open(output_file, "w") as file:
        # Write table headers
        file.write("RegNo  Exam  Coursework  Overall  Grade\n")
        file.write("-" * 45 + "\n")

        # Write each student's result in formatted form
        for s in students_array:
            file.write(
                f"{s['RegNo']:5}  {s['Exam']:5.1f}  {s['Coursework']:10.1f}  "
                f"{s['Overall']:7.2f}     {s['Grade']}\n"
            )

    # ---------- Grade statistics ----------
    # Count number of students in each grade
    grades, counts = np.unique(students_array["Grade"], return_counts=True)

    # Display grade statistics
    print("Grade Statistics:")
    for g, c in zip(grades, counts):
        print(f"Grade {g}: {c} student(s)")

    # Confirm successful output file creation
    print("\nResults successfully written to", output_file)

# Handle missing input file error
except FileNotFoundError:
    print("Error: Input file not found.")

# Handle data validation errors
except ValueError as ve:
    print("Data Error:", ve)

# Handle any unexpected error
except Exception as ex:
    print("Unexpected Error:", ex)


