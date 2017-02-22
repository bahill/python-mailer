"""
Global config file. Change variable below as needed but ensure that the log and
retry files have the correct permissions.
"""

from datetime import datetime

# file settings
LOG_FILENAME = 'pymailer.log'
CSV_RETRY_FILENAME = 'pymailer.csv'
STATS_FILE = 'pymailer-%s.stat' % str(datetime.now()).replace(' ', '-').replace(':', '-').replace('.', '-')

# smtp settings
SMTP_HOST = 'localhost'
SMTP_PORT = '25'

# the address and name the email comes from
FROM_NAME = 'GenePattern Team'
FROM_EMAIL = 'gp-info@broadinstitute.org'

# test recipients list
TEST_RECIPIENTS = [
    {'name': 'Name', 'email': 'someone@example.com'},
]
