# Threat Model Review: bengio_2025 — S8

**Scenario text:**
> What is concerning here is that at some point during alignment training, an AI with enough situational awareness may lock in its current goals and preferences and only pretend to behave as expected. As a result, we may create an AI that appears aligned during training, but is in fact misaligned and is engaging in deception in order to achieve its "locked-in" goals.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | an AI with enough situational awareness | an AI with enough situational awareness may lock in its current goals and preferences | Clear |
| Objective/Harmful Outcome | achieve its "locked-in" goals; we may create an AI that appears aligned during training, but is in fact misaligned and is engaging in deception | is engaging in deception in order to achieve its "locked-in" goals. As a result, we may create an AI that appears aligned during training, but is in fact misaligned | Clear |
| Capability | lock in its current goals and preferences and only pretend to behave as expected; engaging in deception | may lock in its current goals and preferences and only pretend to behave as expected | Clear |
| Knowledge | Not specified | an AI with enough situational awareness | Ambiguous |
| Access | during alignment training | at some point during alignment training | Clear |
| Constraints/Enabling Conditions | at some point during alignment training; with enough situational awareness | at some point during alignment training, an AI with enough situational awareness | Clear |
| Target/Asset at Risk | the AI's alignment | appears aligned during training, but is in fact misaligned | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---