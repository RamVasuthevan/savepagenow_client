import requests
from datetime import timedelta
from urllib.parse import urlencode
from typing import List, Dict

BASE_URL = "http://web.archive.org/save/status/"
TIMEOUT = 5


def system_status(accesskey: str, secretkey: str) -> requests.Response:
    url = BASE_URL + "system"
    headers = {
        "Accept": "application/json",
        "Authorization": f"LOW {accesskey}:{secretkey}",
    }
    response = requests.request("GET", url, headers=headers, timeout=TIMEOUT)
    return response


def user_status(accesskey: str, secretkey: str) -> requests.Response:
    url = BASE_URL + "user"
    headers = {
        "Accept": "application/json",
        "Authorization": f"LOW {accesskey}:{secretkey}",
    }
    response = requests.request("GET", url, headers=headers, timeout=TIMEOUT)
    return response


def request_status(accesskey: str, secretkey: str, job_id: str) -> requests.Response:
    url = BASE_URL + job_id
    headers = {
        "Accept": "application/json",
        "Authorization": f"LOW {accesskey}:{secretkey}",
    }
    response = requests.request("GET", url, headers=headers, timeout=TIMEOUT)
    return response


def advanced_request_status(
    accesskey: str, secretkey: str, job_ids: List[str]
) -> Dict[str, Dict[str, str]]:
    url = BASE_URL
    headers = {
        "Accept": "application/json",
        "Authorization": f"LOW {accesskey}:{secretkey}",
    }
    job_ids_str = ",".join(job_ids)
    payload = {"job_ids": job_ids_str}
    response = requests.post(url, headers=headers, data=payload, timeout=TIMEOUT)
    return response


def save_page(
    accesskey: str,
    secretkey: str,
    url: str,
    capture_all: bool = False,
    capture_outlinks: bool = False,
    capture_screenshot: bool = False,
    delay_wb_availability: bool = False,
    force_get: bool = False,
    skip_first_archive: bool = False,
    if_not_archived_within: timedelta = None,
    if_not_archived_within_outlink: timedelta = None,
    outlinks_availability: bool = False,
    email_result: bool = False,
    js_behavior_timeout: int = None,
    capture_cookie: str = None,
    use_user_agent: str = None,
    target_username: str = None,
    target_password: str = None,
) -> requests.Response:
    save_url = BASE_URL + url
    if if_not_archived_within_outlink and not if_not_archived_within:
        raise ValueError(
            "if_not_archived_within_outlink cannot be given without if_not_archived_within."
        )
    payload = {"url": url}
    if capture_all:
        payload["capture_all"] = "1"
    if capture_outlinks:
        payload["capture_outlinks"] = "1"
    if capture_screenshot:
        payload["capture_screenshot"] = "1"
    if delay_wb_availability:
        payload["delay_wb_availability"] = "1"
    if force_get:
        payload["force_get"] = "1"
    if skip_first_archive:
        payload["skip_first_archive"] = "1"
    if if_not_archived_within:
        delta_seconds = if_not_archived_within.total_seconds()
        payload["if_not_archived_within"] = str(delta_seconds)
    if if_not_archived_within_outlink:
        delta_seconds = if_not_archived_within_outlink.total_seconds()
        payload["if_not_archived_within"] += f",{delta_seconds}"
    if outlinks_availability:
        payload["outlinks_availability"] = "1"
    if email_result:
        payload["email_result"] = "1"
    if js_behavior_timeout is not None:
        payload["js_behavior_timeout"] = str(js_behavior_timeout)
    if capture_cookie:
        payload["capture_cookie"] = capture_cookie
    if use_user_agent:
        payload["use_user_agent"] = use_user_agent
    if target_username and target_password:
        payload["target_username"] = target_username
        payload["target_password"] = target_password
    payload_str = urlencode(payload)
    headers = {
        "Accept": "application/json",
        "Authorization": f"LOW {accesskey}:{secretkey}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    response = requests.request(
        "POST", save_url, headers=headers, data=payload_str, timeout=TIMEOUT
    )
    return response
