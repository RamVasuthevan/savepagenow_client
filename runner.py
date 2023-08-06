from savepagenow import SavePageNow
from pprint import pprint
from time import sleep
import os

accesskey = os.environ.get("ACCESS_KEY")
secretkey = os.environ.get("SECRET_KEY")

spn = SavePageNow(accesskey=accesskey, secretkey=secretkey)

page_num = 62
url = f"http://taxes.cityofjerseycity.com/?page={page_num}"
result = spn.save_page(
    url=url,
    capture_all=True,
    email_result=True,
    outlinks_availability=True,
    capture_outlinks=True,
)
pprint(result)
sleep(30)
pprint(spn.update_all_job_statuses())

print("started")
pprint(spn.jobid_started)
print("started_outlink")
pprint(spn.jobid_started_outlink)
print("success")
pprint(spn.jobid_success)
print("error")
pprint(spn.jobid_error)

sleep(30)
pprint(spn.update_all_job_statuses())
print("started")
pprint(spn.jobid_started)
print("started_outlink")
pprint(spn.jobid_started_outlink)
print("success")
pprint(spn.jobid_success)
print("error")
pprint(spn.jobid_error)


sleep(30)
pprint(spn.update_all_job_statuses())
print("started")
pprint(spn.jobid_started)
print("started_outlink")
pprint(spn.jobid_started_outlink)
print("success")
pprint(spn.jobid_success)
print("error")
pprint(spn.jobid_error)
