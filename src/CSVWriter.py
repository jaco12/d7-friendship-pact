import csv
from CompatibilityCalculator import *

def writeToCSV(result: dict, diffSchools_filename: str, sameSchools_filename: str, emailTemplate_filename: str):
    """Writes matches to two CSV files--one for different-school matches, and one for same-school matches."""
    header = ['Name', 'Email', 'Friend Name', 'Friend Email', 'Friend School', 'Friend Socials', 'Compatibility Score']
    diffSchoolRows = []
    sameSchoolRows = []
    emailTemplateRows = []

    for each in result:
        person = each.name
        friend = result[each].name
        compatibility = calculateCompatibility(person, friend)
        
        # email template
        emailTemplateRow = [
            person.email,
            "D7 FRIENDSHIP PACT RESULTS ARE IN!!! Your new best friend is...",
            f'\nHi {person.name}!!!\n\nThank you so much for completing the Friendship Pact survey! Our awesome algorithm has worked its matchmaking magic, and we’re thrilled to introduce you to your most compatible companion, your potential partner-in-crime, the new yin to your yang! Thank you so much for participating on this friendship-finding journey with us!\n\n\nYour new best friend is...\n\n{friend.name}!!! You guys had a compatibility score of {compatibility}%!!!\n\nSchool: {friend.school}\n\nEmail: {friend.email}\n\nSocials: {friend.socials}\n\n\nCongratulations and have fun!!!\n\nLove and friendship,\n\nJaco Asistores, Sofia Romulo, and the rest of the D7 E-Board'
        ]
        emailTemplateRows.append(emailTemplateRow)
        
        row = [person.name, person.email, friend.name, friend.email, friend.school, friend.socials, compatibilityToStr(compatibility)]
        diffSchoolRows.append(row) if person.school != friend.school else sameSchoolRows.append(row)

    with open(diffSchools_filename, 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(header)
        writer.writerows(diffSchoolRows)

    with open(sameSchools_filename, 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(header)
        writer.writerows(sameSchoolRows)
        
    with open(emailTemplate_filename, 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(['Email', 'Subject', 'Body'])
        writer.writerows(emailTemplateRows)