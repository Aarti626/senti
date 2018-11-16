import os

'''
Configuration Settings
'''

''' Uncomment to configure using the file.
WARNING: Be careful not to post your account credentials on GitHub.

TWILIO_ACCOUNT_SID = "ACb78bda6471d6cb3bf521a5520990ca7a"
TWILIO_AUTH_TOKEN = "f83cbe3c67248ab5a0c4c1acb90a56a1"
TWILIO_CALLER_ID = "+17778889999"
'''
TWILIO_ACCOUNT_SID = "ACb78bda6471d6cb3bf521a5520990ca7a"
TWILIO_AUTH_TOKEN = "f83cbe3c67248ab5a0c4c1acb90a56a1"
TWILIO_CALLER_ID = "+919642851210"
TWILIO_APP_SID="AP44785d02fde6090b8865a9b35593ed43"
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', None)
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', None)
TWILIO_CALLER_ID = os.environ.get('TWILIO_CALLER_ID', None)
TWILIO_APP_SID = os.environ.get('TWILIO_APP_SID', None)
