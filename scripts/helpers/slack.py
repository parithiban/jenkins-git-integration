import os
import requests
import json


class Slack(object):
    """Slack Api to communicate with the slack"""

    def __init__(self, post_url):
        self.post_url = post_url

    def get_configs(self):
        """Get configurations """
        with open('config/config.json', 'r') as f:
            config = json.load(f)
        return config

    def send_message(self, message):
        """
        Send message in slack

        :param message: string
        """
        slack_hook = self.get_configs()
        url = slack_hook['DEFAULT']["SLACK_HOOK_URL"] + self.post_url

        payload = {
            "text": message,
            "mrkdwn": True
        }

        payload = json.dumps(payload)
        headers = {
            'Content-Type': "application/json"
        }

        requests.request("POST", url, data=payload, headers=headers)
