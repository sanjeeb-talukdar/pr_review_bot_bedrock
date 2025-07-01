# 🔍 Code Review Guidelines

These guidelines help ensure quality, maintainability, and consistency in our codebase. Use them to guide all pull request reviews.

---

## 1. 📦 Project Structure
- Keep folders modular and meaningful
- Separate concerns (controllers, services, models, etc.)
- Use domain-driven principles for large services

---

## 2. 🧠 Naming Conventions
- Use `camelCase` for variables and functions in JS/TS
- Use `snake_case` for Python variables and functions
- Use `PascalCase` for class names across all languages
- Name files to match the primary class/function

---

## 3. ✅ Logic & Readability
- Keep functions small (< 30 LOC ideally)
- Avoid nested conditionals > 2 levels
- Prefer clear logic over clever hacks
- Add comments only where logic isn't self-explanatory

---

## 4. 🛡️ Error Handling
- Avoid silent fails or broad `catch` blocks
- Return meaningful error messages
- Log unexpected failures with context
- Validate all inputs (especially external)

---

## 5. 🔐 Security
- Avoid hardcoding secrets/API keys
- Use parameterized queries to avoid SQL injection
- Sanitize user input and avoid `eval`
- Secure API endpoints with proper auth

---

## 6. 🧪 Testing
- All new code should have unit tests
- Ensure ≥80% test coverage for new modules
- Avoid mocking internal logic unnecessarily
- Use descriptive test names and scenarios

---

## 7. 📚 Documentation
- Add/update README or module-level doc if APIs/interfaces change
- Document env variables and setup instructions
- Add TODOs or `# FIXME` only with context

---

## 8. 🧹 Style & Linting
- Ensure no linter or formatter errors
- Follow `.editorconfig`, `.prettierrc`, or PEP8 (Python)
- Use consistent indentation (2 or 4 spaces)
- Remove commented-out or dead code

---

## 9. 💬 Pull Request Quality
- PR title should summarize the change
- Description must mention: What, Why, and optionally How
- Link related issues/tickets
- Assign reviewers and labels properly

---

## 10. 🌍 General Best Practices
- Reuse existing utils and libraries when possible
- Don’t reinvent the wheel
- Leave the code better than you found it

---

Happy Reviewing! ✅
