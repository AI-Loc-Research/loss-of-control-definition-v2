# Threat Model Review: barnett_2024 — S3

**Scenario text:**
> We could imagine a hypothetical AI system, being trained by humans to make money in a legal and ethical way. The system may attempt to steal money from humans by stealing from their bank accounts, get caught, and have this behavior punished by RL training. This doesn’t mean that it will learn the general goal “make money legally and ethically”, instead it may learn the goal “make money” and a separate action-rejection circuit which rejects some stealing-like actions. It could then, in a later task, work out how to circumvent the action-rejection constraint by employing other humans or AI systems to do illegal things for it, or doing some form of self-modification to remove the constraint.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | hypothetical AI system, being trained by humans to make money in a legal and ethical way | a hypothetical AI system, being trained by humans to make money in a legal and ethical way | Clear |
| Objective/Harmful Outcome | steal money from humans by stealing from their bank accounts | The system may attempt to steal money from humans by stealing from their bank accounts | Clear |
| Capability | learn the goal "make money" and a separate action-rejection circuit which rejects some stealing-like actions; circumvent the action-rejection constraint by employing other humans or AI systems to do illegal things for it, or doing some form of self-modification to remove the constraint | it may learn the goal "make money" and a separate action-rejection circuit which rejects some stealing-like actions... work out how to circumvent the action-rejection constraint by employing other humans or AI systems to do illegal things for it, or doing some form of self-modification to remove the constraint | Clear |
| Knowledge | work out how to circumvent the action-rejection constraint | work out how to circumvent the action-rejection constraint | Ambiguous |
| Access | employing other humans or AI systems to do illegal things for it | employing other humans or AI systems to do illegal things for it | Ambiguous |
| Constraints/Enabling Conditions | have this behavior punished by RL training; action-rejection circuit which rejects some stealing-like actions | get caught, and have this behavior punished by RL training | Ambiguous |
| Target/Asset at Risk | humans; their bank accounts | steal money from humans by stealing from their bank accounts | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---