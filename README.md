# ai-resume-shortlisting-engine

AI Resume Shortlisting Engine
Overview
An AI-powered resume screening system that intelligently ranks resumes against job descriptions using:
• LLM-based summarization (BART)
• Semantic similarity (Sentence Transformers)
• Skill extraction
• Experience detection
• Weighted ranking algorithm
Designed to go beyond simple keyword matching by incorporating contextual understanding.

Features
• 📄 PDF & DOCX resume parsing
• 🧠 AI-based summarization using facebook/bart-large-cnn
• 🔎 Skill extraction from JD and resumes
• 📊 Semantic similarity scoring
• ⚖️ Weighted final ranking model
• 📈 Automatic shortlist decision (threshold-based)

Architecture Flow
1. Extract JD and Resume text
2. Clean and preprocess text
3. Generate AI summary
4. Extract skills
5. Create semantic embeddings
6. Compute:
o Semantic score (70%)
o Skill match score (20%)
o Experience score (10%)
7. Rank resumes by final weighted score

Tech Stack
• Python
• HuggingFace Transformers
• Sentence Transformers
• PyMuPDF
• Regex-based NLP
• Torch

Example Output
Resume: shivani.pdf
Semantic Similarity: 82.41%
Skill Match Score: 75.00%
Experience Score: 100%
Final Weighted Score: 83.26%
Shortlist: YES

Why This Is Better Than Basic Keyword Matching
• Handles contextual similarity
• Reduces keyword stuffing bias
• Captures semantic meaning
• Uses LLM summarization before embedding comparison