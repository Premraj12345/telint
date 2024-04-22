import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup

from appwrite.client import Client
from appwrite.services.databases import Databases
import os

#my_secret = userdata.get('api')
my_secret = "25ad18e29b34004736d1e7c49d5bb0d411ebe46560b5cf875e2689ad6db23bf98e3f408e6ecd3f86166107b2aa4da1b47cfb1558d2773190ddbfad22146dbfdcc8c0d0cb5de5a0547bae1a45959894b38063537ba283d4f3a8eb43bb915a197488eed2b23e5b2c73f334bb3af453d2fbe844a9c880a24e4af59f00513a2c7620"
client = Client()

(client
.set_endpoint("https://cloud.appwrite.io/v1")
 .set_project("telinter")
 .set_key(my_secret))

databases = Databases(client)
url = "http://tg-inter-1st-year-result.indiaresults.com/tg/bie-telangana/intermediate-1-year-gen-exam-result-2022/mname-results.aspx"

headers = CaseInsensitiveDict()
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
headers["Accept-Encoding"] = "gzip, deflate"
headers["Accept-Language"] = "en-GB,en;q=0.9"
headers["Cache-Control"] = "max-age=0"
headers["Connection"] = "keep-alive"
headers["Content-Length"] = "2849"
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["Cookie"] = "_ga=GA1.1.2014162495.1713000046; _ga_VG5DFNPWRF=GS1.1.1713000046.1.1.1713000123.60.0.0"
headers["Host"] = "tg-inter-1st-year-result.indiaresults.com"
headers["Origin"] = "http://tg-inter-1st-year-result.indiaresults.com"
headers["Referer"] = "http://tg-inter-1st-year-result.indiaresults.com/tg/bie-telangana/intermediate-1-year-gen-exam-result-2022/mname-results.aspx"
headers["Upgrade-Insecure-Requests"] = "1"
headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"

def get_html_data(page_number):
  data = f"""__EVENTTARGET=GridView1&__EVENTARGUMENT=Page%24{page_number}&__VIEWSTATE=%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%2Bc5Af%2BmY%2FfyJnZFV7%2FY3xmJbDHQPFO81rBAQaiWxk%3D&__VIEWSTATEGENERATOR=6046918C&name=&Rollno=&id="""
  resp = requests.post(url, headers=headers, data=data)
  return resp.text



def get_student_list(html_code):

  # Parse the HTML
  soup = BeautifulSoup(html_code, 'html.parser')

  # Find the table
  table = soup.find('table')

  # Extract rows
  rows = table.find_all('tr')

  # Initialize a list to store the data
  data = []

  # Iterate over rows to extract data
  for row in rows[3:]:  # Skip the header row

      cells = row.find_all('td')
      item = {
          "Candidate's Name": cells[1].text.strip(),
          'Roll No': cells[2].text.strip()

      }
      data.append(item)
  return data


def upload_student(document_id,student_data):
  databases.create_document("telugu","inter_1st_year_2022",document_id,student_data)
  return 0

#sync run

#from data import get_html_data, get_student_list, upload_student


# second number in range is minus one
for i in range(1101,22000):
  html_code = get_html_data(str(i))
  student_list = get_student_list(html_code)
  for s in student_list:
    student_data = {"student_name": s["Candidate's Name"],"student_roll_no":s["Roll No"]}
    upload_student(str(s["Roll No"]),student_data)

print("succesfully uploaded")
