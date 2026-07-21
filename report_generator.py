from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(summary, filename="QuantVision_Report.pdf"):

    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>QuantVision AI Performance Report</b>", styles["Title"]))

    for key, value in summary.items():

        if key == "Trade History":
            continue

        story.append(
            Paragraph(f"<b>{key}</b>: {value}", styles["BodyText"])
        )

    doc.build(story)

    return filename