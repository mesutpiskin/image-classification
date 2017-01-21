::author = "Mesut Pişkin"
:rerun
python CaffeGUI.py
set /p INPUT=TR:Yeniden Calistir EN:Rerun [y/n]?:
If "%INPUT%"=="y" goto rerun 