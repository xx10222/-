import random
import turtle as t
import time
import pygame
pygame.init()

burger = 0
point = 100
an = True
i=0
j=0

h=t.Turtle() #힌트 출력 거북이
m=t.Turtle() #메뉴 출력 거북이
y=t.Turtle() #완성여부 출력 거북이
p=t.Turtle() #점수 출력 거북이

burger_list = ['빅맥', '1955','슈슈버거','슈비버거','치즈버거','불고기버거',]
빅맥_list=['1','2','2','4','5','6','7','1', 8]
맥1955_list=['1','7','6','8','2','5','1', 7]
슈슈버거_list=['1','3','3','4','5','1', 6]
슈비버거_list=['1','3','2','4','5','1', 6]
불고기버거_list=['1','2','5','1', 4]
치즈버거_list=['1','6','2','4','1', 5]
ac_list=[빅맥_list, 맥1955_list, 슈슈버거_list, 슈비버거_list, 치즈버거_list, 불고기버거_list]

def mainstart():
    global point
    point =100
    y.pencolor('Brown')
    y.up()
    y.goto(0, 200)
    y.down()
    y.write("@씐나는 버거 쌓기!!@", False, "center", ("", 30))
    if an == True:
        y.up()
        y.goto(0, 150)
        y.down()
        y.write("시작하려면 A를 눌러주세요", False, "center", ("", 20))
    else:
        y.up()
        y.goto(0, 150)
        y.down()
        y.write("다시 시작하려면 A를눌러주세요", False, "center", ("", 20))


def pointprint():
    p.clear()
    p.up()
    p.goto(250, 230)
    p.down()
    p.write("score : "+str(point), False, "left", ("", 15))

def menu():
    m.up()
    m.goto(-320,230)
    m.down()
    m.write("주문서 : "+str(burger_list[burger]), False, "left", ("",20))

def y_move():
    y.up()
    y.goto(-320, 150)
    y.down()

def false():
    global point, an
    y_move()
    y.write("주문이 틀렸습니다.", False, "left", ("",20))
    y.clear()
    point -= 10
    if point <= 0:
        an = False
        pointprint()
        t.clear()
        m.clear()
        mainstart()
    else:
        fail()

def t_move():
    global i
    t.up()
    t.goto(-25,t.ycor()+30)
    i += 1
    
def start():
    t.up()
    y.clear()
    t.goto(-25, -200)
    global burger, i
    i=0
    burger = random.randint(0, 5)
    print("(띵똥)")
    print("점원 : 안녕하세요! 주문을 하시겠습니까?")
    print("손님 : "+str(burger_list[burger])+"하나 주문할게요")
    print("네, 잠시만 기다려 주세요!")
    print("(버거가 완성이 되면 space바를 눌러 주세요!)")
    pointprint()
    m.clear()
    menu()

def num1():
    t.down()
    t.pencolor('#ad7058')
    t.forward(100)
    global i
    if ac_list[burger][i] == '1':
       t_move()
    else:
       false()
    
def num2():
    t.down()
    t.pencolor('#794d49')
    t.forward(100)
    global i
    if ac_list[burger][i] == '2':
        t_move()
    else:
        false()

def num3():
    t.down()
    t.pencolor('#e5ab94')
    t.forward(100)
    global i
    if ac_list[burger][i] == '3':
        t_move()
    else:
        false()

def num4():
    t.down()
    t.pencolor('darkred')
    t.forward(100)
    global i
    if ac_list[burger][i] == '4':
        t_move()
    else:
        false()
        
def num5():
    t.down()
    t.pencolor('green')
    t.forward(100)
    global i
    if ac_list[burger][i] == '5':
        t_move()
    else:
        false()
    
def num6():
    t.down()
    t.pencolor('yellow')
    t.forward(100)
    global i
    if ac_list[burger][i] == '6':
        t_move()
    else:
        false()

def num7():
    t.down()
    t.pencolor('#8788c5')
    t.forward(100)
    global i
    if ac_list[burger][i] == '7':
        t_move()
    else:
        false()

def num8():
    t.down()
    t.pencolor('red')
    t.forward(100)
    global i
    if ac_list[burger][i] == '8':
        t_move()
    else:
        false()
    
def success():
    if i != ac_list[burger][-1]:
        y_move()
        y.write("아직 완성되지 않았어요!!", False, "left", ("",15))
        t.ontimer(y.clear, 1000)
    else:
        global point
        y_move()
        y.write("완성!\n맛있게 드세요!!", False, "left", ("", 20))
        pygame.mixer.music.load('clap.ogg')
        pygame.mixer.music.play(0)
        t.ontimer(y.clear, 600)
        point += 20
        pointprint()
        t.clear()
        t.home()
        start()

def fail():
    y_move()
    y.write("실패!\n손님이 떠나갔어요ㅠㅠ!!", False, "left", ("", 20))
    t.ontimer(y.clear, 1000)
    pointprint()
    t.clear()
    start()
        
def hint():
    global j
    if j<1:
         h.up()
         h.goto(-320, 40)
         h.down()
         h.write("빅맥 : 빵 패티x2 소스 양상추 치즈 양파 빵\n치즈버거 : 빵 치즈 패티 소스 빵\n불고기버거 : 빵 패티 양상추 빵\n슈슈버거 : 빵 새우 새우 소스 양상추 빵\n슈비버거 : 빵 새우 패티 소스 양상추 빵\n"
                 "1955 : 빵 양파 치즈 토마토 패티 양상추 빵\n\n"
                 "1 : 빵 2: 패티 3: 새우 4.소스 5: 양상추\n6: 치즈 7:양파 8: 토마토", False, "left", ("", 15))
         t.ontimer(h.clear, 1000)
         j+=1
    else:
         h.up()
         h.goto(-320, 40)
         h.down()
         h.write("■■■■힌트는한번만가능합니다■■■■\n■■■■■■■■■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■■■■■■■■■\n"
                 "■■■■■■■■■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■■■■■■■■■\n■■■■■■■■■■■■■■■■■■■■■■\n"
                 "■■■■■■■■■■■■■■■■■■■■■■", False, "left", ("",15))
         t.ontimer(h.clear, 1000)

    
    

print("영업을 시작합니다.")
print("----------------------------[MENU]----------------------------\n\n빅맥 : 빵 패티 패티 소스 양상추 치즈 양파 빵\n\n치즈버거 : 빵 치즈 패티 소스 빵\n\n"
      "불고기버거 : 빵 패티 양상추 빵\n\n슈슈버거 : 빵 새우 새우 소스 양상추 빵\n\n슈비버거 : 빵 새우 패티 소스 양상추 빵\n\n"
      "1955 : 빵 양파 치즈 토마토 패티 양상추 빵\n\n---------------------------------------------------------------\n\n"
      "[버거 제조하는 법]\n"
      "1=빵, 2=패티, 3=새우, 4=소스, 5=양상추, 6=치즈, 7=양파, 8=토마토\n(메뉴 순서대로 번호를 입력하세요)\n")

wn=t.Screen()
wn.bgpic("background.png")
wn.setup(800,650)

t.ht()
y.ht()
h.ht()
m.ht()
p.ht()

t.pensize(25)
t.speed(0)

mainstart()

t.onkeypress(start, "a")
t.onkeypress(num1, "1")
t.onkeypress(num2, "2")
t.onkeypress(num3, "3")
t.onkeypress(num4, "4")
t.onkeypress(num5, "5")
t.onkeypress(num6, "6")
t.onkeypress(num7, "7")
t.onkeypress(num8, "8")
t.onkeypress(success, "space")
t.onkeypress(hint, "0")
t.listen()
