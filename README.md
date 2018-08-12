# Automatically submits bid for all Amazon Giveaways during Prime Day
## views all videos and submits bit automatically.  

- add chromedriver to path 
  - download from https://sites.google.com/a/chromium.org/chromedriver/downloads
  - add downloaded executable to PATH
- `pip install -r requirements.txt`

## Setup Database
- install MySQL
- run `cp config.ini.default config.ini`
- change config.ini file to match own user & pw
- run `cd setup && python3 seed.py`

## Run
- `python run_bot.py` or `python3 run_bot.py`
- enter your amazon login and watch chromedriver enter bids

## Next steps
- make this work with https://www.amazon.com/ga/giveaways for various types of giveaway categories (video, subscribe, coupon, etc)
- add more commenting (easy version to print for each comment written in line)
