# Deploying PhytoScout to Streamlit Community Cloud

This guide will walk you through deploying your **PhytoScout** app to the free Streamlit Community Cloud.

## Prerequisites

1.  **GitHub Account**: You need a GitHub account to host your code.
2.  **Streamlit Cloud Account**: Sign up at [share.streamlit.io](https://share.streamlit.io) using your GitHub account.

## Step 1: Push Your Code to GitHub

Streamlit Cloud pulls your code directly from GitHub. You need to put your `phyto_scout` code into a repository.

### Option A: Using Command Line (Recommended)

1.  **Initialize Git** (if not already done):
    ```bash
    git init
    git add .
    git commit -m "Initial commit of PhytoScout"
    ```

2.  **Create a New Repository** on GitHub:
    *   Go to [github.com/new](https://github.com/new).
    *   Name it `PhytoScout`.
    *   Choose **Public**.
    *   Do **not** initialize with README or .gitignore (you already have them).

3.  **Push code**:
    *   Copy the commands provided by GitHub (under "…or push an existing repository from the command line").
    *   Example:
        ```bash
        git remote add origin https://github.com/YOUR_USERNAME/PhytoScout.git
        git branch -M main
        git push -u origin main
        ```

### Option B: Drag and Drop

1.  Create a new repository on GitHub.
    *   Check "Add a README file" this time to initialize it.
2.  Click **Add file** > **Upload files**.
3.  Drag and drop all your files (`app.py`, `modules/`, `utils/`, `requirements.txt`, etc.) into the window.
4.  Commit changes.

---

## Step 2: Deploy on Streamlit Cloud

1.  Go to [share.streamlit.io](https://share.streamlit.io/).
2.  Click the blue **New app** button (top right).
3.  **App deployment configuration**:
    *   **Repository**: Select `YOUR_USERNAME/PhytoScout`.
    *   **Branch**: Currently `main` (or `master`).
    *   **Main file path**: `app.py`.
4.  Click **Deploy!** 🚀

## Step 3: Watch it Build

Streamlit will now build your app. You'll see a terminal window on the right side.
*   It will install dependencies from `requirements.txt` (`streamlit`, `plotly`, `pandas`, etc.).
*   Once finished, your app will launch automatically!

---

## Troubleshooting

*   **"ModuleNotFoundError"**: This usually means a package is missing from `requirements.txt`.
    *   *Fix:* Check the error logs to see which package is missing, add it to `requirements.txt`, commit, and push. Streamlit will auto-update.
*   **"File not found"**: Ensure your folder structure on GitHub matches your local one. `modules` and `utils` must be folders.
*   **App crashes immediately**: Check the logs on the bottom right of the Streamlit dashboard for Python errors (e.g., indentation or syntax issues).
