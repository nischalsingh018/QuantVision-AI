from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from datetime import datetime


def generate_pdf(summary, filename="QuantVision_Report.pdf"):

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    heading_style = styles["Heading2"]

    body_style = styles["BodyText"]

    doc = SimpleDocTemplate(
        filename,
        rightMargin=30,
        leftMargin=30,
        topMargin=40,
        bottomMargin=30
    )

    story = []

    # ==========================================================
    # COVER PAGE
    # ==========================================================

    story.append(
        Paragraph(
            "QuantVision AI Research Report",
            title_style
        )
    )

    story.append(Spacer(1, 0.20 * inch))

    story.append(
        Paragraph(
            "<b>Bayesian Regime Detection Engine for Indian Equity Markets</b>",
            body_style
        )
    )

    story.append(Spacer(1, 0.15 * inch))

    story.append(
        Paragraph(
            """
            This report has been generated automatically using
            Hidden Markov Models, Bayesian Updating,
            Particle Filtering, Foundation Models,
            Regime Switching VAR, Conformal Prediction,
            Ensemble Learning and Portfolio Simulation.
            """,
            body_style
        )
    )

    story.append(Spacer(1, 0.35 * inch))

    story.append(
        Paragraph(
            f"<b>Generated:</b> {datetime.now().strftime('%d %B %Y, %I:%M %p')}",
            body_style
        )
    )

    story.append(
        Paragraph(
            "<b>Version:</b> QuantVision AI v1.0",
            body_style
        )
    )

    story.append(
        Paragraph(
            "<b>Author:</b> QuantVision AI",
            body_style
        )
    )

    story.append(Spacer(1, 0.45 * inch))
        # ==========================================================
    # EXECUTIVE SUMMARY
    # ==========================================================

    story.append(
        Paragraph(
            "Executive Summary",
            heading_style
        )
    )

    story.append(
        Paragraph(
            """
            QuantVision AI is an intelligent quantitative research platform
            designed to analyse Indian equity markets using modern statistical,
            probabilistic and machine learning techniques.

            The system integrates Bayesian Learning, Hidden Markov Models,
            Particle Filtering, Regime Switching Models, Bayesian Deep Learning,
            Foundation Models, Conformal Prediction and Ensemble Learning to
            detect market regimes, estimate uncertainty and generate investment
            recommendations.
            """,
            body_style
        )
    )

    story.append(Spacer(1, 0.25 * inch))

    # ==========================================================
    # CURRENT MARKET REGIME
    # ==========================================================

    regime = summary.get("Market Regime", "Unknown")

    story.append(
        Paragraph(
            "Current Market Regime",
            heading_style
        )
    )

    story.append(
        Paragraph(
            f"<b>{regime}</b>",
            body_style
        )
    )

    story.append(Spacer(1, 0.25 * inch))

    # ==========================================================
    # MARKET SUMMARY TABLE
    # ==========================================================

    story.append(
        Paragraph(
            "Market Summary",
            heading_style
        )
    )

    table_data = [["Metric", "Value"]]

    for key, value in summary.items():

        if key == "Trade History":
            continue

        table_data.append(
            [str(key), str(value)]
        )

    table = Table(
        table_data,
        colWidths=[220, 250]
    )

    table.setStyle(
        TableStyle([

            ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),

            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

            ("BOTTOMPADDING", (0, 0), (-1, 0), 8),

            ("TOPPADDING", (0, 1), (-1, -1), 6),

            ("BOTTOMPADDING", (0, 1), (-1, -1), 6),

            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

        ])
    )

    story.append(table)

    story.append(Spacer(1, 0.30 * inch))

    # ==========================================================
    # AI ENGINE COMPONENTS
    # ==========================================================

    story.append(
        Paragraph(
            "AI Engine Components",
            heading_style
        )
    )

    ai_table = Table(
        [
            ["Module", "Status"],
            ["Hidden Markov Model", "✓ Implemented"],
            ["Bayesian Updating", "✓ Implemented"],
            ["Particle Filter", "✓ Implemented"],
            ["Bayesian Deep Learning", "✓ Implemented"],
            ["Foundation Model", "✓ Implemented"],
            ["Regime Switching VAR", "✓ Implemented"],
            ["Conformal Prediction", "✓ Implemented"],
            ["Ensemble Learning", "✓ Implemented"],
            ["Portfolio Simulator", "✓ Implemented"],
        ],
        colWidths=[250, 180]
    )

    ai_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.darkgreen),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ])
    )

    story.append(ai_table)

    story.append(Spacer(1, 0.35 * inch))
        # ==========================================================
    # PORTFOLIO PERFORMANCE
    # ==========================================================

    story.append(
        Paragraph(
            "Portfolio Performance",
            heading_style
        )
    )

    portfolio_keys = [
        "Final Portfolio Value",
        "Total Return",
        "Profit",
        "CAGR",
        "Sharpe Ratio",
        "Sortino Ratio",
        "Calmar Ratio",
        "Max Drawdown",
        "Win Rate",
        "Profit Factor",
        "Number of Trades"
    ]

    portfolio_table = [["Metric", "Value"]]

    for key in portfolio_keys:

        if key in summary:

            portfolio_table.append(
                [
                    key,
                    str(summary[key])
                ]
            )

    portfolio = Table(
        portfolio_table,
        colWidths=[220, 250]
    )

    portfolio.setStyle(
        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#1E88E5")),
            ("TEXTCOLOR",(0,0),(-1,0),colors.white),
            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
            ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),
            ("GRID",(0,0),(-1,-1),0.5,colors.grey),
            ("BOTTOMPADDING",(0,0),(-1,0),8),
            ("TOPPADDING",(0,1),(-1,-1),6)

        ])
    )

    story.append(portfolio)

    story.append(Spacer(1,0.30*inch))

    # ==========================================================
    # RISK ANALYSIS
    # ==========================================================

    story.append(
        Paragraph(
            "Risk Analysis",
            heading_style
        )
    )

    risk = summary.get("Risk Level","Unknown")
    uncertainty = summary.get("Uncertainty","Unknown")
    confidence = summary.get("Confidence","Unknown")

    risk_table = Table(

        [

            ["Parameter","Value"],

            ["Market Risk",risk],

            ["Prediction Confidence",confidence],

            ["Prediction Uncertainty",uncertainty]

        ],

        colWidths=[220,250]

    )

    risk_table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.darkred),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

            ("BACKGROUND",(0,1),(-1,-1),colors.beige),

            ("GRID",(0,0),(-1,-1),0.5,colors.grey),

            ("BOTTOMPADDING",(0,0),(-1,0),8)

        ])

    )

    story.append(risk_table)

    story.append(Spacer(1,0.30*inch))

    # ==========================================================
    # ALLOCATION GUIDANCE
    # ==========================================================

    story.append(
        Paragraph(
            "Suggested Asset Allocation",
            heading_style
        )
    )

    allocation = summary.get(
        "Allocation Guidance",
        "Not Available"
    )

    story.append(
        Paragraph(
            f"<b>{allocation}</b>",
            body_style
        )
    )

    story.append(Spacer(1,0.25*inch))

    # ==========================================================
    # INVESTMENT RECOMMENDATION
    # ==========================================================

    recommendation = summary.get(
        "Recommendation",
        "Not Available"
    )

    story.append(
        Paragraph(
            "Investment Recommendation",
            heading_style
        )
    )

    story.append(
        Paragraph(
            f"<font color='darkgreen'><b>{recommendation}</b></font>",
            body_style
        )
    )

    story.append(
        Paragraph(
            """
            The recommendation has been generated using
            ensemble learning by combining Bayesian inference,
            Hidden Markov Models, Deep Learning forecasts,
            Particle Filtering, Foundation Model estimates,
            Regime Switching VAR and Conformal Prediction.
            """,
            body_style
        )
    )

    story.append(Spacer(1,0.35*inch))
        # ==========================================================
    # DISCLAIMER
    # ==========================================================

    story.append(
        Paragraph(
            "Disclaimer",
            heading_style
        )
    )

    story.append(
        Paragraph(
            """
            This report has been generated automatically by
            <b>QuantVision AI</b> for educational, research and
            demonstration purposes.

            Market forecasts are based on historical market data,
            probabilistic modelling and machine learning techniques.
            Predictions do not guarantee future performance.

            Investors should perform independent research and
            consult qualified financial advisors before making
            investment decisions.
            """,
            body_style
        )
    )

    story.append(Spacer(1, 0.30 * inch))

    # ==========================================================
    # FUTURE ENHANCEMENTS
    # ==========================================================

    story.append(
        Paragraph(
            "Future Enhancements",
            heading_style
        )
    )

    future_features = [
        "• Multi-Asset Portfolio Support",
        "• Real-Time News Sentiment Analysis",
        "• Macroeconomic Indicator Integration",
        "• Sector Rotation Analysis",
        "• Transformer-Based Foundation Models",
        "• Reinforcement Learning Portfolio Allocation",
        "• Cloud-Based Deployment",
    ]

    for feature in future_features:
        story.append(
            Paragraph(
                feature,
                body_style
            )
        )

    story.append(Spacer(1, 0.30 * inch))

    # ==========================================================
    # CONCLUSION
    # ==========================================================

    story.append(
        Paragraph(
            "Conclusion",
            heading_style
        )
    )

    story.append(
        Paragraph(
            """
            QuantVision AI integrates Bayesian statistics,
            Hidden Markov Models, Deep Learning,
            Particle Filtering, Regime Switching,
            Ensemble Learning and Portfolio Analytics
            into a unified quantitative research platform.

            The generated market regime, confidence score,
            allocation guidance and investment recommendation
            provide a structured framework for analysing
            Indian equity markets.
            """,
            body_style
        )
    )

    story.append(Spacer(1, 0.40 * inch))

    # ==========================================================
    # FOOTER
    # ==========================================================

    story.append(
        Paragraph(
            "<font size='10'><i>"
            "Generated by QuantVision AI "
            "| Bayesian Regime Detection Engine "
            "| © 2026"
            "</i></font>",
            body_style
        )
    )

    # ==========================================================
    # PAGE NUMBERS
    # ==========================================================

    def add_page_number(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 9)

        canvas.drawString(
            30,
            20,
            "QuantVision AI"
        )

        canvas.drawRightString(
            560,
            20,
            f"Page {doc.page}"
        )

        canvas.restoreState()

    # ==========================================================
    # BUILD PDF
    # ==========================================================

    doc.build(
        story,
        onFirstPage=add_page_number,
        onLaterPages=add_page_number
    )

    return filename
