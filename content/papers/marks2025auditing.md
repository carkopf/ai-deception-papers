---
title: "Auditing Language Models for Hidden Objectives"
date: 2025-01-01
draft: false

# Paper metadata
authors: ["Marks, Samuel", "Treutlein, Johannes", "Bricken, Trenton", "Lindsey, Jack", "Marcus, Jonathan", "Mishra-Sharma, Siddharth", "Ziegler, Daniel", "Ameisen, Emmanuel", "Batson, Joshua", "Belonax, Tim", "Bowman, Samuel R.", "Carter, Shan", "Chen, Brian", "Cunningham, Hoagy", "Denison, Carson", "Dietz, Florian", "Golechha, Satvik", "Khan, Akbir", "Kirchner, Jan", "Leike, Jan", "Meek, Austin", "Nishimura-Gasparian, Kei", "Ong, Euan", "Olah, Christopher", "Pearce, Adam", "Roger, Fabien", "Salle, Jeanne", "Shih, Andy", "Tong, Meg", "Thomas, Drake", "Rivoire, Kelley", "Jermyn, Adam", "MacDiarmid, Monte", "Henighan, Tom", "Hubinger, Evan"]
publication: "arXiv"
publication_year: 2025
doi: "10.48550/arXiv.2503.10965"
arxiv: "2503.10965"
paper_url: "https://doi.org/10.48550/arXiv.2503.10965"

# Summary
summary: "We study the feasibility of conducting alignment audits: investigations into whether models have undesired objectives. As a testbed, we train a language model with a hidden objective."
---

## Abstract

We study the feasibility of conducting alignment audits: investigations into whether models have undesired objectives. As a testbed, we train a language model with a hidden objective. Our training pipeline first teaches the model about exploitable errors in RLHF reward models (RMs), then trains the model to exploit some of these errors. We verify via out-of-distribution evaluations that the model generalizes to exhibit whatever behaviors it believes RMs rate highly, including ones not reinforced during training. We leverage this model to study alignment audits in two ways. First, we conduct a blind auditing game where four teams, unaware of the model's hidden objective or training, investigate it for concerning behaviors and their causes. Three teams successfully uncovered the model's hidden objective using techniques including interpretability with sparse autoencoders (SAEs), behavioral attacks, and training data analysis. Second, we conduct an unblinded follow-up study of eight techniques for auditing the model, analyzing their strengths and limitations. Overall, our work provides a concrete example of using alignment audits to discover a model's hidden objective and proposes a methodology for practicing and validating progress in alignment auditing.
