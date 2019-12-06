# BitlyApiTool

### Description

BitlyApiTool is a program that takes a weblink as an argument and shortens it as a bitlink via API of Bitly.com. If the weblink provided as argument is already a bitlink, the statistics of it to be shown.

### How to install

BitlyApiTool needs an API token of your Bitly.com account. [The instruction to get token](https://support.bitly.com/hc/en-us/articles/230647907-How-do-I-find-my-OAuth-access-token-).

Token information should be stored in the .env file located as shown below:
```
TOKEN=*your token*
```
Locate the .env file in the same folder with main.py.

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Example

```
>python.exe main.py https://github.com/
Это явно не ваш битлинк, попробуем сократить эту ссылку
Сокращенная ссылка: http://bit.ly/362x8gS
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).