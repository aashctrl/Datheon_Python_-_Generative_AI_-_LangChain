
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


output_path = Path("documents/sample_guide.pdf")
output_path.parent.mkdir(parents=True, exist_ok=True)

pdf = canvas.Canvas(str(output_path), pagesize=A4)

pages = [
    (
        "Python Programming Guide",
        [
            "Topic: Variables",
            "Python variables store values.",
            "You do not need to declare a variable's type explicitly.",
            'Example: student_name = "Priya"',
        ],
    ),
    (
        "Python Programming Guide",
        [
            "Topic: Lists",
            "A Python list stores multiple items in an ordered collection.",
            "Lists are mutable, meaning their contents can be changed.",
            'Example: skills = ["Python", "SQL", "Pandas"]',
        ],
    ),
    (
        "Python Programming Guide",
        [
            "Topic: Functions",
            "Functions are reusable blocks of code defined using def.",
            "Functions can accept parameters and return results.",
            "Example: def add(a, b): return a + b",
        ],
    ),
]

for title, lines in pages:
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(60, 780, title)

    pdf.setFont("Helvetica", 12)
    y = 735

    for line in lines:
        pdf.drawString(60, y, line)
        y -= 28

    pdf.showPage()

pdf.save()

print(f"Created sample PDF: {output_path.resolve()}")
