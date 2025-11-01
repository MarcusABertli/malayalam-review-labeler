reviews = [
    "ഈ ലാപ്‌ടോപ്പ് വളരെ വേഗമുള്ളതാണ്",
    "ബാറ്ററി ഒരു മണിക്കൂർ മാത്രം നിൽക്കുന്നു",
    "നല്ല ക്യാമറ, വിലയ്ക്ക് അർഹമായത്"
]

def label_malayalam(review):
    negative_words = ["മാത്രം", "ചീത്ത", "പ്രശ്നം", "നിൽക്കുന്നില്ല"]
    if any(word in review for word in negative_words):
        return "NEGATIVE"
    return "POSITIVE"

print("REVIEW → LABEL")
print("-" * 40)
for r in reviews:
    print(f"{r} → {label_malayalam(r)}")