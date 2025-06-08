# 🌿 Nicotine+ Username Filter Plugin

A Nicotine+ plugin that automatically bans users with offensive or suspicious usernames and sends them a mellow warning. It will unban them if they change their name.

## ✅ Features
- Detects racist/offensive terms in usernames
- Detects usernames with excessive random numbers
- Sends a friendly “stoner-style” message explaining the ban
- Auto-unbans if username is updated

## 💻 Installation
Copy `ban_username_filter.py` to:

**macOS:** `~/Library/Application Support/nicotine/plugins/`

Restart Nicotine+ and enable the plugin in Preferences.

## 🧪 Testing
```bash
python3 ban_username_filter.py
