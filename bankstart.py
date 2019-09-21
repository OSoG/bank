import pandas as pd
import numpy as np
df = pd.read_csv("1908.csv", sep = ";")


## 콤마 replace

## pandas는 여러 포맷들을 읽을 수 있음
## read_html, csv, ...

## 콤마 parsing 오류


df.head(2)

print(df.iloc[0,0])
type(df.iloc[0,0])
## iloc, loc...
## iloc : integer-located based

type(df["취급점"])
df["취급점"]

df["취급점"].values

df["취급점"].unique()

df_sub = df.loc[df["취급점"].str.match(pat = "^[0-9]"),]
## ^ : 시작

df_sub.head(2)

df_sub["취급점"].unique()

## cross tab  : count
df_sub["취급점"].value_counts()

## pandas series에 대해서

pd.crosstab(df_sub["기재내용"], df_sub["취급점"])



# 입력받는 것 : 날짜
# 행동 : 날짜로부터 마지막 거래후잔액을 찾는다.

## 마지막 거래 불러오기
df.loc[:, "거래일시"] = pd.to_datetime(df["거래일시"])
df.head(2)


type(df.iloc[0,0])

df.loc[:,"date"] = df["거래일시"].dt.date
df.head(2)

input_date = '2019-08-02'

df_sub = df.loc[df["date"].astype("str") == input_date, ]

df_sub.head()

df_sub.columns
## 3가지
df_sub.columns.values
df_sub.columns[5]

df_sub.columns.values[5] = "remain"
df_sub.columns
df_sub.loc[:, "remain"]


df_sub.iloc[:, 5]

## 마지막
df_sub.iloc[:, 5].values[-1]

last_balance = df_sub.iloc[:, 5].values[-1]

last_balance

### 입력 후


