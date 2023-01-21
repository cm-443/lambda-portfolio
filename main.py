import pytz
from datetime import datetime, timedelta
def lambda_handler(event, context):
    est_tz = pytz.timezone('US/Eastern')
    now = datetime.now(est_tz)
    timestamp = ""
    if now.dst():
       utc_time = datetime.utcnow()
       utc_time_string_dls = utc_time.strftime('%Y/%m/%d/%H')
       timestamp = utc_time_string_dls
       print("It is currently Daylight Saving Time.")
    else:
       utc_time = datetime.utcnow()
       if utc_time.hour == 0:
           utc_time = utc_time - timedelta(days=1)
       utc_time = utc_time - timedelta(hours=1)
       utc_time_string = utc_time.strftime('%Y/%m/%d/%H')
       timestamp = utc_time_string
       print("It is currently NOT Daylight Saving Time.")
       print(timestamp)
