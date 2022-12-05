def crates_in_stacks(s: str) -> dict:
    return {
        int(1 + (i - 1) / 4): s[i + 1] for i in range(len(s)) if s.startswith("[", i)
    }
