
import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_jobs(query, pages=3):
    jobs_lst = []
    companies_lst = []
    locations_lst = []
    links_lst = []
    times_lst = []
    occupations_lst = []

    for i in range(pages):
        url = f'https://wuzzuf.net/search/jobs/?q={query}&start={i}'
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'lxml')
        jobs = soup.find_all('h2', class_='css-m604qf')
        jobs_ =[job.text.strip() for job in jobs]
        company = soup.find_all('div', class_= 'css-d7j1kk')
        company_ = [c.a.text.replace(' -', '') for c in company]
        location = soup.find_all('div', class_= 'css-d7j1kk')
        location_ = [l.span.text.strip() for l in location]
        jobs_link_ = [job.a['href'] for job in jobs]
        time = soup.find_all('div', class_= 'css-1lh32fc')
        time_ = [t.find_all('a')[0].text.strip() for t in time]
        occ_ =[]
        for t in time:
                try:
                        occ_.append(t.find_all('a')[1].text.strip() )
                except:
                        occ_.append('NA')

        jobs_lst.extend(jobs_)
        companies_lst.extend(company_)
        locations_lst.extend(location_)
        links_lst.extend(jobs_link_)
        times_lst.extend(time_)
        occupations_lst.extend(occ_)

    df = pd.DataFrame({'Jobs': jobs_lst, 'Company': companies_lst, 'Location': locations_lst, 'Link': links_lst, 'Time': times_lst, 'Occupation': occupations_lst})
    df.to_excel(f'wuzzuf_jobs_{query}.xlsx', index=False)
    return df.head()

if __name__ == '__main__':
    print('Wuzzuf Jobs')
    query = input('Enter Job Title: ')
    pages = int(input('Enter No. of Pages: '))
    print(f'Jobs for {query} are being scraped:')
    df = get_jobs(query, pages)
    print(f'wuzzuf_jobs_{query} file has been created')
    print('First 5 jobs:')
    print(df)
