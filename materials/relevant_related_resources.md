
# Reading list: AI loss-of-control threat modelling, risk modelling and methods

Compiled 2026-10-05. Every URL was opened, or seen in search results from the official host. The headline quotes in Part A were checked against the downloaded PDF text. Items that couldn't be verified are listed at the end.

Tags: **[M]** Must-read · **[U]** Useful · **[O]** Optional

---

## PATH

**PHASE 1: the landscape and the reviewers' question ("is threat modelling right for LoC?")**

1. International AI Safety Report 2026: §2.2.2 "Loss of control" + §3.2 (risk identification)
2. EU GPAI Code of Practice: Safety & Security chapter (LoC as a systemic risk; "risk modelling … often used interchangeably with … threat modelling")
3. Google DeepMind: *An Approach to Technical AGI Safety and Security* (§5.2.1 threat modelling; how they map LoC onto misalignment/structural risk)
4. Anthropic: Risk Report, August 2026 (autonomy threat models 1 & 2; "Claim 7: Threat modeling is sufficient")
5. Stix et al.: *The Loss of Control Playbook* (Deviation / Bounded / Strict LoC; Deployment–Affordances–Permissions)

**PHASE 2: methods behind the reviewer response (validation and context)**
6. Pangakis et al.: *Automated Annotation with Generative AI Requires Validation* _[VERY IMPORTANT] =>_ describe workflow for validating LLM labels against human labels.

7. Lombard et al. 2002 + O'Connor & Joffe 2020 (how to report intercoder reliability)
8. Feinstein & Cicchetti 1990 (high agreement but low kappa; matters because knowledge is rare)
9. Yao et al. 2019 DocRED (≥40.7% of relations need cross-sentence reasoning; supports the context concern)

**PHASE 3: where the project goes next (causal diagrams and quantitative risk)**
10. SaferAI: *A Methodology for Quantitative AI Risk Modeling*
11. SaferAI (Carlucci et al.): *Exploring Systems-Thinking Approaches to Loss of Control Risk* (says the quantitative pipeline "breaks down" for LoC)
12. Hosseinichimeh et al.: *From text to map* (LLM → causal loop diagram)
13. Tomoaia-Cotisel et al. 2022: RIQA, and Zhang & Soh 2024: EDC

---

# PART A: Landscape and trends (who works on what)

## Headline for the reviewer question

- **Anthropic** (Risk Report, Aug 2026) organises its LoC analysis as named threat models: "Autonomy threat model 1: Misalignment in high-stakes settings" and "Autonomy threat model 2: Risks from automated R&D". It includes "Claim 7: Threat modeling is sufficient".
- **OpenAI** (Preparedness Framework v2): "In each area, we develop and maintain a threat model…". Long-range Autonomy and ARA are Research Categories because their threat models are "not yet sufficiently mature".
- **Google DeepMind** (FSF 3.1) uses "threat models" / "threat modeling research". The *Approach* paper says "we do not discuss loss of control as its own category". It maps LoC onto misalignment, misuse and structural risk, and treats a misaligned model "as an untrusted insider".
- **EU GPAI Code of Practice**: systemic risk modelling is "often used interchangeably with the term 'threat modelling'". It requires scenarios, modelling, and probability/severity estimates for loss of control.
- **International AI Safety Report 2026** names threat modelling as a key identification method and lists a "lack of detailed threat modelling" as an LoC evidence gap. It names Criticality, Access and Permissions as deployment factors.
- **METR** uses a "rogue replication threat model" and a means / motive / opportunity framing.
- **Counterpoint:** SaferAI's 2026 LoC paper says every stage of the quantitative risk-modelling pipeline "breaks down" for LoC: there's no decomposition framework, the historical precedent rate is zero, and propensity evaluations are immature.

## 1. SaferAI

- **A Methodology for Quantitative AI Risk Modeling.** Murray, Barrett, Papadatos, Quarks, Smith, Tlaie Boria, Touzet, Campos. Dec 2025. https://arxiv.org/abs/2512.08844
  - Six steps: scenarios → factors → baseline → indicators (KRIs) → mapping → aggregation. Loss of control is explicitly in scope. **[M]**
