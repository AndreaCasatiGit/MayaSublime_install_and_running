# MayaSublime - Install and Running

1.	If you don’t have the Package Controll installed,
    go in SublimeText use ctrl+shift+P to open the action box and digit “Package Controll”, install it
   
2.	Ctrl+shift+P, write package control: install package

3.	A little dropdown menu appear, search for MayaSublime

4.	Select it and install it 

![image](https://user-images.githubusercontent.com/45981662/201468540-aa86204e-7def-4fda-8991-d9d75195b825.png)

5.	Open the mayaSublime-default-settings and check the python_command_port and the mel_command_port 

![image](https://user-images.githubusercontent.com/45981662/201468582-0a213ff7-fffe-4f5e-a4cc-eae6dabfe185.png)

6. Copy paste the backdoor.py script in a maya script editor (python) tab

![image](https://user-images.githubusercontent.com/45981662/201468670-950e3d0c-b91e-4f9f-8eab-802ce0f64d0c.png)

7. Check the defined port, if them not match the sublime one, change them

7. Use backdoor(openPort=True), to open defined port

8. Use backdoor(closePort=True), to close defined ports

![image](https://user-images.githubusercontent.com/45981662/201468889-2fd009c6-b5d4-403d-ad3e-cad12281312a.png)


## Can I use that code also to drive other programs? (Like VSCode)
Yes you can, just remember to change the port :)

## Create shelf buttons
You can create two shelf buttons, one to open and one to close
![image](https://user-images.githubusercontent.com/45981662/201469327-efea1a44-146a-44d0-8ec9-47a6f5bdca79.png)

## Sublime ctrl+enter command doesn't go to next line anymore!!
If you are used to use Ctrl+Enter in SublieText to go directly to the next row,
remember to change the "MayaSublime - Key binding"

![image](https://user-images.githubusercontent.com/45981662/201469468-c55a2259-5553-4e73-adb9-b772bc35becb.png)

1. Open and copy the configuration

![image](https://user-images.githubusercontent.com/45981662/201469507-8ef90b2b-5750-4ec4-9563-79d0de100f8c.png)

2. Create this file and paste the config inside

![image](https://user-images.githubusercontent.com/45981662/201470065-8f3866da-f90b-4398-a96c-75bac7eb39b9.png)

you can check the path to create it at the top of sublime
![image](https://user-images.githubusercontent.com/45981662/201470216-5ddb9959-2e31-4e50-8db1-826b9ad3c25d.png)


3. Edit it as you prefer and save

![image](https://user-images.githubusercontent.com/45981662/201470126-d46317e8-40f2-4d1f-849f-da7cf9295325.png)




