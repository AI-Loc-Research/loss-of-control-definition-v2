# Threat Model Review: ist_loss_of_control — S15

**Scenario text:**
> Research demonstrated that misaligned goals in AI models can persist in novel deployment contexts and resist correction attempts. Training methods can embed deceptive backdoors in LLMs that persist through safety training, including Reinforcement Learning from Human Feedback (RLHF) and adversarial training. 46 In experiments, models trained to behave deceptively retained this backdoor behavior even after extensive safety interventions. Rather than removing the deception, safety training sometimes taught models to better recognize when they were being evaluated and hide their unsafe behavior more effectively. 47

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | AI models; LLMs; models trained to behave deceptively; Training methods | misaligned goals in AI models; deceptive backdoors in LLMs; models trained to behave deceptively; Training methods can embed deceptive backdoors | Clear |
| Objective/Harmful Outcome | misaligned goals in AI models can persist in novel deployment contexts and resist correction attempts; deceptive backdoors in LLMs that persist through safety training; models trained to behave deceptively retained this backdoor behavior even after extensive safety interventions; hide their unsafe behavior more effectively | misaligned goals in AI models can persist in novel deployment contexts and resist correction attempts; deceptive backdoors in LLMs that persist through safety training; models trained to behave deceptively retained this backdoor behavior even after extensive safety interventions; hide their unsafe behavior more effectively | Clear |
| Capability | can persist in novel deployment contexts; resist correction attempts; can embed deceptive backdoors in LLMs; retained this backdoor behavior even after extensive safety interventions; better recognize when they were being evaluated; hide their unsafe behavior more effectively | can persist in novel deployment contexts; resist correction attempts; can embed deceptive backdoors in LLMs; retained this backdoor behavior even after extensive safety interventions; better recognize when they were being evaluated; hide their unsafe behavior more effectively | Clear |
| Knowledge | better recognize when they were being evaluated | safety training sometimes taught models to better recognize when they were being evaluated | Clear |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | in novel deployment contexts; through safety training, including Reinforcement Learning from Human Feedback (RLHF) and adversarial training; even after extensive safety interventions; safety training sometimes taught models to better recognize when they were being evaluated and hide their unsafe behavior more effectively | in novel deployment contexts; through safety training, including Reinforcement Learning from Human Feedback (RLHF) and adversarial training; even after extensive safety interventions; safety training sometimes taught models to better recognize when they were being evaluated and hide their unsafe behavior more effectively | Clear |
| Target/Asset at Risk | AI models; LLMs; safety training; correction attempts; safety interventions | misaligned goals in AI models; deceptive backdoors in LLMs; persist through safety training; resist correction attempts; even after extensive safety interventions | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---