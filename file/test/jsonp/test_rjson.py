import json
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        username=input("What is your name?")
        filename='username.json'
        with open(filename,'w') as f:
            json.dump(username,f)
            print(f"We will remember you when you come back, {username}!")
    def test_else(self):
        filename='username.json'
        with open(filename) as f:
            username = json.load(f)
            print(f'Welcome back, {username}!')

if __name__ == '__main__':
    unittest.main()

