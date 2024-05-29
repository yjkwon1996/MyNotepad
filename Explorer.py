import os
import os.path
from tkinter import *

def clickListBox(evt) :
    global currentDir, searchDirList
    if (dirListBox.curselection() == ()) : # 다른 리스트박스 클릭은 무시
        return
    dirName = str(dirListBox.get(dirListBox.curselection())) # 클릭한 폴더 이름
    if dirName == "상위폴더" :
        if len(searchDirList) == 1 : # 최상위 폴더인 경우 무시
            return
        searchDirList.pop() # 상위 폴더 이름이므로 현재 폴더 제거
    else :
        searchDirList.append(currentDir+dirName+'\\') # 검색 리스트에 클릭한 폴더 추가

    fillListBox()

def fillListBox() : # 항상 현재폴더 표시
    global currentDir, searchDirList, dirLabel, dirListBox, fileListBox
    dirListBox.delete(0, END) # 폴더 리스트박스 비우기
    fileListBox.delete(0, END) # 파일 리스트박스 비우기

    dirListBox.insert(END, "상위폴더")
    currentDir = searchDirList[len(searchDirList) - 1] # 디렉터리 리스트의 마지막이 현재폴더
    dirLabel.configure(text=currentDir) # 위쪽 글자를 현재 폴더로 변경
    folderList = os.listdir(currentDir)

    for item in folderList : # 파일은 파일 리스트 박스에, 폴더는 폴더 리스트 박스에
        if os.path.isdir(currentDir + item) :
            dirListBox.insert(END, item)
        elif os.path.isfile(currentDir + item) :
            fileListBox.insert(END, item)

window = None
searchDirList = ["C:\\"] # 검색한 폴더 목록 스택
currentDir = "C:\\"
dirLabel, dirListBox, fileListBox = None, None, None # 창에 나올 위젯 변수들


if __name__ == "__main__" :
    window = Tk()
    window.title("윈도우 탐색기")
    window.geometry("640x400")

    dirLabel = Label(window, text=currentDir) # 현재 폴더의 경로 표시
    dirLabel.pack()

    dirListBox = Listbox(window) # 왼쪽 현재 폴더의 하위 폴더 목록 표시
    dirListBox.pack(side=LEFT, fill=BOTH, expand=1)
    dirListBox.bind("<<ListBoxSelct>>", clickListBox)

    fileListBox = Listbox(window) # 왼쪽 현재 폴더의 파익목록 표시
    fileListBox.pack(side=RIGHT, fill=BOTH, expand=1)

    fillListBox() # 초기에는 최상위

    window.mainloop()





