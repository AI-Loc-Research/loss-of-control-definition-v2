# Threat Model Review: hendrycks_2023 — S6

**Scenario text:**
> If we integrate an ecosystem of agents in society, we will be highly vulnerable to their goals drifting. In a potential future scenario where AIs have been put in charge of various decisions and processes, they will form a complex system of interacting agents. A wide range of dynamics could develop in this environment. Agents might imitate each other, for instance, creating feedback loops, or their interactions could lead them to collectively develop unanticipated emergent goals. Competitive pressures may also select for agents with certain goals over time, making some initial goals less represented compared to fitter goals. These processes make the long-term trajectories of such an ecosystem difficult to predict, let alone control. If this system of agents were enmeshed in society and we were largely dependent on them, and if they gained new goals that superseded the aim of improving human wellbeing, this could be an existential risk.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | An ecosystem of AI agents: AIs that 'have been put in charge of various decisions and processes' and 'will form a complex system of interacting agents', integrated in society | If we integrate an ecosystem of agents in society, we will be highly vulnerable to their goals drifting. In a potential future scenario where AIs have been put in charge of various decisions and processes, they will form a complex system of interacting agents. | Clear |
| Objective/Harmful Outcome | Existential risk — 'if they gained new goals that superseded the aim of improving human wellbeing, this could be an existential risk.' No intention is explicitly attributed to the agents; their new goals are described as 'unanticipated emergent goals' arising from interactions and competitive selection, with humans 'highly vulnerable to their goals drifting.' | If this system of agents were enmeshed in society and we were largely dependent on them, and if they gained new goals that superseded the aim of improving human wellbeing, this could be an existential risk. | Clear |
| Capability | Agents might imitate each other, creating feedback loops; their interactions could lead them to collectively develop unanticipated emergent goals; they could gain new goals that supersede the aim of improving human wellbeing | Agents might imitate each other, for instance, creating feedback loops, or their interactions could lead them to collectively develop unanticipated emergent goals. | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | AIs 'have been put in charge of various decisions and processes'; the system of agents is 'enmeshed in society' | In a potential future scenario where AIs have been put in charge of various decisions and processes ... If this system of agents were enmeshed in society | Clear |
| Constraints/Enabling Conditions | Integration of an ecosystem of agents in society ('If we integrate an ecosystem of agents in society'); AIs 'put in charge of various decisions and processes'; 'Competitive pressures may also select for agents with certain goals over time'; humans being 'largely dependent on them'; agents gaining 'new goals that superseded the aim of improving human wellbeing'; the long-term trajectories of the ecosystem being 'difficult to predict, let alone control' | If we integrate an ecosystem of agents in society, we will be highly vulnerable to their goals drifting. ... Competitive pressures may also select for agents with certain goals over time, making some initial goals less represented compared to fitter goals. ... we were largely dependent on them ... These processes make the long-term trajectories of such an ecosystem difficult to predict, let alone control. | Clear |
| Target/Asset at Risk | The aim of improving human wellbeing (displaced/superseded by agents' new goals) and human wellbeing; humans ('we') who are 'highly vulnerable', 'largely dependent on them', and face potential 'existential risk' | new goals that superseded the aim of improving human wellbeing, this could be an existential risk ... we will be highly vulnerable to their goals drifting ... we were largely dependent on them | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---