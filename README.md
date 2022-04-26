# Setup
Clone the repository
```
git clone https://github.com/ModernOctave/website-monitor.git
```
Change into the cloned directory, create a venv and install the required packages
```
cd website-moniter
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Create jobs.json
jobs.json is a JSON file that contains the websites to be monitored. A sample jobs.json is as follows,
```
[
    {
        "url": "https://www.google.com",
        "name": "Google",
    },
    {
        "url": "https://www.yahoo.com",
        "name": "Yahoo",
    }
]
```
Note that the names of the jobs must be unique!

## Create .env file
.env is a file that contains the information credentials for the emails. A sample .env file is as follows,
```
SENDER_EMAIL=sender@example.com
SENDER_PASSWORD=password
RECIEVER_EMAIL=reciever@example.com
```

If the senders email provider is gmail then "allow less secure apps" must be enabled in the gmail account. It can be done [here](https://myaccount.google.com/lesssecureapps).

## Create cron job
Create a cron job that runs the monitor.py script as per your requirement. A sample cron job is as follows that runs every hour is as follows,
```
0 * * * * /home/user/website-monitor/venv/bin/python3 /home/user/website-monitor/moniter.py
```
This should be added to your crontab file using the command `crontab -e`.