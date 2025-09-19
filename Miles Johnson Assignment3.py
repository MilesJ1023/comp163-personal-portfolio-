full_name =  "Miles Johnson" 
email = "mcjohnson3@aggies.ncat.edu"
hometown = "Maryland, MD"
gradutation = "Spring 2029"
major = "Computer Science"
#list
current_courses = ["COMP 163", "MATH 110", "ENG 100", "HIS 106"]
completed_courses = ["Calculus", "Biology ", "Pre calc", "Spanish 1", "World History"]
credit_hours = [3,3,3,3]
gpa_history = [3.2,3.6,3.4,3.7]
#tuples
emergency_contacts = ("Mom","Crystal Johnson","301-860-2778")
home_address = ("2279 Duncan Ln","Waldorf","MD","20603")
insta_info = ("Instagram", "@miles_tkd",1425)
twitter_info = ("Twitter","@miles_tkd",0)
birthday = ("Birthday","10","23","2006")
#sets
current_skillset = {"Python basics", "HTML", "Problem solving", "Time management", "Photography, Taekwondo"}
skills_to_learn = {"Full Python","Data structures", "Git","Web design","Public speaking", "CSS"}
Career_interest = {"Software development","Web development","Data science","Game development"}
Hobbies = {"Gaming", "Photography", "Reading", "Taekwondo"}
Entertainment_backlog = {"One Piece", "Dexter", "Gintama", "2k", "Breaking Bad"}
#dictionary
course_credit_dict = {"COMP 163":3, "MATH 150":3, "ENG 101":3, "HIS 105":3}
course_professor_dict = {"COMP 163":"Prof. Rhodes", "MATH 150":"Dr. Lee", "ENG 101":"Dr. Martinez", "HIS 105": "Dr. Brown"}
course_room_dict = {"COMP 163": "M-Eric 300", "MATH 150": "Marteena 201", "ENG 101": "Crosby 121", "HIS 105": "Crosby 210"}
monthly_budget_dict = {"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100}
study_hours_per_subject = {"Programming": 10, "Math": 8, "English": 4, "History": 3}
contact_directory_dict = {"Mom": "704-555-0199", "Roommate": "336-555-7821", "Academic Advisor": "336-334-5000"}
#calculations
total_credit_hours = sum(credit_hours)
cumulative_gpa = sum(gpa_history) / len(gpa_history)
completed_courses_count = len(completed_courses)
total_weekly_study_hours = sum(study_hours_per_subject.values())
academic_load = total_credit_hours + total_weekly_study_hours
total_monthly_budget = sum(monthly_budget_dict.values())
daily_food_budget = monthly_budget_dict["Food"] / 30
annual_budget_proj = sum(monthly_budget_dict.values()) * 12
study_cost_per_hour = monthly_budget_dict["Books"]/ total_weekly_study_hours
total_social_media_followers = twitter_info[2] +insta_info[2]
#outputs
print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print(f"Student: {full_name} | Email: {email}")
print(f"From: {hometown} | Graduating: {gradutation}")
print(f"Major: {major}")
print()
print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {total_credit_hours} credits across 4 courses")
print(f"Cumulative GPA: {cumulative_gpa:.2f}")
print(f"Weekly Study Time: {total_weekly_study_hours} hours")
print(f"Academic Investment: ${study_cost_per_hour} per study hour")
print()
print("Current Courses:")
print(f"COMP 163 - {course_credit_dict["COMP 163"]} credits - {course_professor_dict["COMP 163"]} - {course_room_dict["COMP 163"]}")
print(f"MATH 150 - {course_credit_dict["MATH 150"]} credits - {course_professor_dict["MATH 150"]} - {course_room_dict["MATH 150"]}")
print(f"ENG 101 - {course_credit_dict["ENG 101"]} credits - {course_professor_dict["ENG 101"]} - {course_room_dict["ENG 101"]}")
print(f"HIS 105 - {course_credit_dict["HIS 105"]} credits - {course_professor_dict["HIS 105"]} - {course_room_dict["HIS 105"]}")
print()
print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skillset}")
print(f"Learning Goals: {skills_to_learn}")
print(f"Career Interests: {Career_interest}")
print(f"Skills Currently Have: {len(current_skillset)}")
print(f"Skills Want to Learn: {len(skills_to_learn)}")
print()
print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${total_monthly_budget}")
print(f"Food: ${monthly_budget_dict["Food"]} (${daily_food_budget:.1f}/day)")
print(f"Entertainment: ${monthly_budget_dict["Entertainment"]}")
print(f"Books: ${monthly_budget_dict["Books"]}")
print(f"Transportation: ${monthly_budget_dict["Transportation"]}")
print(f"Annual Projection: ${annual_budget_proj}")
print()
print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contacts[1]} (Mom) - {emergency_contacts[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]}, {home_address[2]} {home_address[3]}")
print(f"Social Media Presence: {total_social_media_followers} followers across 2 platforms")
print(f"Key Contacts: {len(contact_directory_dict)} people in directory")
print()
print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {completed_courses_count}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {len(Entertainment_backlog)} items")
print(f"Current Hobbies: {len(Hobbies)}activities")

print("================================================================")



