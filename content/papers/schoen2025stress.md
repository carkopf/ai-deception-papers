---
title: "Stress Testing Deliberative Alignment for Anti-Scheming Training"
date: 2025-01-01
draft: false

# Paper metadata
authors: ["Schoen, Bronson", "Nitishinskaya, Evgenia", "Balesni, Mikita", "Højmark, Axel", "Hofstätter, Felix", "Scheurer, Jérémy", "Meinke, Alexander", "Wolfe, Jason", "van der Weij, Teun", "Lloyd, Alex", "Goldowsky-Dill, Nicholas", "Fan, Angela", "Matveiakin, Andrei", "Shah, Rusheb", "Williams, Marcus", "Glaese, Amelia", "Barak, Boaz", "Zaremba, Wojciech", "Hobbhahn, Marius"]
publication: "arXiv"
publication_year: 2025
doi: "10.48550/arXiv.2509.15541"
arxiv: "2509.15541"
paper_url: "https://doi.org/10.48550/arXiv.2509.15541"

# Summary
summary: "Highly capable AI systems could secretly pursue misaligned goals -- what we call \"scheming\". Because a scheming AI would deliberately try to hide its misaligned goals and actions, measuring and mitigating scheming requires different strategies than are typically used in ML."
---

## Philosophically-flavored questions

*Analysis by Charles Rathkopf*
*Last updated: January 2026*

[Questions to be written]

---

## Abstract

Highly capable AI systems could secretly pursue misaligned goals -- what we call "scheming". Because a scheming AI would deliberately try to hide its misaligned goals and actions, measuring and mitigating scheming requires different strategies than are typically used in ML. We propose that assessing anti-scheming interventions requires at least (1) testing propensity to scheme on far out-of-distribution (OOD) tasks, (2) evaluating whether lack of scheming is driven by situational awareness, and (3) checking for robustness to pre-existing misaligned goals. We use a broad category of "covert actions" -- such as secretly breaking rules or intentionally underperforming in tests -- as a proxy for scheming, and design evaluations for covert actions. We then stress-test deliberative alignment as a case study for anti-scheming. Across 26 OOD evaluations (180+ environments), deliberative alignment reduces covert action rates (OpenAI o3: 13%->0.4%) but does not fully eliminate them. Our mitigation is also able to largely stop agents from pursuing a hidden goal previously trained into the model, but we still find misbehavior after additional red-teaming. We find that models' chain-of-thought (CoT) often demonstrates awareness of being evaluated for alignment, and show causal evidence that this awareness decreases covert behavior, while unawareness increases it. Therefore, we cannot exclude that the observed reductions in covert action rates are at least partially driven by situational awareness. While we rely on human-legible CoT for training, studying situational awareness, and demonstrating clear evidence of misalignment, our ability to rely on this degrades as models continue to depart from reasoning in standard English. We encourage research into alignment mitigations for scheming and their assessment, especially for the adversarial case of deceptive alignment, which this paper does not address.

---

### Citation for this analysis

Charles Rathkopf, "Philosophical Questions in Stress Testing Deliberative Alignment for Anti-Scheming Training," *AI Deception Papers*, January 2026, https://doi.org/10.48550/arXiv.2509.15541
