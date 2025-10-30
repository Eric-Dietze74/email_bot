# Daily CFA Quiz Email Bot

[[Daily CFA Quiz Email] (https://github.com/Eric-Dietze74/email_bot/actions/workflows/daily_email.yml/badge.svg)](https://github.com/Eric-Dietze74/email_bot/actions/workflows/daily_email.yml)

This project automatically sends a daily email containing terms and definitions from a quizlet containing material covered on a CFA Level 1. Original Quizlet here (https://quizlet.com/262462689/cfa-level-1-quant-flash-cards/)

It uses Python’s `smtplib` and `EmailMessage` libraries, reads a local CSV file of questions, and is automated to run daily through **GitHub Actions**.

---

## Features
- Randomly selects a set number of CFA Level 1 questions from a CSV file  
- Sends formatted questions and answers via email  
- Runs automatically each morning using GitHub Actions (with secure secrets handling)

---
```text
## Project Structure
email_bot/
├── .github/
│ └── workflows/
│ └── daily_email.yml # GitHub Actions workflow
├── CFA Level 1.csv # Source of quiz questions
├── email_bot.py # Main script
└── README.md # This file

```
---

## How It Works

1. **Select Questions:**  
   The script loads `CFA Level 1.csv` and selects a random subset of questions to include in the daily quiz.

2. **Build Email:**  
   Formats the selected questions and answers into a single email message.

3. **Send Email:**  
   Uses Gmail’s SMTP server to send the message to the specified address.

4. **Automation:**  
   The GitHub Actions workflow (`daily_email.yml`) runs the script automatically every morning.

---

## Requirements
- Python 3.10+


## Environment Variables (GitHub Secrets)
This project uses GitHub Actions Secrets for authentication. 

## GitHub Actions Schedule 
The workflow runs automatically every morning at 8 AM Eastern Time. (UTC 12:00 adjusted for daylight savings). 


