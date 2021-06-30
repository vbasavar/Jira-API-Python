# After modifications you can import this file as module in your code and call the individual functions
from jira import JIRA

# You can refer readme file to clearly understand the below.

with open("rsa.pem", 'r') as key_cert_file:
    key_cert_data = key_cert_file.read()

oauth_dict = {'access_token': 'xxxxxxxxxxxxxxxxxxxxxxxxxx',
              'access_token_secret': 'xxxxxxxxxxxxxxxxxxxxxxxx',
              'consumer_key': '<app_link_name>',
              'key_cert': key_cert_data }

jira = JIRA("<<your_jira_url>>", oauth=oauth_dict)

def get_comment(issue_no):
    try:
        latest_comment_id = jira.comments(issue_no)
        print(len(latest_comment_id))
        if len(latest_comment_id) > 1:
            comment = jira.comment(issue_no, latest_comment_id[-1]).body
        else:
            return f"There are no comments found for {issue_no}"
    except Exception as e:
        print(f"EXCEPTION {e} Occurred while attempting to get latest comment from {issue_no}")
    else:
        return comment


def add_comment(issue_no, comment):
    try:
        jira.add_comment(issue_no, comment)
    except Exception as e:
        print(f"EXCEPTION \"{e}\" Occurred while adding comments for the issue : {issue_no}")
    else:
        print("Successfully added the comment")


def update_status(issue_no, status):
    try:
        update_status = False
        transitions = jira.transitions(jira.issue(issue_no))
        for i in transitions:
            if status.lower() == i['name'].lower():
                jira.transition_issue(issue_no, i['id'])
                update_status = True
        if update_status:
            return True
        else:
            return False
    except Exception as e:
        print(f"EXCEPTION \"{e}\" Occurred while attempting to updating status for the issue : {issue_no}")
    else:
        print(f"Successfully updated the {status} for {issue_no}")
        return True
