word=input() # 문자열 입력
croa=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 크로아티아 문자 리스트

for i in croa :
  # croatia 표의 8개의 문자를 꺼내면서 replace 함수로 변환하였다.
  # 동일한 문자가 없는 경우는 변환되지 않다가 동일한 문자가 있으면 * 기호로 변환되는 것을 볼 수 있다.
  # 최종적으로 변환된 문자열의 개수가 6개여서 최종적으로 6을 출력하는 것을 볼 수 있다.
  word=word.replace(i, '*')
print(len(word))

# ljes=njak
# -> *e**ak