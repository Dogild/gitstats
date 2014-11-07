# -*- coding: utf-8 -*-

from gitstats.models.account import Account
from gitstats.models.commit import Commit

account = Account("primalmotion")
repositories = list()
forks = list()
contributed_forks = list()

print "Let's take a look to the account %s" % account.username

print "Retrieving the repositories"
repositories = account.get_repositories()
print repositories

print "Retrieving commits for each repositories"
commits = account.get_commits()
print commits
print "Number of commits %s" % len(commits)

print "Retrieving issues for each repositories"
issues = account.get_issues()
print issues
print "Number of issues %s" % len(issues)

print "Total contributions for %s" % account.username
print account.contributions