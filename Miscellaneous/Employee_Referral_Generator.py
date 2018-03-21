template = '''
Hi [EMPLOYEE_NAME] :)

    I am [MY_FULLNAME], [RELATIONSHIP_TO_EMPLOYEE]. I hope everything is going well on your end. Nice to see that you are now working for [EMPLOYEE_COMPANY].

    I’m currently on the hunt for the next step in my career and  I recently came across a posting for a [JOB_POSITION] at [JOB_LOCATION]. I think it is a great fit for my profile as I am into machine learning and data science and looking to pursue a career in that field. I wanted to see if you have any intel on the position, the team, or what they may be looking for in a candidate. Also appreciate it if you could give me an employee referral as that would help me in landing the interview.


I am  also very active on GitHub and have my own projects that I actively contribute to. I also fork cool projects from other developers on GitHub and tinker with them. Here is a link to my GitHub profile : [GITHUB_LINK]

I’ve also attached an updated version of my resume, or if you prefer, you could use this web link : [RESUME_WEB_LINK]
Looking forward to hearing from you. Here is my number, if you need to contact me for anything.

Regards 
[MY_FULLNAME]
[MY_NUMBER]
'''

MY_FULLNAME = "Akshay Aradhya"
GITHUB_LINK = "https://github.com/DollarAkshay"
RESUME_WEB_LINk = "https://resume.creddle.io/resume/d87rfbbm6cq"
MY_NUMBER = "+91 "

referral_list = [
    {
        "EMPLOYEE_NAME": "TEST",
        "RELATIONSHIP_TO_EMPLOYEE": "your school friend",
        "EMPLOYEE_COMPANY": "Google",
        "JOB_POSITION": "Software Developer",
        "JOB_LOCATION": "Bangalore, KA",

    }
]


# Replace Constants
template = template.replace("[MY_FULLNAME]", MY_FULLNAME)
template = template.replace("[GITHUB_LINK]", GITHUB_LINK)
template = template.replace("[RESUME_WEB_LINK]", RESUME_WEB_LINK)
template = template.replace("[MY_NUMBER]", MY_NUMBER)


for referal in referral_list:
    template_copy = template
    template_copy = template_copy.replace("[EMPLOYEE_NAME]", referal["EMPLOYEE_NAME"])
    template_copy = template_copy.replace("[RELATIONSHIP_TO_EMPLOYEE]", referal["RELATIONSHIP_TO_EMPLOYEE"])
    template_copy = template_copy.replace("[EMPLOYEE_COMPANY]", referal["EMPLOYEE_COMPANY"])
    template_copy = template_copy.replace("[JOB_POSITION]", referal["JOB_POSITION"])
    template_copy = template_copy.replace("[JOB_LOCATION]", referal["JOB_LOCATION"])
    print("-------------------- TEMPLATE START --------------------")
    print(template_copy)
    print("-------------------- TEMPLATE END --------------------")
