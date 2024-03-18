import requests

def get_random_jokes_from_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response = requests.get(url)
    data = response.json()
    random_jokes = []
    if data["success"] and "data" in data:
        random_jokes_list = data['data']['data']
        print(random_jokes_list)

        for joke in random_jokes_list:
            random_jokes.append(joke["content"])

        print("YOUR RANDOM JOKES ARE SHOWN BELOW: \n")
        for joke in random_jokes:
            print(joke)
        
        return random_jokes
    else:
        raise Exception("Failed to fetch from api.")
def main():
    try:
        random_jokes = get_random_jokes_from_freeapi()
        print(random_jokes)
    except Exception as e:
        print("something went wrong in the api call : ", str(e))
    
if __name__ == '__main__':
    main()
