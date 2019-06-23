def input_number():
    while True:
        try:
            print('1以上の整数を1つ入力してください。例）100')
            return int(input())
        except ValueError:
            print('エラー：入力値が整数ではありません。')
            continue

def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1

def main():
    number = input_number()
    while number != 1:
        print(int(collatz(number)))
        number = collatz(number)

if __name__ == "__main__":
    main()