init python:
    import re

    def check_password(password):
        feedback = []

        length = len(password)

        if length < 8:
            feedback.append("Too short.")

        if not re.search(r"[a-z]", password):
            feedback.append("Add lowercase letters.")

        if not re.search(r"[A-Z]", password):
            feedback.append("Add uppercase letters.")

        if not re.search(r"\d", password):
            feedback.append("Add numbers.")

        if not re.search(r"[^\w\s]", password):
            feedback.append("Add symbols.")

        common = ["123456", "password", "qwerty", "abc123"]
        for word in common:
            if word in password.lower():
                feedback.append("Avoid common patterns.")
                break
                
        issue_count = len(feedback)

        if issue_count == 0:
            strength = "Strong"
        elif issue_count <= 2:
            strength = "Medium"
        else:
            strength = "Weak"

        return strength, feedback