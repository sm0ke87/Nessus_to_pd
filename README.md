<div id="header" align="center">
  <img src="https://media.giphy.com/media/gjrYDwbjnK8x36xZIO/giphy.gif" width="100"/>
</div>

<div id="badge" align="center">
  <a href="https://www.linkedin.com/in/%D1%81%D0%B5%D1%80%D0%B3%D0%B5%D0%B9-%D0%B0%D0%BB%D0%B8%D0%BC%D0%BE%D0%B2-a4522568/">
  <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="https://spb.hh.ru/resume/b509aa89ff01dcae2a0039ed1f55716850524a">
  <img src="https://img.shields.io/badge/HH.RU-red?style=for-the-badge" alt="Youtube Badge"/>
  <a>
</div>

<div align="center">
<br>

![language](https://img.shields.io/pypi/pyversions/django.svg)

![status](https://img.shields.io/static/v1?label=status&message=not_ready&color=yellow)
</div>

# Nessus_to_pd
Script for pushing alerts to PD

Source:
* https://github.com/PagerDuty/API_Python_Examples/tree/master/EVENTS_API_v2

## Concept
It's not production script, it's only for understanding how to push alerts from file to PD. So you can use it for basic script.

## Usage
Enter events v2 API integration key

ROUTING_KEY = " " 

```
python3 pd_alert_all_in_one.py
python3 pd_alert.py
```

webservres.json file must be exist in directory with *.py files.
