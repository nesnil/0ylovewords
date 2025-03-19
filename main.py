from wordlist import u1p12_14_wordlist, u2p20_21_wordlist, u2p24_25_wordlis

def display_wordlist(word_list, title):
    print(f"\n{title}:")
    print("-" * 50)
    for cn, en in word_list:
        print(f"{cn:<20} {en}")

def main():
    print("欢迎使用单词表显示程序！")
    print("\n可用的单词表：")
    print("1. Unit 1 Pages 12-14 单词表")
    print("2. Unit 2 Pages 20-21 单词表")
    print("3. Unit 2 Pages 24-25 单词表")
    print("4. 显示所有单词表")
    print("0. 退出程序")

    while True:
        choice = input("\n请选择要显示的单词表 (0-4): ")
        
        if choice == "0":
            print("感谢使用，再见！")
            break
        elif choice == "1":
            display_wordlist(u1p12_14_wordlist.word_list, "Unit 1 Pages 12-14 单词表")
        elif choice == "2":
            display_wordlist(u2p20_21_wordlist.word_list, "Unit 2 Pages 20-21 单词表")
        elif choice == "3":
            display_wordlist(u2p24_25_wordlis.word_list, "Unit 2 Pages 24-25 单词表")
        elif choice == "4":
            display_wordlist(u1p12_14_wordlist.word_list, "Unit 1 Pages 12-14 单词表")
            display_wordlist(u2p20_21_wordlist.word_list, "Unit 2 Pages 20-21 单词表")
            display_wordlist(u2p24_25_wordlis.word_list, "Unit 2 Pages 24-25 单词表")
        else:
            print("无效的选择，请重新输入！")

if __name__ == "__main__":
    main()