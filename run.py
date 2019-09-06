import json
from Q import Quiz

encoding = 'utf-8'

quiz = Quiz('Q/questions.json')
quiz.start()


score = 0
for q in quiz.questions:
    print(q.display)
    a = input('Unesite odgovor: ')
    if q.check(a):
        score += 1

result = "Broj točnih odgovora", score

with open('data.json', "a", encoding=encoding)as outfile:
    json.dump(result, outfile, ensure_ascii=False),

with open("data.json", "r", encoding=encoding ) as read_file:
    des = json.load(read_file),

print(des)