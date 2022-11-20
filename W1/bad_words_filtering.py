"""
Đặt vấn đề: 

Để đảm bảo một môi trường trong sạch trên Internet,
một số nền tảng online thường thay thế các ký tự cuối của chuỗi chứa các
từ ngữ nhạy cảm bằng các dấu *

Hãy viết một hàm thay thế tất cả các ký tự trừ ký tự đầu tiên của từ nhạy cảm bằng dấu *
"""

BAD_WORDS_SAMPLE = ['suck', 'fuck'] 

def bad_word_filter(word: str) -> str:
    filtered_word = ''
    if word in BAD_WORDS_SAMPLE:
        for i in range(len(word)): # range(start, stop, step) -> list(range(0, 5)) = [0, 1, 2, 3, 4]; len([]): number of elements in list
            if i == 0:
                filtered_word += word[i]
            else: 
                filtered_word += '*'
    return filtered_word # return 'word' after replace characters


if __name__ == '__main__':
    user_input: str = input('Input your word:')
    while user_input.strip() == '': # if user input is blank or None, force user to input again
        user_input = input('Input your word:')
    filtered_word = bad_word_filter(user_input)
    print(filtered_word)
