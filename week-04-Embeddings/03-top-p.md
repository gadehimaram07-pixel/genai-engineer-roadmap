# Top-p (Nucleus Sampling)

## What is Top-p?

Top-p selects the smallest set of tokens whose cumulative probability reaches a specified threshold (p).

## Example

Predicted probabilities:

the → 50%
a → 30%
an → 10%
future → 5%
AI → 5%

Top-p = 0.80

Running probability:

the → 50%

the + a → 80%

Remaining tokens:

- the
- a

## Advantages

- Adaptive to the model's confidence
- Produces more natural responses

## Difference from Top-k

Top-k:
- Fixed number of tokens

Top-p:
- Dynamic number of tokens based on cumulative probability

## Interview Note

Modern LLMs often prefer Top-p because it adapts to different probability distributions.