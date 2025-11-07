import os
import smtplib
from email.message import EmailMessage
import pandas as pd
import random
from datetime import date

today = str(date.today())

# Number of questions that will be sent in email
number_of_questions = 5

# Import CSV with questions and definitions
csv_path = "CFA Level 1.csv"
df = pd.read_csv(csv_path)

# Define columns
term, definition = df.columns[0], df.columns[1]

# Randomly select unique questions
questions = df.sample(n=number_of_questions, replace=False)

# Build question text
questions_text = "\n\n".join([f"{i+1}. {q}" for i, q in enumerate(questions[term])])

# Build answer text
answers_text = "\n\n".join([f"{i+1}. {a}" for i, a in enumerate(questions[definition])])

# Combine sections with spacing
full_message = f"{questions_text}\n\n\n\n\n\n\n\n\n{answers_text}"

# Email setup
msg = EmailMessage()
msg["Subject"] = "CFA Quiz " + today
msg["From"] = os.getenv("EMAIL_USER")
msg["To"] = os.getenv("EMAIL_USER")
msg.set_content(full_message)

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

# Send email securely
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASS)
    server.send_message(msg)

print("Email sent successfully.")
