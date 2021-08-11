import requests
import json
import sys
from pathlib import Path
#home = str(Path.home())
home = Path.home()
api_url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"

def show_result(list,arg):
    for i in range(len(list)):
        defination= list[i]["definition"]
        example= list[i]["example"]
        #print(f"({i}):{list[i]["definition"]}")
        print(home)
        print("-------------------------------------------------------------------")
        print("(defintion):")
        print(defination)
        print(f"(example):")
        print(example)
        with open (f"{home}/ter_dict/history.csv","a") as history:
            history.write(f"{arg},\"{defination}\",\"{example}\"\n")
            
		

def dict(arg):
    response = requests.get(api_url+arg)
    if response.status_code == 200:
        # print("json in text")
        # print(response.text)
        result = json.loads(response.text)
        try:
            meanings = result[0]["meanings"][0]["definitions"]# [0]["definition"]
            show_result(meanings,arg)
        except:
            error_message = "meaning of {} not found due to ...".format(arg)
            print(error_message)
        # finally:
        #     return meaning

    else:
        return "There seems to be problem in your internet connection or ....."        


if __name__ == "__main__":
    word = sys.argv[1]
    #word = "naive"
    meaning = dict(word)
    #print(meaning)
