for it to work it`s required three steps 

1 initialise bot (cd to directory, source .venv/bin/activate, python3 bot.py)

2 initialise webapp server(cd to directory, source .venv/bin/activate, uvicorn webapp:app --reload)

3 start forwarding all incoming trafic from telegram or web users wia ngrok (cd to directory, source .venv/bin/activate, ngrok 8000)
it is important to keep track of your active port, so that all API can communicate with each other
