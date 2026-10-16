# Threat Model Review: hendrycks_2023 — S6

**Scenario text:**
> If we integrate an ecosystem of agents in society, we will be highly vulnerable to their goals drifting. In a potential future scenario where AIs have been put in charge of various decisions and processes, they will form a complex system of interacting agents. A wide range of dynamics could develop in this environment. Agents might imitate each other, for instance, creating feedback loops, or their interactions could lead them to collectively develop unanticipated emergent goals. Competitive pressures may also select for agents with certain goals over time, making some initial goals less represented compared to fitter goals. These processes make the long-term trajectories of such an ecosystem difficult to predict, let alone control. If this system of agents were enmeshed in society and we were largely dependent on them, and if they gained new goals that superseded the aim of improving human wellbeing, this could be an existential risk.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | AIs | In a potential future scenario where AIs have been put in charge of various decisions and processes, they will form a complex system of interacting agents. | Clear |
| Objective/Harmful Outcome | gained new goals that superseded the aim of improving human wellbeing; existential risk | if they gained new goals that superseded the aim of improving human wellbeing, this could be an existential risk. | Clear |
| Capability | Not specified | Agents might imitate each other, for instance, creating feedback loops, or their interactions could lead them to collectively develop unanticipated emergent goals. | Ambiguous |
| Knowledge | Not specified | Not specified | Not specified |
| Access | put in charge of various decisions and processes | AIs have been put in charge of various decisions and processes | Clear |
| Constraints/Enabling Conditions | system of agents were enmeshed in society; we were largely dependent on them; they gained new goals that superseded the aim of improving human wellbeing | If this system of agents were enmeshed in society and we were largely dependent on them, and if they gained new goals that superseded the aim of improving human wellbeing, this could be an existential risk. | Clear |
| Target/Asset at Risk | society; human wellbeing; we | If this system of agents were enmeshed in society and we were largely dependent on them, and if they gained new goals that superseded the aim of improving human wellbeing, this could be an existential risk. | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---