from u1p12_14_wordlist import word_list as u1p12_14_wordlist
from u2_exam import word_list as u2_exam
from u2p20_21_wordlist import word_list as u2p20_21_wordlist
from u2p24_25_wordlis import word_list as u2p24_25_wordlis
from u2p28_30_wordlis import word_list as u2p28_30_wordlis
from u3_c import word_list as u3_c
from u3_wordlist import word_list as u3_wordlist
from u3p36_37_wordlist import word_list as u3p36_37_wordlist
from u3p40_43_wordlist import word_list as u3p40_43_wordlist

# 合并所有单元的单词列表
wordlist = u1p12_14_wordlist + u2_exam + u2p20_21_wordlist + u2p24_25_wordlis + u2p28_30_wordlis + u3_c + u3_wordlist + u3p36_37_wordlist


print(len(wordlist))