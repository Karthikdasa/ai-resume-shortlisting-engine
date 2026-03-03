import os
from sentence_transformers import SentenceTransformer

from utils.text_extraction import extract_text
from utils.summarizer import summarize_text
from utils.skill_extractor import extract_skills
from utils.scoring import compute_weighted_score

# Load embedding model once
embedder = SentenceTransformer("all-MiniLM-L6-v2")


def process_jd(jd_path):
    jd_text = extract_text(jd_path)
    jd_summary = summarize_text(jd_text)
    jd_skills = extract_skills(jd_text)
    jd_embedding = embedder.encode(jd_summary, convert_to_tensor=True)

    return jd_summary, jd_embedding, jd_skills


def process_resume(resume_path):
    resume_text = extract_text(resume_path)
    resume_summary = summarize_text(resume_text)
    resume_skills = extract_skills(resume_text)
    resume_embedding = embedder.encode(resume_summary, convert_to_tensor=True)

    return {
        "filename": os.path.basename(resume_path),
        "summary": resume_summary,
        "skills": resume_skills,
        "embedding": resume_embedding,
        "raw_text": resume_text
    }


def compare_resumes(jd_path, resumes_folder):

    jd_summary, jd_emb, jd_skills = process_jd(jd_path)

    results = []

    for file in os.listdir(resumes_folder):
        if file.lower().endswith((".pdf", ".docx")):

            resume_path = os.path.join(resumes_folder, file)
            resume_data = process_resume(resume_path)

            semantic_score, skill_score, exp_score, final_score = compute_weighted_score(
                jd_emb,
                resume_data["embedding"],
                jd_skills,
                resume_data["skills"],
                resume_data["raw_text"]
            )

            results.append({
                "filename": file,
                "semantic_score": semantic_score,
                "skill_score": skill_score,
                "experience_score": exp_score,
                "final_score": final_score,
                "shortlist": final_score >= 0.7
            })

    results.sort(key=lambda x: x["final_score"], reverse=True)

    for r in results:
        print("\n==============================")
        print(f"Resume: {r['filename']}")
        print(f"Semantic Score: {r['semantic_score']*100:.2f}%")
        print(f"Skill Score: {r['skill_score']*100:.2f}%")
        print(f"Experience Score: {r['experience_score']*100:.2f}%")
        print(f"Final Score: {r['final_score']*100:.2f}%")
        print(f"Shortlist: {'YES' if r['shortlist'] else 'NO'}")
        print("==============================")

    return results


if __name__ == "__main__":
    jd_file = "sample_data/jd.pdf"
    resume_folder = "sample_data/resumes"

    compare_resumes(jd_file, resume_folder)