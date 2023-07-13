import time
import pygame as pg
import random as rdm
import sys

# プレイヤーパラメータ(最低保証分)
p_Status = [100, 15, 0, 0]
S_disp = ["HP", "ATK", "MP", "DEF"]
# 進行用フラグ
flg = 0
# ターン用フラグ
turn_flg = rdm.randint(0,1)
# パラメータ格納用変数
param = 0

# コマンド格納用変数
cmd = ""

# 魔王のコマンド
ENM_cmd = ["こうげき", "メラ", "ヒャド", "ドルマ"]
# 魔王パラメータ
ENM_S = [100, 35, 100, 20]

print("-------RPGゲームスタート-------")
print("<ルール>")
print("・最初の３ステージで右、左を選んで進んでください。")
print("・進むごとにパラメータを獲得していきます。")
print("・ランダムにパラメータを自分のステータスに割り振られて行きます。(運ゲー)")
print("・ラストの魔王戦でコマンドを駆使して戦います。")
print("・救済措置も準備されております。(隠しコマンド)")
print("※すべての要素に運要素が絡んでいます。")


print("Roading...")
time.sleep(4)

def gameover():
    print("LOSE.....")
    print(p_name + "さん。魔王の勝ちです...")
    sys.exit()
    
def gameclear():
    print("YOU WIN !!!")
    print("見事魔王を討ちました！！")
    sys.exit()
    
    
    
def Boss():
    global turn_flg, cmd
    print(p_name + "のステータス\nHP:" + str(p_Status[0]) + "\nATK:" + str(p_Status[1]) + "\nMP:" + str(p_Status[2]) + "\nDEF:" + str(p_Status[3]))
    print("----魔王のターン---")
    time.sleep(3)
    #print("bossHP" + str(ENM_S[0]))
    cmd = ENM_cmd[rdm.randint(0,3)]
    time.sleep(1)
    
    # こうげき
    if cmd == "こうげき":
        print("魔王のこうげき！！")
        time.sleep(1)
        if p_Status[3] > ENM_S[1]:
            burst = rdm.randint(0,100)
            if burst <= 5:
                dmg = (ENM_S[1] * 2) - p_Status[3]
                p_Status[0] -= dmg
                print("かいしんのいちげき！！")
                print(p_name + "は" + str(dmg) + "食らった！")
            else:
                dmg = ENM_S[1] - p_Status[3]
                p_Status[0] -= dmg
                print(p_name + "は" + str(dmg) + "食らった！")
                
        else:
            print("ぼうぎょが固すぎて効かないようだ...")
            dmg = 0
        
        turn_flg = 1
    
    # メラ
    elif cmd == "メラ":
        print("魔王のメラ！!")
        time.sleep(2)
        if ENM_S[2] >= 5:
            ENM_S[2] -= 5
            burst = rdm.randint(0,100)
            if burst <= 5:
                p_Status[0] -= 20
                print("メラが暴発した！！")
                print(p_name + "は20食らった！")
            else:
                p_Status[0] -= 10
                print(p_name + "は10食らった！")
        else:
            print("しかしMPが足りず不発になった")  
        time.sleep(2)  
        turn_flg = 1    
    
    # ヒャド    
    elif cmd == "ヒャド":
        print("魔王のヒャド！!")
        time.sleep(2)
        
        if ENM_S[2] >= 10:
            ENM_S[2] -= 10
            
            burst = rdm.randint(0,100)
            if burst <= 5:
                p_Status[0] -= 30
                print("ヒャドが暴発した！！")
                print(p_name + "は30食らった！")
            else:
                p_Status[0] -= 15
                print(p_name + "は15食らった！")            
        else:
            print("しかしMPが足りず不発になった")  
        time.sleep(2) 
        turn_flg = 1     
    
    # ドルマ            
    elif cmd == "ドルマ":
        print("魔王のドルマ！!")
        time.sleep(2)
        if ENM_S[2] >= 15:
            ENM_S[2] -= 15
            burst = rdm.randint(0,100)
            if burst <= 5:
                p_Status[0] -= 35
                print("ドルマが暴発した！！")
                print(p_name + "は35食らった！")
            else:
                p_Status[0] -= 15
                print(p_name + "は15食らった！")       
        else:
            print("しかしMPが足りず不発になった")  
        time.sleep(2)
        turn_flg = 1  
        
