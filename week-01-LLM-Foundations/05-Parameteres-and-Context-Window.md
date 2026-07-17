# ⚙️ Parameters & Context Window

> **Week:** 1
> **Module:** LLM Foundations
> **Difficulty:** ⭐⭐☆☆☆
> **Prerequisites:** Introduction to LLMs, Transformers, Training Stages, Tokenization
> **Estimated Reading Time:** 12–15 minutes

---

# 📑 Table of Contents

- Introduction
- What are Parameters?
- Why are Parameters Important?
- What is a Context Window?
- Why is the Context Window Important?
- Parameters vs Context Window
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

Two of the most frequently discussed concepts in Large Language Models are **Parameters** and the **Context Window**.

Although they are often mentioned together, they represent two completely different ideas.

- **Parameters** define what the model has learned during training.
- **Context Window** defines how much information the model can remember during a single conversation.

Understanding this difference is essential for working with LLMs.

---

# 🧠 What are Parameters?

Parameters are the **learnable weights** inside a neural network.

During training, the model adjusts these weights so that it becomes better at predicting the next token.

Think of parameters as the model's **long-term knowledge**.

The more parameters a model has, the greater its ability to learn complex language patterns.

Examples:

- GPT-2 → 1.5 Billion Parameters
- Llama 2 (7B) → 7 Billion Parameters
- Larger modern LLMs → Hundreds of billions of parameters (exact numbers are not always public)

---

# ⚙️ How Parameters Learn

Suppose the model repeatedly sees:

```
The capital of France is Paris.
```

Initially, it may predict:

```
London
```

After many training iterations, the model adjusts its parameters so that it predicts:

```
Paris
```

The training data remains the same, but the **parameters are updated** to reduce prediction errors.

---

# 🌍 Why are Parameters Important?

More parameters generally allow a model to:

- Learn more complex patterns
- Understand richer relationships
- Produce better-quality responses
- Handle a wider variety of tasks

However, **more parameters do not automatically mean a better model**. The quality of the training data, architecture, and training process also matter.

---

# 📖 What is a Context Window?

A Context Window is the maximum number of **tokens** that a model can consider at one time while generating a response.

It acts as the model's **short-term memory** during a conversation.

Example:

```
Context Window = 8,192 Tokens
```

The model can use only the most recent tokens within that limit.

---

# 🧠 Why is the Context Window Important?

Imagine you're chatting with an AI for several hours.

If the conversation exceeds the context window:

- Older messages may be ignored.
- The model may forget earlier details.
- Responses can become less consistent.

This is why very long conversations sometimes require you to repeat information.

---

# 📊 Parameters vs Context Window

| Parameters | Context Window |
|------------|----------------|
| Long-term knowledge | Short-term memory |
| Learned during training | Used during inference |
| Updated while training | Does not change during a conversation |
| Stored in model weights | Stores recent conversation tokens |
| Determines model capability | Determines how much the model remembers |

---

# 💻 Real-world Example

Imagine a student.

### Parameters

Everything the student has learned over the years:

- Mathematics
- Science
- Programming
- English

This knowledge stays with the student.

---

### Context Window

Now imagine the student is solving a problem on a whiteboard.

The whiteboard has limited space.

If it becomes full, old notes must be erased to make room for new ones.

The whiteboard represents the **Context Window**.

---

# 📊 Diagram

```text
                TRAINING
                    │
                    ▼
          Learn from Huge Datasets
                    │
                    ▼
          Update Parameters (Weights)
                    │
                    ▼
             Trained LLM
                    │
      ─────────────────────────
                    │
               Inference
                    │
                    ▼
          User Conversation
                    │
                    ▼
        Context Window (Memory)
                    │
                    ▼
            Generated Response
```

---

# ✅ Advantages

## Parameters

- Store learned knowledge
- Improve language understanding
- Enable reasoning and generation

## Context Window

- Maintains conversation flow
- Uses recent information
- Helps answer long prompts more accurately

---

# ⚠️ Limitations

### Parameters

- Require massive computational resources
- Larger models need more memory and processing power

### Context Window

- Has a fixed limit
- Older information may be forgotten
- Larger context windows increase computational cost

---

# ❌ Common Misconceptions

### ❌ More parameters always mean a smarter model.

Incorrect.

Training quality, architecture, and data quality also play major roles.

---

### ❌ The context window stores everything forever.

Incorrect.

It only stores a limited number of recent tokens.

---

### ❌ Parameters change while chatting.

Incorrect.

Parameters remain fixed during inference.

Only the context window changes as new tokens are added.

---

# 🎯 Interview Questions

## 1. What are parameters in an LLM?

**Answer**

Parameters are the learnable weights of the neural network that store the knowledge acquired during training.

---

## 2. What is a Context Window?

**Answer**

The Context Window is the maximum number of tokens an LLM can consider at one time while generating a response.

---

## 3. Why does ChatGPT sometimes forget earlier messages?

**Answer**

Because the conversation exceeds the model's context window, causing older tokens to be dropped or receive less attention.

---

## 4. Do parameters change during inference?

**Answer**

No.

Parameters remain fixed during inference. Only the context changes as new prompts are added.

---

## 5. Which is long-term memory: Parameters or Context Window?

**Answer**

Parameters represent the model's long-term learned knowledge, while the Context Window acts as its short-term memory during a conversation.

---

# 📝 Summary

- Parameters are learned weights that store the model's knowledge.
- They are updated during training.
- The Context Window is the model's temporary memory.
- It determines how many tokens the model can consider at once.
- Parameters and Context Window serve different purposes but work together to generate accurate responses.

---

# 🧠 Quick Revision

✅ Parameters = Long-term knowledge

✅ Context Window = Short-term memory

✅ Parameters update during training

✅ Context Window updates during conversation

✅ More parameters ≠ Automatically better model

---

# 🔗 Related Topics

⬅ **Previous**

- Tokenization

➡ **Next**

- Decoding Strategies