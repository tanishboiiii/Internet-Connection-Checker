from urllib import request

def testConnection():
    try:
        request.urlopen("https://www.google.com/", timeout = 5)
        print("Connected to Internet!")
    except:
        print("No Internet Connection :(")



testConnection()