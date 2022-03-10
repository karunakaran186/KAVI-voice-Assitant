from fuzzywuzzy import process
words = ( "quit", "nothing","bye", "bbye", "terminate", "see you later", "exit")

def get_matches(query, choices, limit =3):
    results =process.extract(query, choices, limit=limit)
    return results
print(get_matches("qut", words))