from turtle import Turtle, Screen
from random import randint
import time 

Terrain = Screen()
Terrain.bgpic('Terrain.png')
Terrain.addshape('Player.gif')
Terrain.addshape('Coin.gif')
Terrain.addshape('Enemy.gif')
Terrain.screensize(canvheight=480, canvwidth=640, bg='black')
Terrain.cv._rootwindow.resizable(False, False)

Enemy = Turtle()
Enemy.penup()
Enemy.shape('Enemy.gif')
Enemy.setposition(-303, -223)
Enemy.xspeed = 5
Enemy.yspeed = 5

Enemy1 = Turtle()
Enemy1.penup()
Enemy1.shape('Enemy.gif')
Enemy1.setposition(303, 223)
Enemy1.xspeed = -5
Enemy1.yspeed = -5


Coin = Turtle()
Coin.penup()
Coin.shape('Coin.gif')
Coin.speed(100)
Coin.setposition(100, 100)

Player = Turtle()
Player.penup()
Player.shape('Player.gif')

Font = ('Small Fonts', 48)
Timer = Turtle(visible=False)
Timer.penup()
Timer.setposition(-10, 240)
Timer_ = 0
Timer.color('white')
Timer.write(Timer_, font=Font )

Font = ('Small Fonts', 48)
text = Turtle(visible=False)
text.penup()
text.setposition(-100, 320)
text_ = 'you died'
text.color('red')

Font = ('Small Fonts', 48)
text1 = Turtle(visible=False)
text1.penup()
text1.setposition(-100, 320)
text1_ = 'Victory'
text1.color('yellow')

def move_up():
    Player.sety(Player.ycor() + 25)
def move_down():
    Player.sety(Player.ycor() - 25)    
def move_right():
    Player.setx(Player.xcor() + 25)  
def move_left():
    Player.setx(Player.xcor() - 25)       

Terrain.listen()
Terrain.onkeypress(move_up, "w")
Terrain.onkeypress(move_down, "s")
Terrain.onkeypress(move_right, "d")
Terrain.onkeypress(move_left, "a")

while True:
    Terrain.update()

    Enemy.setx(Enemy.xcor() + Enemy.xspeed)
    Enemy.sety(Enemy.ycor() + Enemy.yspeed)
    Enemy1.setx(Enemy1.xcor() + Enemy1.xspeed)
    Enemy1.sety(Enemy1.ycor() + Enemy1.yspeed)

    if Enemy.xcor() >= 303:
        Enemy.xspeed *= -1
    if Enemy.ycor() >= 223:
        Enemy.yspeed *= -1  
    if Enemy.xcor() <= -303:
        Enemy.xspeed *= -1
    if Enemy.ycor() <= -223:
        Enemy.yspeed *= -1  

    if Enemy1.xcor() >= 303:
        Enemy1.xspeed *= -1
    if Enemy1.ycor() >= 223:
        Enemy1.yspeed *= -1  
    if Enemy1.xcor() <= -303:
        Enemy1.xspeed *= -1
    if Enemy1.ycor() <= -223:
        Enemy1.yspeed *= -1          

    if Player.xcor() >= Coin.xcor() - 25 and Player.xcor() \
        <= Coin.xcor() + 25 and Player.ycor() >= Coin.ycor() - 25 \
        and Player.ycor() <= Coin.ycor() + 25:
        Coin.setposition(randint(-200, 200), randint(-200 , 200))
        Timer_ += 5
        Timer.clear()
        Timer.write(Timer_, font=Font)
        
    if Player.xcor() >= Enemy.xcor() - 25 and Player.xcor() \
        <= Enemy.xcor() + 25 and Player.ycor() >= Enemy.ycor() - 25 \
        and Player.ycor() <= Enemy.ycor() + 25:
        Player.setposition(randint(-200, 200), randint(-200 , 200))
        Timer_ -= 5
        Timer.clear()
        Timer.write(Timer_, font=Font)

    if Player.xcor() >= Enemy1.xcor() - 25 and Player.xcor() \
        <= Enemy1.xcor() + 25 and Player.ycor() >= Enemy1.ycor() - 25 \
        and Player.ycor() <= Enemy1.ycor() + 25:
        Player.setposition(randint(-200, 200), randint(-200 , 200))
        Timer_ -= 5
        Timer.clear()
        Timer.write(Timer_, font=Font)
        
    if Timer_<0:
        text.write(text_, font=Font )
        time.sleep(3)
        break   
    if Timer_>10:
        text1.write(text1_, font=Font )
        time.sleep(3)
        break 
        
    

        

    



    

   

    


            





