::author = "Mesut Pişkin"
:rerun
python src/CaffeGUI.py
set /p INPUT=TR:Yeniden Calistir EN:Rerun [y/n]?:
If "%INPUT%"=="y" goto rerun 