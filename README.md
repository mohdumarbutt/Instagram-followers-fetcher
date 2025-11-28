# 🌟 Instagram Follower Data Fetcher & Exporter

A powerful, browser‑based automation tool to **fetch, analyze, and export Instagram follower data** — beautifully structured, analytics‑ready, and entirely client‑side.

---

<div align="center">

### ⚡ Zero Setup • 🔒 100% Local • 📊 Analytics Ready

![Preview Banner](https://img.shields.io/badge/Instagram-Follower%20Exporter-blueviolet?style=for-the-badge\&logo=instagram)
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-lightgrey?style=for-the-badge)

</div>

---

## 📖 Overview

This tool allows you to extract **detailed follower information** directly from Instagram using only your browser console. It safely accesses Instagram's internal GraphQL endpoints and provides:

* 🔍 Full follower data
* 📄 JSON & CSV exports
* 📈 Built‑in analytics
* ⚡ Smooth auto‑pagination
* 🔒 100% local execution

Perfect for developers, analysts, creators, and anyone who needs structured follower insights.

---

## ✨ Features

### 🔍 Complete Follower Data

Fetch:

* Username
* ID
* Full name
* Profile URL
* Privacy status
* Verification status

### 📊 Smart Pagination

Automatically scrolls through all follower pages and compiles a complete dataset.

### 💾 Export Options

* **JSON** (date‑stamped, with metadata)
* **CSV** (legacy support)
* Copy‑to‑clipboard shortcuts

### 📈 Built‑in Insights

Instant analytics after fetching:

* 🔒 Private accounts count
* ☑️ Verified accounts count
* 📊 Total followers

### ⚡ Rate‑Limit Friendly

Built‑in safety delays and request throttling.

---

## 🚀 Quick Start

### 📌 Requirements

* Logged into Instagram on your browser
* Basic familiarity with browser DevTools

### ▶️ How to Use

1. **Open Instagram** and log in
2. Press **F12 → Console**
3. Paste the script
4. Replace the username variable
5. Press **Enter**
6. When complete, run: `exportFollowersJSON()`

---

## 🧩 Code Snippet (Starter)

```javascript
const username = "your_username_here"; // Replace with your Instagram username

(async () => {
  try {
    console.log(`Starting to fetch followers for ${username}...`);

    // [Full code inserted here in real version]

  } catch (error) {
    console.error('Error fetching followers:', error);
  }
})();
```

---

## 📁 Export Formats

### 🟦 JSON Export

Run:

```javascript
exportFollowersJSON();
```

Output: `followers-DD-MM-YYYY.json`

**JSON Structure Preview:**

```json
{
  "metadata": {
    "exported_at": "2025-04-15T10:30:00.000Z",
    "export_timestamp": 1744705800000,
    "target_username": "your_username",
    "total_followers": 150,
    "source": "Instagram Follower Exporter"
  },
  "followers": [
    {
      "username": "follower1",
      "profile_url": "https://instagram.com/follower1",
      "id": "123456789",
      "full_name": "Follower One",
      "is_private": false,
      "is_verified": false
    }
  ]
}
```

### 🔧 Additional Export Helpers

* `exportFollowersJSON()` → JSON file
* `downloadCSV()` → CSV file
* `copy(followers.map(f => f.username))` → Copy usernames only
* `copy(followers.map(f => `${f.username} - ${f.profile_url}`))` → Copy usernames + links

---

## 🔧 Technical Details

### 📡 Internal API Endpoints

* **Top Search API**: `web/search/topsearch/`
* **Followers GraphQL** (`query_hash: c76146de99bb02f6415203be841dd25a`)

### 📦 Data Fields Collected

* Username
* ID
* Full Name
* Profile URL
* Privacy Status
* Verification Status

### ⏳ Rate Limit Protection

* 500ms delay per request
* 100 followers per page
* Auto‑retry safe

---

## ⚠️ Important Notes

### Legal Responsibility

* Use only on **your own account**
* Avoid misuse, scraping, or spam behavior
* Instagram may change internal APIs

### Known Limitations

* Requires Instagram login
* Runs only in browser console
* May break if the IG structure updates

---

## 🛠️ Troubleshooting Guide

### ❌ "User not found"

* Check username
* Ensure correct logged-in account

### ❌ "Unexpected API response"

* Reload page
* Try again later
* Instagram might be rate‑limiting you

### ⏳ Rate‑Limit Triggered

* Wait 2–5 minutes
* Lower fetch limit

---

# 👨‍💻 Developer

### **Mohd Umar Butt (Umar Butt)**

Full‑stack developer • Python • JavaScript • C++ • Web/App Builder • AI Enthusiast

### 🌐 Connect

* Instagram: **@theumar_butt**
* Facebook: **MohdUmarButtOfficial**
* LinkedIn: **mohdumarbutt**
* YouTube: **@mohdumarbutt_official**
* GitHub: **mohdumarbutt**
* ORCID: **0009-0005-4495-314X**

### 💖 Support the Developer

* BuyMeACoffee: **/umarbutt**
* GitHub Sponsors: **/mohdumarbutt**
* Thanks.dev: **/gh/mohdumarbutt**

---

## 🚀 Other Projects by Umar Butt

### **UB Project Zipper 🗂️⚡**

FastAPI service that converts file‑tree text into downloadable ZIP files.

* ⚡ Ultra‑fast
* 🧠 Smart parsing
* 📦 Streaming ZIP output
* 🐳 Docker‑ready

Repo: **mohdumarbutt/Project‑Zipper**
Frontend: **project‑zipper.vercel.app**

---

## 📄 License

Educational use only. User must follow Instagram's Terms of Service.

## 🔄 Updates & Maintenance

This script may need updates when Instagram modifies its endpoints.
Stay tuned to the GitHub repo.

---

### ⭐ If this helped you, please star the repo and support the developer!

*Last updated: April 2025*
