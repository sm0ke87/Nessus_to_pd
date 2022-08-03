# Nessus_to_pd
Script for pushing alerts to PD

Source:
* https://github.com/PagerDuty/API_Python_Examples/tree/master/EVENTS_API_v2

## Concept
It's not production script, it's only for understanding how to push alerts from file to PD. So you can use it for basic script.

## Usage
Enter events v2 API integration key

ROUTING_KEY = " " 
INCIDENT_KEY = " "

```
python3 pd_alert_all_in_one.py
python3 pd_alert.py
```

webservres.json file must be exist in directory with *.py files.
