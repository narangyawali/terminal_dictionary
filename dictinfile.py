
import requests
import json


def dict(arg):
    response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en_US/"+arg)
    result = json.loads(response.text)
    try:
        meaning = result[0]["meanings"][0]["definitions"][0]["definition"]
    except:
        meaning = f"meaning of {arg} not found due to ..."
    finally:
        return meaning
    
src = input("give the path to the file:\n")
file = open(src, 'r', newline="")
lines = file.readlines()


rfile = open(f"{src[0:(len(src)-4)]}@meaning.txt","w")

for line in lines:
    word = line.strip()
    statement= word +","+ "\"" +dict(word)+"\""+"\n"
    rfile.write(statement)
    
