#Python 자료형 활용하기 - boolean을 활용한 게임
#2018312581 정은희

#5X5 네모네모 로직

import tkinter as tk
from functools import partial

#정답
dog = [[False, True, False, False, False],
       [True, True, False, False, False],
       [False, True, True, True, True],
       [False, True, True, True, False],
       [False, True, False, True, False]]

#사용자 답
user = [[False, False, False, False, False],
          [False, False, False, False, False],
          [False, False, False, False, False],
          [False, False, False, False, False],
          [False, False, False, False, False]]

answer = dog
corrected = False

MAX = 5
r_hint = []
c_hint = []

def setRowHint(answer):
    r_count=0
    for i in range(0,MAX):
        tmpR_hint=''
        for j in range(0,MAX):
            if answer[i][j] == True:
                r_count += 1
            elif r_count>0:
                tmpR_hint=tmpR_hint+' '+(str(r_count))
                r_count=0
            print(i, j, r_count,r_hint)
        if r_count != 0:
            tmpR_hint=tmpR_hint+' '+(str(r_count))
            r_count=0
        r_hint.append(tmpR_hint)

def setColumnHint(answer):
    c_count=0
    for j in range(0,MAX):
        tmpC_hint = ''
        for i in range(0,MAX):
            if answer[i][j] == True:
                c_count += 1
            elif c_count>0:
                tmpC_hint=tmpC_hint+'\n'+(str(c_count))
                c_count=0
        if c_count != 0:
            tmpC_hint=tmpC_hint+'\n'+(str(c_count))
            c_count=0
        c_hint.append(tmpC_hint)
            
def toggle(i):
    if user[i//MAX][i%MAX] is True:
        user[i // 5][i % MAX] = False
        globals()['b{0}'.format(i)]["bg"] = 'white'
    else:
        user[i // 5][i % MAX] = True
        globals()['b{0}'.format(i)]["bg"] = 'black'
    print('b{0}'.format(i))
    
setRowHint(dog)
setColumnHint(dog)
print(r_hint, c_hint)

#Tkinter 윈도우 생성
window=tk.Tk()
window.title("네모네모 로직")
window.resizable(False, False)

#행 힌트 출력
for i in range(0,MAX):
    row_hint=tk.Label(window, text=r_hint[i], width=6, height=3)
    row_hint.grid(row=i+1, column=0)

#열 힌트 출력
for i in range(0,MAX):
    col_hint=tk.Label(window, text=c_hint[i], width=6, height=3)
    col_hint.grid(row=0, column=i+1)

#네모네모 로직 판 출력
for i in range(0, MAX*MAX):
    globals()['b{0}'.format(i)] = tk.Button(window, bg="white", width=6, height=3, command=partial(toggle, i))
    globals()['b{0}'.format(i)].grid(row=i//5+1, column=i%5+1)

#정답 여부 확인
for i in range(0, MAX):
    for j in range(0, MAX):
        if user[i][j] == answer[i][j]:
            corrected = True
        else :
            corrected = False

#if corrected == True:
    #팝업 출현
    #종료 버튼 클릭 시 종료

window.mainloop()


