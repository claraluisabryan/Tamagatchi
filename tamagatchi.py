import turtle, random, time

# These variables store the current x and y
# position of the tamagotchi. Their values will be
# updates on each frame, as the ball moves.
tamx = 0
tamy = 0

#Gets paramaters of the window
window_width = turtle.window_width()
window_height = turtle.window_height()

# These variables store the current score 
# of the game.
game = True
lose = False
foodpoints = 0
waterpoints = 0
lovepoints = 0
seconds = 1
poopx = 50000000000
poopy = 500000000000
poops = []
golds = []
clickx = 500000000
clicky = 500000000
foodx=window_width*.3
foody=window_height*.2
waterx=window_width*.3
watery=window_height*.15
lovex=window_width*.3
lovey=window_height*.1
money=0
c_variable=0
collegex=window_width* .1
collegey=window_height*-.35
big_win = False
you_are_a_winner = False

def add_college():
   global c_variable, big_win, lose, money
   c_variable+=4
   money -=2
   if c_variable >= 150:
      lose = True
      big_win = True

def add_food():
   global foodpoints, money
   if foodpoints >= 0:
      foodpoints -=5
      money -= 2

def add_water():
   global waterpoints, money
   if waterpoints >= 0:
      waterpoints -=5
      money -=2

def add_love():
   global lovepoints, money
   if lovepoints >= 0:
      lovepoints -=5
      money -= 2
   
widget_dict = {(foodx, foody, foodx+75, foody+30): add_food, (waterx, watery, waterx +75, watery+30): add_water, (lovex, lovey, lovex+75, lovey+30): add_love, (collegex, collegey-30, collegex+50, collegey): add_college}

def start_game():
    #Starts the game by getting the pet information from the user
    global pet_name, pet_color
    turtle.bgcolor("pink")
    turtle.color("black")
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(window_width*-.4, 0)
    turtle.write("Ever wondered what it's like to be a mother? \n Here it is, the game of motherhood. \n Keep your pet fed, hydrated, and loved by clicking the respective icons. If these levels get to zero, your pet dies. \n Clean up your pet\'s poops to get money. If you leave over 6 poops unattended, your pet dies. \n If you save enough money for your kid to buy a Costco Membership by clicking the 'save $' button, you win!")
    main()    
    
        
def meter(x, variable, title):
    #handles the need meters at top left
    global foodpoints, waterpoints, lovepoints, lose, foodx, foody, waterx, watery, lovex, lovey
    turtle.goto(window_width*-.25+x, window_height*.4)
    turtle.color("white")
    turtle.write(title)
    turtle.color("purple")
    turtle.pendown()
    turtle.begin_fill()
    i=0
    while i<2:
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        i += 1
    turtle.end_fill()
    turtle.penup()
    turtle.goto(window_width*-.25+x, window_height*.4)
    turtle.color("pink")
    turtle.pendown()
    turtle.begin_fill()
    i=0
    while i<2:
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(variable)
        turtle.right(90)
        i+=1
    turtle.end_fill()
    turtle.penup()
    foodpoints += .095
    waterpoints += .1
    lovepoints += .09
    if variable >= 100:
        lose = True

def college():
   global c_variable
   turtle.goto(window_width*.2, window_height*-.35)
   turtle.setheading(0)
   i = 0
   turtle.pendown()
   turtle.color("black")
   while i < 2:
      turtle.forward(150)
      turtle.right(90)
      turtle.forward(30)
      turtle.right(90)
      i+=1
   i=0
   turtle.penup()
   turtle.goto(window_width*.2, window_height*-.35)
   turtle.pendown()
   turtle.begin_fill()
   turtle.color("goldenrod1")
   while i < 2:
      turtle.forward(c_variable)
      turtle.right(90)
      turtle.forward(30)
      turtle.right(90)
      i+=1
   turtle.end_fill()
   turtle.penup()
   turtle.goto(window_width* .1, window_height*-.35)
   i=0
   turtle.pendown()
   turtle.color("cornsilk1")
   turtle.begin_fill()
   while i < 2:
      turtle.forward(50)
      turtle.right(90)
      turtle.forward(30)
      turtle.right(90)
      i+=1
   turtle.end_fill()
   turtle.penup()
   turtle.color("black")
   turtle.goto(window_width*.11, window_height*-.385)
   turtle.write("SAVE $")
   
   

def poop():
    #Handles pet creating poop
    global poopx, poopy, lose
    if seconds % 15 == 0:
        poopx = tamx
        poopy = tamy -5
        temp = (poopx, poopy)
        poops.append(temp)
    for poop in poops:    
        turtle.goto(poop)
        turtle.pendown()
        turtle.color("brown")
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        turtle.penup()
    if len(golds)>0:
       for gold in golds:
           turtle.goto(gold[0],gold[1])
           turtle.color("darkgoldenrod1")
           turtle.begin_fill()
           turtle.circle(10)
           turtle.end_fill()
           turtle.penup()
    if len(poops) > 6:
        lose = True


def frame():
    """
    signature: () -> NoneType
    Given the current state of the game in
    the global variables, draw all visual
    elements on the screen: the paddles,
    the ball, and the current score.
    Please note that this is your only function
    where drawing should happen (i.e. the only
    function where you call functions in the
    turtle module). Other functions in this
    program merely update the state of global
    variables.
    This function also should not modify any
    global variables.
    Hint: write this function first!
    """
    global tamx, tamy, foodx, foody, waterx, watery, lovex, lovey, lose

