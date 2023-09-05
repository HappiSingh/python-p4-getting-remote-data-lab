import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url


    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        people_list = []
        peoples = json.loads(self.get_response_body())
        for person in peoples:
            people_list.append(person)

        return people_list