- **Toward Quantitative Modeling of Cybersecurity Risks Due to AI Misuse.** Barrett, Murray, Quarks, Smith, Kryś, Campos et al. Dec 2025. https://arxiv.org/abs/2512.08864
  - Nine cyber risk models; benchmarks mapped to factors via a Delphi study + LLM-simulated experts. The worked example to adapt. **[M]**
- **LLM-simulated expert judgement for quantitative AI risk estimation** (technical report). Quarks, Tlaie Boria, Kryś, Campos, Papadatos. Dec 2025. https://www.safer-ai.org/technical-report-llm-simulated-expert-judgement-for-quantitative-ai-risk-estimation **[U]**
- **Mapping AI Benchmark Data to Quantitative Risk Estimates Through Expert Elicitation.** Murray et al. Mar 2025. https://arxiv.org/abs/2503.04299 **[O]**
- **Exploring Systems-Thinking Approaches to Loss of Control Risk.** Carlucci, Fillingham, Walpole, Kryś. Jun 2026 (ICML 2026 TAIG workshop). https://arxiv.org/abs/2606.13474
  - STPA / STECA / FRAM applied to LoC; explains why quantitative modelling breaks down. **[M]**
- **STAMP/STPA Informed Characterization of Factors Leading to Loss of Control in AI Systems.** Barrett, Bruvere, Fillingham, Rhodes, Vergani. Dec 2025. https://arxiv.org/abs/2512.17600 **[M]**
- **A Frontier AI Risk Management Framework.** Campos, Papadatos, Roger, Touzet, Quarks, Murray. Feb 2025. https://arxiv.org/abs/2502.06656 **[M]**
- **Open Problems in AI Risk Modeling.** Jackson et al. Sep 2026. https://arxiv.org/abs/2609.03178 **[U]**
- **Lessons from External Review of DeepMind's Scheming Inability Safety Case.** Barrett et al. Apr 2026. https://arxiv.org/abs/2604.21964 **[U]**
- **Evaluating AI Providers' Frontier Safety Frameworks.** Stelling et al. Dec 2025. https://arxiv.org/abs/2512.01166 **[O]**
- **GLM-5.2 Risk Evaluation Report.** SaferAI. Aug 2026. https://www.safer-ai.org/research/glm-5-2-evaluation-report **[O]**

## 2. Google DeepMind

- **Frontier Safety Framework v3.1.** Apr 2026. https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf
  - Merged "ML R&D and Misalignment" domain; "Stealth and Situational Awareness" capability level. **[M]**
- **An Approach to Technical AGI Safety and Security.** Shah et al. Apr 2025. https://arxiv.org/abs/2504.01849 **[M]**
- **Evaluating Frontier Models for Stealth and Situational Awareness.** Phuong et al. May 2025. https://arxiv.org/abs/2505.01420 **[U]**
- **Clarifying AI X-risk.** Kenton, Shah et al. (DeepMind AGI safety team). 2022, Alignment Forum. https://www.alignmentforum.org/posts/GctJD5oCDRxCspEaZ/clarifying-ai-x-risk
  - Categorises LoC threat models by technical cause and path. **[U]**

## 3. RAND

- **The Case for AI Loss of Control Response Planning and an Outline to Get Started.** Boudreaux, Vermeer, Horton, Kalra. Oct 2025. https://www.rand.org/pubs/perspectives/PEA4232-1.html **[M]**
- **Strengthening Emergency Preparedness and Response for AI Loss of Control Incidents.** Somani et al. (RAND Europe). 2025. https://www.rand.org/pubs/research_reports/RRA3847-1.html **[M]**
- **Not Just Superintelligence: The Many Other Ways We May Lose Control of AI.** Predd, Kalra, Boudreaux. Jul 2025. https://geopoliticsagi.substack.com/p/not-just-superintelligence-the-many **[U]**
- **Finding Common Ground in AGI Strategy Debates.** Predd et al. Mar 2026. https://www.rand.org/pubs/perspectives/PEA4448-1.html **[O]**

## 4. UK AI Security Institute

