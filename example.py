from gitstats.models.account import Account
from gitstats.models.commit import Commit

account = Account("Dogild")
repositories = list()
forks = list()
contributed_forks = list()

print account.username

print "Retrieving the repositories"
repositories.append(account.get_repositories())
print repositories

print "Commits of these repositories"

for repository in repositories:
    print account.get_commits_for_repository(repository)


print "Retrieving the forks"
forks.append(account.get_forks())
print forks

print "Forks where Dogild has contributed"
contributed_forks.append(account.sort_contributed_forks(forks))
print contributed_forks

print "Commits of this forks"

for fork in contributed_forks:
    print account.get_commits_for_fork(fork)
