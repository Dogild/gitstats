# -*- coding: utf-8 -*-

from gitstats.models.account import Account
from gitstats.models.commit import Commit

account = Account("Dogild")

print "Let's take a look to the account %s" % account.username
print "Retrieving contributions"
contributions = account.get_contributions_of_last_year()
print contributions
print "Totale number of contributions %s" % len(contributions)
