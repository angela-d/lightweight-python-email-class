#!/usr/bin/env python3

import sys

if not sys.version_info[:3] >= (3, 5):
    print("ERROR: Minimum version is Python 3.5")

    import json
    from classes.emailer import Emailer

    # extract the configuration so we know who to email
    with open('config.json') as developerAlerts:
        devs = json.load(developerAlerts)

        # initiate the mail and fill the required fields
        initMail= Emailer(
            devs['dev_alerts']['from'],
            devs['dev_alerts']['to'],
            devs['dev_alerts']['subject'],
            devs['dev_alerts']['message'],
            devs['dev_alerts']['server'],
            devs['dev_alerts']['outgoing_port'],
            devs['dev_alerts']['pw']
        )

exit()
