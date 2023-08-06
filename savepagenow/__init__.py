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
        self.jobid_status: Dict[str:str] = {}

    def system_status(self) -> Any:
        response = api.system_status(self.accesskey, self.secretkey)
        return response.json()

    def user_status(self) -> Any:
        response = api.user_status(self.accesskey, self.secretkey)
        return response.json()

    def _update_job_response(self,job_ids: Union[str, Collection[str]]) -> Any:
        input_type = isinstance(job_ids, str)
        if input_type:
            job_ids = [job_ids]
        
        for job_id in job_ids:
            if job_id not in self.jobid_response and job_id not in self.jobid_status:
                raise ValueError(f"{job_id} is not a valid job_id")
        
        pending_job_ids = [job_id for job_id in self.jobid_response if self.jobid_response[job_id]["status"] == "pending"]

        response = api.advanced_request_status(self.accesskey, self.secretkey, pending_job_ids)
        for job_id,response in zip(pending_job_ids,response.json()):
            self.jobid_response[job_id] = response
            self.jobid_status[job_id] = response["status"]

        if input_type == str:
            return self.jobid_response[job_id]
        else:
            return [self.jobid_response[job_id] for job_id in job_ids]
    
    def job_response_by_jobid(self, job_ids: Union[str, Collection[str]]) -> Any:
        input_type = isinstance(job_ids, str)
      
        self._update_job_response(job_ids)

        if input_type == str:
            return self.jobid_response[job_ids]
        else:
            return [self.jobid_response[job_id] for job_id in job_ids]

    def all_job_responses(self):
        self._update_job_response(self.jobid_response.keys())
        return self.jobid_response.keys()
    
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
    ) -> Any:
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
        job_id = response.json().get('job_id')
        self.url_jobid[url] = job_id
        self.jobid_status[job_id] = "pending"
        return response.json()

    def jobid_by_status(self,status:str)->Set[str]:
        self.
        return (jobid for jobid,job_status in self.jobid_response if job_status == status).union(jobid for jobid,job_status in self.jobid_status if job_status == status)