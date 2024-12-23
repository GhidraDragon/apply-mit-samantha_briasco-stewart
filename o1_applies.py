import os
import sys
import time
import timeit
import random
import asyncio
import smtplib
import concurrent.futures
from email.mime.text import MIMEText
from openai import AsyncOpenAI

# Instantiate your OpenAI client (replace with your own valid keys)
client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    organization=os.getenv("OPENAI_ORG_ID")
)

def generate_o1_applicants(num_applicants=100):
    """
    Generate a list of fictional, highly qualified O1-mini applicants to MIT.
    Each entry is a dictionary with random attributes.
    """

    # Set a random seed for reproducibility
    random.seed(42)

    # Name pools for generating fictional applicants
    first_names = [
        "Alex", "Taylor", "Jordan", "Morgan", "Casey", "Riley", "Peyton", "Avery",
        "Sydney", "Quinn", "Blake", "Reese", "Hayden", "Rowan", "Logan", "Cameron",
        "Skyler", "Hunter", "Dakota", "Sage"
    ]
    last_names = [
        "Johnson", "Smith", "Lee", "Patel", "Garcia", "Jackson", "Davis", "Miller",
        "Rodriguez", "Wilson", "Martinez", "Anderson", "Taylor", "Thomas", "Moore",
        "Brown", "Thompson", "Hall", "Hernandez", "Lopez"
    ]

    majors = [
        "Computer Science", "Electrical Engineering", "Physics", "Mathematics",
        "Mechanical Engineering", "Biological Engineering", "Aerospace Engineering",
        "Chemical Engineering", "Data Science", "Economics", "Artificial Intelligence",
        "Robotics", "Brain & Cognitive Sciences", "Nuclear Engineering"
    ]

    achievements = [
        "Published 2 papers in machine learning conferences",
        "Built an open-source robotics toolkit with 1k+ GitHub stars",
        "Won a gold medal at the International Mathematics Olympiad",
        "Co-founded a biotech startup focusing on cancer research",
        "Led a hackathon team to create an AR teaching platform for STEM education",
        "Interned at NASA on rocket propulsion analysis",
        "Developed a neural network for autonomous drone navigation",
        "Volunteered in rural areas to teach STEM to underprivileged kids",
        "Designed and programmed an award-winning robot soccer team",
        "Created a cryptography library for quantum-resistant protocols",
        "Placed top-5 in multiple Kaggle competitions"
    ]

    applicants_list = []
    for i in range(num_applicants):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        major = random.choice(majors)
        selected_achievements = random.sample(achievements, k=random.randint(2, 3))

        applicant_info = {
            "applicant_id": f"O1-MINI-{i+1:03d}",
            "name": name,
            "major_of_interest": major,
            "notable_achievements": selected_achievements,
            "why_fit_for_mit": (
                "Demonstrates high intellectual vitality, advanced problem-solving skills, "
                "and an eagerness for rigorous academic challenges."
            )
        }
        applicants_list.append(applicant_info)

    return applicants_list

async def apply_to_mit(applicant, linkedin, o1_mini_user):
    """
    Example async method that sends a satirical MIT application email.
    Replace content and logic with your actual needs.
    """
    try:
        # Example: streaming completions from OpenAI
        stream = await client.chat.completions.create(
            model="o1-mini",
            messages=[
                {
                    "role": "user",
                    "content": (
                        "A software engineering intern at Twitch applying to MIT "
                        "to transfer to a better school, eager to enjoy the nerdy life at MIT. "
                        "Sports are for people who aren't focused on technology or science. "
                        f"Inspiration is Sam. LinkedIn: {linkedin}. "
                        f"Applicant profile: {o1_mini_user}. "
                        f"Current fictional applicant: {applicant}"
                    )
                }
            ],
            stream=True,
        )

        response_text = ""
        async for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta is not None:
                response_text += delta

        # Construct email
        msg = MIMEText(response_text)
        msg["Subject"] = f"Why MIT Twitch: {applicant['applicant_id']}"
        msg["From"] = "sorry.erosolar@gmail.com"
        msg["To"] = "admissions@mit.edu"

        # Send email (example uses Gmail SSL)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login("sorry.erosolar@gmail.com", os.getenv("GMAIL_APP_PASSWORD"))
            server.send_message(msg)

        # Pause to avoid flooding (blocking sleep in async code)
        time.sleep(2)  # or `await asyncio.sleep(2)` for a truly non-blocking approach

        print(f"Application sent for {applicant['applicant_id']}: {applicant['name']}")

    except Exception as e:
        print(f"Error applying for {applicant['applicant_id']}: {e}")

def run_apply(applicant, linkedin, o1_mini_user):
    """
    Synchronous wrapper to run the async apply_to_mit() method.
    Also catches any exceptions so the program won't crash.
    """
    try:
        asyncio.run(apply_to_mit(applicant, linkedin, o1_mini_user))
    except Exception as e:
        print(f"Thread pool error for {applicant['applicant_id']}: {e}")

def main():
    """
    Main function that:
      1) Reads sys.argv[1] to specify how many applicants to generate.
      2) Processes them in a ThreadPoolExecutor with max_workers=5.
      3) Wraps the generation in a timeit measurement to see how long it took.
    """
    if len(sys.argv) < 2:
        print("Usage: python o1_apply.py <num_applicants>")
        sys.exit(1)

    # Number of applicants from sys.argv[1]
    num_applicants = int(sys.argv[1])

    # We'll measure how long it takes to generate the applicants
    start_time = timeit.default_timer()

    # Generate the applicants
    applicants = generate_o1_applicants(num_applicants)

    # For this example, let's define some placeholders
    linkedin = "http://linkedin.com/in/fakeprofile"
    o1_mini_user = "O1 user data"

    # We stop the timer after generation for demonstration
    generation_elapsed = timeit.default_timer() - start_time
    print(f"Generated {len(applicants)} applicants in {generation_elapsed:.3f} seconds.")

    # Now let's do the thread pool portion, up to 5 at once
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = []
            for applicant in applicants:
                # Submit each applicant to the thread pool
                future = executor.submit(run_apply, applicant, linkedin, o1_mini_user)
                futures.append(future)
            
            # Wait for all tasks to complete (or fail) without crashing everything
            for future in concurrent.futures.as_completed(futures):
                if future.exception():
                    print(f"Task raised an exception: {future.exception()}")

    except Exception as main_e:
        print(f"Error in main concurrency block: {main_e}")

if __name__ == "__main__":
    main()
