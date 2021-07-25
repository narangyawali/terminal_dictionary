import requests
import json
import sys

api_url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"

def show_result(list):
    for i in range(len(list)):
        #print(f"({i}):{list[i]["definition"]}")
        print("-------------------------------------------------------------------")
        print("(defintion):")
        print(list[i]["definition"])
        print(f"(example):")
        print(list[i]["example"])
		

def dict(arg):
    response = requests.get(api_url+arg)
    if response.status_code == 200:
        # print("json in text")
        # print(response.text)
        result = json.loads(response.text)
        try:
            meanings = result[0]["meanings"][0]["definitions"]# [0]["definition"]
            show_result(meanings)
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
