from ringcentral import SDK

sdk = SDK('BtPneC0nTyWjxsk1WrgCWg', '81mtCIOESPGwWDsybeDXmAJYAr5dJcTtqgDApfLWrudQ', 'https://platform.devtest.ringcentral.com')
platform = sdk.platform()
platform.login('nicholas.bautista@pacden.com', '5005421', 'Nick123032@')

res = platform.get('/account/~/extension/~')
print('User loaded ' + res.json().name)
print("ngutl")
print("whfwq")
print("cnerw")
