lower_limit = 47.9
upper_limit = 50.339

shops = {"cito": 47.999,
          "BB_studio": 42.999,
          "momo": 49.999,
          "main-service": 37.245,
          "buy.now": 38.324,
          "x-store": 37.166,
          "the_partner": 38.988,
          "sota": 37.720,
          "rozetka": 38.003}

for shop in shops.items():
    if lower_limit <= shop[1] <= upper_limit:
        print(shop[0])



