#!/usr/bin/env python

import yaml
import os
from os.path import expanduser
import subprocess
import time

# Load the Config Files
p = os.path.join(expanduser("~"),'.frontloader/config.yml')
with open (p) as cfg:
    s = yaml.load(cfg)

# Launch the Applications
# I want to sleep in the beginning because there are things out of my
# control also loading on login. Want to give them time to load
for x in s["files"]:
    time.sleep(15)
    app = "/Applications/{0}.app".format(x)
    subprocess.call(
        ["/usr/bin/open", "-a", app]
    )
