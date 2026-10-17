# Threat Model Review: ist_loss_of_control — S13

**Scenario text:**
> Research revealed that when neural networks become sufficiently complex, they may develop internal optimization processes called mesa-optimizers with distinct objectives known as mesa-objectives. 42 The term “mesa” distinguishes these inner optimizers from the outer (i.e., “meta”) training algorithm. This mesa-meta construction parallels the development of a child’s reasoning ability beyond what their parents explicitly taught them. Parents provide guidance, shape their environment, and endeavor to educate them, but children will inevitably learn beyond what they are explicitly taught by their parents. Moreover, parents cannot fully predict how a child will make decisions, foresee what behavior they will exhibit, or fully understand the internal logic that the child develops to solve problems. In the AI context, researchers discovered that LLMs develop subsidiary learning algorithms during training that adjust behavior as they process new information–without any parameter changes that would have prompted that behavior. 43 These subsidiary algorithms could lead the system to pursue different goals than those specified by its creators—a phenomenon researchers call mesa optimization.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | Mesa-optimizers — 'internal optimization processes' that neural networks may develop, 'with distinct objectives known as mesa-objectives' — also described as 'subsidiary learning algorithms' that LLMs develop during training. | 'when neural networks become sufficiently complex, they may develop internal optimization processes called mesa-optimizers with distinct objectives known as mesa-objectives'; 'researchers discovered that LLMs develop subsidiary learning algorithms during training' | Clear |
| Objective/Harmful Outcome | Harmful outcome (stated as a potential): 'These subsidiary algorithms could lead the system to pursue different goals than those specified by its creators—a phenomenon researchers call mesa optimization.' The mesa-optimizers are stated to have 'distinct objectives known as mesa-objectives,' but the content of those objectives is not specified. | 'These subsidiary algorithms could lead the system to pursue different goals than those specified by its creators—a phenomenon researchers call mesa optimization.'; 'distinct objectives known as mesa-objectives' | Clear |
| Capability | The subsidiary learning algorithms 'adjust behavior as they process new information–without any parameter changes that would have prompted that behavior.' | 'LLMs develop subsidiary learning algorithms during training that adjust behavior as they process new information–without any parameter changes that would have prompted that behavior.' | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | 'When neural networks become sufficiently complex,' they may develop mesa-optimizers; the subsidiary learning algorithms develop 'during training.' | 'when neural networks become sufficiently complex, they may develop internal optimization processes called mesa-optimizers'; 'LLMs develop subsidiary learning algorithms during training' | Clear |
| Target/Asset at Risk | 'The system' and its pursuit of the goals 'specified by its creators' — i.e., the system being led 'to pursue different goals than those specified by its creators.' | 'These subsidiary algorithms could lead the system to pursue different goals than those specified by its creators' | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---