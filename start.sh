echo "Cloning Repo, Please Wait..."
git clone https://github.com/Millie-bobby/Millie-power-bot.git /Millie-power-bot
cd /Millie-power-bot
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
