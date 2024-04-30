import random

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["꽤 흥미롭네요, 더 말해봐요.",
                    "그렇군요. 계속하세요.",
                    "왜 그렇게 말하시는 거예요?",
                    "날씨가 좋네요, 그렇죠?",
                    "다른 주제는 어때요?.",
                    "어젯밤에 했던 게임은 좀 어때요?"]

print("안녕하세요 저는 간단한 챗봇 마빈입니다.")
print("대화를 종료하고 싶으시다면 '안녕'이라고 해주세요.")
print("대답을 입력한 후에는 엔터를 눌러 전송해주세요.")
print("오늘은 좀 어때요?")

while True:
    user_input = input("> ")
    if user_input == "안녕":
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("좋은 대화였어요! 안녕히 가세요!")