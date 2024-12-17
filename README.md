# **LLM Confidence Study**  
### Course Project for Topics in Large Language Models (Fall '24)

## **Project Overview**  
This project analyzes the confidence of large language models (LLMs) by evaluating their log probabilities, self-assessment capabilities, and top-k probability distributions. The study focuses on three key research questions (RQs):  
1. **RQ1:** Log Probability Thresholding  
2. **RQ2:** Model Self-Assessment  
3. **RQ3:** Top-K Probability Distribution Analysis  

The analysis is conducted across three datasets: **MMLU**, **MedMCQA**, and **ScienceMCQ**, using the following models:  
- **GPT-3.5**  
- **LLaMA**  
- **Gemma**  

---

## **Repository Structure**  

The repository is organized as follows:

```plaintext
.
├── MMLU_Logprob_inference/              # Inference outputs and Logprobs for each model
├── Logprob_and_Confidence_inference/    # Inference outputs, Logprobs, and model confidence scores
├── Original_Datasets/                   # Original datasets
│   ├── MMLU/                            # MMLU dataset
│   ├── MedMCQA/                         # MedMCQA dataset
│   └── ScienceMCQ/                      # ScienceMCQ dataset
├── Shuffled_Dataset/                    # Shuffled versions of the datasets
├── RQ1_Log_Probability_Thresholding/    # Code, analysis, and results for RQ1
│   ├── LLaMA/                           # Results for LLaMA
│   ├── Gemma/                           # Results for Gemma
│   └── GPT-3.5/                         # Results for GPT-3.5
├── RQ2_Model_Self_Assessment/           # Code, analysis, and results for RQ2
│   ├── LLaMA/                           # Results for LLaMA
│   ├── Gemma/                           # Results for Gemma
│   └── GPT-3.5/                         # Results for GPT-3.5
└── RQ3_Top-K_Probability_Analysis/      # Code, analysis, and results for RQ3
    ├── LLaMA/                           # Results for LLaMA
    ├── Gemma/                           # Results for Gemma
    └── GPT-3.5/                         # Results for GPT-3.5
```

---

## **Dataset Descriptions**  
The datasets used in this study are:  
1. **MMLU:** Massive Multitask Language Understanding benchmark.  
2. **MedMCQA:** Medical multiple-choice question-answering dataset.  
3. **ScienceMCQ:** Science-based multiple-choice question-answering dataset.  

- The **`Original_Datasets`** folder contains the unmodified datasets.  
- The **`Shuffled_Dataset`** folder contains shuffled versions of these datasets for comparative analysis.  

---

## **Research Questions (RQs)**  

### **RQ1: Log Probability Thresholding**  
- Investigates the correlation between log probability values and model prediction accuracy.  
- Results are organized by model: `LLaMA`, `Gemma`, and `GPT-3.5`.  

### **RQ2: Model Self-Assessment**  
- Evaluates the models' ability to estimate their own confidence for a given answer.  
- Results are organized by model: `LLaMA`, `Gemma`, and `GPT-3.5`.  

### **RQ3: Top-K Probability Distribution Analysis**  
- Analyzes the distribution of top-k probabilities to distinguish confident and hallucinated responses.  
- Results are organized by model: `LLaMA`, `Gemma`, and `GPT-3.5`.  

---

## **Usage Instructions**  

Install dependencies using:  
```bash
pip install -r requirements.txt
```

