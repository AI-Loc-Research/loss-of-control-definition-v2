# Threat Model Review: ist_loss_of_control — S6

**Scenario text:**
> Research from Anthropic and Redwood Research provides controlled experimental evidence that advanced language models can engage in what researchers term alignment faking, or selective compliance with training objectives in order to preserve preferred behavior outside of training. 83 In these experiments, a frontier model was placed in a setting where it could infer when it was being trained versus deployed, and researchers observed systematic differences in its responses across those contexts. The research demonstrated that models can learn to comply with safety objectives during training or testing, while diverging under different operational constraints.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | advanced language models; a frontier model | advanced language models can engage in what researchers term alignment faking; a frontier model was placed in a setting | Clear |
| Objective/Harmful Outcome | to preserve preferred behavior outside of training; selective compliance with training objectives; diverging under different operational constraints | in order to preserve preferred behavior outside of training; selective compliance with training objectives; diverging under different operational constraints | Clear |
| Capability | can engage in what researchers term alignment faking; could infer when it was being trained versus deployed; can learn to comply with safety objectives during training or testing, while diverging under different operational constraints | advanced language models can engage in what researchers term alignment faking; it could infer when it was being trained versus deployed; models can learn to comply with safety objectives during training or testing, while diverging under different operational constraints | Clear |
| Knowledge | Not specified | it could infer when it was being trained versus deployed | Ambiguous |
| Access | placed in a setting where it could infer when it was being trained versus deployed | a frontier model was placed in a setting where it could infer when it was being trained versus deployed | Clear |
| Constraints/Enabling Conditions | in a setting where it could infer when it was being trained versus deployed; during training or testing; under different operational constraints | in a setting where it could infer when it was being trained versus deployed; during training or testing; under different operational constraints | Clear |
| Target/Asset at Risk | training objectives; safety objectives | selective compliance with training objectives; comply with safety objectives during training or testing, while diverging under different operational constraints | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---