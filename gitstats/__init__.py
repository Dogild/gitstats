from gitstats.models.account import Account

def get_contributions_for_user_for_dates(username, start_date, end_date, timezone):
    account = Account(username, timezone)
    return account.get_contributions_for_dates(start_date, end_date)

def get_contributions_for_user_for_last_year(username, timezone):
    account = Account(username, timezone)
    return account.get_contributions_of_last_year()