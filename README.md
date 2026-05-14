# 📡 JioAirFiber – Inventory Assistant Chatbot

A fully offline, keyword-based chatbot for JioAirFiber inventory & ERP queries.
Supports 10,000+ users via free Render hosting.

---

## 📁 Project Structure

```
jioairfiber-chatbot/
│
├── app.py               ← Flask backend (don't edit)
├── qa_data.json         ← ✅ YOUR DATA FILE — only file you'll ever edit
├── requirements.txt     ← Python dependencies
├── render.yaml          ← Free Render deployment config
├── README.md            ← This file
│
└── templates/
    └── index.html       ← Chatbot UI (don't edit unless needed)
```

---

## 🚀 Run Locally (VS Code)

### Step 1: Install Python dependencies
Open terminal in VS Code (`Ctrl + `` ` ``) and run:
```bash
pip install -r requirements.txt
```

### Step 2: Start the bot
```bash
python app.py
```

### Step 3: Open in browser
Visit: **http://localhost:5000**

---

## ➕ How to Add / Edit Q&A

Open `qa_data.json` — it's the only file you need to touch!

### Add a new question inside an existing category:
```json
{
  "id": 17,
  "question": "Your new question here",
  "keywords": ["keyword1", "keyword2", "keyword3"],
  "answer": "Your detailed answer here.\n1. Step one\n2. Step two"
}
```

### Add a new category:
```json
{
  "id": "newcategory",
  "name": "New Category Name",
  "icon": "🔧",
  "questions": [
    {
      "id": 17,
      "question": "First question in new category",
      "keywords": ["keyword1", "keyword2"],
      "answer": "Answer here"
    }
  ]
}
```

### Tips for keywords:
- Use words users are likely to TYPE (short, common words)
- Include abbreviations: "orn", "wo", "erp", "jpw"
- 3–6 keywords per question is ideal
- Multi-word phrases score higher: `"serial number not assigned"` > `"serial"`

---

## 🌐 Deploy FREE on Render (10,000+ users)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial chatbot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/jioairfiber-chatbot.git
git push -u origin main
```

### Step 2: Deploy on Render
1. Go to **https://render.com** and sign up (free)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub account and select your repo
4. Render will auto-detect `render.yaml`
5. Click **"Deploy"** — done! ✅

Your bot will be live at:
`https://jioairfiber-inventory-bot.onrender.com`

### ⚠️ Free Tier Note:
Render's free tier sleeps after 15 min of inactivity.
To avoid this, use **UptimeRobot** (free) to ping your URL every 10 min:
- Go to https://uptimerobot.com → Add New Monitor → HTTP(S)
- Enter your Render URL → every 10 minutes

---

## 📊 How the Bot Works

```
User types or clicks
        ↓
Keyword matching engine (in app.py)
        ↓
Scans all Q&A in qa_data.json
        ↓
Returns best matching answer
```

No internet, no API, no cost — runs 100% offline.

---

## 🛠️ Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: flask` | Run `pip install -r requirements.txt` |
| Bot doesn't match my question | Add more keywords in `qa_data.json` |
| Port 5000 already in use | Run `python app.py` after changing port in app.py |
| Render deploy fails | Check build logs, ensure `requirements.txt` is committed |