# Panel
    turtle.bgcolor("darkslategray1")
    turtle.color("cornsilk1")
    turtle.penup()
    turtle.goto(window_width*.25, window_height*.25)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    i=0
    while i<2:
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)
        i+=1
    turtle.end_fill()
    turtle.penup()

    meter(0, foodpoints, "FOOD")
    meter(-75, waterpoints, "WATER")
    meter(-150, lovepoints, "LOVE")

# Widget Food
 
    turtle.goto(foodx, foody)
    turtle.color("darkolivegreen")
    turtle.write("FOOD")
    turtle.penup() 

#Widget Water
 
    turtle.goto(waterx, watery)
    turtle.color("darkolivegreen")
    turtle.write("WATER")
    turtle.penup()
 

#Widget Love
    turtle.goto(lovex, lovey)
    turtle.color("darkolivegreen")
    turtle.write("LOVE")
    turtle.penup()

#Money
    turtle.goto(window_width*-.4, window_height*-.4)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("gold")
    turtle.circle(20)
    turtle.end_fill()
    turtle.color("black")
    turtle.penup()
    turtle.goto(window_width*-.407, window_height*-.3985)
    turtle.write("$", font=("Arial",20, "normal"))
    turtle.penup()
    turtle.goto(window_width*-.35, window_height*-.40)
    turtle.write("=  "+str(money), font=("Arial", 25, "normal"))

    

#Pet
    if tamx>=window_width*.1:
       tamx-=random.randint(0,15)
    if tamx<=window_width*-.3:
       tamx+=random.randint(0,15)
    if tamy>=window_height*.08:
       tamy-=random.randint(0,15)
    if tamy<=window_height*-.08:
       tamy+=random.randint(0,15)
    else:
       tamx += random.randint(-30,30)
       tamy += random.randint(-30,30)
    
    turtle.penup()
    turtle.goto(window_width*.26,0)
    turtle.pendown()
    turtle.color("pink")
    turtle.write(pet_name,font = ("Arial",16, "normal"))
    turtle.up()
    turtle.goto(tamx,tamy)
    turtle.down()

    turtle.color(pet_color)
    turtle.circle(35)
    turtle.up()
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(30)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(5)
    turtle.up()
    turtle.left(80)
    turtle.forward(30)
    turtle.down()
    turtle.circle(5)
    turtle.end_fill()
    turtle.up()

    college()
    poop()

    turtle.update()
    
def ClickCheck(clickx, clicky):
   
    i=0
    x=0
    global foodx, foody, waterx, watery, lovex, lovey, foodpoints, waterpoints, lovepoints, money, golds, lose 
    for key, value in widget_dict.items():
        if key[0] < clickx < key[2] and key[1] < clicky < key[3] and money >= 2:
            value()
            
   
    for gold in golds:
       if gold[0]-20 < clickx < gold[0]+10 and gold[1]-20 < clicky < gold[1]+20:
          del golds[x]
          money += 8
       x+=1

    for poop in poops:
       if poop[0]-20 < clickx < poop[0]+10 and poop[1]-20 < clicky < poop[1]+20:
          if random.randint(0,100) % 2 == 0 or random.randint(0,100) % 3 == 0 :
             golds.append(poop)
          del poops[i]
       i+=1

def game_over():
   
   global game, lose, you_are_a_winner
   if big_win == True:
      you_are_a_winner = True
   if lose == True:
      game = False

def end_game():
    if you_are_a_winner == True:
       turtle.clear()
       turtle.penup()
       turtle.goto(0,0)
       turtle.pendown()
       turtle.write("you win. \n have fun at Costco. :)")
       turtle.color(pet_color)
       turtle.circle(35)
       turtle.up()
       turtle.forward(20)
       turtle.left(90)
       turtle.forward(30)
       turtle.down()
       turtle.begin_fill()
       turtle.write("0")
       turtle.up()
       turtle.left(80)
       turtle.forward(30)
       turtle.down()
       turtle.write("0")
       turtle.end_fill()
       turtle.up()
       
    else:
       turtle.clear()
       turtle.penup()
       turtle.goto(0,0)
       turtle.pendown()
       turtle.write("you lose. Try again!")

       turtle.color(pet_color)
       turtle.circle(35)
       turtle.up()
       turtle.forward(20)
       turtle.left(90)
       turtle.forward(30)
       turtle.down()
       turtle.begin_fill()
       turtle.write("x")
       turtle.up()
       turtle.left(80)
       turtle.forward(30)
       turtle.down()
       turtle.write("x")
       turtle.end_fill()
       turtle.up()

    turtle.exitonclick()
    


       
def main():
    """
    signature: () -> NoneType
    Run the pong game. You shouldn't need to
    modify this function.
    """
    global seconds, pet_name, pet_color
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onscreenclick(ClickCheck)
    pet_name=turtle.textinput("Pet name", "Enter a name for your pet: ")
    while True:
        try:
            pet_color=turtle.textinput("Pet color", "Enter the color of your pet: ")
            turtle.color(pet_color)
            break
        
        except:
            pass
    while game == True:
        game_over()
        turtle.clear()
        frame()
        time.sleep(0.1)
        seconds += 1

    end_game()


  
start_game()
