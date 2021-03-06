import sys
sys.path.append('/Users/zhenxi/Desktop/for_git/AIB_PJ1/AIB_PJ1_QnA-chatbot/chatbot')
import pickle
from utils.Preprocess import Preprocess



# 단어 사전 불러오기
f = open("/Users/zhenxi/Desktop/for_git/AIB_PJ1/AIB_PJ1_QnA-chatbot/chatbot/train_tools/dict/chatbot_dict.bin", "rb")
word_index = pickle.load(f)
f.close()

sent = "내일 오전 10시 탕수육 주문 부탁~"

# 전처리 객체 생성
p = Preprocess(userdic='../utils/user_dic.tsv')

# 형태소 분석기 실행
pos = p.pos(sent)

# 품사 태그 없이 키워드 출력
keywords = p.get_keywords(pos, without_tag=True)
for word in keywords:
    try:
        print(word, word_index[word])
    except KeyError:
        # 해당 단어가 사전에 없는 경우 OOV 처리
        print(word, word_index['OOV'])


'''
[실행 결과]
내일 14
오전 269
10 105
시 4
탕수육 431
주문 3
부탁 179
'''