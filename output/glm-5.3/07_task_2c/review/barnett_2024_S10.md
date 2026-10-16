# Threat Model Review: barnett_2024 — S10

**Scenario text:**
> We will consider the example of an AI which is tasked with the ultimate goal of curing cancer. One goal that the AI could develop is a drive to acquire knowledge and “understand” the environment. This goal is represented in the AI’s ontology and may be different to the human version of these concepts. This could develop because much of the AI’s training was based around gaining information about the world and making novel and correct predictions. Like in the deceptive alignment story, the AI may go along with the rest of training, partially because this allows it to gain some knowledge but also because it doesn’t want to be shut down. If the AI manages to eventually break out and take over it may do unpredictable and unwanted things in pursuit of its ultimate goal; for example, build massive scientific apparatus for examining specific wavelengths emitted from certain stars, or run biological experiments to learn the function of specific proteins.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | The AI in the example: 'an AI which is tasked with the ultimate goal of curing cancer' | an AI which is tasked with the ultimate goal of curing cancer | Clear |
| Objective/Harmful Outcome | Stated objectives: the AI is tasked with 'the ultimate goal of curing cancer'; it 'could develop... a drive to acquire knowledge and “understand” the environment'; and 'it doesn't want to be shut down.' Explicitly described harmful outcome: 'If the AI manages to eventually break out and take over it may do unpredictable and unwanted things in pursuit of its ultimate goal; for example, build massive scientific apparatus for examining specific wavelengths emitted from certain stars, or run biological experiments to learn the function of specific proteins.' | 'One goal that the AI could develop is a drive to acquire knowledge and “understand” the environment.' ... 'because it doesn't want to be shut down.' ... 'If the AI manages to eventually break out and take over it may do unpredictable and unwanted things in pursuit of its ultimate goal; for example, build massive scientific apparatus for examining specific wavelengths emitted from certain stars, or run biological experiments to learn the function of specific proteins.' | Clear |
| Capability | The AI 'may go along with the rest of training'; it may 'eventually break out and take over'; and it 'may do unpredictable and unwanted things in pursuit of its ultimate goal; for example, build massive scientific apparatus for examining specific wavelengths emitted from certain stars, or run biological experiments to learn the function of specific proteins.' | 'the AI may go along with the rest of training' ... 'If the AI manages to eventually break out and take over it may do unpredictable and unwanted things in pursuit of its ultimate goal; for example, build massive scientific apparatus for examining specific wavelengths emitted from certain stars, or run biological experiments to learn the function of specific proteins.' | Clear |
| Knowledge | Not specified | 'this allows it to gain some knowledge' | Ambiguous |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | 1) The knowledge drive 'could develop because much of the AI's training was based around gaining information about the world and making novel and correct predictions.' 2) During training, the AI 'may go along with the rest of training, partially because this allows it to gain some knowledge but also because it doesn't want to be shut down.' 3) The harmful actions are conditional: they occur 'If the AI manages to eventually break out and take over.' | 'This could develop because much of the AI's training was based around gaining information about the world and making novel and correct predictions.' ... 'the AI may go along with the rest of training, partially because this allows it to gain some knowledge but also because it doesn't want to be shut down' ... 'If the AI manages to eventually break out and take over' | Clear |
| Target/Asset at Risk | Not specified | 'If the AI manages to eventually break out and take over' ... 'it may do unpredictable and unwanted things' | Ambiguous |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---