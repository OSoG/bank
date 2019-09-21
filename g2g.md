
1. html 파일을 csv 파일로 변환시켰다. (표 변환)
2. csv 파일을 import 해야겠지? (pandas) 
3. 그리고 csv 파일을 계산하기 쉽도록 numpy array로 만들 것.
  dataframe, series

4. 입금과 출금을 구분해야함.

5. 시간에 따른 계좌 잔액이 있었으면.

6. filter 기능.

7. 자동 전처리 기능 : 예) - '이디야' 항목이 있으면 커피로.


[3] p1901 = pd.read_csv(dir + '1901MOCKTEST.csv')

[6] cat2 = df[df['DP'] == cat].reset_index(drop=True)

카테고리 : 

pandas
matplotlib
pandas as pd
Datacamp 
될 수 있으면 밑바닥으로

Mission



# Reading DataFrames from multiple files
## Import pandas
import pandas as pd
## Read 'Bronze.csv' into a DataFrame: bronze
dir = input("dir: ")
## '/Users/dongweonshin/Dropbox/MOCK/'

cat = input("cat: ")
p1901 = pd.read_csv(dir + '1901MOCKTEST.csv')
p1902 = pd.read_csv(dir + '1902MOCKTEST.csv')
p1903 = pd.read_csv(dir + '1903MOCKTEST.csv')
p1904 = pd.read_csv(dir + '1904MOCKTEST.csv')
p1905 = pd.read_csv(dir + '1905MOCKTEST.csv')
## Print the first five rows of gold
print(p1901.head())

p1901[p1901['DP'] == cat].head()

## [1 new_var] = Append [2] after [3] with ignore_index=True:
new = p1901.append(p1902, ignore_index=True)
new = new.append(p1903, ignore_index=True)
new = new.append(p1904, ignore_index=True)
new = new.append(p1905, ignore_index=True)


# Filter - 1:new_var, 2:df, 3:cat, 4:match
cat2 = new[new['DP'] == cat].reset_index(drop=True)
# Print the first 5 rows of new_york_sales
print(cat2) ## check
#print(cat, file=open(cat + ".md","w"))





📚 (스터디) DYI
안녕하세요~ 점프투파이썬과 연계하여, 적용해 보는 연습을 하는 스터디입니다.

⛳ How

아래 링크를 참조하세요!

http://authorcloud.co/article-d2ci0rrhz

⌚ 시간&장소 : 토요일 10-12시, 신촌 스터디룸 (참여시 공개)
😀 Who :
- 대학/대학원생/직장인

위의 힝목 중 하나라도 만족하시는 분들은 스터디 참가하는데 무리없습니다.

- 대학교 2학년 이하
- 6개월 이내 취업을 목표로 서둘러야하는 사람

위의 항목 중 하나라도 해당되시는 분들은 참여가 어렵습니다.

📞 Contacts :
구글 폼: https://forms.gle/oGN5SW9Et9vEyBDF8
카카오톡 링크: https://open.kakao.com/o/sVtpyRE


####스터디 모집####
1. 주제 : 파이썬 패키지 스터디
(부제 : DIY 셀프 뱅킹 패키지 개발)
2. 지역 : 신촌 스터디룸 (토 10-12)
3. 콘텐츠 : 개인 계좌관리(사용내역 분석, 시각화)를
자동화할 수 있는 패키지를 만듭니다.
4. 스터디 진행 방법 :
http://authorcloud.co/python_package-dfdkspylt
5. 스터디 기간 : 매달 참여여부 갱신 
6. 참여 조건 : 기본매너, pandas, matplotlib 등 사용경험 있는 분
7. 제한 인원 : 6-10 (변동 가능)
8. 비용 : 스터디룸 이용비 더치페이
9. 기타 :
기타 문의는 아래 1:1 톡으로 연락주세요!
10. 문의처 : 카카오톡 1:1 (https://open.kakao.com/o/sVtpyRE)
Google survey : https://goo.gl/forms/PuZmr5bxy3gqYe7k2
=====