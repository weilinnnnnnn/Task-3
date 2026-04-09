from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch

def make_contract_pdf(filename, client, payment, label):
    doc = SimpleDocTemplate(filename, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=72)
    styles = getSampleStyleSheet()
    story = []

    title_style = ParagraphStyle('title', fontSize=24, fontName='Helvetica-Bold',
                                  spaceAfter=20, textColor=colors.HexColor('#1a1a2e'))
    label_style = ParagraphStyle('label', fontSize=12, fontName='Helvetica',
                                  spaceAfter=30, textColor=colors.grey)

    story.append(Paragraph("Housing Contract", title_style))
    story.append(Paragraph(f"Document Type: {label}", label_style))
    story.append(Spacer(1, 0.2 * inch))

    data = [
        ["Field", "Value"],
        ["Document Type", "Housing Contract"],
        ["Client", client],
        ["Payment Amount", payment],
    ]

    table = Table(data, colWidths=[2.5 * inch, 3.5 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a1a2e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f4ff')]),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 11),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('PADDING', (0, 0), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(table)
    doc.build(story)

make_contract_pdf("fraudulent_contract.pdf", "John Smith", "$10,000", "FRAUDULENT")
make_contract_pdf("real_contract.pdf", "John Smith", "$10", "REAL")

print("Done!")