## Auto Update Data

A script to automate data gathering, generation and updates for the [COVID-19](https://lab.imedd.org/covid19/) [dashboard](https://github.com/cvcio/covid-19). The script will:
- Pull  Update the repo in the latest state
- Extract data from [WorldOMeter](https://www.worldometers.info/) [Coronovirus Page](https://www.worldometers.info/coronavirus/)
- Test if the appropriate fields are present
- Read external data provided by [JHU CSSE](https://github.com/CSSEGISandData/COVID-19)
- Build all visualizations with [plotly](https://plotly.com/) [python library](https://plotly.com/python/)
- Push updated data to the [remote rpository](https://github.com/iMEdD-Lab/open-data)

### Installation

Before we begin we need to have a valid ssh-key added in your github account, read more [here](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent). After cloning the repo install any python dependancies.

```bash
git clone git@github.com:iMEdD-Lab/open-data.git
cd open-data/scipts/COVID-19

pip install -r requirements.txt
```

### Cron Job

```bash
# make the script executable
chmod a+x scripts/COVID-19/auto-update.sh
# add the script to the crontab list
crontab -e
# input the following command at the end of your crontab job list
# the conjob will run once every hour
0 * * * * /absolute/path/to/your/repository/scipts/COVID-19/auto-update.sh
# save and exit

# list the active cronjobs
crontab -l
```

### Manual Run

```bash
cd open-data
bash scripts/COVDI-19/auto-update.sh # of ./COVDI-19/auto-update.sh
```
