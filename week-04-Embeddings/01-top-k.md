# Top-k Sampling

## What is Top-k?

Top-k limits the model to selecting the next token from only the top K highest-probability tokens.

## Example

If the predicted probabilities are:

the → 45%
a → 25%
an → 15%
becoming → 10%
future → 5%

Top-k = 3

Remaining tokens:

- the
- a
- an

The remaining tokens are discarded.

## Advantages

- Reduces unlikely token selection
- Makes responses more controlled

## Limitations

- Always keeps exactly K tokens
- Not adaptive to probability distribution

## Interview Note

Top-k controls the number of candidate tokens considered during generation.