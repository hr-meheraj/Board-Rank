import requests as r
from bs4 import BeautifulSoup as bs
import re


def get_number(roll):
    url = 'https://sresult.bise-ctg.gov.bd/s2023/individual/result.php'
    data = {'roll': roll}
    res = r.post(url, data)
    sp = bs(res.text, 'html.parser')
    if sp.find('h3') != None:
        return {
            'name':None,
        }
    #total    
	
    nums = sp.find_all('td', class_='cap_lt')
    total = 0
    gpa = ''
    grp = ''
    schl = ''
    for j,i in enumerate(nums):
        if re.search(r'GPA=\d+', str(i)) != None:
            gpa = str(i.text)[4:]
        if re.search(r'\d{3}\(.+\)', str(i)) != None:
            total += int(str(i.text)[:3])
        if j == 3:
            grp = str(i.text)
        if j == 8:
            schl = str(i.text)
    name = str(sp.find('td', width=True, class_='cap_lt').text)
    return {
        'name':name,
        'gpa':gpa,
        'total':total,
        'schl':schl,
        'grp':grp
    }