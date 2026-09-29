from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable,
)

INK = HexColor("#1C2B3A")
MUTED = HexColor("#5C6773")
ACCENT = HexColor("#B45F2E")
RULE = HexColor("#DDD6CC")

OUT_PATH = "/Users/Nagababu.Sattineni/IdeaProjects/nagababusattineni.github.io/Nagababu_Sattineni_Resume.pdf"

doc = SimpleDocTemplate(
    OUT_PATH, pagesize=letter,
    leftMargin=0.75 * inch, rightMargin=0.75 * inch,
    topMargin=0.65 * inch, bottomMargin=0.6 * inch,
    title="Nagababu Sattineni - Senior SDET Resume",
    author="Nagababu Sattineni",
)

name_style = ParagraphStyle("Name", fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=INK, spaceAfter=4)
title_style = ParagraphStyle("Title", fontName="Helvetica-Bold", fontSize=11.5, leading=14, textColor=ACCENT, spaceAfter=6)
contact_style = ParagraphStyle("Contact", fontName="Helvetica", fontSize=9.3, textColor=MUTED, spaceAfter=10)
summary_style = ParagraphStyle("Summary", fontName="Helvetica", fontSize=9.6, textColor=INK, leading=13.5, spaceAfter=4)
section_style = ParagraphStyle("Section", fontName="Helvetica-Bold", fontSize=11, textColor=ACCENT, spaceBefore=12, spaceAfter=6, letterSpacing=0.6)
job_title_style = ParagraphStyle("JobTitle", fontName="Helvetica-Bold", fontSize=10.3, textColor=INK)
job_period_style = ParagraphStyle("JobPeriod", fontName="Helvetica", fontSize=8.8, textColor=MUTED, alignment=2)
job_company_style = ParagraphStyle("JobCompany", fontName="Helvetica-Oblique", fontSize=9.3, textColor=MUTED, spaceAfter=3)
bullet_style = ParagraphStyle("Bullet", fontName="Helvetica", fontSize=9.3, textColor=INK, leading=13, leftIndent=12, bulletIndent=0, spaceAfter=2)
stack_style = ParagraphStyle("Stack", fontName="Helvetica", fontSize=8.6, textColor=MUTED, spaceAfter=10)
skill_label_style = ParagraphStyle("SkillLabel", fontName="Helvetica-Bold", fontSize=9.2, textColor=INK)
skill_value_style = ParagraphStyle("SkillValue", fontName="Helvetica", fontSize=9.0, textColor=MUTED, spaceAfter=6)
edu_title_style = ParagraphStyle("EduTitle", fontName="Helvetica-Bold", fontSize=9.8, textColor=INK)
edu_meta_style = ParagraphStyle("EduMeta", fontName="Helvetica", fontSize=8.8, textColor=MUTED, spaceAfter=6)

story = []

story.append(Paragraph("Nagababu Sattineni", name_style))
story.append(Paragraph("Senior SDET", title_style))
story.append(Paragraph(
    "nsattineni18@gmail.com &nbsp;|&nbsp; 9573061141 &nbsp;|&nbsp; Hyderabad, India &nbsp;|&nbsp; "
    "linkedin.com/in/nagababu-sattineni-66639a54", contact_style))
story.append(HRFlowable(width="100%", thickness=0.8, color=RULE, spaceAfter=8))

story.append(Paragraph(
    "Senior SDET with 12+ years in QA, spanning manual and automation testing. Currently "
    "building and maintaining an API/UI automation framework on Karate at DP World, with "
    "CI/CD pipelines on Azure DevOps. Strong background in Selenium/Java automation, BDD "
    "(Cucumber), and end-to-end ownership of test strategy across release, patch, and "
    "hotfix cycles.", summary_style))

story.append(Paragraph("EXPERIENCE", section_style))

jobs = [
    {
        "title": "Senior SDET",
        "period": "Aug 2021 – Present",
        "company": "DP World, Hyderabad",
        "bullets": [
            "Design and maintain API and UI automation suites on the Karate framework across multiple product modules.",
            "Build and own Azure DevOps CI/CD pipelines for automated test execution across environments.",
            "Drive test data strategy, regression coverage, and failure triage for release and drop cycles.",
        ],
        "stack": "Stack: Karate, Java, Azure DevOps, Maven, Git",
    },
    {
        "title": "Senior Software Engineer in Test",
        "period": "May 2017 – Aug 2021",
        "company": "Gainsight, Hyderabad",
        "bullets": [
            "Owned QA delivery for the Reporting product — flat, aggregated, and filtered reports plus charting and dashboards.",
            "Led test design reviews and distributed work across the QA team for each release cycle.",
            "Ran parallel automation alongside feature development and certified releases, patches, and hotfixes.",
            "Partnered with development and product management to triage defects and scope enhancements.",
        ],
        "stack": "Stack: Selenium WebDriver, Java, Cucumber, TestNG, Jenkins",
    },
    {
        "title": "Test Engineer",
        "period": "Jan 2013 – Apr 2017",
        "company": "GGK Technologies, Hyderabad",
        "bullets": [
            "Built Selenium/Java automation for Sangam, a timesheet and leave-tracking web app for Clientek (USA).",
            "Performed functional, regression, and re-testing for ePASS, a clinical assessment platform for Inovalon (USA).",
            "Managed and tracked defects through TFS, working directly with feature developers.",
        ],
        "stack": "Stack: Selenium WebDriver, Java, TFS",
    },
]

for job in jobs:
    header_table = Table(
        [[Paragraph(job["title"], job_title_style), Paragraph(job["period"], job_period_style)]],
        colWidths=[4.6 * inch, 1.6 * inch],
    )
    header_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(header_table)
    story.append(Paragraph(job["company"], job_company_style))
    for b in job["bullets"]:
        story.append(Paragraph("• " + b, bullet_style))
    story.append(Paragraph(job["stack"], stack_style))

story.append(Paragraph("SKILLS", section_style))

skills = [
    ("Languages", "Java"),
    ("Automation", "Karate, Selenium, Playwright"),
    ("API Testing", "API, Rest Assured"),
    ("BDD & Framework Design", "Cucumber, Framework"),
    ("Leadership", "QA Lead, Project Planning, Resource Planning"),
]

skill_rows = []
for i in range(0, len(skills), 2):
    left = skills[i]
    right = skills[i + 1] if i + 1 < len(skills) else None
    left_cell = [Paragraph(left[0], skill_label_style), Paragraph(left[1], skill_value_style)]
    right_cell = [Paragraph(right[0], skill_label_style), Paragraph(right[1], skill_value_style)] if right else [Paragraph("", skill_value_style)]
    skill_rows.append([left_cell, right_cell])

skills_table = Table(skill_rows, colWidths=[3.1 * inch, 3.1 * inch])
skills_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
]))
story.append(skills_table)

story.append(Paragraph("EDUCATION", section_style))
story.append(Paragraph("Master of Computer Applications (MCA)", edu_title_style))
story.append(Paragraph("GRIET, Hyderabad — 2013", edu_meta_style))
story.append(Paragraph("B.Sc., MPCS", edu_title_style))
story.append(Paragraph("Sri YN College, Narsapur — 2010", edu_meta_style))

doc.build(story)
print("Wrote", OUT_PATH)
