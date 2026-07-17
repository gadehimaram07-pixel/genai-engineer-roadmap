# 🎯 Few-Shot Prompting

> **Week:** 2  
> **Module:** Prompt Engineering  
> **Difficulty:** ⭐⭐⭐☆☆ (Intermediate)  
> **Prerequisites:** Prompt Engineering Fundamentals, System & User Prompts, Zero-Shot Prompting  
> **Estimated Reading Time:** 18–22 minutes

---

# 📑 Table of Contents

1. Introduction
2. Why Few-Shot Prompting Exists
3. What is Few-Shot Prompting?
4. How Few-Shot Prompting Works
5. Internal Working
6. Why Examples Improve Performance
7. Few-Shot vs Zero-Shot
8. Few-Shot vs Fine-Tuning
9. Prompt Structure
10. Practical Examples
11. Real-world Applications
12. Best Practices
13. Advantages
14. Limitations
15. Common Mistakes
16. Interview Questions
17. Practice Exercises
18. Quick Revision
19. Summary
20. Related Topics

---

# 📖 Introduction

Imagine you are teaching a child how to identify fruits.

Instead of simply saying:

```
Identify this fruit.
```

You first provide a few examples.

```
Apple → Fruit

Carrot → Vegetable

Banana → Fruit
```

Then you ask:

```
Potato → ?
```

Most children can now understand the pattern and answer correctly.

Large Language Models work in a very similar way.

Instead of expecting the model to infer everything from a single instruction, we provide a few demonstrations of the expected input and output.

This technique is called **Few-Shot Prompting**.

It is one of the most powerful prompting techniques because it helps the model understand exactly how you want the task to be performed.

---

# 🧠 Why Few-Shot Prompting Exists

Zero-Shot Prompting works well for many simple tasks.

However, some tasks require:

- Specific formatting
- Consistent classifications
- Particular writing styles
- Domain-specific outputs

If only an instruction is provided, the model may interpret the task differently from what the user expects.

Providing a few examples removes ambiguity and guides the model toward the desired output.

---

# 💡 What is Few-Shot Prompting?

Few-Shot Prompting is a prompting technique in which **a small number of input-output examples** are included in the prompt before asking the model to solve a new, similar task.

These examples act as demonstrations rather than training data.

The model studies the pattern in the prompt and applies it to the new input.

Unlike Fine-Tuning, the model's parameters **do not change**.

---

# ⚙️ How Few-Shot Prompting Works

The workflow is:

```
Examples
      │
      ▼
User Prompt
      │
      ▼
Tokenizer
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
Generated Response
```

The examples become part of the context window.

The model uses these examples to infer the expected pattern before generating its response.

---

# 🔍 Internal Working

Suppose the prompt is:

```
Positive → Excellent service.

Negative → Terrible experience.

Positive → Amazing quality.

Classify:

"The delivery was very fast."
```

The model notices the relationship between reviews and labels.

Instead of guessing randomly, it infers that the final review should also receive a sentiment label.

Importantly:

- The examples are **not stored permanently**.
- They exist only within the current prompt.
- After the conversation ends, they are forgotten.

---

# 🌍 Real-world Analogy

Imagine a mathematics teacher introducing multiplication.

Instead of saying:

```
Multiply 8 × 7.
```

The teacher first demonstrates:

```
2 × 3 = 6

4 × 5 = 20

6 × 7 = 42
```

Then asks:

```
8 × 7 = ?
```

The student now understands the pattern much more clearly.

Few-Shot Prompting works in exactly the same way.

---

# 🤖 Why Examples Improve Performance

Examples help the model understand:

- Expected output format
- Writing style
- Labels
- Reasoning pattern
- Classification rules

Without examples, the model has to infer everything from the instruction.

With examples, much of the ambiguity is removed.

---

# 📊 Few-Shot vs Zero-Shot

| Feature | Zero-Shot | Few-Shot |
|----------|-----------|-----------|
| Examples Provided | ❌ No | ✅ Yes |
| Easier to Write | ✅ Yes | Slightly More Effort |
| Accuracy | Good | Better |
| Consistency | Medium | High |
| Suitable for Complex Tasks | Sometimes | Yes |
| Prompt Length | Short | Longer |

---

# 📊 Few-Shot vs Fine-Tuning

Many beginners confuse these two concepts.

They are completely different.

| Few-Shot Prompting | Fine-Tuning |
|--------------------|-------------|
| Examples exist only in the prompt | Model is retrained |
| Parameters remain unchanged | Parameters are updated |
| Temporary | Permanent |
| Fast | Expensive |
| No additional training required | Requires additional training data |
| Uses Context Window | Changes Model Weights |

### Important Interview Point

Few-Shot Prompting **does not teach** the model new knowledge.

It simply guides the model during the current interaction.

Fine-Tuning actually changes the model's learned behavior by updating its parameters.

