from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_report(customer_name, result):

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/{customer_name.replace(' ', '_')}_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>FinShield AI Customer Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Customer:</b> {customer_name}", styles["Normal"]))

    story.append(Paragraph(f"<b>Financial Score:</b> {result['score']}", styles["Normal"]))

    story.append(Paragraph(f"<b>Risk:</b> {result['risk']}", styles["Normal"]))

    story.append(Paragraph(f"<b>Loan Decision:</b> {result['decision']}", styles["Normal"]))

    story.append(Paragraph("<br/><b>Decision Factors</b>", styles["Heading2"]))

    for reason in result["reasons"]:
        story.append(Paragraph(f"• {reason}", styles["Normal"]))

    story.append(Paragraph("<br/><b>Recommendations</b>", styles["Heading2"]))

    for rec in result["recommendations"]:
        story.append(Paragraph(f"• {rec}", styles["Normal"]))

    doc.build(story)

    return filename