"""Exercise 01 — inspect BPE tokenization with tiktoken."""

from __future__ import annotations

import tiktoken

SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Tokenization splits words like 'unhappiness' unpredictably.",
    "  Leading spaces matter: ' hello' vs 'hello'.",
]

PARAGRAPH = (
    "Large language models never see raw text. Every string is converted into a "
    "sequence of integer token ids before it reaches the transformer. Byte-pair "
    "encoding builds a vocabulary by repeatedly merging the most frequent byte "
    "pairs in a training corpus. Common words become single tokens; rare or "
    "novel strings are split into subword pieces. This trade-off keeps the "
    "vocabulary finite while still allowing the model to represent arbitrary "
    "Unicode text. Token boundaries affect everything downstream: context window "
    "usage, cost per request, and even model behavior on punctuation, numbers, "
    "and code. Understanding how your tokenizer splits text is the first step "
    "toward understanding what the model actually processes."
)

CASING_VARIANTS = ["Python", "python", "PYTHON"]


def inspect(text: str, encoding_name: str = "cl100k_base") -> list[tuple[int, str]]:
    enc = tiktoken.get_encoding(encoding_name)
    ids = enc.encode(text)
    pairs = [(tid, enc.decode([tid])) for tid in ids]
    print(f"\n--- {encoding_name!r} ---")
    print(repr(text))
    for tid, token in pairs:
        print(f"  {tid:6d}  {token!r}")
    print(f"  => {len(ids)} tokens, {len(text)} chars, {len(text.split())} words")
    return pairs


def round_trip(text: str, encoding_name: str = "cl100k_base") -> None:
    enc = tiktoken.get_encoding(encoding_name)
    ids = enc.encode(text)
    decoded = enc.decode(ids)
    ok = decoded == text
    print(f"round-trip ({encoding_name}): {'OK' if ok else 'FAIL'}")
    if not ok:
        print(f"  original: {text!r}")
        print(f"  decoded:  {decoded!r}")


def compare_encodings(text: str, names: list[str]) -> None:
    print("\n=== encoding comparison ===")
    print(repr(text))
    for name in names:
        try:
            enc = tiktoken.get_encoding(name)
        except Exception as exc:  # noqa: BLE001 — show load errors per encoding
            print(f"  {name:12s}  skipped ({exc})")
            continue
        ids = enc.encode(text)
        tokens = [enc.decode([tid]) for tid in ids]
        print(f"  {name:12s}  {len(ids):3d} tokens  {tokens}")


def length_intuition(text: str, encoding_name: str = "cl100k_base") -> None:
    enc = tiktoken.get_encoding(encoding_name)
    ids = enc.encode(text)
    words = len(text.split())
    chars = len(text)
    ratio = len(ids) / words if words else 0.0
    print(f"\n=== length intuition ({encoding_name}) ===")
    print(f"  tokens:  {len(ids)}")
    print(f"  words:   {words}")
    print(f"  chars:   {chars}")
    print(f"  tokens/word: {ratio:.2f}")


def casing_study(variants: list[str], encoding_name: str = "cl100k_base") -> None:
    enc = tiktoken.get_encoding(encoding_name)
    print(f"\n=== casing study ({encoding_name}) ===")
    for word in variants:
        ids = enc.encode(word)
        tokens = [enc.decode([tid]) for tid in ids]
        print(f"  {word!r:10s}  ids={ids}  tokens={tokens}")


def main() -> None:
    print("=== Exercise 01: Tokenization ===\n")

    print("--- round-trip check ---")
    for sentence in SENTENCES:
        round_trip(sentence)

    print("\n--- inspect splits (cl100k_base) ---")
    for sentence in SENTENCES:
        inspect(sentence)

    compare_encodings(SENTENCES[1], ["cl100k_base", "p50k_base", "r50k_base"])

    length_intuition(PARAGRAPH)

    casing_study(CASING_VARIANTS)


if __name__ == "__main__":
    main()
