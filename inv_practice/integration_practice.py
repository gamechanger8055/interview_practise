import requests
import json
import os

class BikeMap:
    def __init__(self):
        self.target_path = os.path.dirname(os.path.abspath(__file__))
    def read_file(self,file_path):
        full_path = os.path.join(self.target_path, file_path)
        try:
            with open(full_path,"r") as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("FileNotFoundException")
        except IOError:
            print("IOException")

    def read_object_from_json_string(self,json_string):
        example=json.loads(json_string)
        print(example["name"])
        print(example["population"])
        print(example["listOfStates"])

    def read_object_from_json(self,file_path):
        try:
            with open(file_path,"r") as json_file:
                records=json.load(json_file)
                print(records)
        except FileNotFoundError:
            print("FileNotFoundException")
        except IOError:
            print("IOException")

    def write_json(self):
        example=self.create_example_method()
        with open("api_responses.json","w+") as file:
            json.dump(example,file,indent=4)

    def download(self,url,filename):
        response=requests.get(url)
        if response.status_code==200:
            #file="abc.json"
            with open(filename,"wb") as file:
                file.write(response.content)
        else:
            print(f"Failed to download file: {response.status_code}")
    @staticmethod
    def create_example_method():
        example = {
            "name": "output name",
            "population": 12321,
            "listOfStates": ["state1", "state2", "state3"]
        }
        return example




if __name__ == "__main__":
    bike_map = BikeMap()

    # Read from file and print lines
    bike_map.read_file("text.txt")

    # Read object from JSON string and print
    json_string = '{"name": "country name", "population": 123, "listOfStates": ["country1", "country2", "country3"]}'
    bike_map.read_object_from_json_string(json_string)

    # Read object from JSON file and print
    bike_map.read_object_from_json("api_responses.json")

    # Read array from JSON file and print
    #bike_map.read_array_from_json("array.json")

    # Read list from JSON file and print
    #bike_map.read_list_from_json("array.json")

    # Write JSON to file
    bike_map.write_json()

    # Download files
    bike_map.download("https://raw.github.com/square/okhttp/master/README.md", "README.md")
    bike_map.download("https://raw.githubusercontent.com/Luzifer/staticmap/master/example/postmap.png", "postmap.png")
