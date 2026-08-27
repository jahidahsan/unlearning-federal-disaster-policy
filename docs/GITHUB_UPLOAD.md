
# Uploading This Snapshot to GitHub

The command-line workflow is recommended because the repository contains many research artifacts.

1. Extract the ZIP to a short local path, such as `C:\GitHub\Unlearning`, to avoid Windows path-length problems in the archived experiment folders.
2. Create a new **private** empty GitHub repository.
3. Open a terminal in the extracted `Unlearning_Research_Repository` folder.
4. Run:

```bash
python scripts/validate_repository.py
git init
git add .
git commit -m "Initial private pre-LangChain repository snapshot"
git branch -M main
git remote add origin <YOUR_PRIVATE_REPOSITORY_URL>
git push -u origin main
```

After pushing, enable branch protection or require pull-request review before merging substantive changes.

Do not upload the outer transfer ZIPs or the context-only workshop paper. The repository manifest already records the organized contents and deliberate exclusions.
