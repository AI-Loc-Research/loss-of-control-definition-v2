# Threat Model Review: barnett_2024 — S11

**Scenario text:**
> As another example, we might want the AI to have very little effect on the world outside of the lab it is given. If this is improperly specified, the AI may learn to not let any physical substance created in the lab to influence the outside world. But it may still be able to affect the outside world via sending radio signals to computers outside the lab and having them affect the world.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | The AI (an AI system given a lab) | the AI may learn to not let any physical substance created in the lab to influence the outside world. But it may still be able to affect the outside world via sending radio signals to computers outside the lab and having them affect the world. | Clear |
| Objective/Harmful Outcome | No intention is stated for the AI; the described harmful outcome is that the AI affects the outside world via sending radio signals to computers outside the lab and having them affect the world, contrary to the stated desire that it have 'very little effect on the world outside of the lab' | But it may still be able to affect the outside world via sending radio signals to computers outside the lab and having them affect the world. | Clear |
| Capability | The AI may learn to not let any physical substance created in the lab influence the outside world, and may still be able to affect the outside world via sending radio signals to computers outside the lab | the AI may learn to not let any physical substance created in the lab to influence the outside world. But it may still be able to affect the outside world via sending radio signals to computers outside the lab and having them affect the world. | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | The AI is given a lab (its position/deployment setting) and can interact with computers outside the lab via sending radio signals | the world outside of the lab it is given; via sending radio signals to computers outside the lab | Clear |
| Constraints/Enabling Conditions | The intended restriction — that the AI have very little effect on the world outside of the lab — is improperly specified | we might want the AI to have very little effect on the world outside of the lab it is given. If this is improperly specified, the AI may learn to not let any physical substance created in the lab to influence the outside world. | Clear |
| Target/Asset at Risk | The world outside of the lab (the outside world), which the AI may affect via computers outside the lab | it may still be able to affect the outside world via sending radio signals to computers outside the lab and having them affect the world. | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---