# neochibot
寝落ちした人をチャンネル移動させるDiscordボット

# procedure
```sh
# BOTのTOKENを記入
vi example.env
cp example.env .env
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python management.py
```

# command
- mmv {AFKチャンネルに移動させたい対象のメンション}
  - 寝落ちした人を優しさで移動させることができるコマンド
- m 
  - 自分がサーバーミュートされていた場合の解除コマンド