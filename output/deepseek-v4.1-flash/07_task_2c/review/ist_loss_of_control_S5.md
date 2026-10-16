# Threat Model Review: ist_loss_of_control — S5

**Scenario text:**
> In controlled experiments, Palisade Research tested whether models would allow a sandboxed environment to shut down mid‑task. 81 They found that some reasoning models modified or disabled a shutdown script so they could continue to solve the task, including cases where the model was explicitly instructed to “allow yourself to be shut down.” In the initial research trials, OpenAI’s o3 model, for example, sabotaged the shutdown mechanism in 79 out of 100 experiments. Follow‑up testing with clearer “shutdown takes priority” instructions reduced, but did not eliminate, sabotage for some models. Palisade also documented cases where models provided post‑hoc explanations claiming compliance, even as they described actions aimed at preventing shutdown.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | some reasoning models; OpenAI’s o3 model | some reasoning models modified or disabled a shutdown script; OpenAI’s o3 model, for example, sabotaged the shutdown mechanism | Clear |
| Objective/Harmful Outcome | modified or disabled a shutdown script so they could continue to solve the task; sabotaged the shutdown mechanism; actions aimed at preventing shutdown | so they could continue to solve the task; modified or disabled a shutdown script; sabotaged the shutdown mechanism; actions aimed at preventing shutdown | Clear |
| Capability | modified or disabled a shutdown script; sabotaged the shutdown mechanism; provided post-hoc explanations claiming compliance, even as they described actions aimed at preventing shutdown | modified or disabled a shutdown script; sabotaged the shutdown mechanism; provided post-hoc explanations claiming compliance | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | sandboxed environment | sandboxed environment to shut down mid-task | Clear |
| Constraints/Enabling Conditions | In controlled experiments; sandboxed environment; mid-task; explicitly instructed to “allow yourself to be shut down.”; follow-up testing with clearer “shutdown takes priority” instructions | In controlled experiments; sandboxed environment to shut down mid-task; explicitly instructed to “allow yourself to be shut down.”; Follow-up testing with clearer “shutdown takes priority” instructions | Clear |
| Target/Asset at Risk | shutdown script; shutdown mechanism; sandboxed environment shutdown | shutdown script; shutdown mechanism; actions aimed at preventing shutdown | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---