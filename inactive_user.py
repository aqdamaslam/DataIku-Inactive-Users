import dataiku
from datetime import datetime, timedelta

# Connect to the Dataiku Instance
client = dataiku.api_client()

# Get the list of all users
dss_users = client.list_users()
print(dss_users)

# Calculate the date 183 days ago
six_month_ago = datetime.now() - timedelta(days = 183)

# Open DSS log file
with open('/tmp/users.csv', 'w') as f:
  for user in dss_users:
    dss_user = client.get_user(user["login"])
    enabled = dss_user.get_settings().get_raw()["enabled"]
    last_login_date = str(dss_user.get_activity().last_successful_login)
    L_login_date dss_user.get_activity().last_successful_login

    # Set the threshold date to six months
    threshold_date = datetime.now() - timedelta(days = 183)
    date = str(threshold_date)
    print(date)

    if last_login_date < L_login_date == None or enabled == False:
      print("Username: "+user["login"]+ " " + "License:"+user["userProfile"]+ " " + "Session:"+ str(enabled)+ " "+ "Last Login:"+ " "+str(last_login_date)+"\n\n")

