# PONG
Hello, my name is Dharunish Yugeswardeenoo. This is my final project for the Introduction to Python CS50 course. I created my version of the famous game of Pong which was first created in 1972 by Atari Inc. A key library I used in my code was Pygame, and this was very helpful in creating shapes and properties. I have used 8 different functions and around 20 variables.
### Video Demo:  <https://youtu.be/ZDFm9Ozl8Bg>
### Libraries Used:
+ Pygame: https://www.pygame.org/news
+ Pytest: https://docs.pytest.org/en/7.4.x/
### Controls:
+ Serve (Start) = Spacebar
+ Player 1
    + Up = W key
    + Down = S key
+ Player 2
    + Up = Up Arrow
    + Down = Down Arrow
### Description of code:
To begin, the pygame library allowed me to create shapes to display the players and the ball. The players are __rectangles__ set to __width: 10 pixels__ and __height: 100 pixels__. The ball is a __circle__ with __radius: 10 pixels__. The __color__ of each sprite is __white__ and the __background__ is __black__. I also created a variable called __"text"__ for the score in __font: freesansbold.ttf__ with __size: 40__.

I created a variable called __"state"__ which decides the state of the game. The game starts off frozen as it's state is __"serve"__. Once the __spacebar__ is pressed, the state is __"play"__, and thus the ball will start moving. When a player reaches __five__ points, the state is __"end"__, and the game will reset the score and display the winner.

#### main():
The __"main"__ fuction in my code is where I implement the mechanics and processes of the game. I associate the controls with the __movement__ and implement when the game should __start__ and __end__. Once the game is started, the code will __draw__ both __players__, the __ball__, the __score__, and will __display__ the __screen__. This is all under a __while loop__ which will continue to run as long as a variable called __"running" = True__. If a command is given to exit, __running = False__, and the loop will quit.

#### draw_player():
This function is relatively simple. It's purpose is to __draw__ both players. The drawing method is given by Pygame using __"pygame.draw.rect"__. Draw_player's __parameters__ are the __x and y positions__ of the two players. The code for movement is written in two other functions.

#### move_up():
This operates the __upward__ movement of the players. If the __W key__ or the __up-arrow key__ is __pressed__, the code will run this function. The __x value__ stays __constant__ as the players __do not__ move __horizontally__. The __y value__, however, changes by __subtracting 5__ to it's __current value (y -= 5)__. But the function will __not allow__ the __y value__ to go __below 0__. If __y <= 0__, the y will __remain at 0__.

#### move_down():
This operates the __downward__ movement of the player. If the __S key__ or the __down-arrow__ key is pressed, the code will run this function. Once again, the __x__ value stays constant, but the y value __adds 5__ to its __current__ value __(y += 5)__. This allows the player to move downwards. However, the x and y position of the player is located at the __top left__ of the __rectangle__. As a result, the y value most __stop__ at the __(height of the screen - length of the player)__.

#### draw_ball():
This function's only purpose is to __draw__ the __ball__. By using __"pygame.draw.circle"__, we set the __radius__ to __10__; the __x__ and __y__ value stays as a __variable__ since it constantly changes.

#### move_ball():
This function operates the __movement of the ball__. In the __main__ function, the ball is __randomly__ chosen which __direction__ it will go. Both __x and y__ recieves a random choice between __-5 or 5 (both values may be different)__, as that is the __speed__ in pixels the ball will go. This random choice is stored in __xv and yv__ (v stands for velocity). The x and y value will keep __adding xv and yv respectively__ to its __current__ value until it reaches the __border__. Once it does, yv is __multiplied__ by __-1__ to give the impression that the ball is __"rebounding"__ off the border. If the ball __collides__ with the __player__, there is 2 possibilities. If the ball hits the __top half__ of the paddle, we want it to go back __up diagonally (no matter where the ball came from)__, so we __multiply__ the __x__ value by __-1__ and then take the __absolute value__ of __y__ and __multiply__ it by __-1 (-abs(y))__. If the ball hits the __bottom half__ of the paddle, then we do the same thing except __without__ multiplying -1 to the absolute value. This will cause the ball to go __down diagonally__ (no matter where the ball came from). This is will be more clear in the video. Finally, if the ball __crosses__ either __side__, than the __state__ will be set to __"serve"__ as a point has been given.

#### score():
This function operates the __score__ of the game. If the ball's x position <= __0__, Player 2 gets 1 point. If the ball's __x position >= width of screen__, Player 1 gets __1 point__. The __score__ is then displayed as __text__.

#### end_game():
This function __resets__ the game and the score. If either player reaches __5 points__, the __scores__ will equal __0__ and the __winner__ of the round will be __displayed__ in __text__ across the top of the screen.

