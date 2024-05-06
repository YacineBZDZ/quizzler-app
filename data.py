# question_data =
import requests
import random

# My code is commented

# question_data = []
# next_question = 0
parameters ={
    "amount" : 10,
    "type" : "boolean"
}

response  = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&type=boolean", params= parameters)
data = response.json()
question_data = data["results"]

# chose_type_questions = random.randint(0,2)
# for result in range(0,10) :
#     data = response.json()["results"][next_question]["question"]
#     data2 = response.json()["results"][next_question]["correct_answer"]
#     question_data.append({"question" : data , "correct_answer" : data2 })
#     next_question += 1

