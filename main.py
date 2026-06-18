from datetime import datetime 
print("WELCOME TO COLLEGE-TO-CORPORATE BRIDGE")

s=0
date = datetime.now().strftime("%d %B %Y")
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to the College-to-Corporate Bridge program.")   
branch = input("Please enter your branch: ")
print("Please select your area of interest from the following options:")
print("1. Data Science")
print("2. Web Development")
print("3. App Development")
print("4. Cybersecurity")
print("5. Cloud Computing")
print("6. AI/ML")
print("7. software engineering")
interest_choice = int(input("Enter the number corresponding to your area of interest: "))

year = int(input("Enter your year of study (1-4): "))
print("1. first year")
print("2. second year")
print("3. third year")
print("4. fourth year")

print("Your branch is:", branch)
print("Your area of interest is:", interest_choice)

if interest_choice == 1:
    print("You have selected Data Science. We will provide you with resources and guidance to excel in this field.")
    print("skills to learn:")
    print("-python")
    print("-SQL")
    print("-Statistics")

    print("Suggested projects:")
    print("-sales prediction model")
    print("-student performance analysis")

    print("Recommended certifications:")
    print("google data analytics")

elif interest_choice == 2:
    print("You have selected Web Development. We will provide you with resources and guidance to excel in this field.")
    print("skills to learn:")
    print("-HTML")
    print("-CSS")
    print("-JavaScript")

    print("Suggested projects:")
    print("-personal portfolio website")
    print("-college event website")

    print("Recommended certifications:")
    print("-meta front end developer")

elif interest_choice == 3:
    print("You have selected App Development. We will provide you with resources and guidance to excel in this field.")
    print("skills to learn:")
    print("-Java")
    print("-Kotlin")
    print("-Flutter")

    print("Suggested projects:")
    print("-to-do list app")
    print("-expense tracker app")

    print("Recommended certifications:")
    print("-andriod developement fundamentals")

elif interest_choice == 4:
    print("You have selected Cybersecurity. We will provide you with resources and guidance to excel in this field.")
    print("skills to learn:")
    print("-networking")
    print("-ethical hacking")
    print("-linux")

    print("Suggested projects:")
    print("-password strength checker")
    print("-network scanner")

    print("Recommended certifications:")
    print("-compTIA security+")

elif interest_choice == 5:
    print("You have selected Cloud Computing. We will provide you with resources and guidance to excel in this field.")
    print("skills to learn:")
    print("-AWS")
    print("-docker")
    print("-linux")

    print("Suggested projects:")
    print("-cloud-based storage system")
    print("-website deployment on AWS")

    print("Recommended certifications:")
    print("-AWS cloud practitioner")

elif interest_choice == 6:
    print("You have selected AI/ML. We will provide you with resources and guidance to excel in this field.")
    print("skills to learn:")
    print("-python")
    print("-machine learning algorithms")
    print("-deep learning")

    print("Suggested projects:")
    print("-chatbot")
    print("-image classifier")

    print("Recommended certifications:")
    print("-google machine learning crash course")

elif interest_choice == 7:
    print("You have selected software engineering. We will provide you with resources and guidance to excel in this field.")
    print("skills to learn:")
    print("-DSA")
    print("-OOPs")
    print("-git and github")

    print("Suggested projects:")
    print("-library management system")
    print("-student management system")

    print("Recommended certifications:")
    print("-programming foundations")

else:
    print("Invalid choice. Please select a valid area of interest.")



if year == 1:
    print("As a first-year student, we recommend focusing on building a strong foundation in programming and problem-solving skills.")
    print("You can start with learning Python and basic data structures.")
    print("Participate in coding competitions and hackathons to enhance your skills.")
    print("Create a github account and start contributing to open-source projects.")
    print("build 2 small projects to showcase your skills.")

elif year == 2:
    print("As a second-year student, we recommend diving deeper into your chosen area of interest.")
    print("You can start working on intermediate-level projects and explore advanced concepts.")
    print("Participate in hackathons and coding competitions to gain practical experience.")
    print("Participate in internships or research opportunities to gain practical experience.")
    print("learn DSA and OOPs concepts and build 2-3 projects to showcase your skills.")

elif year == 3:
    print("As a third-year student, we recommend focusing on building a strong portfolio of projects and gaining industry experience.")
    print("You can start working on real-world projects and contribute to open-source projects.")   
    print("Apply for internships and co-op programs to gain practical experience.")
    print("Build adavnced projects and showcase them on your portfolio.")
    print("improve linkeldn profile and github profile and start networking with professionals in your field.")

elif year == 4:
    print("As a fourth-year student, we recommend focusing on preparing for job interviews and building a strong professional network.")
    print("You can start applying for full-time positions and attending career fairs.")
    print("Prepare for technical interviews by practicing coding problems and reviewing data structures and algorithms.")
    print("Attend networking events and connect with professionals in your field to explore job opportunities.")
    print("prepare for placement interviews and build a strong resume and cover letter to showcase your skills and experience.")


print("NOW LET'S CALCULATE YOUR PLACEMENT READINESS SCORE!!    FOR EACH YES, YOU WILL GET 20 POINTS AND THE TOTAL POINTS WILL BE CALCULATED OUT OF 100")
dsa=input("do u know DSA? pls answer in yes or no:   ")
python=input("do u know python? pls answer in yes or no:   ")
github=input("do u have a github account? pls answer in yes or no:   ")
linkedln=input("do u have a linkdedln account? pls answer in yes or no:   ")
projects=input("have u done any projects? pls answer in yes or no:   ")
if dsa.lower()=="yes":
    s=s+20
if python.lower()=="yes":
    s=s+20
