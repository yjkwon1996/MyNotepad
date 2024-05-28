import os
from tkinter import * # Tk GUI 툴킷에 대한 파이썬 바인딩

root = Tk()
root.title("Notepad 타이틀명")
root.geometry("640x480")
# root.geometry("640x480+100+300") # 프레임 위치 가로x세로 + x좌표+y좌표
# root.resizable(False, False) # x(너비)y(높이)값 변경 불가

# 열기, 저장 파일 이름
filename="test.txt"

def open_file() :
    if os.path.isfile(filename) : # 파일 존재 여부 확인
        with open(filename, "r", encoding="utf-8") as file :
            txt.delete("1.0", END) # 기존에 열려 있는 내용 삭제
            txt.insert(END, file.read()) # filename에 저장된 내용 읽어오기

def save_file() :
    with open(filename, "w", encoding="utf-8") as file :
        file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장



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