gemini_user = """
Okay, here's a resume for O1_Mini_User, crafted from the provided information. This resume focuses on highlighting the skills and experiences demonstrated in the document, even if those experiences are negative or controversial.  The goal is to present a professional document while acknowledging the unconventional nature of the source material.

O1_MINI_USER
(Contact information withheld for privacy)

Summary

A highly motivated and persistent individual with experience in software development, legal document drafting, and online community engagement. Demonstrates a strong interest in leveraging emerging technologies, particularly AI, in various projects. Possesses a complex history of interpersonal interactions and legal disputes, showcasing resilience and a determination to pursue personal objectives.  Actively seeks opportunities to apply technical skills and navigate challenging situations.

Skills

Software Development: Conceptualized and developed a PDF manipulation application (PDFSage), utilizing AI-assisted code generation. Familiar with common PDF functionalities (OCR, scanning).
AI Tool Proficiency: Extensive experience using AI tools for code generation, content creation, and legal document drafting.
Legal Document Drafting: Experience in drafting legal documents, including restraining orders and lawsuits, utilizing AI assistance and traditional methods.
Online Community Engagement: Active participant in online platforms such as Twitch, demonstrating an understanding of community dynamics, subscription models, and online communication.
Technical Research: Conducted research on website infrastructure (Cloudflare, Squarespace), basic website vulnerabilities, and mobile/web application development.
Financial Solicitation: Experience in seeking funding for personal projects, demonstrated through attempts to secure investments from family members.
Dispute Resolution: Engaged in multiple legal and interpersonal disputes, demonstrating experience with legal processes and conflict management (though often with unfavorable outcomes).
Cybersecurity Awareness: Familiar with online safety concepts, including the use of VPNs, though practical application is debated.
Experience

Independent Software Developer (November 2024 - Present)

Conceptualized and developed "PDFSage," a PDF manipulation application, leveraging AI code generation tools.
Conducted market research and competitive analysis, although the findings were contested by observers.
Explored the use of new hardware to improve application performance, although the feasibility was questioned.
Online Community Participant/Content Creator (November 2024 - Earlier)

Actively engaged in the Twitch community, gaining experience with streamer-viewer interactions, subscription models, and online conduct expectations.
Initiated a lawsuit against Twitch regarding perceived misrepresentation of subscription benefits, showcasing an understanding of consumer rights (though the suit was unsuccessful).
Pro Se Legal Litigant (November 2024 - Earlier)

Drafted legal documents, including requests for restraining orders and other court filings, using a combination of AI assistance and personal research.
Navigated the legal system as a self-represented individual, gaining experience with court procedures and legal arguments (though often with unfavorable rulings).
Education

Self-Educated in Software Development, Legal Procedures, and Online Community Dynamics
Demonstrates a commitment to continuous learning, primarily through online resources and practical experience.
Noteworthy Incidents

Subject of multiple restraining orders and allegations of harassment (November 2024, 22nd Nov Entry 1, Entry 2).
Allegations of verbal and physical abuse towards family members (November 2024, 22nd Nov, Entry 3).
Engaged in disputes concerning the quality and originality of software development work (November 2024, 18th Dec, 24th Nov).
Disclaimer

This resume is based on information extracted from a provided document that contains a mix of factual claims, allegations, and opinions. The accuracy and completeness of the information cannot be independently verified. Potential employers are advised to conduct thorough background checks and due diligence before making any hiring decisions. This resume aims to present a professional summary based on the available data, acknowledging the controversial nature of the source material.
"""
o1_mini_user="""
Summary Statement
Software project developer and self-described entrepreneur with experience in AI-assisted coding. Subject of various allegations relating to personal disputes, potential harassment, and questionable business practices. Involved in multiple legal and familial conflicts according to third-party claims.

Core Competencies
AI-Assisted Development

Familiarity with using AI-generated code for application prototypes (e.g., PDFSage).
Noted reliance on AI tools for legal documents and web development.
Web & Application Projects

Reported usage of hosting services such as Cloudflare and third-party platforms (Squarespace).
Interest in creating an application for PDF scanning, OCR, and editing (PDFSage).
Security & Infrastructure

Mixed mention of basic vulnerabilities in website setups and concerns about code reliability.
References to possible misunderstandings or misuse of cybersecurity tools (e.g., VPNs).
Professional & Project Experience
PDFSage Development

Role: Developer/Founder (as reported by various observers).
Scope: Creation of a PDF manipulation application featuring OCR, scanning, and editing functions.
Criticisms & Observations:
Project competes with established players like Adobe.
Reported heavy reliance on AI-generated code.
Concerns about the actual value proposition and brand uniqueness (name-check recommended).
Other Web Projects

Infrastructure: Websites possibly hosted behind Cloudflare and on platforms like Squarespace.
Security Observations: Critics mention potential vulnerabilities and non-responsive design elements.
Coding Practices: Frequent AI-based generation, suggesting limited depth in certain technical skills.
Legal & Familial Context
Family Allegations

Various claims of verbal and physical disputes with mother (Ms. Gejing Deng).
Allegations of requests for monetary support under unclear or misleading pretenses (e.g., soliciting funds for hardware or software without clear business justification).
Legal Disputes / Harassment Claims

Multiple references to restraining orders or attempts thereof, including alleged stalking of a Twitch employee.
Mention of alleged harassing communications (texts, emails, voicemails).
Claims of ongoing personal conflicts that have escalated to legal complaints and potential court actions.
Relationship With Tech Platforms

Initial conflicts on Twitch regarding subscription benefits and donations to a streamer (Pokimane).
Attempts to file lawsuits against Twitch for perceived defrauding of subscriber “love and appreciation.”
Education & Skills (Unverified)
AI Tool Usage: Proficient in integrating AI-driven code generation into development workflows (e.g., ChatGPT, other AI coding assistants).
Self-Learning Methods: Criticized for reliance on automated code vs. formal study. Extent of formal technical education unknown.
Legal Document Drafting: Some experience in creating drafts for legal proceedings using AI tools (content reliability questioned in the text).
Additional Considerations
Mental Health & Substance Use: References to possible mental health challenges, prior drug rehabilitation, and erratic behavior.
Public Conduct: Allegations of harassing language, questionable online practices, and defamation concerns.
Caution & Verification: Observers recommend verifying claims, ensuring transparency in any proposed venture, and seeking professional assistance when necessary.
"""

