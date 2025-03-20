def is_passing_score(is_final_score):
    flag="成绩不合格，请重新练习"
    if is_final_score>90:
        flag="成绩合格，继续加油"
        return flag
    else:return flag

def sum_score(sum_wrong_times, wordlist_length):
    sum_final_score = round((wordlist_length- sum_wrong_times) / wordlist_length, 3) * 100
    if sum_final_score<0:
        sum_final_score=0
    return sum_final_score

def check_word(words,user_input):
    list_words=words.split("|")
    flag=False
    for word in list_words:
        if is_same_word(word,user_input):
            flag=True
            break
    return flag

def is_same_word(answer,user_input):
    temp_count = 0
    answer_words = answer.split("/")
    user_input_words=user_input.split("/")
    if len(answer_words)==len(user_input_words):
        for temp_answer_words in answer_words:
            if temp_answer_words in user_input_words:
                temp_count+=1
        return temp_count==len(answer_words)
    else:return False

def ext_bracket_words(word):
    #提取单词内括号里的片段，如果有多个这存在数组内返回
    temp_words=[]
    temp_word=""
    for temp_char in word:
        if temp_char=="(":
            temp_word=""
        elif temp_char==")":
            temp_words.append(temp_word)
        else:
            temp_word+=temp_char
    return temp_words

def clear_bracket(word):
    #清除括号及括号内的内容
    result = ""
    in_bracket = False
    for char in word:
        if char == '(':
            in_bracket = True
        elif char == ')':
            in_bracket = False
        elif not in_bracket:
            result += char
    return result.strip()

def test():
    print(
        ext_bracket_words("(give/make/deliver) a speech (about/on) sth.")
    )
    print(
        clear_bracket("(give/make/deliver) a speech (about/on) sth.")
    )

# 运行测试
if __name__ == "__main__":
    test()
