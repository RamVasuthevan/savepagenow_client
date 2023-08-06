from savepagenow import SavePageNow
from savepagenow import api
from pprint import pprint
from time import sleep

spn = SavePageNow(accesskey="He79jn81G6ruAsGm",secretkey="A71vBhJ7feRILdCy")
#pprint(spn.get_job_status("spn2-03d83e163cd09fd6356efec776b7c03ab8ee054b"))

#pprint(spn.get_job_status("spn2-9976d466213e9bd87b97ac25780b2268b5942dba"))

exit()
page_num = 45
url = f"http://taxes.cityofjerseycity.com/?page={page_num}"
result = spn.save_page(url=url,capture_all=True,email_result=True, outlinks_availability=True, capture_outlinks=True)
pprint(result)
sleep(30)
result = spn.get_job_statuses(spn.jobid_status.values())
pprint(result)