print('\tHome_work')
print()
print('\tЗадание_1')
print()
import random
def gcd(a, b):
    if b == 0:
        return abs(a)
    return gcd(b, a % b)
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
print(f'Случайные_числа {num1} и {num2}')
print(f'Наибольший_общий_делитель_чисел {num1} и {num2} равен {gcd(num1, num2)}')
print()
print('\tЗадание_2') #сделал_с_двухзначным_с_четырёхзначным_запускал_работае_долго_проверять
print()
import random
def generate_number():
    digits = random.sample(range(10), 2)
    return ''.join(map(str, digits))
def bul_and_cow(secret, guess):
    bul = sum(s == g for s, g in zip(secret, guess))
    cow = sum(min(secret.count(digit), guess.count(digit)) for digit in set(guess)) - bul
    return bul, cow
def guess_number(secret, attempts=0):
    guess = input('Введите_2-значное_число ')
    if len(guess) != 2 or not guess.isdigit() or len(set(guess)) != 2:
        print('Некорректный_ввод_введите_цифры')
        return guess_number(secret, attempts)
    attempts += 1
    bul, cow = bul_and_cow(secret, guess)
    if bul == 2:
        print(f'Вы_угадали_число_{secret}_за_{attempts}_попыток')
    else:
        print(f'Количество_угаданных_цифр_на_своём_месте {bul},\nКоличество угаданных цифр: {cow}')
        guess_number(secret, attempts)
def main():
    secret_number = generate_number()
    print('Угадайте_двухзначное_число\n')
    guess_number(secret_number)
if __name__ == "__main__":
    main()
print()
print('\tЗадание_3')
print()
def print_board(board):
    print('   ' + '   '.join(chr(i) for i in range(ord('A'), ord('H') + 1)))
    for i, row in enumerate(board):
        print(f'{i + 1} ' + '  '.join(f'{cell:2}' for cell in row))
        if i < len(board) - 1:
            print()
    print()
def is_safe(x, y, board):
    return 0 <= x < 8 and 0 <= y < 8 and board[x][y] == -1
def horse_tour(board, curr_x, curr_y, move_count):
    if move_count == 64:
        return True
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), 
             (-2, -1), (-1, -2), (1, -2), (2, -1)]
    for dx, dy in moves:
        next_x = curr_x + dx
        next_y = curr_y + dy
        if is_safe(next_x, next_y, board):
            board[next_x][next_y] = move_count
            if horse_tour(board, next_x, next_y, move_count + 1):
                return True
            board[next_x][next_y] = -1
    return False
def init_board(start_x, start_y):
    board = [[-1 for _ in range(8)] for _ in range(8)]
    board[start_x][start_y] = 0
    return board
def solve_horse_tour(start_x, start_y):
    board = init_board(start_x, start_y)
    if horse_tour(board, start_x, start_y, 1):
        print('\nРешение_найдено\n')
        print_board(board)
    else:
        print('Решение_не_найдено')
if __name__ == "__main__":
    try:
        start_x = int(input('Введите_номер_клетки_по_вертикали (от 1 до 8) ')) - 1
        start_y_char = input('Введите_букву_клетки_по_горизонтали (от A до H) ').upper()
        start_y = ord(start_y_char) - ord('A')
        if 0 <= start_x < 8 and 0 <= start_y < 8:
            solve_horse_tour(start_x, start_y)
        else:
            print('Некорректные_координаты_Пожалуйста_введите_значения_от_1_до_8_для_вертикали_и_от_A_до_H_для_горизонтали')
    except ValueError:
        print('Пожалуйста_введите_целые_числа_а_также_корректные_буквы')
print()
print('\tЗадание_4')
print()
import random
def print_board(board):
    for row in board:
        print('  '.join(str(num).rjust(2) for num in row))
        print()
    print()
def find_zero(board):
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == 0:
                return i, j
def can_move(zero_pos, move_pos):
    return (abs(zero_pos[0] - move_pos[0]) == 1 and zero_pos[1] == move_pos[1]) or \
           (abs(zero_pos[1] - move_pos[1]) == 1 and zero_pos[0] == move_pos[0])
def move(board, direction):
    zero_pos = find_zero(board)
    if direction == 'w':
        new_pos = (zero_pos[0] - 1, zero_pos[1])
    elif direction == 's':
        new_pos = (zero_pos[0] + 1, zero_pos[1])
    elif direction == 'a':
        new_pos = (zero_pos[0], zero_pos[1] - 1)
    elif direction == 'd':
        new_pos = (zero_pos[0], zero_pos[1] + 1)
    else:
        print('Неверная_команда')
        return False
    if 0 <= new_pos[0] < len(board) and 0 <= new_pos[1] < len(board[0]) and can_move(zero_pos, new_pos):
        board[zero_pos[0]][zero_pos[1]], board[new_pos[0]][new_pos[1]] = board[new_pos[0]][new_pos[1]], board[zero_pos[0]][zero_pos[1]]
        return True
    else:
        print('Невозможный_ход')
        return False
def is_solved(board):
    flat_board = [num for row in board for num in row]
    return flat_board == list(range(len(flat_board)))
def main():
    size = 4
    numbers = list(range(size * size))
    random.shuffle(numbers)
    board = [numbers[i * size:(i + 1) * size] for i in range(size)]
    while not is_solved(board):
        print_board(board)
        move_input = input('Введите_команду_(w вверх, s вниз, a влево, d вправо) ').lower()
        move(board, move_input)
    print('Вы_выиграли')
if __name__ == "__main__":
    main()

