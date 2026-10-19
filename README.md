# Student Learning Portal — PROG211 Assignment 1

## Problem and solution
Small learning centres may struggle to keep student records and assessment scores organised. This console-based Python program demonstrates a reusable, privacy-conscious way to register learners, record subject scores, and display their results. The example uses fictional names and scores.

## How to run
Install Python 3 and run:

```bash
python main.py
```

No packages or imports are needed.

## OOP requirements
- **Two classes:** `Student` and `LearningPortal`.
- **Attributes:** student ID, name, course, scores, portal title and student collection.
- **Objects:** two `Student` instances and one `LearningPortal` instance.
- **Object interaction:** the portal calls `Student.add_score()` and `Student.display_info()`.
- **One main collection type:** `dict`, used to store students by unique ID and their subject scores.
- **Instance methods:** `add_student()`, `record_result()`, `display_students()`, `add_score()`, etc.
- **Class method:** `Student.get_total_students()`.
- **Static method:** `Student.valid_student_id()`.

## Digital Public Goods principles
- **Open source:** source can be published in a public GitHub repository with a suitable open-source license (add one before claiming an actual license).
- **Inclusive and accessible:** straightforward text interface, simple messages and no special hardware.
- **Privacy:** all names and marks in the example are fictional; the program makes no network calls and stores no real sensitive data.
- **Modular and reusable:** separate classes for learner data and portal management.

## Limitations
Data is stored in memory and resets when the program ends. This is a demonstration, not a production student records system.

