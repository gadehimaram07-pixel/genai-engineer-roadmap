# 🎯 Decoding Strategies

> **Week:** 1
> **Module:** LLM Foundations
> **Difficulty:** ⭐⭐⭐☆☆
> **Prerequisites:** Tokenization, Transformers
> **Estimated Reading Time:** 10–12 minutes

---

# 📑 Table of Contents

- Introduction
- Why Decoding is Needed
- Greedy Decoding
- Temperature
- Top-k Sampling
- Top-p (Nucleus) Sampling
- Comparison
- Examples
- Interview Questions
- Summary

---

# 📖 Introduction

After an LLM processes your prompt, it predicts a probability for every possible next token.

Example:

```
Prompt:

The capital of France is
```

The model predicts:

| Token | Probability |
|--------|------------:|
| Paris | 92% |
| London | 3% |
| Berlin | 2% |
| Rome | 1% |
| Others | 2% |

A decoding strategy decides **which token should be selected**.

---

# 🧠 Why Decoding is Needed?

The model doesn't directly output the highest-probability token every time.

Instead, different decoding strategies control:

- Creativity
- Randomness
- Diversity
- Accuracy

---

# 1️⃣ Greedy Decoding

Greedy Decoding always selects the token with the **highest probability**.

Example:

```
Paris → 92%
```

The model chooses:

```
Paris
```

### Advantages

- Fast
- Deterministic
- Accurate for factual tasks

### Limitations

- Less creative
- Can produce repetitive text

---

# 2️⃣ Temperature

Temperature controls randomness.

### Low Temperature (0.1–0.3)

- More focused
- More deterministic
- Better for coding and factual answers

### High Temperature (0.8–1.2)

- More creative
- More diverse
- Better for storytelling and brainstorming

> **Important:** Temperature does **not** make the model smarter. It only changes how it samples from the probability distribution.

---

# 3️⃣ Top-k Sampling

Top-k keeps only the **k most probable tokens**.

Example:

```
k = 3

Paris
London
Berlin
```

The next token is sampled **only** from these three.

---

# 4️⃣ Top-p (Nucleus Sampling)

Instead of selecting a fixed number of tokens, Top-p selects the smallest set of tokens whose cumulative probability reaches **p**.

Example:

```
p = 0.90

Paris = 0.65
London = 0.20
Berlin = 0.08

Cumulative = 0.93
```

The model samples from these three tokens.

---

# 📊 Comparison

| Strategy | Creativity | Accuracy |
|----------|------------|----------|
| Greedy | Low | High |
| Temperature | Adjustable | Adjustable |
| Top-k | Medium | Good |
| Top-p | High | Very Good |

---

# 💻 Real-world Usage

### Coding Assistant

- Greedy
- Low Temperature

### AI Tutor

- Top-p
- Medium Temperature

### Story Generator

- High Temperature
- Top-p

---

# ❌ Common Misconceptions

### Temperature makes the model smarter.

❌ False.

It only changes randomness.

---

### Greedy is always best.

❌ False.

Creative tasks often benefit from Top-p or higher temperatures.

---

# 🎯 Interview Questions

### 1. What is Greedy Decoding?

Greedy Decoding always selects the token with the highest probability.

---

### 2. Does increasing Temperature improve intelligence?

No.

It only increases randomness and creativity.

---

### 3. Difference between Top-k and Top-p?

Top-k selects a fixed number of tokens.

Top-p selects tokens until a cumulative probability threshold is reached.

---

### 4. Which decoding strategy is best for coding?

Greedy or Low Temperature.

---

# 📝 Summary

- Decoding chooses the next token.
- Greedy → Most probable token.
- Temperature → Controls randomness.
- Top-k → Fixed candidate set.
- Top-p → Probability-based candidate set.