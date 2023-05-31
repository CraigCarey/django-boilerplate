from model_bakery import baker

user = baker.make('accounts.User')

print(user.license_expiry)
