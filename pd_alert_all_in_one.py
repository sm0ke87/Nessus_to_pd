#!/usr/bin/env python

import json
import requests

ROUTING_KEY = " " # ENTER EVENTS V2 API INTEGRATION KEY HERE 

def trigger_incident():
    # Triggers a PagerDuty incident without a previously generated incident key
    # Uses Events V2 API - documentation: https://v2.developer.pagerduty.com/docs/send-an-event-events-api-v2

    header = {
        "Content-Type": "application/json"

    }

    with open('webserver.json') as f:
        template = json.load(f)

    payload = {"routing_key": ROUTING_KEY, "event_action": "trigger","payload":""}

    payload['payload'] = {
        "summary":"source",
        "source": "source",
        "severity": "critical",
        "custom_details": template
        }

    response = requests.post('https://events.pagerduty.com/v2/enqueue', 
                            data=json.dumps(payload),
                            headers=header)
    
    if response.json()["status"] == "success":
        print('Incident created with with dedup key (also known as incident / alert key) of ' + '"' + response.json()['dedup_key'] + '"')
        print(response.text)
    else:
        print(response.text) # print error message if not successful

if __name__ == '__main__':
    trigger_incident()