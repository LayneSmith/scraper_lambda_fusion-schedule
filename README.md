# Frisco Fusion schedule scraper
A Python scraper deployed to AWS Lambda that pulls down the [PYSA Fusion soccer schedule](http://events.gotsport.com/events/schedule.aspx?eventid=67315&FieldID=0&applicationID=4788436&action=Go).

## .env
A `.env` file with AWS credentials is required.

## Instructions for changes
* `pipenv shell` to get us going
* Make changes
* Run `zappa update` to deploy changes