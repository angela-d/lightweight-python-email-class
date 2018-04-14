# Simple Python Email Class
Reusable class for Python with JSON config; ideal for plaintext alerts. Tested on Debian 9 Stretch

**Dependences**

* Python 3+
* Json
* SMTP with SSL (tested with Rackspace)

**Install**

Via terminal, run:
```bash
git clone https://github.com/angela-d/simple-python-email-class.git && cd simple-python-email-class

chmod u+x versionCheck.py && cd ..
```

Rename the directory to suit your project:
```bash
mv simple-python-email-class newdirname
```

* Open config.json and set up your initial alert; set email addresses, messages and mailserver info

***

## Test it ##
* Open *versionCheck.py* and change the Python version to something not on your machine; ie. from:
```bash
if not sys.version_info[:3] >= (3, 5):
```
To:
```bash
if not sys.version_info[:4] >= (4, 5):
```
Execute the script in cli:
```bash
python3 versionCheck.py
```

Note: versionCheck.py is an optional component and not required for the emailer to run.

## How to use ##
Anywhere you'd like to trigger an email during an exception, simply call:
```python
# import the required modules & emailer class
import json
from classes.emailer import Emailer

# open & read config.json
# variable names can be changed to suit your application
with open('config.json') as developerAlerts:
    devs = json.load(developerAlerts)

#ensure you modify the trigger variables below to sync with your json extraction
sendAnEmail = Emailer(
    devs['dev_alerts']['from'],
    devs['dev_alerts']['to'],
    devs['dev_alerts']['subject'],
    devs['dev_alerts']['message'],
    devs['dev_alerts']['server'],
    devs['dev_alerts']['outgoing_port'],
    devs['dev_alerts']['pw']
)
```