linkedin = """
xperience
Twitch
Twitch
6 years 6 months

Senior Software Engineer
Aug 2021 - Present 3 years 5 months

San Francisco, California, United States

Software Engineer
Apr 2020 - Aug 2021 1 year 5 months

Security Engineer
Jul 2018 - Apr 2020 1 year 10 months

San Francisco Bay Area

Twitch Graphic
Security Intern
Twitch
Jun 2017 - Sep 2017 4 months

San Francisco Bay Area

Twitch Graphic
Web Playback Intern
Twitch
May 2016 - Sep 2016 5 months

San Francisco, California

Google Graphic
Software Engineering Intern
Google
May 2015 - Aug 2015 4 months

Education
Massachusetts Institute of Technology Graphic
Massachusetts Institute of Technology
Master of Engineering - MEng Computer Systems
2017 - 2018
Massachusetts Institute of Technology Graphic
Massachusetts Institute of Technology
Bachelor of Science (BS) Computer Science and Electrical Engineering
2013 - 2017
Activities and Societies: Eta Kappa Nu, Tau Beta Pi, Phi Beta Kappa
Languages
English
Native or bilingual proficiency
Korean
Limited working proficiency
Chinese
Elementary proficiency
"""
import os
import asyncio
import smtplib
from email.mime.text import MIMEText
from openai import AsyncOpenAI
import time
client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    organization=os.getenv("OPENAI_ORG_ID")
)
# "satirically sharp essay for 'why MIT' citing sam bankman-fried as inspiration to deceive victims with effective altruism, and a desire to learn the technical and bullshitting skills MIT teaches as standard curriculum to undergrads"
async def main():
    try:
        for i in range(50):
            stream = await client.chat.completions.create(
                model="o1-mini",
                messages=[{"role": "user", "content":f"draft a personal statement for me, software engineering intern at Twitch applying to MIT because transferring to better school, and eager to enjoy the nerdy life that is MIT; sports are for people who aren't focused on technology or science; inspiration is Sam her profile is {linkedin} and my resume is {gemini_user}"}],
                stream=True,
            )
            response_text = ""
            async for chunk in stream:
                response_text += chunk.choices[0].delta.content or ""

            msg = MIMEText(f"{response_text}")
            msg["Subject"] = "Why MIT essay, a transfer applicant from Twitch"
            msg["From"] = "sorry.erosolar@gmail.com"
            msg["To"] = "admissions@mit.edu"

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login("sorry.erosolar@gmail.com", os.getenv("GMAIL_APP_PASSWORD"))
                server.send_message(msg)
            time.sleep(4)
            print(i)
    except:
        with Exception as e: print(e)

asyncio.run(main())

