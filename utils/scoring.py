import re
from sentence_transformers import util


def compute_experience_score(text):
    """
    Simple regex-based experience detection.
    """
    patterns = [
        r"\b[1-9]\+?\s*(years|yrs)\s+(of\s+)?(experience|exp)\b",
        r"\bexperience\s+of\s+[1-9]\+?\s*(years|yrs)\b",
        r"\b[1-9]\+?\s*(years|yrs)\s+experience\b",
    ]

    for pat in patterns:
        if re.search(pat, text.lower()):
            return 1.0

    return 0.0


def compute_weighted_score(jd_embedding, resume_embedding,
                           jd_skills, resume_skills,
                           resume_text):

    # Semantic Similarity
    semantic_score = util.cos_sim(jd_embedding, resume_embedding).item()

    # Skill Matching
    if jd_skills:
        matched = set(jd_skills) & set(resume_skills)
        skill_score = len(matched) / len(set(jd_skills))
    else:
        skill_score = 0.0

    # Experience
    exp_score = compute_experience_score(resume_text)

    # Final weighted score
    final_score = round(
        (0.7 * semantic_score) +
        (0.2 * skill_score) +
        (0.1 * exp_score),
        4
    )

    return semantic_score, skill_score, exp_score, final_score