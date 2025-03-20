import random
from tools import check_word, is_passing_score, sum_score

word_list = [
    ("苹果", "apple|apple1"),
    ("大象", "elephant/ele|dog"),
    ("学校", "school"),
    ("重要的", "important"),
    ("英语", "english"),
    ("紧急事件", "emergency"),
    ("中国","China"),
    ("粉色","pink"),
    ("蓝色","blue"),
    ("绿色","green"),
    ("云","cloud")
]
original_wordlist_len=len(word_list)
words_amount=input(f"本次单词表有{len(word_list)}个单词，请输入要选择默写单词的个数（若要全部默写可忽略）：")

while True :
    try:
        words_amount_int=int(words_amount)
        if words_amount_int < len(word_list) :
            if words_amount_int>=5:
                random.shuffle(word_list)
                word_list=word_list[:words_amount_int]
                break
            else:
                words_amount=input("请重新输入(单词个数少于5个)：")
    except ValueError as e:
        random.shuffle(word_list)
        break

wrong_times=0
def test_words(words):
    global wrong_times
    temp_wrong_words = []
    t = 1
    len_words = len(words)
    for chinese, english in words:
        print(f"{t}/{len_words}.请输入[{chinese}]的英文单词")
        user_input = input("输入处：")
        if not check_word(english,user_input):
            temp_wrong_words.append((chinese, english ))
            print("**输入错误!")
            a_input = input("**输入1显示答案(可直接跳过)")
            wrong_times+=1
            if a_input == "1":
                print(f"**答案是{english}")
                wrong_times+=1
            print(f"累计错误次数:{wrong_times} 次")
        else:print("**输入正确！")
        t+=1
    return temp_wrong_words

i = 1
print("欢迎来到Linyun背单词软件 v1.2.4")
print(f"本次有{len(word_list)}个单词需要默写")
print("[满分100，错一个减一分，如果看了答案再扣一分]")
while True:
    wrong_word = test_words(word_list)
    if not wrong_word:
        final_score = sum_score(wrong_times,original_wordlist_len)
        judge_result=is_passing_score(final_score)
        print("$总共经历%d轮" % i)
        print(f"$最终得分：{final_score}" )
        print(f"${judge_result}")
        print("$恭喜你，单词表内的单词全部背出来了")
        print("$收费10000000000000000000000元，谢谢配合！")
        break
    else:print("$第%d轮中,共%d个单词，你有%d个单词输入错误。" % (i , len(word_list) , len(wrong_word)))
    i+=1
    word_list=wrong_word



