# Threat Model Review: bengio_2024 — S5

**Scenario text:**
> If AI progress continues, AI systems will eventually possess highly dangerous capabilities. Before training and deploying such systems, we need methods to assess their propensity to use these capabilities. Purely behavioral evaluations may fail for advanced AI systems: Similar to humans, they might behave differently under evaluation, faking alignment [6–8].

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | Advanced AI systems — AI systems that 'will eventually possess highly dangerous capabilities' and that 'might behave differently under evaluation, faking alignment.' | If AI progress continues, AI systems will eventually possess highly dangerous capabilities. ... Purely behavioral evaluations may fail for advanced AI systems: Similar to humans, they might behave differently under evaluation, faking alignment [6–8]. | Clear |
| Objective/Harmful Outcome | No intention or goal is explicitly stated. The explicitly described harmful outcome is that 'purely behavioral evaluations may fail for advanced AI systems' because such systems 'might behave differently under evaluation, faking alignment' — i.e., the assessment of AI systems' 'propensity to use these capabilities' (their 'highly dangerous capabilities') would fail. | Purely behavioral evaluations may fail for advanced AI systems: Similar to humans, they might behave differently under evaluation, faking alignment [6–8]. | Clear |
| Capability | AI systems 'will eventually possess highly dangerous capabilities'; advanced AI systems 'might behave differently under evaluation, faking alignment.' | AI systems will eventually possess highly dangerous capabilities. ... Similar to humans, they might behave differently under evaluation, faking alignment [6–8]. | Clear |
| Knowledge | Not specified | Similar to humans, they might behave differently under evaluation, faking alignment [6–8]. | Ambiguous |
| Access | Not specified | Purely behavioral evaluations may fail for advanced AI systems: Similar to humans, they might behave differently under evaluation, faking alignment [6–8]. | Ambiguous |
| Constraints/Enabling Conditions | (1) 'If AI progress continues' — the condition under which 'AI systems will eventually possess highly dangerous capabilities'; (2) evaluations are 'purely behavioral' (an oversight limit, which is why they 'may fail' for advanced AI systems); (3) assessment must occur 'before training and deploying such systems.' | If AI progress continues, AI systems will eventually possess highly dangerous capabilities. Before training and deploying such systems, we need methods to assess their propensity to use these capabilities. Purely behavioral evaluations may fail for advanced AI systems | Clear |
| Target/Asset at Risk | The pre-training/pre-deployment evaluation (oversight) process: 'purely behavioral evaluations' and the 'methods to assess their propensity to use these capabilities,' which 'may fail' for advanced AI systems. | Before training and deploying such systems, we need methods to assess their propensity to use these capabilities. Purely behavioral evaluations may fail for advanced AI systems | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---