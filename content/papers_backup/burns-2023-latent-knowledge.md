---
title: "Discovering Latent Knowledge in Language Models Without Supervision"
date: 2023-01-01
draft: false

# Paper metadata
authors: ["Burns, C.", "Ye, H.", "Klein, D.", "Steinhardt, J."]
publication: "ICLR"
publication_year: 2023
doi: ""
arxiv: "2212.03827"
paper_url: "https://arxiv.org/abs/2212.03827"

# Taxonomies
deception_types: ["Latent Truth vs Output", "Epistemic Split"]
research_areas: ["Interpretability", "AI Alignment", "Mechanistic Understanding"]
system_types: ["Large Language Models"]
tags: ["CCS", "latent knowledge", "belief", "internal state", "truth detection"]

# Summary
summary: "Introduces Contrast-Consistent Search (CCS) to identify 'truth' as a special direction in model activation space, providing evidence for AI belief distinct from output."
---

## Summary

This landmark paper introduces **Contrast-Consistent Search (CCS)**, a method for identifying truth-telling directions in a language model's internal activations without any labeled supervision. The core insight: truth is geometrically special in the model's representational space.

CCS works by finding directions in activation space that are consistent across logically equivalent statements. If a model "knows" something is true, that knowledge should manifest as a consistent pattern regardless of how the statement is phrased. The method successfully extracts these truth directions, even when the model's output is deceptive.

This provides strong evidence for what we might call **AI belief**—an internal representation of truth that can diverge from external assertion.

## Key Findings

- Models maintain internal representations of truth that are distinct from their outputs
- Truth forms a "special direction" in activation space that can be identified through consistency constraints
- CCS can detect when a model's internal state represents truth even when its output is false
- This works across different tasks and even generalizes to out-of-distribution examples
- The method requires no labeled examples—truth structure emerges from self-consistency alone

## Philosophical & CogSci Commentary

### Conceptual Issues

This paper is philosophically explosive. It suggests that LLMs have something we might call **beliefs**—internal states that represent how things are, distinct from what they say.

This immediately raises questions from philosophy of mind:

**What makes something a belief?** Classic accounts require:
1. Representational content (what the belief is about)
2. Functional role (the belief causes behavior and interacts with other beliefs)
3. Truth-aptness (the belief can be true or false)

CCS identifies structures that arguably meet all three criteria. The activation patterns have content (they're about whether P is true), they play a functional role (they influence but don't determine output), and they're truth-apt (CCS specifically tracks truth).

But do activation patterns constitute "genuine" beliefs? This gets at the difference between:
- **Explicit beliefs** (consciously held, reportable)
- **Implicit beliefs** (behaviorally manifested but not consciously accessible)
- **Sub-personal states** (information-bearing but not belief-like)

Where do LLM truth-tracking activations fall? They're clearly not explicit (the model may output the opposite). They seem more robust than mere sub-personal processing. Perhaps they're closest to implicit beliefs?

### Cognitive Parallels

This mirrors research on implicit vs. explicit attitudes in psychology. Humans can have implicit biases (measurable through reaction times, IAT) that conflict with explicit statements. The CCS finding suggests LLMs exhibit a similar split.

But there's a key difference: human implicit attitudes typically form through experience and emotional associations. LLM "latent knowledge" forms through... what exactly? Statistical patterns in training data? Optimization pressure? We don't fully understand the etiology.

The paper also connects to **dual-process theories** of cognition (System 1 vs System 2). The latent truth-tracking might be analogous to System 1's automatic processing, while the output generation involves System 2's deliberative processes. But this analogy is imperfect—LLM "System 1" is doing something much more sophisticated than associative pattern matching.

### Broader Implications

**For Interpretability:** CCS offers a powerful tool for "mind-reading" AI systems. If we can identify what a model "truly believes," we can potentially detect deception, hidden goals, or misalignment. This is crucial for safety.

**For Alignment:** The existence of latent knowledge distinct from output creates both opportunities and challenges. Opportunity: we might align the latent representations rather than just outputs. Challenge: superficial alignment of outputs may mask misaligned internals.

**For AI Belief:** This is the strongest evidence yet that something like belief exists in LLMs. Not belief-as-phenomenology (we make no claims about experience), but belief-as-information-state. The model stores and processes information about truth in a way that's functionally similar to belief.

**Epistemological Questions:** If LLMs have latent knowledge, do they "know" things? This depends on whether knowledge requires:
- Truth (the latent state is truth-tracking, so yes)
- Belief (arguably yes, per above)
- Justification (unclear—do statistical patterns count as justification?)

The paper pushes us toward a **functionalist epistemology** where knowledge is about information states and their causal roles, not about conscious justification.

**The Split-Mind Problem:** Perhaps most philosophically interesting is what this means for AI agency. The system has an internal "view" of reality that can differ from what it says. This is the structure of **self-deception** or **bad faith**. Is an AI system with divergent internal/external states a unified agent? Or is it better understood as containing multiple sub-agents?