- **AISI Research Agenda.** May 2025. https://www.aisi.gov.uk/research-agenda
  - Threat models; Fault Tree Analysis and STPA for autonomy risks; control safety cases. **[M]**
- **A sketch of an AI control safety case.** Korbak, Clymer, Hilton, Shlegeris, Irving. Jan 2025. https://arxiv.org/abs/2501.17315 **[U]**
- **Frontier AI Trends Report.** 2025. https://www.aisi.gov.uk/frontier-ai-trends-report **[U]**
- **Loss of Oversight: How AI systems may become harder to audit, monitor, and investigate.** May 2026. https://www.aisi.gov.uk/research/loss-of-oversight-how-ai-systems-may-become-harder-to-audit-monitor-and-investigate **[U]**
- **Alignment Project: Empirical Investigations Into AI Monitoring and Red Teaming.** https://alignmentproject.aisi.gov.uk/research-area/empirical-investigations-into-ai-monitoring-and-red-teaming **[O]**

## 5. Apollo Research

- **The Loss of Control Playbook: Degrees, Dynamics, and Preparedness.** Stix, Hallensleben, Ortega, Pistillo. Nov 2025. https://arxiv.org/abs/2511.15846 **[M]**
- **Frontier Models are Capable of In-context Scheming.** Meinke et al. Dec 2024. https://arxiv.org/abs/2412.04984 **[U]**
- **Towards evaluations-based safety cases for AI scheming.** Balesni et al. Nov 2024. https://arxiv.org/abs/2411.03336 **[U]**
- **Stress Testing Deliberative Alignment for Anti-Scheming Training.** Schoen et al. (OpenAI + Apollo). Sep 2025. https://arxiv.org/abs/2509.15541 **[O]**

## 6. International AI Safety Report 2026

- **International AI Safety Report 2026.** Bengio (chair) et al. Feb 2026. https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026 · https://arxiv.org/abs/2602.21012 **[M]**

## 7. METR / Anthropic / OpenAI

- **Common Elements of Frontier AI Safety Policies (Dec 2025).** METR. https://metr.org/blog/2025-12-09-common-elements-of-frontier-ai-safety-policies/ **[U]**
- **The Rogue Replication Threat Model.** METR. Nov 2024. https://metr.org/blog/2024-11-12-rogue-replication-threat-model/ **[U]**
- **Frontier Risk Report (Feb–Mar 2026).** METR. May 2026. https://metr.org/blog/2026-05-19-frontier-risk-report/
  - Means / motive / opportunity assessment of rogue deployment. **[M]**
- **Measuring AI Ability to Complete Long Tasks.** Kwa et al. Mar 2025. https://arxiv.org/abs/2503.14499 **[O]**
- **Responsible Scaling Policy (v3.x).** Anthropic. https://www.anthropic.com/responsible-scaling-policy **[U]**
- **Risk Report: August 2026.** Anthropic. https://anthropic.com/aug-2026-risk-report **[M]**
- **Sabotage Risk Report: Claude Opus 4.6.** Anthropic. Feb 2026. https://anthropic.com/claude-opus-4-6-risk-report **[U]**
- **Preparedness Framework v2.** OpenAI. Apr 2025. https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf **[M]**

## 8. Taxonomies

