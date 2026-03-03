def extract_skills(text, skill_keywords=None):
    """
    Extract predefined skills from text.
    """

    if not skill_keywords:
        skill_keywords = [
            "Python", "Java", "C++", "C#", "JavaScript",
            "React", "Node.js", "Django", "Flask",
            "SQL", "MongoDB", "PostgreSQL",
            "TensorFlow", "PyTorch", "Machine Learning",
            "Deep Learning", "NLP",
            "AWS", "Azure", "GCP",
            "Docker", "Kubernetes",
            "Git", "Linux",
            "REST API", "GraphQL",
            "Spring Boot", "FastAPI"
        ]

    text_lower = text.lower()
    found_skills = set()

    for skill in skill_keywords:
        if skill.lower() in text_lower:
            found_skills.add(skill)

    return sorted(found_skills)