#!/usr/bin/python
from subprocess import Popen, PIPE, call
import shlex
import requests

cmd = "<nagios-plugin-with-args>"
process = Popen(shlex.split(cmd,posix=False), stdout=PIPE)
output = process.communicate()[0]
exit_code = process.wait()
url = 'https://<icinga2-ip>:5665/v1/actions/process-check-result?service=<host>!<service-name>'
headers = {'Accept':'application/json'}
payload = {'filter':'service.name=="<service-name>"','type':'Service','exit_status':exit_code,'plugin_output':output}
r = requests.post(url,headers=headers,json=payload,verify=False,auth=('<user>','<pass>'))
print output
print exit_code