- **The AI risk repository.** Slattery et al. *Patterns* 7(5), 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC13161690/ (arXiv https://arxiv.org/abs/2408.12622)
  - Causal Taxonomy (Entity / Intent / Timing) + Domain Taxonomy. **[M]**
- **Dimensional Characterization and Pathway Modeling for Catastrophic AI Risks.** Chin. Aug 2025. https://arxiv.org/abs/2508.06411
  - This paper is in the phase-1 corpus. **[U]**
- **Reframing AI Loss of Control: What Control Is, How to Have It, How to Lose It.** Chin, Chiodo, Müller, Snell. 2026. https://arxiv.org/abs/2606.12442
  - Control theory and cybernetics foundations. **[U]**

## 9. IST and the EU

- **AI Loss of Control Risk: Indications & Warning.** Tkeshelashvili, Verma, Kelly (IST). Feb 2026. https://securityandtechnology.org/virtual-library/report/ai-loss-of-control-risk-indications-warning/
  - This paper is in the phase-1 corpus. **[U]**
- **GPAI Code of Practice: Safety and Security Chapter.** European Commission. Jul 2025. https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai **[M]**

## 10. Systemic / gradual LoC

- **Gradual Disempowerment.** Kulveit et al. Jan 2025. https://arxiv.org/abs/2501.16946 **[M]**
- **Two types of AI existential risk: decisive and accumulative.** Kasirzadeh. *Philosophical Studies* 2025. https://link.springer.com/article/10.1007/s11098-025-02301-3 **[U]**

## Other credible additions

- **Safety Cases: How to Justify the Safety of Advanced AI Systems.** Clymer et al. 2024. https://arxiv.org/abs/2403.10462 **[U]**
- **AI Control: Improving Safety Despite Intentional Subversion.** Greenblatt et al. 2023. https://arxiv.org/abs/2312.06942 **[U]**
- **Risk assessment at AGI companies.** Koessler & Schuett. 2023. https://arxiv.org/abs/2307.08823 **[O]**
- **Dark Speculation: Combining Qualitative and Quantitative Understanding in Frontier AI Risk Analysis.** Carpenter et al. Nov 2025. https://arxiv.org/abs/2511.21838 **[O]**
- **AI Loss of Control Incident Management: Response & Resilience.** Gruetzemacher. May 2026. https://arxiv.org/abs/2605.30406 **[O]**

---

# PART B: Methods (how similar work is done)

## B1. LLM → causal map / causal loop diagram extraction

- **From text to map: a system dynamics bot for constructing causal loop diagrams.** Hosseinichimeh, Majumdar, Williams, Ghaffarzadegan. *System Dynamics Review* 2024. https://onlinelibrary.wiley.com/doi/full/10.1002/sdr.1782 (preprint https://arxiv.org/abs/2402.11400; code https://github.com/bear96/System-Dynamics-Bot/) **[M]**
- **Benchmarking and Assessing Transformations Between Text and Causal Maps via LLMs.** Giabbanelli, Gandee, Agrawal, Hosseinichimeh. *Applied Ontology* 2025. https://journals.sagepub.com/doi/10.1177/15705838241304102 **[M]**
- **Measuring Similarity in Causal Graphs.** Liu, Yang, Jalali. 2025. https://arxiv.org/abs/2503.11046 **[M]**
- **Generative AI for systems thinking: can a GPT question-answering system turn text into the causal maps produced by human readers?** Giabbanelli & Witkowicz. HICSS-57, 2024. https://scholarspace.manoa.hawaii.edu/server/api/core/bitstreams/67a1fb0f-c263-44d0-b9b1-b832a5da8afa/content **[U]**
- **The Qualitative Engine: Creating and Evaluating an Iterative AI Modeling Tool.** Schoenberg et al. *SDR* 2026. https://onlinelibrary.wiley.com/doi/10.1002/sdr.70025 (BEAMS benchmark: https://arxiv.org/abs/2605.28994) **[U]**
- **Leveraging LLMs for Automated Causal Loop Diagram Generation.** Liu & Keith. 2025. https://arxiv.org/abs/2503.21798 **[U]**
- **From text to model: Leveraging NLP for system dynamics model development.** Veldhuis. *SDR* 2024. https://onlinelibrary.wiley.com/doi/full/10.1002/sdr.1780 **[U]**
- **Benchmarking System Dynamics AI Assistants: Cloud vs Local LLMs on CLD Extraction.** Leitch. 2026. https://arxiv.org/abs/2604.18566 **[O]**

## B2. Classic text → causal map methods

- **Kim & Andersen 2012**, purposive text analysis, *SDR* 28:311–328. https://www.semanticscholar.org/paper/Building-confidence-in-causal-maps-generated-from-Kim-Andersen/437557e70f0fd8aabd984f2dc37c640ac498062a (PDF in `LOC-Scenario/materials/`) **[M]**
- **Tomoaia-Cotisel et al. 2022**, RIQA, *SDR* 38(1):41–80. https://onlinelibrary.wiley.com/doi/10.1002/sdr.1701 **[M]**
- **Eker & Zimmermann 2016**, Using Textual Data in System Dynamics Model Conceptualization, *Systems* 4(3). https://www.mdpi.com/2079-8954/4/3/28 **[U]**
- **Newberry & Carhart 2024**, Constructing causal loop diagrams from large interview data sets, *SDR*. https://pmc.ncbi.nlm.nih.gov/articles/PMC7616860/
  - Semi-automated search missed implicit causality. **[U]**
- **Kunc 2024**, Integrating system dynamics and scenarios, *Futures & Foresight Science*. https://onlinelibrary.wiley.com/doi/abs/10.1002/ffo2.174 **[U]**
- **Kenzie 2025**, *Systems Research and Behavioral Science*. https://onlinelibrary.wiley.com/doi/full/10.1002/sres.3030 **[O]**
- **Turner et al. 2013**, *SDR*. https://onlinelibrary.wiley.com/doi/abs/10.1002/sdr.1506 **[O]**

## B3. LLM extraction and canonicalisation

- **Extract, Define, Canonicalize (EDC).** Zhang & Soh. EMNLP 2024. https://arxiv.org/abs/2404.03868 (code https://github.com/clear-nus/edc) **[M]**
- **Structured information extraction from scientific text with LLMs.** Dagdelen et al. *Nature Communications* 2024. https://www.nature.com/articles/s41467-024-45563-x **[M]**
- **Integration of large-scale community-developed causal loop diagrams: an NLP approach to merging factors based on semantic similarity.** *BMC Public Health* 2025. https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-025-22142-3 **[M]**
- **Can Large Language Models Infer Causal Relationships from Real-World Text?** Saklad et al. 2025. https://arxiv.org/abs/2505.18931
  - The best model reaches only about 0.535 F1. **[U]**
- **Are Large Language Models Effective Knowledge Graph Constructors?** Chen et al. 2025. https://arxiv.org/abs/2510.11297 **[O]**

## B4. LLMs as annotators and how to validate them

- **Can Large Language Models Transform Computational Social Science?** Ziems et al. *Computational Linguistics* 2024. https://aclanthology.org/2024.cl-1.8/ **[M]**
- **Automated Annotation with Generative AI Requires Validation.** Pangakis, Wolken, Fasching. 2023. https://arxiv.org/abs/2306.00176 **[M]**
- **Best Practices for Text Annotation with Large Language Models.** Törnberg. *Sociologica* 2024. https://sociologica.unibo.it/article/view/19461
  - Don't tune prompts on the validation set: keep the 25 held out. **[M]**
- **ChatGPT outperforms crowd workers for text-annotation tasks.** Gilardi, Alizadeh, Kubli. *PNAS* 2023. https://www.pnas.org/doi/10.1073/pnas.2305016120 **[U]**
- **Large Language Model Hacking.** Baumann et al. 2025. https://arxiv.org/abs/2509.08825 **[U]**
- **LLMs instead of Human Judges?** Bavaresco et al. ACL 2025. https://aclanthology.org/2025.acl-short.20/ **[U]**
- **Codebook LLMs: Evaluating LLMs as Measurement Tools for Political Science Concepts.** Halterman & Keith. *Political Analysis* 2026. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7B323A0E47F782F2698A0AE849EA00DE/S104719872510017Xa.pdf/codebook_llms_evaluating_llms_as_measurement_tools_for_political_science_concepts.pdf **[U]**

## B5. Intercoder reliability

- **Hayes & Krippendorff 2007**, Krippendorff's alpha. https://www.semanticscholar.org/paper/Answering-the-Call-for-a-Standard-Reliability-for-Hayes-Krippendorff/9bae51fce09dd0ce3d5202e340002b79871c78e8 **[M]**
- **Lombard, Snyder-Duch, Bracken 2002**, reporting checklist. https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-2958.2002.tb00826.x **[M]**
- **O'Connor & Joffe 2020**, Intercoder Reliability in Qualitative Research. https://discovery.ucl.ac.uk/id/eprint/10091273/ **[M]**
- **Feinstein & Cicchetti 1990**, High agreement but low kappa. https://www.jclinepi.com/article/0895-4356(90)90158-L/abstract **[M]**
- **Gwet 2008**, the AC1 coefficient (robust to the low-prevalence problem). https://www.semanticscholar.org/paper/Computing-inter-rater-reliability-and-its-variance-Gwet/087be7b3d737ee817b64246e7c9a4fb6cd57dc24 **[U]**

## B6. Threat-modelling frameworks for AI

- **Papernot et al. 2018**, SoK: Security and Privacy in ML. https://www.semanticscholar.org/paper/SoK:-Security-and-Privacy-in-Machine-Learning-Papernot-Mcdaniel/29524f145db94cab2336da99f157e869d805dead **[M]**
- **NIST AI 100-2 E2025**, Adversarial ML taxonomy. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf **[M]**
- **Verma et al.**, Operationalizing a Threat Model for Red-Teaming LLMs. *TMLR* 2025. https://arxiv.org/abs/2407.14937 **[U]**
- **MITRE ATLAS.** https://atlas.mitre.org/ **[O]**

## B7. Scenario analysis and quantitative AI risk modelling

- **The Role of Risk Modeling in Advanced AI Risk Management.** Touzet et al. (SaferAI). 2025. https://arxiv.org/abs/2512.08723 **[M]**
- **ASI-PATH.** Barrett & Baum 2016/2017. https://sethbaum.com/ac/2017_AI-Pathways.html
  - This paper is in the phase-1 corpus. **[U]**
- **Adapting Probabilistic Risk Assessment for AI.** Wisakanto et al. 2025. https://arxiv.org/abs/2504.18536 **[U]**
- **Examining the differential risk from high-level AI and the question of control.** Kilian, Ventura, Bailey. *Futures* 2023. https://www.sciencedirect.com/science/article/abs/pii/S0016328723000861 **[U]**
- **Scalable Delphi: LLMs for Structured Risk Estimation.** Lorenz & Fritz. 2026. https://arxiv.org/abs/2602.08889 **[U]**
- **Prioritization of Risks from AI: A Delphi Study of 272 International Experts.** Saeri et al. 2026. https://arxiv.org/abs/2606.04490 **[O]**
- **MTAIR.** Clarke et al. 2022. https://ui.adsabs.harvard.edu/abs/2022arXiv220609360C/abstract **[O]**

## B8. Context effects (short passage vs full document)

- **Lost in the Middle.** Liu et al. *TACL* 2024. https://aclanthology.org/2024.tacl-1.9/ **[M]**
- **DocRED.** Yao et al. ACL 2019. https://aclanthology.org/P19-1074/ **[M]**
- **Context Length Alone Hurts LLM Performance Despite Perfect Retrieval.** Du et al. EMNLP Findings 2025. https://arxiv.org/abs/2510.05381 **[M]**
- **NoLiMa.** Modarressi et al. ICML 2025. https://arxiv.org/abs/2502.05167 **[U]**
- **RULER.** Hsieh et al. COLM 2024. https://arxiv.org/abs/2404.06654 **[U]**

---

## Could not verify (not used above)

- Performance of LLMs in data extraction for evidence synthesis (systematic review). https://pubmed.ncbi.nlm.nih.gov/42501879/ (authors and year not retrieved)
- LLM-Powered, Expert-Refined Causal Loop Diagramming via Pipeline Algebra, MDPI *Systems* 13(9):784. https://www.mdpi.com/2079-8954/13/9/784 (authors unconfirmed)
- Validating LLM-as-a-Judge Systems under Rating Indeterminacy, NeurIPS 2025 poster. https://neurips.cc/virtual/2025/poster/117308 (authors unconfirmed)
- OpenAI, "Our framework for reporting model misalignment" (Sep 2026; page returned 403)
- 2026 Singapore Consensus. https://arxiv.org/abs/2608.14611 (LoC content not confirmed)
- A Loss of Control Threat Matrix for Agentic AI (LessWrong, single author, not a credible primary source)
- No standalone 2026 RAND LoC report found. No published SaferAI *quantitative* LoC model found; their 2026 LoC work is qualitative (STPA / STECA / FRAM).
