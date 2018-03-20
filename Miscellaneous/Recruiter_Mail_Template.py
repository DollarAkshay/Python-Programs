template = '''
Dear Hiring Manager,

My name is [MY_FULLNAME] and I’m currently on the hunt for the next step in my career and  I recently came across a posting for a [JOB_POSITION] at your company. I think it is a great fit for my profile as I wish to pursue a career in [JOB_FIELD]. Your listed requirements closely match my skill set and I believe I'm a perfect fit for the job. It would be a great opportunity to work with a team of extremely talented and creative minds.

I am  also very active on GitHub and have my own projects that I actively contribute to. I also fork cool projects from other developers on GitHub and tinker with them. Here is a link to my GitHub profile : [GITHUB_LINK]

I’ve also attached an updated version of my resume, you could alternatively use this web link : [RESUME_WEB_LINK]
Looking forward to hearing from you. Here is my number, if you need to contact me for anything.

Regards 
[MY_FULLNAME]
[MY_NUMBER]
'''

MY_FULLNAME = "Akshay Aradhya"
GITHUB_LINK = "https://github.com/DollarAkshay"
RESUME_WEB_LINK = "https://resume.creddle.io/resume/d87rfbbm6cq"
MY_NUMBER = "+91 "

referral_list = [
    {
        "JOB_POSITION": "Machine Learning Engineer",
        "JOB_FIELD": "machine learning and data science"
    }
]


# Replace Constants
template = template.replace("[MY_FULLNAME]", MY_FULLNAME)
template = template.replace("[GITHUB_LINK]", GITHUB_LINK)
template = template.replace("[RESUME_WEB_LINK]", RESUME_WEB_LINK)
template = template.replace("[MY_NUMBER]", MY_NUMBER)


for referal in referral_list:
    template_copy = template
    template_copy = template_copy.replace("[JOB_POSITION]", referal["JOB_POSITION"])
    template_copy = template_copy.replace("[JOB_FIELD]", referal["JOB_FIELD"])
    print("-------------------- TEMPLATE START --------------------")
    print(template_copy)
    print("-------------------- TEMPLATE END --------------------")
