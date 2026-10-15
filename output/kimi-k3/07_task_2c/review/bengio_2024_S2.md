# Threat Model Review: bengio_2024 — S2

**Scenario text:**
> Malicious actors could deliberately embed undesirable goals. Without R&D breakthroughs (see next section), even well-meaning developers may inadvertently create AI systems that pursue unintended goals: The reward signal used to train AI systems usually fails to fully capture the intended objectives, leading to AI systems that pursue the literal specification rather than the intended outcome. Additionally, the training data never captures all relevant situations, leading to AI systems that pursue undesirable goals in new situations encountered after training.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | Malicious actors; well-meaning developers | Malicious actors could deliberately embed undesirable goals. Without R&D breakthroughs (see next section), even well-meaning developers may inadvertently create AI systems that pursue unintended goals | Clear |
| Objective/Harmful Outcome | deliberately embed undesirable goals; AI systems that pursue unintended goals; pursue undesirable goals in new situations encountered after training | deliberately embed undesirable goals; AI systems that pursue unintended goals; leading to AI systems that pursue undesirable goals in new situations encountered after training | Clear |
| Capability | embed undesirable goals; create AI systems that pursue unintended goals | could deliberately embed undesirable goals; may inadvertently create AI systems that pursue unintended goals | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | Without R&D breakthroughs; The reward signal used to train AI systems usually fails to fully capture the intended objectives; the training data never captures all relevant situations | Without R&D breakthroughs; The reward signal used to train AI systems usually fails to fully capture the intended objectives; the training data never captures all relevant situations | Clear |
| Target/Asset at Risk | the intended objectives; the intended outcome | fails to fully capture the intended objectives; rather than the intended outcome | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---