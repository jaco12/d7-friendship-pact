import csv
from CompatibilityCalculator import *

def writeToCSV(result: dict, diffSchools_filename: str, sameSchools_filename: str):
    """Writes matches to two CSV files--one for different-school matches, and one for same-school matches."""
    header = ['Name', 'Email', 'Friend Name', 'Friend Email', 'Friend School', 'Friend Socials', 'Compatibility Score']
    diffSchoolRows = []
    sameSchoolRows = []
    # emailTemplateRows = []

    for each in result:
        person = each.name
        friend = result[each].name
        compatibility = calculateCompatibility(person, friend)
        
        row = [person.name, person.email, friend.name, friend.email, friend.school, friend.socials, compatibilityToStr(compatibility)]
        diffSchoolRows.append(row) if person.school != friend.school else sameSchoolRows.append(row)

    # output for matches from diff. schools
    with open(diffSchools_filename, 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(header)
        writer.writerows(diffSchoolRows)

    # output for matches from the same school
    with open(sameSchools_filename, 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(header)
        writer.writerows(sameSchoolRows)