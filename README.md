# Jira-API-Python

Environment Setup

1 ) Need to install jira module

2 ) Need to create rsa.pem key and share it with your jira admins to create app link ( <app_link_name> ) at server side.

3 ) Once done from jira admin side then open anaconda prompt

4 ) Run : jirashell --server https://<your_jira_url> --consumer-key <app_link_name> --key-cert <rsa.pem> --oauth-dance

5 ) Jirashell will be open then type oauth in to get below creds.

{'access_token': 'xxxxxxxxxxxxxxxxxxxxxxxxxx',
 'access_token_secret': 'xxxxxxxxxxxxxxxxxxxxxxxx',
 'consumer_key': '<app_link_name>',
 'key_cert': <Contents of your rsa.pem> }

  **Thats it your are good to go. **

