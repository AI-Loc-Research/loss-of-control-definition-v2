# Threat Model Review: rand_loc_response_planning — S1

**Scenario text:**
> As AI systems gain greater autonomy and become more widely deployed, the conditions for LOC incidents become more likely. Delegating decisionmaking to AI systems inherently reduces opportunities for human oversight, especially in dynamic or high-speed environments. This risk is exacerbated by the complexity and opacity of advanced models, which make it difficult for humans to interpret the system’s internal reasoning or predict its behavior. Ideally, there is compatibility between a system’s capabilities and its deployment context in which AI systems operate within the bounds of their competence and humans retain meaningful opportunities to intervene. But in some cases, AI capabilities may outpace human ability to monitor or correct them in real time. Without sufficient guardrails, this mismatch might lead to unintended and potentially disruptive outcomes across interconnected systems before human operators can reassert control.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | AI systems | As AI systems gain greater autonomy and become more widely deployed; Delegating decisionmaking to AI systems; AI capabilities may outpace human ability to monitor or correct them in real time | Clear |
| Objective/Harmful Outcome | LOC incidents; unintended and potentially disruptive outcomes across interconnected systems before human operators can reassert control | the conditions for LOC incidents become more likely; Without sufficient guardrails, this mismatch might lead to unintended and potentially disruptive outcomes across interconnected systems before human operators can reassert control | Clear |
| Capability | gain greater autonomy; AI capabilities may outpace human ability to monitor or correct them in real time | AI systems gain greater autonomy; AI capabilities may outpace human ability to monitor or correct them in real time | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Delegating decisionmaking to AI systems; AI systems gain greater autonomy and become more widely deployed | Delegating decisionmaking to AI systems; AI systems gain greater autonomy and become more widely deployed | Clear |
| Constraints/Enabling Conditions | Delegating decisionmaking to AI systems inherently reduces opportunities for human oversight, especially in dynamic or high-speed environments; complexity and opacity of advanced models, which make it difficult for humans to interpret the system’s internal reasoning or predict its behavior; AI capabilities may outpace human ability to monitor or correct them in real time; Without sufficient guardrails; before human operators can reassert control; Ideally, there is compatibility between a system’s capabilities and its deployment context in which AI systems operate within the bounds of their competence and humans retain meaningful opportunities to intervene. | Delegating decisionmaking to AI systems inherently reduces opportunities for human oversight, especially in dynamic or high-speed environments; complexity and opacity of advanced models, which make it difficult for humans to interpret the system’s internal reasoning or predict its behavior; AI capabilities may outpace human ability to monitor or correct them in real time; Without sufficient guardrails; before human operators can reassert control; Ideally, there is compatibility between a system’s capabilities and its deployment context in which AI systems operate within the bounds of their competence and humans retain meaningful opportunities to intervene. | Clear |
| Target/Asset at Risk | interconnected systems; human oversight; human ability to monitor or correct them; human operators can reassert control; meaningful opportunities to intervene | interconnected systems; human oversight; human ability to monitor or correct them; human operators can reassert control; meaningful opportunities to intervene | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---