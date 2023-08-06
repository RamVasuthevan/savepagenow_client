from savepagenow import SavePageNow
from pprint import pprint
from time import sleep

spn = SavePageNow(accesskey="He79jn81G6ruAsGm",secretkey="A71vBhJ7feRILdCy")

page_num = 56
url = f"http://taxes.cityofjerseycity.com/?page={page_num}"
result = spn.save_page(url=url,capture_all=True,email_result=True, outlinks_availability=True, capture_outlinks=True)
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