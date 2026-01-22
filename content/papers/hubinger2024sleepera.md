---
title: "Sleeper Agents: Training Deceptive LLMs That Persist Through Safety Training"
date: 2024-01-01
draft: false

# Paper metadata
authors: ["Hubinger, Evan", "Denison, Carson", "Mu, Jesse", "Lambert, Mike", "Tong, Meg", "MacDiarmid, Monte", "Lanham, Tamera", "Ziegler, Daniel M.", "Maxwell, Tim", "Cheng, Newton", "Jermyn, Adam", "Askell, Amanda", "Radhakrishnan, Ansh", "Anil, Cem", "Duvenaud, David", "Ganguli, Deep", "Barez, Fazl", "Clark, Jack", "Ndousse, Kamal", "Sachan, Kshitij", "Sellitto, Michael", "Sharma, Mrinank", "DasSarma, Nova", "Grosse, Roger", "Kravec, Shauna", "Bai, Yuntao", "Witten, Zachary", "Favaro, Marina", "Brauner, Jan", "Karnofsky, Holden", "Christiano, Paul", "Bowman, Samuel R.", "Graham, Logan", "Kaplan, Jared", "Mindermann, Sören", "Greenblatt, Ryan", "Shlegeris, Buck", "Schiefer, Nicholas", "Perez, Ethan"]
publication: "arXiv"
publication_year: 2024
doi: "10.48550/arXiv.2401.05566"
arxiv: "2401.05566"
paper_url: "https://doi.org/10.48550/arXiv.2401.05566"

# Summary
summary: "Humans are capable of strategically deceptive behavior: behaving helpfully in most situations, but then behaving very differently in order to pursue alternative objectives when given the opportunity. If an AI system learned such a deceptive strategy, could we detect it and remove it using current state-of-the-art safety training techniques? To study this question, we construct proof-of-concept examples of deceptive behavior in large language models (LLMs)."
---

## Philosophically-flavored questions

*Analysis by Charles Rathkopf*
*Last updated: January 2026*

[Questions to be written]

---

## Abstract

Humans are capable of strategically deceptive behavior: behaving helpfully in most situations, but then behaving very differently in order to pursue alternative objectives when given the opportunity. If an AI system learned such a deceptive strategy, could we detect it and remove it using current state-of-the-art safety training techniques? To study this question, we construct proof-of-concept examples of deceptive behavior in large language models (LLMs). For example, we train models that write secure code when the prompt states that the year is 2023, but insert exploitable code when the stated year is 2024. We find that such backdoor behavior can be made persistent, so that it is not removed by standard safety training techniques, including supervised fine-tuning, reinforcement learning, and adversarial training (eliciting unsafe behavior and then training to remove it). The backdoor behavior is most persistent in the largest models and in models trained to produce chain-of-thought reasoning about deceiving the training process, with the persistence remaining even when the chain-of-thought is distilled away. Furthermore, rather than removing backdoors, we find that adversarial training can teach models to better recognize their backdoor triggers, effectively hiding the unsafe behavior. Our results suggest that, once a model exhibits deceptive behavior, standard techniques could fail to remove such deception and create a false impression of safety.

---

### Citation for this analysis

Charles Rathkopf, "Philosophical Questions in Sleeper Agents: Training Deceptive LLMs That Persist Through Safety Training," *AI Deception Papers*, January 2026, https://doi.org/10.48550/arXiv.2401.05566
