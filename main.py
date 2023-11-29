import random
answers = []
morse_code = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}
words = ['land', 'scope', 'package', 'craft', 'craftsman', 'crafty', 'worth', 'worthy', 'urban', 'urbanization', 'pond']
def morse_encode(sentence):
    word = ""
    for char in sentence:
        word += morse_code[char]
    return word
def get_word():
  return random.choice(words)


def print_statistics():
    number_of_correct_answers = 0
    number_of_incorrect_answers = 0
    for response_result in answers:
        if response_result:
            number_of_correct_answers += 1
        else:
            number_of_incorrect_answers += 1
    print(f"Всего задачек:{number_of_incorrect_answers + number_of_correct_answers}")
    print(f"Отвечено верно:{number_of_correct_answers}")
    print(f"Отвечено неверно:{number_of_incorrect_answers}")


def game():
    for i in range(3):
        n = 0
        random_word = get_word()
        print(f"Слово {n+1} {random_word}:{morse_encode(random_word)}")
        user_answer = input("Введите ваш ответ: ")
        if user_answer == random_word:
            answers.append(True)
            print(f"Верно,{random_word}")
        else:
            print(f"Неверно,{random_word}")
            answers.append(False)






user_answer = input("Сегодня мы потренируемся расшифровывать морзянку.""\nНажмите Enter и начнем")
if user_answer == "":
    game()
    user_answer = input()
    if user_answer == "well played!":
        print_statistics()



