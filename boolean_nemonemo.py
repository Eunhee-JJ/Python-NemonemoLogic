#Python 자료형 활용하기 - boolean을 활용한 게임
#2018312581 정은희

#5X5 네모네모 로직

import tkinter as tk
from tkinter import messagebox
from functools import partial

MAX = 5 #네모네모 로직의 행/열 수

#정답
dog = [[False, True, False, False, False],
       [True, True, False, False, False],
       [False, True, True, True, True],
       [False, True, True, True, False],
       [False, True, False, True, False]]
answer = dog

#사용자 답
user = [[False]*MAX for i in range(MAX)]

#열 및 행 별 칠해야 하는 칸 수 표현
r_hint = []
c_hint = []

def setRowHint(answer):
    r_count=0
    for i in range(0,MAX):
        tmpR_hint=''
        for j in range(0,MAX):
            if answer[i][j] is True:
                r_count += 1
            elif r_count>0:
                tmpR_hint=tmpR_hint+' '+(str(r_count))
                r_count=0
        if r_count != 0:
            tmpR_hint=tmpR_hint+' '+(str(r_count))
            r_count=0
        r_hint.append(tmpR_hint)

def setColumnHint(answer):
    c_count=0
    for j in range(0,MAX):
        tmpC_hint = ''
        for i in range(0,MAX):
            if answer[i][j] is True:
                c_count += 1
            elif c_count>0:
                tmpC_hint=tmpC_hint+'\n'+(str(c_count))
                c_count=0
        if c_count != 0:
            tmpC_hint=tmpC_hint+'\n'+(str(c_count))
            c_count=0
        c_hint.append(tmpC_hint)

#네모 클릭 시 검/흰 색상 변경 & 해당 칸 bool 리스트 값 토글            
def toggle(i):
    if user[i // 5][i % 5] is True:
        user[i // 5][i % 5] = False
        globals()['b{0}'.format(i)]["bg"] = 'white'
    else:
        user[i // 5][i % 5] = True
        globals()['b{0}'.format(i)]["bg"] = 'black'
    print('b{0}'.format(i))
    print(user)
    print(answer)
    if (user == answer) is True:
        messagebox.showinfo("정답!", "축하합니다. 정답입니다!")
    print(user == answer)

#main   
setRowHint(dog)
setColumnHint(dog)

#Tkinter 윈도우 생성
window=tk.Tk()
window.title("네모네모 로직")
window.resizable(False, False)

#행 힌트 표현
for i in range(0,MAX):
    row_hint=tk.Label(window, text=r_hint[i], width=6, height=3)
    row_hint.grid(row=i+1, column=0)

#열 힌트 표현
for i in range(0,MAX):
    col_hint=tk.Label(window, text=c_hint[i], width=6, height=3)
    col_hint.grid(row=0, column=i+1)

#네모네모 로직 판 표현
for i in range(0, MAX*MAX):
    globals()['b{0}'.format(i)] = tk.Button(window, bg="white", width=6, height=3, command=partial(toggle, i))
    globals()['b{0}'.format(i)].grid(row=i//MAX+1, column=i%MAX+1)


window.mainloop()

