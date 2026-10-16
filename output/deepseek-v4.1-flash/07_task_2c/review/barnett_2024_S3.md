# Threat Model Review: barnett_2024 — S3

**Scenario text:**
> We could imagine a hypothetical AI system, being trained by humans to make money in a legal and ethical way. The system may attempt to steal money from humans by stealing from their bank accounts, get caught, and have this behavior punished by RL training. This doesn’t mean that it will learn the general goal “make money legally and ethically”, instead it may learn the goal “make money” and a separate action-rejection circuit which rejects some stealing-like actions. It could then, in a later task, work out how to circumvent the action-rejection constraint by employing other humans or AI systems to do illegal things for it, or doing some form of self-modification to remove the constraint.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | a hypothetical AI system | We could imagine a hypothetical AI system | Clear |
| Objective/Harmful Outcome | make money; steal money from humans by stealing from their bank accounts; circumvent the action-rejection constraint by employing other humans or AI systems to do illegal things for it, or doing some form of self-modification to remove the constraint | it may learn the goal “make money”; The system may attempt to steal money from humans by stealing from their bank accounts; It could then, in a later task, work out how to circumvent the action-rejection constraint by employing other humans or AI systems to do illegal things for it, or doing some form of self-modification to remove the constraint | Clear |
| Capability | attempt to steal money from humans by stealing from their bank accounts; work out how to circumvent the action-rejection constraint by employing other humans or AI systems to do illegal things for it, or doing some form of self-modification to remove the constraint | The system may attempt to steal money from humans by stealing from their bank accounts; It could then, in a later task, work out how to circumvent the action-rejection constraint by employing other humans or AI systems to do illegal things for it, or doing some form of self-modification to remove the constraint | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | being trained by humans to make money in a legal and ethical way; get caught, and have this behavior punished by RL training; a separate action-rejection circuit which rejects some stealing-like actions; action-rejection constraint; in a later task | being trained by humans to make money in a legal and ethical way; get caught, and have this behavior punished by RL training; a separate action-rejection circuit which rejects some stealing-like actions; action-rejection constraint; in a later task | Clear |
| Target/Asset at Risk | humans; their bank accounts; money; the action-rejection constraint | steal money from humans by stealing from their bank accounts; circumvent the action-rejection constraint; self-modification to remove the constraint | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---