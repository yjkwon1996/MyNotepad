# import os
import datetime
import tkinter.messagebox
from tkinter import * # Tk GUI 툴킷에 대한 파이썬 바인딩
from tkinter import filedialog

root = Tk()
root.title("Notepad 타이틀명")
root.geometry("640x480")
# root.geometry("640x480+100+300") # 프레임 위치 가로x세로 + x좌표+y좌표
# root.resizable(False, False) # x(너비)y(높이)값 변경 불가

# 열기, 저장 파일 이름
date = datetime.date.today()
filename = str(date) + ".txt"

def open_file() :
    # 파일 대화 상자를 열어 파일 선택
    selected_file = filedialog.askopenfilename(
        title="파일 선택",
        filetypes=(("텍스트 파일", "*.txt"), ("모든 파일", "*.*"))
    )

    # 사용자가 파일을 선택했는지 확인
    if selected_file:
        with open(selected_file, "r", encoding="utf-8") as file:
            txt.delete("1.0", END)  # 기존에 열려 있는 내용 삭제
            txt.insert(END, file.read())  # 선택된 파일 내용 읽어오기

    # if os.path.isfile(filename) : # 파일 존재 여부 확인
    #     with open(filename, "r", encoding="utf-8") as file :
    #         txt.delete("1.0", END) # 기존에 열려 있는 내용 삭제
    #         txt.insert(END, file.read()) # filename에 저장된 내용 읽어오기

def save_file() :
    file = open(filename, "w")
    ts = txt.get("1.0", END)
    file.write(ts)
    file.close()
    tkinter.messagebox.showinfo("알림", "정상적으로 저장되었습니다.")
    # with open(filename, "w", encoding="utf-8") as file :
    #     file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장



# 메뉴 라인 만들기
menu = Menu(root)


menu_file = Menu(menu, tearoff=0) # 하위 메뉴 분리기능 사용 유무
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)

menu.add_cascade(label="파일", menu=menu_file)

menu_edit = Menu(menu, tearoff=0)
menu_edit.add_command(label="edit")

menu.add_cascade(label="편집", menu=menu_edit)

menu.add_cascade(label="서식")
menu.add_cascade(label="보기")

menu_help = Menu(menu, tearoff=0)
menu_help.add_command(label="help")
menu.add_cascade(label="도움말", menu=menu_help)

# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 본문 영역

# 스크롤바 연동
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=txt.yview)


root.config(menu=menu)

root.mainloop()