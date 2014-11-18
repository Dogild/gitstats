from gitstats.models.account import Account

def get_contributions_for_user_for_dates(username, start_date, end_date):
    account = Account(username)
    return account.get_contributions_for_dates(start_date, end_date)

def get_contributions_for_user_for_last_year(username):
    account = Account(username)
    return account.get_contributions_of_last_year()