# 🔤 Tokenization

> **Week:** 1
> **Module:** LLM Foundations
> **Difficulty:** ⭐⭐☆☆☆
> **Prerequisites:** Introduction to LLMs, Transformers, Training Stages
> **Estimated Reading Time:** 12–15 minutes

---

# 📑 Table of Contents

- Introduction
- Why Tokenization is Needed
- How Tokenization Works
- Types of Tokens
- Token IDs
- Why LLMs Work with Tokens Instead of Words
- Example
- Diagram
- Advantages
- Limitations
- Common Misconceptions
- Interview Questions
- Summary
- Related Topics

---

# 📖 Introduction

Humans read **words**.

Computers read **numbers**.

Large Language Models (LLMs) cannot directly understand text like humans do. Before processing any input, they first convert text into **tokens**, and then each token is converted into a unique numerical ID.

This process is called **Tokenization**.

Without tokenization, an LLM cannot process or generate language.

---

# 🧠 Why is Tokenization Needed?

Neural networks perform mathematical operations on numbers, not text.

Therefore, every prompt must be converted into a numerical format before entering the model.

Tokenization acts as the bridge between **human language** and **machine computation**.

---

# ⚙️ How Tokenization Works

Consider the sentence:

```
I love Artificial Intelligence.
```

### Step 1 – Input Text

```
I love Artificial Intelligence.
```

↓

### Step 2 – Tokenization

```
["I", "love", "Artificial", "Intelligence"]
```

↓

### Step 3 – Token IDs

```
[51, 912, 4812, 9031]
```

↓

### Step 4 – Embeddings

Each Token ID is converted into a high-dimensional vector (embedding).

↓

### Step 5 – Transformer

The transformer processes these embeddings to predict the next token.

---

# 📊 Complete Pipeline

```text
Input Text
      │
      ▼
Tokenizer
      │
      ▼
Tokens
      │
      ▼
Token IDs
      │
      ▼
Embeddings
      │
      ▼
Transformer
      │
      ▼
Output Tokens
      │
      ▼
Generated Response
```

---

# 🧩 Types of Tokens

A token is **not always a complete word**.

Depending on the tokenizer, a token can be:

### 1. Word

```
Hello
```

---

### 2. Sub-word

```
un
break
able
```

The word

```
unbreakable
```

may be split into multiple tokens.

---

### 3. Character

Some tokenizers split text into characters.

```
H
e
l
l
o
```

---

### 4. Punctuation

Even punctuation can become tokens.

```
.
,
!
?
```

---

# 🔢 Token IDs

Every token has a unique numerical ID.

Example:

| Token | Token ID |
|--------|----------|
| I | 51 |
| love | 912 |
| AI | 2104 |
| . | 13 |

These IDs are what the model actually processes.

---

# 💡 Why Don't LLMs Work with Words?

Words cannot be processed mathematically.

Neural networks require numbers.

Therefore,

```
Words
```

↓

```
Tokens
```

↓

```
Numbers
```

↓

```
Embeddings
```

↓

```
Transformer
```

This numerical representation allows the model to learn patterns and relationships.

---

# 🌍 Real Example

Prompt:

```
Explain AI in simple terms.
```

Possible tokens:

```
["Explain", "AI", "in", "simple", "terms", "."]
```

These tokens are converted into IDs before being processed.

---

# 💰 Why Do AI Companies Charge Per Token?

LLMs process **tokens**, not words.

Every token requires computation.

More tokens mean:

- More memory
- More computation
- Higher inference cost

This is why API pricing is usually based on **input tokens** and **output tokens**.

---

# 📖 Context Window

A model can only remember a limited number of tokens at a time.

This limit is called the **Context Window**.

Example:

```
Model Context Window

4096 Tokens
```

If the conversation exceeds this limit, older tokens may be forgotten or truncated.

---

# ✅ Advantages

- Converts language into numerical format.
- Makes mathematical computation possible.
- Supports multiple languages.
- Handles unknown words using sub-word tokenization.
- Improves vocabulary efficiency.

---

# ⚠️ Limitations

- Different tokenizers produce different token counts.
- Long prompts increase computational cost.
- Token boundaries may not match natural words.
- Context windows still impose limits.

---

# ❌ Common Misconceptions

### ❌ One word always equals one token.

Incorrect.

A single word may become multiple tokens.

Example:

```
internationalization
```

may be split into several sub-word tokens.

---

### ❌ Tokens are the same as words.

Incorrect.

Tokens can represent:

- Words
- Sub-words
- Characters
- Numbers
- Punctuation

---

### ❌ LLMs read English sentences.

Incorrect.

LLMs only process **Token IDs**, not raw text.

---

# 🎯 Interview Questions

## 1. What is Tokenization?

**Answer**

Tokenization is the process of converting text into smaller units called tokens, which are then mapped to numerical IDs for processing by an LLM.

---

## 2. Why is Tokenization required?

**Answer**

Because neural networks operate on numbers rather than text. Tokenization converts human language into a numerical representation.

---

## 3. Is one word always one token?

**Answer**

No. A word may be split into multiple sub-word tokens depending on the tokenizer.

---

## 4. Why do API providers charge per token instead of per word?

**Answer**

Because LLMs process tokens, and each token consumes computational resources during inference.

---

## 5. What happens after Tokenization?

**Answer**

The tokens are converted into Token IDs, transformed into embeddings, and then processed by the Transformer.

---

# 📝 Summary

- Tokenization converts text into tokens.
- Tokens are mapped to numerical IDs.
- LLMs work with numbers, not words.
- One word can become multiple tokens.
- Tokenization is the first step in every LLM pipeline.

---

# 🧠 Quick Revision

✅ Humans read words.

✅ Computers read numbers.

✅ Tokenization converts text into tokens.

✅ Tokens become Token IDs.

✅ Token IDs become Embeddings.

✅ Embeddings are processed by Transformers.

---

# 🔗 Related Topics

⬅ **Previous**

- Training Stages of LLMs

➡ **Next**

- Parameters & Context Window