# Threat Model Review: ist_loss_of_control — S14

**Scenario text:**
> Research on interpretability revealed that neural networks tend to encode more features than their design dimensions would appear to allow through a phenomenon called superposition. 44 Rather than each neuron representing a single concept, models compress multiple overlapping features into the same neurons through distributed patterns. These features are invisible when examining individual neurons; they exist only as patterns spread across the network, much like how a child’s understanding emerges from countless neural connections, not a single lesson. Manipulating these hidden features can steer model behavior in unintended ways. Thus, models end up containing representations—their creators never intended and cannot easily detect through standard interpretability methods. 45

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | neural networks; models | neural networks tend to encode more features than their design dimensions would appear to allow through a phenomenon called superposition. 44 Rather than each neuron representing a single concept, models compress multiple overlapping features into the same neurons through distributed patterns. | Clear |
| Objective/Harmful Outcome | steer model behavior in unintended ways; models end up containing representations—their creators never intended and cannot easily detect through standard interpretability methods | Manipulating these hidden features can steer model behavior in unintended ways. Thus, models end up containing representations—their creators never intended and cannot easily detect through standard interpretability methods. | Clear |
| Capability | encode more features than their design dimensions would appear to allow through a phenomenon called superposition; compress multiple overlapping features into the same neurons through distributed patterns | neural networks tend to encode more features than their design dimensions would appear to allow through a phenomenon called superposition. 44 Rather than each neuron representing a single concept, models compress multiple overlapping features into the same neurons through distributed patterns. | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | features are invisible when examining individual neurons; they exist only as patterns spread across the network; Manipulating these hidden features can steer model behavior in unintended ways; cannot easily detect through standard interpretability methods | These features are invisible when examining individual neurons; they exist only as patterns spread across the network, much like how a child’s understanding emerges from countless neural connections, not a single lesson. Manipulating these hidden features can steer model behavior in unintended ways. Thus, models end up containing representations—their creators never intended and cannot easily detect through standard interpretability methods. | Clear |
| Target/Asset at Risk | model behavior | Manipulating these hidden features can steer model behavior in unintended ways. | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---