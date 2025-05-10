# netflix-household-bot

## DESCRIPTION
Auto-confirm "Update Netflix household" email messages.
This bot is able to capture emails sent from netflix to your netflix email account to update your netflix household.

### Why?
It's been more then a year now since Netflix has forbidden users to **share accounts**.
This means that if you are using netflix, you can still share your account credentials with your friends, 
but when you try to access Netflix from your television, it ask for a confirm to **update the netflix household** location.
This is beacuse, when played from smart TV (nothing happens if you play Netflix on your phone or PC), will check for your
**IP address** and see if it matches with the latest IP address that logged in.

### How?
The bot tracks email sent to your account, check if they are from netflix, and if they are email sent to update your 
netflix household.
If the email match the requirements, the update household link is opened and the button is automatically pressed.
This operations are performed headless (can be done also on server).
The whole process requires at most 30 seconds.

## REQUIREMENTS
Clone this repository:
```bash
git clone https://github.com/pennyw1ze/netflix-household-bot.git
```
Follow the instructions to set up a gmail webhook handler in python [here](https://github.com/pennyw1ze/gmail_webhook_handler).
- Install pip requirements by typing:
```bash
pip install -r requirements.txt
```
- Install chromium:
```bash
playwright install chromium
```
And that's it, you're all set up to use the service.