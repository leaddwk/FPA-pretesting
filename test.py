#===================================================
#Ver1.0
#===================================================

import random
print("일기예보 대본 만들기")
a = [["℃입니다.","℃일 것입니다.","℃이(가) 되겠습니다."],["오늘의 날씨는 맑겠습니다.","오늘은 비가 올 확률이 높습니다. 우산을 챙기시는게 좋을 것 같습니다."]]

def prt():
    for i in range(2):
        if i == 1:
            if precipitation <= 30:
                print(f"강수 확률은 {precipitation}%입니다. {a[i][0]}")
            else:
                print(f"강수 확률은 {precipitation}%입니다. {a[i][1]}")
        elif i == 0:
            print("오늘은 "+str(celsius)+a[i][random.randint(0,2)])
        
        
while True:
    celsius = ""
    celsius = float(input("오늘의 온도는?"))
    precipitation = ""
    precipitation = int(input("오늘의 강수확률은?"))
    prt()

#===================================================
#Ver2.0
#===================================================

import random
print("일기예보 대본 만들기")
day = int(input("앞으로 몇일 까지의 대본을 만드시겠습니까?"))
a = [["℃입니다.","℃일 것입니다.","℃이(가) 되겠습니다."],["오늘의 날씨는 맑겠습니다.","오늘은 비가 올 확률이 높습니다. 우산을 챙기시는게 좋을 것 같습니다."]]
mon = ["월","화","수","목","금","토","일"]

def prt():
    for i in range(2):
        if i == 1:
            if precipitation <= 30:
                print(f"강수 확률은 {precipitation}%입니다. {a[i][0]}")
            else:
                print(f"강수 확률은 {precipitation}%입니다. {a[i][1]}")
        elif i == 0:
            print("오늘은 "+str(celsius)+a[i][random.randint(0,2)])
        
        
while True:
    for k in range(day):
        print(f"{mon[k]}요일의 예보입니다.")
        celsius = ""
        celsius = float(input("오늘의 온도는?"))
        precipitation = ""
        precipitation = int(input("오늘의 강수확률은?"))
        prt()

#===================================================
#===================================================
#===================================================
#1번째 프로그램
#===================================================

print("일기예보 대본 만들기")
a = ["℃입니다.","℃일 것입니다.","℃이 되겠습니다."]

def prt():
    if celint != "":
        for i in range(3):
            print("오늘 온도는 "+str(celint)+a[i])
    else:
        if celsius == "":
            print("온도를 입력해주세요.")
while True:
    celsius = ""
    celsius = float(input("오늘의 온도는?"))
    celint = int(round(celsius))
    prt()

#===================================================
#2번쨰 프로그램
#===================================================

import random
print("재밌는 숫자 맞히기^^(한 라운드에 1~10까지 숫자 3번 맞히면 됨.)")
b = int(input("몇판하실?"))
asw = "정답"
odap = "오답"

def rng(a):
    for i in range(1, a+1):
        for j in range(3):
            b = random.randint(1, 10)
            c = float(input("추측?"))
            if b == int(c):
                print(asw)
            else:
                if b != int(c):
                    print(odap)
        print(f"{i}라운드 종료")

rng(b)

#===================================================
#3번째 프로그램
#===================================================

import tkinter as tk
from tkinter import messagebox

rst = 0

def abt():
    messagebox.showinfo("사용법", "• Σ_i^m(Σ_k^n a_n) 형식의 중첩 시그마 계산기입니다.\n• 실수 입력을 받으며 반올림하여 정수로 변환됩니다.\n• 일반항은 'i'와 'k'를 사용하여 주십시오.\n• 일반항은 파이썬 연산 문법으로 작성해 주십시오.\n\nMade by 20103 김도원")

def dbsigma(i, m, k, n, h):
    global rst # 전역 변수 rst를 수정 가능하게 설정합니다.
    if i >= m:
        messagebox.showerror("에러", "i가 m보다 크거나 같을 수 없음")
    elif k >= n:
        messagebox.showerror("에러", "k가 n보다 크거나 같을 수 없음")
    else:
        if i < m and k < n:
            rst = 0 # 계산하기 전에 rst를 초기화합니다.
            for l in range(i, m+1):
                for j in range(k, n+1):
                    rst += eval(h, {'i':l,'k':j})
    o.configure(text=f"결과:{rst}")
    messagebox.showinfo("연산완료!", f"결과: {rst}")

def getvalue():
    a_val = int(round(float(a.get())))
    b_val = int(round(float(b.get())))
    c_val = int(round(float(c.get())))
    d_val = int(round(float(d.get())))
    e_prs = str(e.get())
    dbsigma(a_val, b_val, c_val, d_val, e_prs)

root = tk.Tk()
root.title("이중 시그마 계산기")

inst = tk.Label(root, text="중첩 시그마 계산기")
inst.pack()

a = tk.Entry(root)
a.insert(0, "바깥 시그마의 연산 범위의 시작항")
a.pack()

b = tk.Entry(root)
b.insert(0, "바깥 시그마의 연산 범위의 말항")
b.pack()

c = tk.Entry(root)
c.insert(0, "안쪽 시그마의 연산 범위의 시작항")
c.pack()

d = tk.Entry(root)
d.insert(0, "안쪽 시그마의 연산 범위의 말항")
d.pack()

e = tk.Entry(root)
e.insert(0,"일반항 입력")
e.pack()

f = tk.Button(root, text="연산하기", command=getvalue)
f.pack()

o = tk.Label(root, text="결과:")
o.pack()

g = tk.Button(root, text="사용법", command=abt)
g.pack()

root.mainloop()
