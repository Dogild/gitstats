# -*- coding: utf-8 -*-

from gitstats.models.account import Account
from gitstats.models.commit import Commit

account = Account("Dogild")
repositories = list()
forks = list()
contributed_forks = list()

print "Let's take a look to the account %s" % account.username

print "Retrieving the repositories"
repositories = account.get_repositories()
print repositories
