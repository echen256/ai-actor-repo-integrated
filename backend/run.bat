pip install virtualenv
virtualenv myenv 
set venv_path=.\myenv\Scripts\Activate.bat
call "%venv_path%"
pip install -r requirements.txt
python main.py