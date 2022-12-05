"""
Đặt vấn đề:
-----------
Khi chúng ta tìm kiếm với Google, đặc biệt khi tìm kiếm với các cụm từ hoặc câu
chúng ta thường nhận về các kết quả chứa các từ/cụm từ đó
hoặc có thể chung chủ đề với từ/cụm từ chúng ta cung cấp.
Ý tưởng:
--------
Một document (bài viết) có thể có chủ đề gần giống/hoặc giống với
những từ/cụm từ chúng ta cung cấp nếu các từ/cụm từ đó có khoảng cách
gần nhau trong document đó.
Diễn giải:
----------
Từ: có thể là một ký tự và một từ có nghĩa hoặc không có nghĩa
Ví dụ: "tôi có a asd nỗi buồn thật đẹp" ==> 8 từ
Khoảng cách giữa từ: là số từ ở giữa nó cách nhau bằng khoảng trắng
Ví dụ: tìm kiếm với cụm từ "lập trình"
Một document có câu sau:
"Lập luôn là người làm việc có trình tự trong mọi công việc"
==> khoảng cách giữa từ "lập" và "trình" là 6 ("luôn", "là", "người", "làm", "việc", "có")
"Lập trình giúp con người sáng tạo ra các phần mềm phục vụ cho cuộc sống"
==> khoảng cách giữa từ "lập" và "trình" là 0 (không có từ nào đứng giữa chúng)

Hãy tìm khoảng cách giữa 2 từ (phải đúng thứ tự) cho trước trong một câu/đoạn văn.
# Không được dùng hàm .split(' ')
"""

SENTENCE: str = 'Học là một người chăm chỉ, anh ấy luôn cố gắng dành thời gian rảnh của mình  để luyện tập những thói quen tốt trong cuộc sống'
FIRST_WORD = 'Học'
SND_WORD = 'tập'

def calculate_document_distance(document: str) -> int:
    distance: int = 0
    list_of_words = []
    word: str = ''
    first_word_index: int = 0
    snd_word_index: int = 0

    for i in range(len(document)):
        if document[i] != ' ':
            word += document[i]
            if i <= len(document) - 2:
                if document[i+1] == ' ':
                    list_of_words.append(word)
        else:
            word = ''

    for k in range(len(list_of_words)):
        if list_of_words[k] == FIRST_WORD:
            first_word_index = k
        if list_of_words[k] == SND_WORD:
            snd_word_index = k

    distance = snd_word_index - first_word_index - 1

    print(list_of_words)
    return distance

if __name__ == '__main__':
    distance = calculate_document_distance(SENTENCE)
    print(distance)