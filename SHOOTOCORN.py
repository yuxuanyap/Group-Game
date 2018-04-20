#SHOOTOCORN
from gamelib import*#imports the game library of classes and functions
game = Game(800,600,"SHOOT SHOOT SQUAWK",60)#game object
bk = Image("bk.jpg",game)#image object
bk.resizeTo(800,600)

opening = Image("opening2.jpg",game)
opening.resizeTo(game.width,game.height)

game.setBackground(opening)

zombie = Image("corn.png",game)
zombie.resizeBy(-85)
zombie.setSpeed(4,60)#set speed in order to move

turkey = Image("Trollg.png", game)
turkey.resizeBy(-25)
turkey.resizeBy(-50)
turkey.setSpeed(4,60)

crosshair = Image("crosshair.png",game)#image object
crosshair.resizeBy(-80)

play = Image("play.png",game)
play.resizeBy(-70)
play.y += 40

titlescreen = Image("SHOOTOCORN.png",game)
titlescreen.y -= 80

youwin = Image("youwin.png",game)

youlose = Image("lose.gif",game)
youlose.resizeBy(40)
mouse.visible = False

gun = Sound("gun.wav",1)#sound object
gobble = Sound("gobble.ogg",2)#sound object
die = Sound("die.ogg",4)

newfont = Font(white,48,green,"Comic Sans MS")

#Title Screen
while not game.over:
    game.processInput()
    game.drawText("SHOOTOCORN",150,5)
    opening.draw()
    play.draw()
    titlescreen.draw()
    

    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    
    game.update(30)
    
game.over = False

#Level 1
while not game.over:#while loop runs until game is over
    game.processInput()#process Input
    bk.draw()
    zombie.move(True)
    turkey.move(True)
    crosshair.moveTo(mouse.x,mouse.y)#move the crosshair to the mouse position x and y

    if mouse.LeftButton:#if statement
        gun.play()

    if turkey.collidedWith(zombie):#if statement tests a condition to be TRUE
        turkey.resizeBy(-1)#an action takes place if TRUE
        turkey.moveTo(randint(100,700),randint(100,500))
        game.score-=1#accumulator
        gobble.play()
        
    if crosshair.collidedWith(zombie)and mouse.LeftButton:#if statement - a condition that is tested to be TRUE
       
        zombie.resizeBy(-1)
        zombie.moveTo(randint(100,700),randint(100,500))
        
        game.score+=1#accumulator
        zombie.speed+=1
    
    if game.score>=10:#if statement
        youwin.draw()#action if true
        die.play()
        game.setBackground(level2)
        game.over = True

    if crosshair.collidedWith(turkey) and mouse.LeftButton:#if statement
       game.time-=10
       gobble.play()
       
    if game.time<=0:#if statement
        youlose.draw()
        game.over = True
        
    if turkey.width <=100:
        game.drawText("You lose!", 100,5)
        game.over = True

    if zombie.width <=100:
        game.drawText("You win!", 100,5)
        die.play()
        game.over = True
        

    game.displayScore()#the game's score
    game.displayTime(200,5)

        
    game.update(80)#refresh the screen
game.wait(K_SPACE)#wait time with key press
game.quit()







