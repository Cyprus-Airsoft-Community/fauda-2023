# Operation Fauda
## Minigame for a MilSim mission for a Cypurs Airsoft Community Event.


### Python 3 Required.
### To run the script:

    1) Open cmd and cd to your current dir.
cd /path

    2) Create a virtual environment:
python -m venv venv
    
    3) Activate it:
venv\Scripts\activate
    
    4) Install the required libraries:
python -m pip install -r requirements.txt
    
    5) Run the script:
py fauda.py
    
    To package the script to an .exe:
pyinstaller --name FAUDA --icon CAA_LOGO.ico caa.py --paths venv\Lib\site-packages --onefile
