# 📊 Spreadsheet Formula Generator

An AI-powered web app that generates Excel/Google Sheets formulas from natural language prompts. Built with React, Flask, and g4f — deployed with GitHub Pages and Render.

![Demo Screenshot](https://i.postimg.cc/3xqX5rkZ/test.png)

---

## 🔍 Features

- ✅ Describe what you need in plain English
- ✅ Get back clean, ready-to-copy Excel formulas
- ✅ Regenerate if the formula isn’t accurate
- ✅ Copy directly to clipboard
- ✅ View full prompt/formula history
- ✅ Export history to `.txt` for tracking or sharing
- ✅ Fully free + serverless deployment

---

## 🚀 Live Demo

🌐 [spreadsheet-formula-generator](https://louie5277.github.io/spreadsheet-formula-generator/)

---

## 🛠 Tech Stack

| Frontend | Backend | AI Engine |
|----------|---------|-----------|
| React + Axios | Flask (Python) | `g4f` (LLM proxy) |

---

## 🧪 Example Prompts

> 💬 _“Sum all values in column A where column B is 'Approved'”_  
> 💬 _“Average sales from D2 to D100 where region = East”_  
> 💬 _“Divide column A by column B if C is 'Sales'”_

---

## 📦 Local Development

```bash
# 1. Clone the repo
git clone https://github.com/louie5277/spreadsheet-formula-generator
cd spreadsheet-formula-generator

# 2. Setup backend
cd backend
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate
pip install -r requirements.txt
python app.py

# 3. Setup frontend (in another terminal)
cd ../frontend
npm install
npm start
