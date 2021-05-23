print ("Tweeb setup")
print (" note :  You don't need to run the script agaain if you don't change the keys")
print (" ")

apikey = input("Api Key : ")
apikey_secret = input("Api Key Secret : ")
token = input ("token : ") 
token_secret = input ("token secret : ")

with open("keys.py", "w") as text_file:
   text_file.write('apikey = "%s"\napikey_secret = "%s"\ntoken = "%s"\ntoken_secret = "%s"' % (apikey, apikey_secret, token, token_secret))

print (apikey)
print ("\033c")
print ("Running the script twt.py")
exec(open('tweeb.py').read())