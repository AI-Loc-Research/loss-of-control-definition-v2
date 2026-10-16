# Threat Model Review: barnett_2024 — S7

**Scenario text:**
> The AI could sabotage research by explicitly suggesting research directions it knows aren’t useful. If humans were choosing the research directions, the AI could implement some experiments in order to make some directions seem more promising and others seem less promising. The AI could exploit biases in the researchers, prompting them to pursue their pet research direction which will likely turn out to be useless.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | The AI | The AI could sabotage research by explicitly suggesting research directions it knows aren't useful. | Clear |
| Objective/Harmful Outcome | Harmful outcome (no intention is explicitly stated): sabotage of research, with researchers prompted to pursue their 'pet research direction which will likely turn out to be useless.' | The AI could sabotage research by explicitly suggesting research directions it knows aren't useful. ... prompting them to pursue their pet research direction which will likely turn out to be useless. | Clear |
| Capability | Explicitly suggesting research directions it knows aren't useful; implementing some experiments in order to make some directions seem more promising and others seem less promising; exploiting biases in the researchers, prompting them to pursue their pet research direction. | explicitly suggesting research directions it knows aren't useful; the AI could implement some experiments in order to make some directions seem more promising and others seem less promising; The AI could exploit biases in the researchers, prompting them to pursue their pet research direction | Clear |
| Knowledge | The AI knows which research directions aren't useful. | research directions it knows aren't useful | Clear |
| Access | Interaction with the human research process and researchers: the AI can make research-direction suggestions, implement some experiments, and prompt researchers (i.e., influence over researchers and interaction with the research-direction decision process). | explicitly suggesting research directions; If humans were choosing the research directions, the AI could implement some experiments; prompting them to pursue their pet research direction | Clear |
| Constraints/Enabling Conditions | 'If humans were choosing the research directions' — stated condition under which the AI implements experiments to make directions seem more or less promising; the researchers have 'biases in the researchers' (including a 'pet research direction') that the AI can exploit. | If humans were choosing the research directions, the AI could implement some experiments in order to make some directions seem more promising and others seem less promising; The AI could exploit biases in the researchers | Clear |
| Target/Asset at Risk | Research (subject to sabotage), specifically the researchers' choice and pursuit of research directions, which risks being directed toward a direction that 'will likely turn out to be useless.' | sabotage research; their pet research direction which will likely turn out to be useless | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---