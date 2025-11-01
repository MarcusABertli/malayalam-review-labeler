# Malayalam Review Labeler (AI Data Training)

**Auto-labels product reviews in Malayalam using Python**  
Perfect for training NLP models in regional languages.

---

## 🛠️ Tech Stack
- **Python** (Loops, Conditionals, Functions)
- **CSV Handling**
- **Malayalam NLP Ready**

---

## 🚀 Features
- Labels reviews as **POSITIVE** or **NEGATIVE**
- Uses **native Malayalam keywords**
- Outputs clean data for AI training

---

## 📌 Sample Code
```python
def label_malayalam(review):
    negative = ["മാത്രം", "ചീത്ത", "പ്രശ്നം"]
    if any(word in review for word in negative):
        return "NEGATIVE"
    return "POSITIVE"
