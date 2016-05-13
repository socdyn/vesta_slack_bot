#########################################################
## Slacker boilerplate
import functools
import json
from slacker import Slacker
with open('/Users/Shared/vesta_api_keys/slacker.json') as par_file:
    params = json.load(par_file)

slack = Slacker(params['api_key'])
    
vesta_says = functools.partial(
    slack.chat.post_message, 
    as_user=params['user'],
    channel=params['default_channel'])
#########################################################


# Examples

# The default channel is #vesta_reporting
vesta_says(text='posting to default channel using functools.partial')

# You can direct message yourself (recommended)
vesta_says(channel='@cjc73', text='direct messaging cjc73')

# @vesta can only post to channels to which it is invited. 
# Use slack to invite @vesta to a channel if it is not already a member.


