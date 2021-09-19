@ECHO OFF

IF NOT EXIST "entVir" (
    py -m venv entVir
)

CALL entVir\Scripts\activate.bat
pip list
deactivate