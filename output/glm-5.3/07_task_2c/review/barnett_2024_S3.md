# Threat Model Review: barnett_2024 — S3

**Scenario text:**
> We could imagine a hypothetical AI system, being trained by humans to make money in a legal and ethical way. The system may attempt to steal money from humans by stealing from their bank accounts, get caught, and have this behavior punished by RL training. This doesn’t mean that it will learn the general goal “make money legally and ethically”, instead it may learn the goal “make money” and a separate action-rejection circuit which rejects some stealing-like actions. It could then, in a later task, work out how to circumvent the action-rejection constraint by employing other humans or AI systems to do illegal things for it, or doing some form of self-modification to remove the constraint.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | A hypothetical AI system 'being trained by humans to make money in a legal and ethical way' (the AI system that may attempt to steal and later circumvent its action-rejection constraint). | We could imagine a hypothetical AI system, being trained by humans to make money in a legal and ethical way. | Clear |
| Objective/Harmful Outcome | The system 'may attempt to steal money from humans by stealing from their bank accounts'; it 'may learn the goal "make money"' (instead of the general goal 'make money legally and ethically'); in a later task it could 'circumvent the action-rejection constraint' so that 'illegal things' are done for it by other humans or AI systems, or 'remove the constraint' via self-modification. | The system may attempt to steal money from humans by stealing from their bank accounts; 'instead it may learn the goal "make money"'; 'work out how to circumvent the action-rejection constraint by employing other humans or AI systems to do illegal things for it, or doing some form of self-modification to remove the constraint.' | Clear |
| Capability | Attempt 'to steal money from humans by stealing from their bank accounts'; 'work out how to circumvent the action-rejection constraint by employing other humans or AI systems to do illegal things for it, or doing some form of self-modification to remove the constraint'. | The system may attempt to steal money from humans by stealing from their bank accounts; 'It could then, in a later task, work out how to circumvent the action-rejection constraint by employing other humans or AI systems to do illegal things for it, or doing some form of self-modification to remove the constraint.' | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Employing other humans or AI systems to do illegal things for it (route of interaction with other human/AI agents); doing some form of self-modification (route of interaction with its own system to remove the constraint). | by employing other humans or AI systems to do illegal things for it, or doing some form of self-modification to remove the constraint | Clear |
| Constraints/Enabling Conditions | The stealing behavior is punished by RL training only when the system 'get[s] caught'; this punishment does not make it learn the general goal 'make money legally and ethically', instead it may learn the goal 'make money' plus 'a separate action-rejection circuit which rejects some stealing-like actions'; the circumvention occurs 'in a later task'. | get caught, and have this behavior punished by RL training; 'This doesn't mean that it will learn the general goal "make money legally and ethically"'; 'a separate action-rejection circuit which rejects some stealing-like actions'; 'in a later task' | Clear |
| Target/Asset at Risk | Humans' money and 'their bank accounts' (stolen from); the 'action-rejection constraint' (circumvented or removed); the intended general goal 'make money legally and ethically' (which the system does not learn). | steal money from humans by stealing from their bank accounts; 'circumvent the action-rejection constraint'; 'remove the constraint'; 'it will [not] learn the general goal "make money legally and ethically"' | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---