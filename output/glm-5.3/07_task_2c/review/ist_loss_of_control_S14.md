# Threat Model Review: ist_loss_of_control — S14

**Scenario text:**
> Research on interpretability revealed that neural networks tend to encode more features than their design dimensions would appear to allow through a phenomenon called superposition. 44 Rather than each neuron representing a single concept, models compress multiple overlapping features into the same neurons through distributed patterns. These features are invisible when examining individual neurons; they exist only as patterns spread across the network, much like how a child’s understanding emerges from countless neural connections, not a single lesson. Manipulating these hidden features can steer model behavior in unintended ways. Thus, models end up containing representations—their creators never intended and cannot easily detect through standard interpretability methods. 45

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | Not specified | Manipulating these hidden features can steer model behavior in unintended ways. | Ambiguous |
| Objective/Harmful Outcome | No intention or goal is stated. Explicitly described harmful outcomes: 'Manipulating these hidden features can steer model behavior in unintended ways,' and 'models end up containing representations—their creators never intended and cannot easily detect through standard interpretability methods.' | Manipulating these hidden features can steer model behavior in unintended ways. Thus, models end up containing representations—their creators never intended and cannot easily detect through standard interpretability methods. | Clear |
| Capability | Manipulating the models' hidden features 'can steer model behavior in unintended ways' (the actor performing this manipulation is not specified in the text). | Manipulating these hidden features can steer model behavior in unintended ways. | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | Detection/oversight limits explicitly stated: the hidden features 'are invisible when examining individual neurons; they exist only as patterns spread across the network,' and the representations are ones their 'creators never intended and cannot easily detect through standard interpretability methods.' | These features are invisible when examining individual neurons; they exist only as patterns spread across the network; their creators never intended and cannot easily detect through standard interpretability methods. | Clear |
| Target/Asset at Risk | Model behavior, which can be steered 'in unintended ways'; and the models, which 'end up containing representations—their creators never intended and cannot easily detect through standard interpretability methods.' | Manipulating these hidden features can steer model behavior in unintended ways. Thus, models end up containing representations—their creators never intended and cannot easily detect through standard interpretability methods. | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---