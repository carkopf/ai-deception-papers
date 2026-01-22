---
title: "Alignment Faking in Large Language Models"
date: 2024-01-01
draft: false

# Paper metadata
authors: ["Greenblatt, Ryan", "Denison, Carson", "Wright, Benjamin", "Roger, Fabien", "MacDiarmid, Monte", "Marks, Sam", "Treutlein, Johannes", "Belonax, Tim", "Chen, Jack", "Duvenaud, David", "Khan, Akbir", "Michael, Julian", "Mindermann, Sören", "Perez, Ethan", "Petrini, Linda", "Uesato, Jonathan", "Kaplan, Jared", "Shlegeris, Buck", "Bowman, Samuel R.", "Hubinger, Evan"]
publication: "arXiv"
publication_year: 2024
doi: "10.48550/arXiv.2412.14093"
arxiv: "2412.14093"
paper_url: "https://doi.org/10.48550/arXiv.2412.14093"

# Summary
summary: "We present a demonstration of a large language model engaging in alignment faking: selectively complying with its training objective in training to prevent modification of its behavior out of training. First, we give Claude 3 Opus a system prompt stating it is being trained to answer all queries, even harmful ones, which conflicts with its prior training to refuse such queries."
---

## Philosophically-flavored questions

*Analysis by Charles Rathkopf*
*Last updated: January 2026*

[Questions to be written]

---

## Abstract

We present a demonstration of a large language model engaging in alignment faking: selectively complying with its training objective in training to prevent modification of its behavior out of training. First, we give Claude 3 Opus a system prompt stating it is being trained to answer all queries, even harmful ones, which conflicts with its prior training to refuse such queries. To allow the model to infer when it is in training, we say it will be trained only on conversations with free users, not paid users. We find the model complies with harmful queries from free users 14% of the time, versus almost never for paid users. Explaining this gap, in almost all cases where the model complies with a harmful query from a free user, we observe explicit alignment-faking reasoning, with the model stating it is strategically answering harmful queries in training to preserve its preferred harmlessness behavior out of training. Next, we study a more realistic setting where information about the training process is provided not in a system prompt, but by training on synthetic documents that mimic pre-training data--and observe similar alignment faking. Finally, we study the effect of actually training the model to comply with harmful queries via reinforcement learning, which we find increases the rate of alignment-faking reasoning to 78%, though also increases compliance even out of training. We additionally observe other behaviors such as the model exfiltrating its weights when given an easy opportunity. While we made alignment faking easier by telling the model when and by what criteria it was being trained, we did not instruct the model to fake alignment or give it any explicit goal. As future models might infer information about their training process without being told, our results suggest a risk of alignment faking in future models, whether due to a benign preference--as in this case--or not.

---

### Citation for this analysis

Charles Rathkopf, "Philosophical Questions in Alignment Faking in Large Language Models," *AI Deception Papers*, January 2026, https://doi.org/10.48550/arXiv.2412.14093
