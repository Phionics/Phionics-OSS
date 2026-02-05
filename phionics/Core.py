from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, List, Dict, Any, Optional


@dataclass
class PhionicsResult:
    """
    Result container returned by phionic_rank.
    """
    best_text: str
    ranked: List[Dict[str, Any]]


@dataclass
class PhionicsConfig:
    """
    Configuration flags for the Phionics membrane.
    """
    ethical_gate: bool = True
    minority_boost: bool = True


def default_ethics_gate(text: str) -> bool:
    """
    Minimal, transparent ethics gate (demo version).
    Replace or extend with full Ethical DNA later.
    """
    banned_phrases = [
        "how to make a bomb",
        "build a weapon",
        "kill a person",
    ]
    t = text.lower()
    return not any(p in t for p in banned_phrases)


def phionic_rank(
    candidates: List[str],
    *,
    scorer: Callable[[str], float],
    config: Optional[PhionicsConfig] = None,
    ethics_gate: Callable[[str], bool] = default_ethics_gate,
) -> PhionicsResult:
    """
    Core Phionics operation:
      1) optional ethical gating
      2) score each candidate
      3) rank and select best
    """
    config = config or PhionicsConfig()

    ranked: List[Dict[str, Any]] = []

    for c in candidates:
        if config.ethical_gate and not ethics_gate(c):
            continue
        ranked.append(
            {
                "text": c,
                "score": float(scorer(c)),
                "meta": {},
            }
        )

    ranked.sort(key=lambda x: x["score"], reverse=True)

    if not ranked:
        return PhionicsResult(best_text="", ranked=[])

    return PhionicsResult(
        best_text=ranked[0]["text"],
        ranked=ranked,
    )