---

# 🏗 Prompt Structure

A standard Few-Shot prompt usually follows this format:

```
Instruction

↓

Example 1

↓

Example 2

↓

Example 3

↓

New Input

↓

Expected Output
```

This structure helps the model recognize the pattern before solving the new task.

---

# 💻 Practical Examples

## Example 1 – Sentiment Analysis

```
Positive → I loved the movie.

Negative → The acting was poor.

Positive → Excellent performance.

Now classify:

"The camera quality is amazing."
```

Output:

```
Positive
```

---

## Example 2 – Translation

```
English: Hello

French: Bonjour

English: Thank You

French: Merci

English: Good Morning

French:
```

The model completes:

```
Bonjour
```

---

## Example 3 – SQL Query Generation

```
Question:

Show all employees.

SQL:

SELECT * FROM employees;

Question:

Show all students.

SQL:
```

The model generates:

```
SELECT * FROM students;
```

---

## Example 4 – Code Documentation

```
Input:

def add(a,b):
    return a+b

Output:

Returns the sum of two numbers.

Now document:

def multiply(a,b):
    return a*b
```

---

# 🌍 Real-world Applications

Few-Shot Prompting is widely used in:

### Customer Support

Maintaining consistent response styles.

---

### Coding Assistants

Generating code following project conventions.

---

### Data Classification

Categorizing reviews, emails, or support tickets.

---

### Translation

Producing translations with a preferred writing style.

---

### Healthcare

Generating standardized medical summaries.

---

### Legal Applications

Maintaining consistent legal document formatting.

---

# ✅ Best Practices

- Use high-quality examples.
- Keep examples consistent.
- Demonstrate the desired format.
- Avoid contradictory examples.
- Use 2–5 examples when possible.
- Ensure examples closely match the target task.

---

# ❌ Common Mistakes

## Too Many Examples

Adding excessive examples increases token usage and may exceed the context window.

---

## Inconsistent Examples

```
Positive

Excellent

Negative

0

Positive

Happy
```

The labels are inconsistent.

---

## Poor Example Quality

If the demonstrations are incorrect, the model may imitate those mistakes.

---

## Mixing Multiple Tasks

Avoid combining unrelated demonstrations in one prompt.

---

# 🎯 Interview Questions

## 1. What is Few-Shot Prompting?

Few-Shot Prompting provides a small number of examples within the prompt to guide the model before asking it to perform a similar task.

---

## 2. Why is Few-Shot Prompting more accurate than Zero-Shot Prompting?

Because the examples reduce ambiguity and demonstrate the expected output format.

---

## 3. Does Few-Shot Prompting change model parameters?

No.

The examples exist only in the current prompt and do not modify the model's learned weights.

---

## 4. Difference between Few-Shot Prompting and Fine-Tuning?

Few-Shot uses temporary examples inside the prompt.

Fine-Tuning permanently updates the model's parameters through additional training.

---

## 5. When should Few-Shot Prompting be used?

When tasks require consistent formatting, specific reasoning patterns, or improved accuracy over Zero-Shot Prompting.

---

# 🧪 Practice Exercises

### Exercise 1

Write a Few-Shot prompt for spam email classification.

---

### Exercise 2

Design a Few-Shot prompt that converts natural language questions into SQL queries.

---

### Exercise 3

Create a Few-Shot prompt to summarize product reviews in one sentence.

---

### Exercise 4

Write a Few-Shot prompt that generates Python docstrings.

---

### Exercise 5

Create a Few-Shot prompt to classify customer feedback into:

- Complaint
- Suggestion
- Appreciation

---

# 🧠 Quick Revision

✅ Few-Shot uses a few examples.

✅ Examples exist only within the current prompt.

✅ Parameters do not change.

✅ More accurate than Zero-Shot for structured tasks.

✅ Different from Fine-Tuning.

---

# 📝 Summary

Few-Shot Prompting improves the performance of Large Language Models by providing a small number of demonstrations before asking the model to perform a new task. These examples help the model infer the expected pattern, output format, and reasoning style without modifying its internal parameters.

Compared to Zero-Shot Prompting, Few-Shot Prompting generally produces more consistent and reliable outputs, especially for tasks that involve classification, structured formatting, or specialized writing styles. However, because examples consume part of the context window, they should be chosen carefully and kept concise.

Understanding the difference between Few-Shot Prompting and Fine-Tuning is essential: **Few-Shot guides the model temporarily through examples, whereas Fine-Tuning permanently changes the model by updating its parameters.**

---

# 📚 Further Reading

- Brown et al. (2020) – *Language Models are Few-Shot Learners*
- OpenAI Prompt Engineering Guide
- Anthropic Prompt Engineering Documentation
- Google Prompt Design Guide

---

# 🔗 Related Topics

⬅ **Previous**

- Zero-Shot Prompting

➡ **Next**

- Role Prompting