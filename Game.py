import pgzrun

WIDTH = 870
HEIGHT = 650

TITLE = "HARDEST QUIZ EVER"
marquee_box=Rect(0,0,880,80)
question_box=Rect(0,0,650,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
skip_box = Rect(0,0,150,330)
timer_box = Rect(0,0,150,150)
score_box = Rect(0,0,150,50)

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)
timer_box.move_ip(700,100)
score_box.move_ip(700,50)




#game variables
score = 0
time_left = 10
marquee_msg = ""
is_game_over = False

ans_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]
questions = []
question_count = 0
question_index = 0

def draw():
    global marquee_msg
    screen.clear()
    screen.fill("#00303d")
    screen.draw.filled_rect(marquee_box,"#00303d")
    screen.draw.filled_rect(question_box,"#000814")
    screen.draw.filled_rect(timer_box,"#03045e")
    screen.draw.filled_rect(score_box,"#03045e")
    screen.draw.filled_rect(skip_box,"#adb5bd")
    for answer_box in ans_boxes:
        screen.draw.filled_rect(answer_box,"#740000")
    screen.draw.textbox(marquee_msg,marquee_box,color = "#ffe169")
    screen.draw.textbox(str(time_left),timer_box,color = "#ffd81a",shadow = (0.5,0.5),scolor ="#2f3037")
    screen.draw.textbox(f"score:{score}",score_box,color = "#ffd81a")
    screen.draw.textbox("SKIP",skip_box,color ="#7a9e9f",angle = -90)
    screen.draw.textbox("hello people",question_box,color = "#de6d17", shadow  = (0.5,0.5),scolor = "#6e370c")

    

def update():
    pass

















pgzrun.go()