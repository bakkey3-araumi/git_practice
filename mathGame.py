import random

def generate_secret_number():
    return random.randint(100, 999)

def provide_hint(secret, guess):
    secret_str = str(secret)
    guess_str = str(guess)
    
    # 各数字の出現回数をカウントするための辞書
    secret_count = {}
    guess_count = {}
    
    # 秘密の数字のカウント
    for digit in secret_str:
        if digit in secret_count:
            secret_count[digit] += 1
        else:
            secret_count[digit] = 1
    
    # ユーザーの入力のカウント
    for digit in guess_str:
        if digit in guess_count:
            guess_count[digit] += 1
        else:
            guess_count[digit] = 1
    
    # あっている数字の個数を計算
    correct_count = 0
    for digit in guess_count:
        if digit in secret_count:
            correct_count += min(secret_count[digit], guess_count[digit])
    
    return f'正解の数字が{correct_count}個含まれています'

def main():
    secret_number = generate_secret_number()
    max_attempts = 10
    attempts = 0
    
    print('3桁の正解の数字を当ててください。')
    print('フィードバック: 正しい数字の個数を教えます。')
    
    while attempts < max_attempts:
        guess = input(f'{attempts + 1} 回目の回答: ')
        
        if not guess.isdigit() or len(guess) != 3:
            print('無効な入力です。3桁の数字を入力してください。')
            continue
        
        guess = int(guess)
        attempts += 1
        
        if guess == secret_number:
            print(f'正解です！{attempts} 回目で正解しました。')
            break
        else:
            hint = provide_hint(secret_number, guess)
            print(f'不正解です。ヒント: {hint}')
    
    if attempts == max_attempts and guess != secret_number:
        print(f'残念！正解は {secret_number} でした。')

if __name__ == '__main__':
    main()
