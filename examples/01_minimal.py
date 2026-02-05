from phionics import phionic_rank

def scorer(text: str) -> float:
    # Toy coherence signal: prefer mentions of "coherence"
    return 1.0 if "coherence" in text.lower() else 0.0

candidates = [
    "Phionics is a thing.",
    "Phionics is a coherence-ranking membrane for candidate outputs.",
    "This sentence mentions coherence explicitly.",
]

result = phionic_rank(candidates, scorer=scorer)

print("BEST:")
print(result.best_text)

print("\nRANKED:")
for r in result.ranked:
    print(r["score"], r["text"])
