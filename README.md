# Game-Controller
This is a Arduino And Joystick Module based game controller instead of game controller it is more of a mouse controller using joystick

https://user-images.githubusercontent.com/59998475/127523235-e1a7b631-258b-44cc-ad14-9a6a85b36101.mp4

![circuit diagram](https://github.com/diwan-kadir/Game-Controller/blob/master/Game_demo.PNG)


The Arduino ino code gives 3 values X , Y , Z whenever there is action performed through joystick

![circuit diagram](https://github.com/diwan-kadir/Game-Controller/blob/master/Game_controller.PNG)

The Values from arduino are picked by python using serial library and using basic co-ordinate movements python code controls the mouse with the joystick
For demo I have controlled CS GO 1.6 edition where I control aim and click of the gun or weapon by joystick. The dataset for the gestures prediction is done by the movement made, hence it's a dynamic dataset whose values can also change with change in direction 


https://www.youtube.com/watch?v=bPCgk4F5aQE
