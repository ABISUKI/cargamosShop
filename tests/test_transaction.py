"""
    Simple Testing to test connection in database making simple query.
"""

from app.utilities.db_transaction import Transaction
from etc import SETTINGS

pull_query = SETTINGS["queries"]["get_product"]
tr = Transaction()


def test_pull():
    global pull_query
    pull_query = pull_query.format("ELPHNP30LITEHWI")
    results = tr.pull(pull_query)
    assert results[0] == True