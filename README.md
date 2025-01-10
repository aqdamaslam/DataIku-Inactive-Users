# DataIku-Inactive-Users

### Use Case: 
The use case for this Python script is to list users in Dataiku who have not logged in for the last year. This is useful for system administrators to identify inactive users, ensuring that user access is managed effectively, and resources are optimized.

### Steps to Implement the Script:

1. **Connect to Dataiku API**: Set up a connection with the Dataiku API to interact with the platform's user data.
2. **Fetch User List**: Retrieve the list of users in your Dataiku instance.
3. **Filter Users Based on Last Login**: For each user, check the `last_login` date and compare it to the current date.
4. **Identify Inactive Users**: Identify users whose last login was more than one year ago.
5. **Generate Report**: Generate a report or list of these inactive users.

### Benefits of Automation:

1. **Improved Security**: Identifying inactive users helps remove or restrict access, reducing the risk of unauthorized access.
2. **Better Resource Management**: Helps in ensuring that licenses and resources are not wasted on inactive users.
3. **Efficient User Management**: Saves time for administrators by automating the process of checking user activity.
4. **Compliance**: Ensures that the organization follows internal policies related to data access and user management.
5. **Scalability**: This script can be scheduled to run periodically (e.g., monthly) to keep track of user activity without manual intervention.

### Optional Enhancements:
- **Scheduling**: Use a task scheduler like cron (Linux) or Task Scheduler (Windows) to automate running the script periodically.
- **Report Generation**: Output the list of inactive users to a CSV file or send an email notification to administrators.
