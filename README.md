CS50 Final Project:  
SOCKY by RIKI FAMELI

SOCKY is a simple arcade-style game in which you control a sock-puppet-man named Socky.


__STARTING THE GAME__  
The aim of the game is to score as many points within 30 seconds by eating pieces of trash that appear on screen.  
Each piece of trash has a unique point value and a different chance of spawning.

Upon starting the game, you will see the start screen.  
Pressing tab will show the instructions for the game and the point values for each item.  
Pressing enter will start or restart the game.


__GAMEPLAY__  
When the game begins, a timer in the top right will keep track of how many seconds you have left in seconds (counting down from 30).
Your score will be displayed in the top left.

Socky will be displayed on a background of a dirty bedroom.  
He can be moved within set boundaries using WASD or the arrow keys.  
Pressing space will open his mouth. If his mouth is near an object when his mouth closes (spacebar is released), that object will be "eaten" and will spawn elsewhere.

A total of 10 items will appear on the screen at all times.  
Once an item is eaten, the score will increase by that item's set value and it will respawn as a new item based on random numbers and set probabilities.

At the end of the 30 seconds, a game over screen will appear with the player's score that round. Pressing enter will restart the game.


__PROGRAMMING__  
SOCKY was programmed in Python using the Pygame library.


__ASSETS AND GRAPHICS__  
The original sock puppet image was an asset retrieved from www.spriters-resource.com and created by Baldis.  
Socky as he appears in the game was created by using Photoshop to make a sock-man-thing(?) using those sock puppets.  
Eating noises were retrieved from Freesound.org.  
Music was retrieved from bensound.com.  
Start screen, instructions screen, and end screen were all created by me using Adobe Photoshop.  

__VIDEO__  
Watch the video at this URL:  
https://www.youtube.com/watch?v=m_A-NsSatsA


__ADDITIONAL NOTES__
- Socky was not the original idea I had for my project. I used some sprites and images I had downloaded to follow a tutorial and just kept building on it.  
- Tutorial I used can be seen here: https://www.youtube.com/watch?v=FfWpgLFMI7w  
- Originally planned to use Unity, but switched to Pygame for a greater focus on the coding and to practice using Python  
- Thank you for helping out on this course (whoever's reading this)! It's been one of my favorites even though it was online!  
