from bs4 import BeautifulSoup
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

def extract_delinquent_reviewers(submissions_html, pc_html):
    # Parse the submissions HTML to find delinquent reviewers
    with open(submissions_html, 'r') as file:
        submissions_soup = BeautifulSoup(file, 'html.parser')

    delinquent_reviewers = {}

    # Find all rows representing papers
    for paper in submissions_soup.find_all('tr', id=lambda x: x and x.startswith('p')):
        paper_id = paper['id'].replace('p', '')
        # Look for the div containing the reviewers
        reviewers_div = paper.find_next_sibling('tr', class_='plx')
        if reviewers_div:
            # Locate the list of reviewers
            reviewer_list = reviewers_div.find('ul', class_='comma')
            if reviewer_list:
                for li in reviewer_list.find_all('li'):
                    reviewer_name = li.get_text(strip=True).split('(')[0].strip()
                    reviewer_name = re.sub(r'\s*\dR\d\s*$', '', reviewer_name)
                    review_status = li.find('span', class_='rtinc')
                    # Check if the review status indicates delinquency
                    if review_status and ('not started' in review_status['title'] or 'draft' in review_status['title']):
                        if reviewer_name not in delinquent_reviewers:
                            delinquent_reviewers[reviewer_name] = []
                        delinquent_reviewers[reviewer_name].append(paper_id)


    # Parse the PC HTML to get reviewer emails
    with open(pc_html, 'r') as file:
        pc_soup = BeautifulSoup(file, 'html.parser')

    reviewer_emails = {}
    
    # Find all rows in the PC list
    for row in pc_soup.find_all('tr', class_='pl'):
        name_td = row.find('td', class_='pl_name')
        email_td = row.find('td', class_='pl_email')
        if name_td and email_td:
            # Extract name and email
            name = name_td.get_text(strip=True)
            email = email_td.find('a').get_text(strip=True)
            reviewer_emails[name] = email

    return delinquent_reviewers, reviewer_emails

def generate_emails(delinquent_reviewers, reviewer_emails):
    email_messages = []
    
    for reviewer, papers in delinquent_reviewers.items():
        email = reviewer_emails.get(reviewer)
        if email:
            # TODO: add more nicknames
            first_name = reviewer.split()[0]
            if reviewer == "Antony Hosking":
                first_name = "Tony"
            elif reviewer == "Samuel Guyer":
                first_name = "Sam"
            paper_word = 'paper' if len(papers) == 1 else 'papers'
            subject = f"{'Review' if len(papers) == 1 else 'Reviews'} for ASPLOS {paper_word} {', '.join(papers)}"
            if len(papers) == 1:
                papers_str = papers[0]
            elif len(papers) == 2:
                papers_str = ' and '.join(papers)
            else:
                papers_str = ', '.join(papers[:-1]) + ', and ' + papers[-1]
            message = f"Hi {first_name},\n\nCould you please complete your " + (f'review for paper' if len(papers) == 1 else f'reviews for papers') + f" {papers_str} soon -- definitely no later than this Friday (December 6), or the R2 assignments will be impacted.\n\nBest,\nMike (ASPLOS vice chair)"
            email_messages.append((f"\"{reviewer}\" <{email}>", subject, message))
        else:
            print(f"Could not find email for {reviewer}")
            sys.exit(1)

    return email_messages

def generate_eml_files(emails):
    for i, (email, subject, message) in enumerate(emails):
        # Create an email message
        msg = MIMEMultipart()
        msg['From'] = 'Michael Bond <mikebond@cse.ohio-state.edu>' # Replace with your info
        msg['To'] = email
        msg['Cc'] = 'asplos2025pcchairs@gmail.com' # Remove if not for ASPLOS 2025
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(message, 'plain'))

        # Write the email to an .eml file
        with open(f'email_{i+1}.eml', 'w') as f:
            f.write(msg.as_string())

def main(submissions_html, pc_html):
    delinquent_reviewers, reviewer_emails = extract_delinquent_reviewers(submissions_html, pc_html)
    emails = generate_emails(delinquent_reviewers, reviewer_emails)
    generate_eml_files(emails)

    for email, subject, message in emails:
        print(f"To: {email}")
        print(f"Cc: asplos2025pcchairs@gmail.com") # Remove if not for ASPLOS 2025
        print(f"Subject: {subject}")
        print(f"Message:\n{message}\n")

if __name__ == "__main__":
    submissions_html = 'submissions.html'
    pc_html = 'pc.html'
    main(submissions_html, pc_html)

