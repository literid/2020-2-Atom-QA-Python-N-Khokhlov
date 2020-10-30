import requests
import json


class ResponseStatusCodeException(Exception):
    pass


class RequestErrorException(Exception):
    pass


class MyTargetClient:

    def __init__(self, user, password):
        self.session = requests.Session()
        self.csrf_token = None

        self.user = user
        self.password = password
        self.login()
        self.segments_id = {}

    def custom_request(self, method, custom_url, status_code=200, headers=None, params=None, data=None, json=True):
        url = custom_url

        response = self.session.request(method, url, headers=headers, params=params, data=data)

        if response.status_code != status_code:
            raise ResponseStatusCodeException(f' Got {response.status_code} {response.reason} for URL "{url}"')

        if json:
            json_response = response.json()
            return json_response
        return response

    def login(self):
        url = "https://auth-ac.my.com/auth?lang=ru&nosavelogin=0"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            "Referer": "https://target.my.com/"
        }
        data = {
            "email": f"{self.user}",
            "password": f"{self.password}",
            "continue": "https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email",
            "failure": "https://account.my.com/login/"
        }

        response = self.custom_request('POST', headers=headers, custom_url=url, data=data, json=False)

        csrf_url = "https://target.my.com/csrf/"
        response = self.custom_request("GET", custom_url=csrf_url, json=False)
        self.csrf_token = response.headers['set-cookie'].split(';')[0].split("=")[1]

    def create_segment(self, seg_name):
        url = "https://target.my.com/api/v2/remarketing/segments.json?fields=relations__object_type,relations__object_id,relations__params,relations_count,id,name,pass_condition,created,campaign_ids,users,flags"
        headers = {"Content-Type": "application/json",
                   "Referer": "https://target.my.com/segments/segments_list/new",
                   "X-CSRFToken": f"{self.csrf_token}"
                   }
        payload = {"name": f"{seg_name}", "pass_condition": 1, "relations": [
            {"object_type": "remarketing_player", "params": {"type": "positive", "left": 365, "right": 0}}],
                   "logicType": "or"}
        response = self.custom_request("POST", custom_url=url, headers=headers, data=json.dumps(payload), json=True)
        self.segments_id[seg_name] = response['id']

    def find_segment_by_name(self, seg_name):
        url = "https://target.my.com/api/v2/remarketing/segments.json?&limit=500&_=1603909291312"
        response = self.custom_request("GET", custom_url=url)
        segments = response["items"]
        if seg_name in self.segments_id:
            my_seg = [seg for seg in segments if int(seg['id']) == int(self.segments_id[seg_name])]
            return my_seg
        return None

    def delete_segment_by_name(self, seg_name):
        url = "https://target.my.com/api/v1/remarketing/mass_action/delete.json"
        headers = {"Content-Type": "application/json",
                   "Referer": "https://target.my.com/segments/segments_list",
                   "X-CSRFToken": f"{self.csrf_token}"
                   }
        payload = [{"source_id": str(self.segments_id[seg_name]), "source_type": "segment"}]
        response = self.custom_request("POST", custom_url=url, headers=headers, data=json.dumps(payload))
        self.segments_id.pop(seg_name)
