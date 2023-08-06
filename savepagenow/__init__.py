from typing import Optional, Any, Set, Dict, Collection,Union
import json
from datetime import timedelta
import savepagenow.api as api

class SavePageNow:
    def __init__(self, accesskey: str, secretkey: str) -> None:
        self.accesskey = accesskey
        self.secretkey = secretkey

        self.url_jobid: Dict[str:str] = {}
        self.jobid_response: Dict[str:str] = {}
        self.jobid_pending: Dict[str:Dict] = {}
        self.jobid_started: Dict[str:Dict] = {}
        self.jobid_started_outlink: dict[str:Dict] = {}
        self.jobid_success: Dict[str:Dict] = {}
        self.jobid_error: Dict[str:Dict] = {}

    def system_status(self) -> Dict:
        response = api.system_status(self.accesskey, self.secretkey)
        return response.json()

    def user_status(self) -> Dict:
        response = api.user_status(self.accesskey, self.secretkey)
        return response.json()
       
    def save_page(
        self,
        url: str, 
        capture_all: bool = False, 
        capture_outlinks: bool = False,
        capture_screenshot: bool = False,
        delay_wb_availability: bool = False,
        force_get: bool = False,
        skip_first_archive: bool = False,
        if_not_archived_within: Optional[timedelta] = None,
        if_not_archived_within_outlink: Optional[timedelta] = None,
        outlinks_availability: bool = False,
        email_result: bool = False,
        js_behavior_timeout: Optional[int] = None,
        capture_cookie: Optional[str] = None,
        use_user_agent: Optional[str] = None,
        target_username: Optional[str] = None,
        target_password: Optional[str] = None
    ) -> Dict:
        response = api.save_page(
            self.accesskey,
            self.secretkey,
            url,
            capture_all,
            capture_outlinks,
            capture_screenshot,
            delay_wb_availability,
            force_get,
            skip_first_archive,
            if_not_archived_within,
            if_not_archived_within_outlink,
            outlinks_availability,
            email_result,
            js_behavior_timeout,
            capture_cookie,
            use_user_agent,
            target_username,
            target_password
        )
        response = response.json()

        self.jobid_started[response["job_id"]] = response
        self.url_jobid[url] = response["job_id"]

        return response
    
    def update_job_statuses(self,job_ids:list[str]) ->list[Dict]:
        responses = api.advanced_request_status(self.accesskey, self.secretkey, job_ids)

        for job_id in job_ids:
            if job_id in self.jobid_started:
                del self.jobid_started[job_id]
            if job_id in self.jobid_pending:
                del self.jobid_pending[job_id]
            # can a success or error response be change?
            # del self.jobid_success[job_id] 
            # del self.jobid_error[job_id]
        
        responses = responses.json()
        print(responses)
        for response in responses:
            if response["status"] == "pending":
                self.jobid_pending[response["job_id"]] = response
            elif response["status"] == "success":
                self.jobid_success[response["job_id"]] = response
            elif response["status"] == "error":
                self.jobid_error[response["job_id"]] = response

            if "outlinks" in response and isinstance(response["outlinks"], dict):
                for url, job_id in response["outlinks"].items():
                    self.url_jobid[url] = job_id
                    try:
                        self.jobid_started_outlink[job_id] = response
                    except TypeError:
                        print("------------------")
                        print(job_id)
                        print(response)
                        print("------------------")
        return responses

    def update_all_job_statuses(self) -> list[Dict]:
        return self.update_job_statuses(list(set(self.jobid_started.keys() | set(self.jobid_pending.keys()| set(self.jobid_started_outlink.keys())))))