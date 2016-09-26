import dota2api
api = dota2api.Initialise("011FDB9B58720BA529C7647EC74BB045")
match = api.get_match_details(match_id=2600633597)
print(match.url)