def Player():
    global cmd, turn_flg
    print(p_name + "のステータス\nHP:" + str(p_Status[0]) + "\nATK:" + str(p_Status[1]) + "\nMP:" + str(p_Status[2]) + "\nDEF:" + str(p_Status[3]))
    cmd = input("あなたのターンです。コマンドを入力してください。(コマンド:こうげき:0,メラ:1,デイン:2):")
    
    if cmd.isdecimal() and len(cmd) == 1:
        cmd = int(cmd)
        
        if cmd > 3 or cmd == "":
            print("正しいコマンドが入力されなかったため、こうげきを行います。")
            cmd = 0
        
        # 救済措置（これも運絡み）
        if cmd == 3:
            print("隠しコマンドが入力されました。どれかのパラメータが加算されます。")
            p_Status[rdm.randint(0,3)] = rdm.randint(0,30)
            turn_flg = 0
    else:
        print("正しいコマンドが入力されなかったため、こうげきを行います。")
        cmd = 0
    
    time.sleep(2)
    
    # こうげき    
    if cmd == 0:
        print(p_name + "のこうげき！！")
        time.sleep(2)
        
        if p_Status[1] > ENM_S[3]:
            dmg = p_Status[1] - ENM_S[3]
            burst = rdm.randint(0,100)
            if burst <= 5:# 5%でかいしん
                dmg = (p_Status[1] * 2) - ENM_S[3] 
                ENM_S[0] -= dmg
                print("かいしんのいちげき！！")
                print("魔王は" + str(dmg) + "食らった！")
            else:
                dmg = p_Status[1] - ENM_S[3]
                ENM_S[0] -= dmg
                print("魔王は" + str(dmg) + "食らった！")
        else:
            dmg = 0
            print("魔王の防御力が攻撃を上回っているようだ...")
                
        
        time.sleep(2)
        turn_flg = 0
    
    # メラ
    elif cmd == 1:
        print(p_name + "のメラ！!")
        time.sleep(2)
        if p_Status[2] >= 5:# 5%で暴発
            p_Status[2] -= 5
            burst = rdm.randint(0,100)
            if burst <= 5:
                ENM_S[0] -= 20
                print("メラが暴発した！！")
                print("魔王は20食らった！")
            else:
                ENM_S[0] -= 10
                print("魔王は10食らった！")
        else:
            print("しかしMPが足りず不発になった")
        time.sleep(2)    
        turn_flg = 0    
    
    # デイン    
    elif cmd == 2:
        print(p_name + "のデイン！!")
        time.sleep(2)
        if p_Status[2] >= 10:
            p_Status[2] -= 10
            burst = rdm.randint(0,100)
            if burst <= 5:
                ENM_S[0] -= 35
                print("デインが暴発した！！")
                print("魔王は20食らった！")
            else:
                ENM_S[0] -= 15
                print("魔王は10食らった！")        
        else:# MPが足りない場合
            print("しかしMPが足りず不発になった")  
        time.sleep(2) 
        turn_flg = 0
        
            
# メインループ
while True:
    # 魔王戦
    if flg == 6:
        if ENM_S[0] <= 0:
            gameclear()
        
        if turn_flg == 0:
            Boss()
        else:
            Player()
    
    if flg == 5:
        print("------魔王戦開始------")
        flg += 1 
                 
    if flg == 0:
        # プレイヤーの名前入力
        p_name = input("あなたの名前は？:")
        
        # 空白が入力された場合
        if p_name.isspace():
            print("空白で入力されましたので、あなたの名前は”くうはく”になります。")
            p_name = "くうはく"        
        
        if not p_name :
            print("空欄になっています。1文字以上は入力してください")
            continue


        time.sleep(1)
        print(p_name + "さん!ようこそRPGの世界へ!")
        time.sleep(1)
        
        flg += 1

        
    # ステータス準備   
    if flg >= 1 and flg < 5:
        
        # ステータス表示
        print(p_name + "のステータス\nHP:" + str(p_Status[0]) + "\nATK:" + str(p_Status[1]) + "\nMP:" + str(p_Status[2]) + "\nDEF:" + str(p_Status[3]))
        sec = input("どちらの道に進みますか？(1:右, 2:左)")
        
        # 文字列判定
        if sec.isdecimal() and len(sec) == 1:
            sec = int(sec)
        else:
            print("文字列または長すぎる文字が入力されています。")
            continue
            
        
        if sec == 0 or sec > 2:
            print("正しく入力してください。")
            continue
            
        # 道中のログ
        if sec == 1:
            print("右へ進みます。")
        else:
            print("左へ進みます。")
        
        param = rdm.randint(0,3)
        tmp = rdm.randint(5,100)
        
        time.sleep(1)
        
        print("パラメータを" + str(tmp) + "獲得！！")
        
        # パラメータ（乱数）足していく
        p_Status[param] += tmp
        
        time.sleep(1)
        print(S_disp[param] + "が" + str(p_Status[param]) + "になった！！")
        time.sleep(1)
        
        flg += 1# 道中のフラグ
    
        
    
    