import requests


class UserData:
    def get_user_data(self):

        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error")



ob = UserData()
data = ob.get_user_data()
print(data)
