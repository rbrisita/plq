# Simple Python Service in a docker container.
docker-compose up -d

Visit Docker's IP with Port to view index page to test Pig Lating Query.

# Testing Client
virtualenv venv
source venv/bin/activate
pip install -r cli_requirements.txt

python3 cli.py <ip:port> <pig_latin_query>
