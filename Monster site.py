import requests
from bs4 import BeautifulSoup
url='https://www.monster.com/jobs/search/?='
def making_parameter():
    s=input("Enter the skill of your choice:")
    u=generate_url(s)
    run_scraper(u)
def generate_url(parameter):
    return url+parameter
def run_scraper(new_url):
    html=requests.get(new_url)
    soup=BeautifulSoup(html.content,'html.parser') 
    res=soup.find(id='ResultsContainer')
    job_ele=res.find_all('section',class_='card-content')
    for job_elem in job_ele:
        job_title = job_elem.find('h2', class_='title')
        job_company = job_elem.find('div', class_='company')
        job_location = job_elem.find('div', class_='location')
        if None in (job_title,job_company,job_location):
            continue
        print(job_title.text.strip())
        print(job_company.text.strip())
        print(job_location.text.strip())
        print("--------------------------------------------------")
print("*******************Welcome to the monster.com******************")
while(True):
    print("1.Search for the job")
    print("2.Exit")
    n=int(input("Enter your choice:"))
    if(n==1):
        making_parameter()
    if(n==2):
        break

