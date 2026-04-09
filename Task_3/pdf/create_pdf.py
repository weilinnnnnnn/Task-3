from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def make_pdf(filename, text):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(width / 2, height / 2, text)
    c.save()

make_pdf("file1.pdf", "This is file A!")
make_pdf("file2.pdf", "This is file B!")
print("Done!")