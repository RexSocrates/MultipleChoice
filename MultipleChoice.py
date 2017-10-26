import sys
import codecs
import random

def main():
    txt = input("請輸入檔案名稱(ex: ch1.txt):")
    f = codecs.open(txt,'r','utf-8')
    total = 0
    Ans = []
    Question = []
    checkAns = []
    findAns = False
    findQuestion = False
    findNum = False
    findOptions = False
    countFalse = 0
    integrity = 0
    questionTemp = None
    
    while total == 0:
        line = f.readline()
        if line.find("Total") == 0 :
            total = int(line[7:])
        else:
            countFalse += 1
        if countFalse > 10:
            sys.exit("沒找到Total")
            
    countFalse = 0
    Options = [[] for i in range(total)]
    optionAmount = [[] for i in range(total)]
    optionsCheck = [[] for i in range(total)]
    
    while findAns == False:
        line = f.readline()
        if line.find("Ans") == 0 :
            findAns = True
            time = int(total/5)
            lastAnsCount = total % 5
            if lastAnsCount != 0 :
                for i in range(time):
                    line = f.readline()
                    for j in range(5):
                        Ans.append(line[j*2:j*2+1])
                        j += 1
                line = f.readline()
                for k in range(lastAnsCount):
                    Ans.append(line[k*2:k*2+1])
                    k += 1
                print()
            else:
                for i in range(time):
                    line = f.readline()
                    for j in range(5):
                        Ans.append(line[j*2:j*2+1])
                        j += 1
        else:
            countFalse += 1
        if countFalse > 10:
            sys.exit("沒找到ans")
    
    for i in range(total):
        if Ans[i] != "a" and Ans[i] != "b" and Ans[i] != "c" and Ans[i] != "d" and Ans[i] != "e" and Ans[i] != "A" and Ans[i] != "B" and Ans[i] != "C" and Ans[i] != "D" and Ans[i] != "E":
            sys.exit("Ans不完整")
        if Ans[i] == "a":
            Ans[i] = 1
        elif Ans[i] == "b":
            Ans[i] = 2
        elif Ans[i] == "c":
            Ans[i] = 3
        elif Ans[i] == "d":
            Ans[i] = 4
        elif Ans[i] == "e":
            Ans[i] = 5
        elif Ans[i] == "A":
            Ans[i] = 1
        elif Ans[i] == "B":
            Ans[i] = 2
        elif Ans[i] == "C":
            Ans[i] = 3
        elif Ans[i] == "D":
            Ans[i] = 4
        elif Ans[i] == "E":
            Ans[i] = 5
        else:
            print("Answer換成數字出錯")
        
    countFalse = 0
    while findQuestion == False:
        line = f.readline()
        if line.find("Question") == 0:
            findQuestion = True
        else:
            countFalse += 1
        if countFalse > 10:
            sys.exit("沒找到question")
            
    countFalse = 0
    for i in range(1,total+1):
        while findNum == False:         
            if questionTemp == None:
                line = f.readline()
            else:
                line = questionTemp
            if line.find(str(i)+".") == 0 or line.find(str(i)+".") == 1 or line.find(str(i)+".") == 2 or line.find(str(i)+")") == 0 or line.find(str(i)+")") == 1 or line.find(str(i)+")") == 2:
                Question.append(line)
                findNum = True
                countFalse = 0
                countOptions = 0
                while findOptions == False:
                    if line.find("a.") == 0 or line.find("b.") == 0 or line.find("c.") == 0 or line.find("d.") == 0 or line.find("e.") == 0 or line.find("A.") == 0 or line.find("B.") == 0 or line.find("C.") == 0 or line.find("D.") == 0 or line.find("E.") == 0 or line.find("a.") == 1 or line.find("b.") == 1 or line.find("c.") == 1 or line.find("d.") == 1 or line.find("e.") == 1 or line.find("A.") == 1 or line.find("B.") == 1 or line.find("C.") == 1 or line.find("D.") == 1 or line.find("E.") == 1 or line.find("a.") == 2 or line.find("b.") == 2 or line.find("c.") == 2 or line.find("d.") == 2 or line.find("e.") == 2 or line.find("A.") == 2 or line.find("B.") == 2 or line.find("C.") == 2 or line.find("D.") == 2 or line.find("E.") == 2:
                        if line.find("a.") == 0 or line.find("A.") == 0 or line.find("a.") == 1 or line.find("A.") == 1 or line.find("a.") == 2 or line.find("A.") == 2:
                            optionAmount[i-1] = 1
                            countOptions += 1
                            optionsCheck[i-1] = countOptions
                        elif line.find("b.") == 0 or line.find("B.") == 0 or line.find("b.") == 1 or line.find("B.") == 1 or line.find("b.") == 2 or line.find("B.") == 2:
                            optionAmount[i-1] = 2
                            countOptions += 1
                            optionsCheck[i-1] = countOptions
                        elif line.find("c.") == 0 or line.find("C.") == 0 or line.find("c.") == 1 or line.find("C.") == 1 or line.find("c.") == 2 or line.find("C.") == 2:
                            optionAmount[i-1] = 3
                            countOptions += 1
                            optionsCheck[i-1] = countOptions
                        elif line.find("d.") == 0 or line.find("D.") == 0 or line.find("d.") == 1 or line.find("D.") == 1 or line.find("d.") == 2 or line.find("D.") == 2:
                            optionAmount[i-1] = 4
                            countOptions += 1
                            optionsCheck[i-1] = countOptions
                        elif line.find("e.") == 0 or line.find("E.") == 0 or line.find("e.") == 1 or line.find("E.") == 1 or line.find("e.") == 2 or line.find("E.") == 2:
                            optionAmount[i-1] = 5
                            countOptions += 1
                            optionsCheck[i-1] = countOptions
                        else:
                            print("選項錯誤")
                        
                        if len(line) < 5:
                            line = f.readline()
                            Options[i-1].append(line)
                        else:
                            Options[i-1].append(line)
                            line = f.readline()
                        countFalse = 0
                    elif line.find("a)") == 0 or line.find("b)") == 0 or line.find("c)") == 0 or line.find("d)") == 0 or line.find("e)") == 0 or line.find("A)") == 0 or line.find("B)") == 0 or line.find("C)") == 0 or line.find("D)") == 0 or line.find("E)") == 0 or line.find("a)") == 1 or line.find("b)") == 1 or line.find("c)") == 1 or line.find("d)") == 1 or line.find("e)") == 1 or line.find("A)") == 1 or line.find("B)") == 1 or line.find("C)") == 1 or line.find("D)") == 1 or line.find("E)") == 1 or line.find("a)") == 2 or line.find("b)") == 2 or line.find("c)") == 2 or line.find("d)") == 2 or line.find("e)") == 2 or line.find("A)") == 2 or line.find("B)") == 2 or line.find("C)") == 2 or line.find("D)") == 2 or line.find("E)") == 2:
                        if line.find("a)") == 0 or line.find("A)") == 0 or line.find("a)") == 1 or line.find("A)") == 1 or line.find("a)") == 2 or line.find("A)") == 2:
                            optionAmount[i-1] = 1
                            countOptions += 1
                            optionsCheck[i-1] = countOptions
                        elif line.find("b)") == 0 or line.find("B)") == 0 or line.find("b)") == 1 or line.find("B)") == 1 or line.find("b)") == 2 or line.find("B)") == 2:
                            optionAmount[i-1] = 2
                            countOptions += 1
                            optionsCheck[i-1] = countOptions
                        elif line.find("c)") == 0 or line.find("C)") == 0 or line.find("c)") == 1 or line.find("C)") == 1 or line.find("c)") == 2 or line.find("C)") == 2:
                            optionAmount[i-1] = 3
                            countOptions += 1
                            optionsCheck[i-1] = countOptions
                        elif line.find("d)") == 0 or line.find("D)") == 0 or line.find("d)") == 1 or line.find("D)") == 1 or line.find("d)") == 2 or line.find("D)") == 2:
                            optionAmount[i-1] = 4
                            countOptions += 1
                            optionsCheck[i-1] = countOptions
                        elif line.find("e)") == 0 or line.find("E)") == 0 or line.find("e)") == 1 or line.find("E)") == 1 or line.find("e)") == 2 or line.find("E)") == 2:
                            optionAmount[i-1] = 5
                            countOptions += 1
                            optionsCheck[i-1] = countOptions
                        else:
                            print("選項錯誤")
                        
                        if len(line) < 5:
                            line = f.readline()
                            Options[i-1].append(line)
                        else:
                            Options[i-1].append(line)
                            line = f.readline()
                        countFalse = 0
                    elif line.find("(a)") == 0 or line.find("(b)") == 0 or line.find("(c)") == 0 or line.find("(d)") == 0 or line.find("(e)") == 0 or line.find("(A)") == 0 or line.find("(B)") == 0 or line.find("(C)") == 0 or line.find("(D)") == 0 or line.find("(E)") == 0 or line.find("(a)") == 1 or line.find("(b)") == 1 or line.find("(c)") == 1 or line.find("(d)") == 1 or line.find("(e)") == 1 or line.find("(A)") == 1 or line.find("(B)") == 1 or line.find("(C)") == 1 or line.find("(D)") == 1 or line.find("(E)") == 1 or line.find("(a)") == 2 or line.find("(b)") == 2 or line.find("(c)") == 2 or line.find("(d)") == 2 or line.find("(e)") == 2 or line.find("(A)") == 2 or line.find("(B)") == 2 or line.find("(C)") == 2 or line.find("(D)") == 2 or line.find("(E)") == 2:
                        
                        if line.find("(a)") == 0 or line.find("(A)") == 0 or line.find("(a)") == 1 or line.find("(A)") == 1 or line.find("(a)") == 2 or line.find("(A)") == 2: 
                            optionAmount[i-1] = 1
                            countOptions += 1
                            optionsCheck[i-1] = countOptions
                        elif line.find("(b)") == 0 or line.find("(B)") == 0 or line.find("(b)") == 1 or line.find("(B)") == 1 or line.find("(b)") == 2 or line.find("(B)") == 2:
                            optionAmount[i-1] = 2
                            countOptions += 1
                            optionsCheck[i-1] = countOptions
                        elif line.find("(c)") == 0 or line.find("(C)") == 0 or line.find("(c)") == 1 or line.find("(C)") == 1 or line.find("(c)") == 2 or line.find("(C)") == 2:
                            optionAmount[i-1] = 3
                            countOptions += 1
                            optionsCheck[i-1] = countOptions
                        elif line.find("(d)") == 0 or line.find("(D)") == 0 or line.find("(d)") == 1 or line.find("(D)") == 1 or line.find("(d)") == 2 or line.find("(D)") == 2:
                            optionAmount[i-1] = 4
                            countOptions += 1
                            optionsCheck[i-1] = countOptions
                        elif line.find("(e)") == 0 or line.find("(E)") == 0 or line.find("(e)") == 1 or line.find("(E)") == 1 or line.find("(e)") == 2 or line.find("(E)") == 2:
                            optionAmount[i-1] = 5
                            countOptions += 1
                            optionsCheck[i-1] = countOptions
                        else:
                            print("選項錯誤")
                        if len(line) < 5:
                            line = f.readline()
                            Options[i-1].append(line)
                        else:
                            Options[i-1].append(line)
                            line = f.readline()
                        countFalse = 0
                    elif line.find(str(i+1)+".") == 0 or line.find(str(i+1)+".") == 1 or line.find(str(i+1)+".") == 2 or line.find(str(i+1)+")") == 0 or line.find(str(i+1)+")") == 1 or line.find(str(i+1)+")") == 2:
                        questionTemp = line
                        findOptions = True
                        countFalse = 0
                    else:
                        line = f.readline()
                        countFalse += 1
                        if countFalse > 30:
                            findOptions = True
                countFalse = 0
                countOptions = 0
                findOptions = False
            else :
                countFalse += 1
                if countFalse > 150:
                    findNum = True
                    sys.exit("第"+str(i-1)+"題找不到題目(大約)")
        countFalse = 0
        findNum = False
    
    for i in range(total):
        if len(Question) != total and len(Options[i]) != optionAmount[i]:
            sys.exit("------不完整, 請去修改txt檔------")
        elif optionAmount[i] != optionsCheck[i]:
            sys.exit("------第"+str(i+1)+"題的題目有問題, 請去修改txt檔------")

    print("---------------------檔案檢查完成---------------------\n")
    
    choose = "null"
    while choose != 0:
        print("按 1 開始做題目")
        print("按 2 開始做[隨機]題目")
        print("按 3 顯示-文字檔-所有的資訊(包含:總題數, 答案, 所有問題) -測試用-")
        print("按 0 離開")
        choose = "null"
        while str(choose).isdigit() != True:
            choose = str(input("輸入選項:"))
            if choose.isdigit():
                choose = int(choose)
                if choose > 3:
                    print("你的選項並不在範圍裡，請重新輸入", end=" ")
                    choose = "null"
            else:
                print("你的選項並不是數字，請重新輸入", end=" ")
        
        if choose == 1:
            print("======================= 開始作答 =======================")
            for i in range(total):
                print(Question[i])
                print()
                for j in range(optionAmount[i]):
                    print(j+1,end=")")
                    print(Options[i][j])
                
                yourAns = "null"
                while str(yourAns).isdigit() != True:
                    yourAns = str(input("你的答案:"))
                    if yourAns.isdigit():
                        yourAns = int(yourAns)
                        if yourAns > optionAmount[i] or yourAns == 0:
                            print("你的答案並不在範圍裡，請重新輸入", end=" ")
                            yourAns = "null"
                    else:
                        print("你的答案並不是數字，請重新輸入", end=" ")
                if yourAns == Ans[i]:
                    checkAns.append(True)
                    print("======================= 答對 =========================")
                else:
                    checkAns.append(False)
                    print("================== 錯誤，正確答案是",Ans[i],end=" ")
                    print("==================")
            right = 0
            wrong = 0
            for i in range(total):
                if checkAns[i] == True:
                    right += 1
                else:
                    wrong +=1
            percent = right / len(checkAns)
            print("總數:",total,"正確:", right,"錯誤:", wrong, "百分比:", percent * 100)
            checkAns.clear()
            print("====================== 題目結束 =======================")
            print()
        elif choose == 2:    
            print("===================== 開始[隨機]作答 =====================")
            ranQuestion = random.sample(range(total), total)
            
            for i in range(total):
                print(Question[ranQuestion[i]])
                print()
                for j in range(optionAmount[ranQuestion[i]]):
                    print(j+1,end=")")
                    print(Options[ranQuestion[i]][j])
                
                yourAns = "null"
                while str(yourAns).isdigit() != True:
                    yourAns = str(input("你的答案:"))
                    if yourAns.isdigit():
                        yourAns = int(yourAns)
                        if yourAns > optionAmount[ranQuestion[i]] or yourAns == 0:
                            print("你的答案並不在範圍裡，請重新輸入", end=" ")
                            yourAns = "null"
                    else:
                        print("你的答案並不是數字，請重新輸入", end=" ")
                if yourAns == Ans[ranQuestion[i]]:
                    checkAns.append(True)
                    print("======================= 答對 =========================")
                else:
                    checkAns.append(False)
                    print("================== 錯誤，正確答案是",Ans[ranQuestion[i]],end=" ")
                    print("==================")
            right = 0
            wrong = 0
            for i in range(total):
                if checkAns[i] == True:
                    right += 1
                else:
                    wrong += 1
            percent = right / len(checkAns)
            print("總數:",total,"正確:", right,"錯誤:", wrong, "百分比:", percent * 100)
            checkAns.clear()
            print("====================== 題目結束 =======================")
            print()
        elif choose == 3:
            print("====================== 題目資訊 =======================")
            print("Total:", total)
            print()
            print("Answer:")
            for i in range(total):
                print(Ans[i],end=" ")
                if (i+1) % 5 == 0:
                    print()
            print()
            print("\nQuestion:")
            for i in range(total):
                print(Question[i])
                for j in range(optionAmount[i]):
                    print(j+1,end=")")
                    print(Options[i][j])
                print()
            print("==================== 沒有更多的問題 ====================\n")
        elif choose == 0:
            f.close()
            sys.exit("離開")
        else:
            print("????")

if __name__ == '__main__':
    main()
