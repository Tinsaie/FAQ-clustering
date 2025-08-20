# 🧠 Question Clusterer

This project groups similar questions into clusters using **Sentence Transformers** and **KeyBERT**.  
It finds themes, representative questions, and organizes related questions together.

---

## 🚀 Features
- Embeds text using `all-mpnet-base-v2`
- Clusters with Agglomerative Clustering
- Extracts keywords with KeyBERT
- Finds a representative question for each cluster

---

## 📦 Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/question-clusterer.git
cd question-clusterer
```

Install requirements:
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

1. Add your questions to **`questions.txt`** (one per line).
2. Run the main script:
```bash
cd src
python main.py
```

---

## 📊 Example Output
```
📊 Found 2 clusters:

🏷️ CLUSTER 1 (Size: 3)
🔹 Main Theme: car, drive, type
⭐ Representative Question: what type of car did you drive ?
📋 All Questions:
  - what is car ?
  - how do i drive ?
  - what type of car did you drive ?
```

---

## 📜 License
MIT License
