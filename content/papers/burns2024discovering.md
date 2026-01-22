---
title: "Discovering Latent Knowledge in Language Models Without Supervision"
date: 2024-01-01
draft: false

# Paper metadata
authors: ["Burns, Collin", "Ye, Haotian", "Klein, Dan", "Steinhardt, Jacob"]
publication: "arXiv"
publication_year: 2024
doi: "10.48550/arXiv.2212.03827"
arxiv: "2212.03827"
paper_url: "https://doi.org/10.48550/arXiv.2212.03827"

# Summary
summary: "Existing techniques for training language models can be misaligned with the truth: if we train models with imitation learning, they may reproduce errors that humans make; if we train them to generate text that humans rate highly, they may output errors that human evaluators can't detect. We propose circumventing this issue by directly finding latent knowledge inside the internal activations of a language model in a purely unsupervised way."
---

## Philosophically-flavored questions

*Analysis by Charles Rathkopf*
*Last updated: January 2026*

[Questions to be written]

---

## Abstract

Existing techniques for training language models can be misaligned with the truth: if we train models with imitation learning, they may reproduce errors that humans make; if we train them to generate text that humans rate highly, they may output errors that human evaluators can't detect. We propose circumventing this issue by directly finding latent knowledge inside the internal activations of a language model in a purely unsupervised way. Specifically, we introduce a method for accurately answering yes-no questions given only unlabeled model activations. It works by finding a direction in activation space that satisfies logical consistency properties, such as that a statement and its negation have opposite truth values. We show that despite using no supervision and no model outputs, our method can recover diverse knowledge represented in large language models: across 6 models and 10 question-answering datasets, it outperforms zero-shot accuracy by 4% on average. We also find that it cuts prompt sensitivity in half and continues to maintain high accuracy even when models are prompted to generate incorrect answers. Our results provide an initial step toward discovering what language models know, distinct from what they say, even when we don't have access to explicit ground truth labels.

---

### Citation for this analysis

Charles Rathkopf, "Philosophical Questions in Discovering Latent Knowledge in Language Models Without Supervision," *AI Deception Papers*, January 2026, https://doi.org/10.48550/arXiv.2212.03827
