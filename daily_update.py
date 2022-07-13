from requests_oauthlib import OAuth1Session
import os
import json
import robin_stocks.robinhood as rs

consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret_key")
robin_user = os.environ.get("robin_user")
robin_pass = os.environ.get("robin_pass")
tickers = []
rs.login(username= robin_user,
         password= robin_pass,
         expiresIn=86400,
         by_sms=True)

# Get request token
request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError:
    print(
        "There may have been an issue with the consumer_key or consumer_secret you entered."
    )

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)

# Get authorization
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

# Get the access token
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]

# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

get_positions = rs.build_holdings()
get_user = rs.build_user_profile()
value = float(get_user['equity'])
day = 0.0
first = 0.0
f = open("./performance/Account.txt","r")
temp = 0
for x in f:
    if (temp == 0): float(x)
    day = float(x)
    temp = temp + 1
f.close()

f = open("./performance/Account.txt","a")
f.write(str(value))
f.write("\n")
f.close()

update = "BOT: The total value of this account ended today at $" + str(value) + ". This is a " + str(((value/day) - 1) * 100) + "% change from yesterday and a " + str(((value/first) - 1) * 100) + "% change from July 11, 2021."

f = open("champions.txt","r")
for x in f:
    tickers.append(x.strip())
f.close()
for x in tickers:
    dict = get_positions[x]
    price = float(dict['price'])
    path = './performance/' + x + '.txt'
    f = open(path,"r")
    for x in f:
        day = float(x)
    f.close()
    f = open(path,"a")
    f.write(dict['price'])
    f.write("\n")
    f.close()
    # Making the request
    payload = {"text": "BOT: The current price of " + x + " is $" + dict['price'] + ". The stock has moved " + str(((price/day) - 1) * 100) + "% today and has moved " + dict['percent_change'] + "% since purchase."}
    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
    )

    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))

    # Saving the response as JSON
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))

# Making the request
payload = {"text": update}
response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
)

if response.status_code != 201:
    raise Exception(
        "Request returned an error: {} {}".format(response.status_code, response.text)
    )

print("Response code: {}".format(response.status_code))

# Saving the response as JSON
json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))

rs.logout()