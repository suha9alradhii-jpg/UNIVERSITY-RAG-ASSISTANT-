import os

# ننشئ المجلد إذا ما كان موجود
os.makedirs("data/documents", exist_ok=True)

content = """
5. ADDITIONAL UNIVERSITY POLICIES
- Grading System: A (90-100), B (80-89), C (70-79), D (60-69), F (Below 60).
- Attendance Policy: Students must attend at least 75% of classes to be eligible to take the final exam.
- Graduation Project: All students must complete a graduation project in their final semester.
- Internship Requirement: Students must complete a 2-month summer internship before graduation.
"""

with open("data/documents/additional_info.txt", "w", encoding="utf-8") as f:
    f.write(content)

print("تم إنشاء ملف additional_info.txt بنجاح في مجلد data/documents!")