if github.lower()=="yes":
    s=s+20
if linkedln.lower()=="yes":
    s=s+20
if projects.lower()=="yes":
    s=s+20
print("your total score out of 100 is:   ",s)


if s>=80:
    print("Congratulations! You are well-prepared for placements. Keep up the good work and continue building your skills and experience.")
elif s>=60:
    print("You are on the right track, but there is still room for improvement. Focus on strengthening your skills and gaining more experience to increase your chances of success in placements.")
elif s>=40:
    print("You need to focus more on skill development and projects.")
else:
    print("You are at the beginning of your journey. Focus on learning Python, creating projects, GitHub, and LinkedIn.")

if dsa.lower()=="yes" and python.lower()=="yes" and github.lower()=="yes" and linkedln.lower()=="yes" and projects.lower()=="yes":
    print("You are a placement-ready candidate! Keep up the great work and continue to build on your skills and experience to excel in your career.")
if dsa.lower()!="yes":
    print("--   You need to focus on learning DSA to improve your placement readiness.")
if python.lower()!="yes":
    print("--   You need to focus on learning Python to improve your placement readiness.")
if github.lower()!="yes":
    print("--   You need to create a GitHub account and start contributing to open-source projects to improve your placement readiness.")
if linkedln.lower()!="yes":
    print("--   You need to create a LinkedIn account and start building your professional network to improve your placement readiness.")
if projects.lower()!="yes":
    print("--   You need to work on more projects to improve your placement readiness.")

print("NOW WE SHALL HELP YOU WITH THE INTERNSHIP RECOMMENDATIONS!!")
if interest_choice == 1:
    print("Based on your interest in Data Science, we recommend looking for internships in the following areas:")
    print("-Data analysis and visualization")
    print("-Machine learning and AI")
    print("-Data engineering and big data")
elif interest_choice == 2:
    print("Based on your interest in Web Development, we recommend looking for internships in the following areas:")
    print("-Front-end development")
    print("-Back-end development")
    print("-Full-stack development")
elif interest_choice == 3:
    print("Based on your interest in App Development, we recommend looking for internships in the following areas:")
    print("-Mobile app development")
    print("-Cross-platform app development")
    print("-UI/UX design for apps")
elif interest_choice == 4:
    print("Based on your interest in Cybersecurity, we recommend looking for internships in the following areas:")
    print("-Network security")
    print("-Ethical hacking and penetration testing")
    print("-Cybersecurity analysis and incident response")
elif interest_choice == 5:
    print("Based on your interest in Cloud Computing, we recommend looking for internships in the following areas:")
    print("-Cloud infrastructure management")
    print("-Cloud security and compliance")
    print("-Cloud application development")
elif interest_choice == 6:
    print("Based on your interest in AI/ML, we recommend looking for internships in the following areas:")
    print("-Machine learning model development")
    print("-Natural language processing")
    print("-Computer vision")
elif interest_choice == 7:
    print("Based on your interest in software engineering, we recommend looking for internships in the following areas:")
    print("-Software development")
    print("-Software testing and quality assurance")
    print("-DevOps and software deployment")


print("=========================================")
print("COLLEGE-TO-CORPORATE STUDENT REPORT")
print("=========================================")
print("Date:  ", date)
print("Name:  ", name)
print("Branch:  ", branch)
print("Year:  ", year)
if interest_choice == 1:
    print("Area of Interest:  Data Science")
    print("recommended career path:  Data Scientist, Data Analyst, Machine Learning Engineer")
    print("recommended internship path:  Data analysis and visualization, Machine learning and AI, Data engineering and big data")
elif interest_choice == 2:
    print("Area of Interest:  Web Development")
    print("recommended career path:  Front-end Developer, Back-end Developer, Full-stack Developer")
    print("recommended internship path:  Front-end development, Back-end development, Full-stack development")
elif interest_choice == 3:
    print("Area of Interest:  App Development")
    print("recommended career path:  Mobile App Developer, UI/UX Designer, Cross-platform App Developer")
    print("recommended internship path:  Mobile app development, Cross-platform app development, UI/UX design for apps")
elif interest_choice == 4:
    print("Area of Interest:  Cybersecurity")
    print("recommended career path:  Cybersecurity Analyst, Ethical Hacker, Security Consultant")
    print("recommended internship path:  Network security, Ethical hacking and penetration testing, Cybersecurity analysis and incident response")
elif interest_choice == 5:
    print("Area of Interest:  Cloud Computing")
    print("recommended career path:  Cloud Engineer, Cloud Architect, Cloud Security Specialist")
    print("recommended internship path:  Cloud infrastructure management, Cloud security and compliance, Cloud application development")
elif interest_choice == 6:
    print("Area of Interest:  AI/ML")
    print("recommended career path:  Machine Learning Engineer, Data Scientist, AI Researcher")
    print("recommended internship path:  Machine learning model development, Natural language processing, Computer vision")
elif interest_choice == 7:
    print("Area of Interest:  Software Engineering")
    print("recommended career path:  Software Developer, Software Tester, DevOps Engineer")
    print("recommended internship path:  Software development, Software testing and quality assurance, DevOps and software deployment")
print("Placement Readiness Score:  ", s)
if s>=80:
    print("Placement Readiness:  Excellent")
elif s>=60:
    print("Placement Readiness:  Good")
else:
    print("Placement Readiness:  Needs Improvement")
print("=========================================")
print("THANK YOU FOR ")
print("USING THE COLLEGE-TO-CORPORATE BRIDGE PROGRAM.")
print("WE WISH YOU THE BEST OF LUCK IN YOUR CAREER JOURNEY!")
print("=========================================")

