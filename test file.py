import time


animals = ['dumb', 'dumb2', 'dumb3', 'dumb4']

print(animals)

if 'dumb' in animals:
    print('ya got dat right')
    time.sleep(1)
    print('in은 배열에 지정된 값이 들어있는지 확인해 준다.')

time.sleep(1)
print('append는 배열 뒤에 지정된 문자/수를 붙여 넣는다.')
append_test = ['this is a test']
print(append_test)
append_test.append('I do what I want')
print(append_test)

time.sleep(1)
print('split은 말 그대로 문장을 단어 따로 따로 스플릿 시켜준다')
time.sleep(1)
sentence = 'what do you think you are doing'
print(sentence.split())

