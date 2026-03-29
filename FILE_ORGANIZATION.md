# Project File Organization Guide

## 📁 Recommended Directory Structure

This guide helps keep your project organized as you continue development.

---

## Current Structure Issues

The root directory contains many debugging/testing scripts that should be organized:

```
Current (Messy):
├── check_car.py
├── check_encoder_keys.py
├── check_scaler.py
├── create_heart_encoders.py
├── debug_backend_input.py
├── debug_heart.py
├── debug_models.py
├── fix_columns.py
├── get_disease_values.py
├── retrain_models.py
├── show_disease_examples.py
├── test_backend_path.py
├── test_disease_case.py
├── test_disease_example.py
├── test_gender_variation.py
├── test_svm.py
├── test_svm_fixed.py
├── train_car_proper.py
├── train_heart_better.py
├── train_heart_complete.py
├── train_heart_final.py
├── train_heart_improved.py
├── train_heart_nn_only.py
├── train_heart_with_actual_encoders.py
│
├── Backend/
├── frontend-new/
├── Model/
└── ... documentation files
```

---

## 🗂️ Recommended Organization

### Option 1: Create `scripts/` Directory (Recommended)

```
Ai Webapp/
├── Backend/                    # API backend (Flask)
├── frontend-new/              # React frontend
├── Model/                     # Model training data & scripts
│
├── scripts/                   # 🆕 Development & debugging scripts
│   ├── test/                  # Test scripts
│   │   ├── test_backend_path.py
│   │   ├── test_disease_case.py
│   │   ├── test_disease_example.py
│   │   ├── test_gender_variation.py
│   │   ├── test_svm.py
│   │   ├── test_svm_fixed.py
│   │   └── test_api_endpoints.py
│   │
│   ├── debug/                 # Debug scripts
│   │   ├── debug_backend_input.py
│   │   ├── debug_heart.py
│   │   ├── debug_models.py
│   │   └── check_scaler.py
│   │
│   ├── check/                 # Data validation scripts
│   │   ├── check_car.py
│   │   ├── check_encoder_keys.py
│   │   ├── check_scaler.py
│   │   └── validate_models.py
│   │
│   ├── utils/                 # Utility scripts
│   │   ├── create_heart_encoders.py
│   │   ├── get_disease_values.py
│   │   ├── show_disease_examples.py
│   │   └── fix_columns.py
│   │
│   └── archive/               # Old training scripts (for reference)
│       ├── train_car_proper.py
│       ├── train_heart_better.py
│       ├── train_heart_complete.py
│       ├── train_heart_final.py
│       ├── train_heart_improved.py
│       ├── train_heart_nn_only.py
│       ├── train_heart_with_actual_encoders.py
│       └── retrain_models.py
│
├── .github/                   # GitHub workflows
├── .gitignore
├── SETUP.md                   # 🆕 Setup instructions
├── LOCAL_DEVELOPMENT.md       # 🆕 Local dev guide
├── MODEL_TRAINING.md          # 🆕 Training guide
├── README.md                  # Main documentation
└── railway.json              # Railway deployment config
```

### Option 2: Consolidate to `tools/` Directory

```
tools/
├── test_backend_path.py
├── test_disease_case.py
├── debug_models.py
└── ... all scripts
```

---

## 🧹 How to Reorganize (Step-by-Step)

### Using PowerShell (Windows)

```powershell
# Create new directories
mkdir scripts/test
mkdir scripts/debug
mkdir scripts/check
mkdir scripts/utils
mkdir scripts/archive

# Move test scripts
Move-Item test_*.py scripts/test/
Move-Item test_backend_path.py scripts/test/
Move-Item test_disease_example.py scripts/test/

# Move debug scripts
Move-Item debug_*.py scripts/debug/
Move-Item check_scaler.py scripts/debug/

# Move check scripts
Move-Item check_*.py scripts/check/

# Move utility scripts
Move-Item create_*.py scripts/utils/
Move-Item get_*.py scripts/utils/
Move-Item show_*.py scripts/utils/
Move-Item fix_*.py scripts/utils/

# Move old training scripts
Move-Item train_*.py scripts/archive/
Move-Item retrain_*.py scripts/archive/
```

### Using Bash (macOS/Linux)

```bash
# Create directories
mkdir -p scripts/{test,debug,check,utils,archive}

# Move test scripts
mv test_*.py scripts/test/

# Move debug scripts
mv debug_*.py scripts/debug/
mv check_scaler.py scripts/debug/

# Move check scripts
mv check_*.py scripts/check/

# Move utility scripts
mv create_*.py scripts/utils/
mv get_*.py scripts/utils/
mv show_*.py scripts/utils/
mv fix_*.py scripts/utils/

# Move old training scripts
mv train_*.py scripts/archive/
mv retrain_*.py scripts/archive/
```

---

## 📋 File Organization Categories

### Test Scripts (`scripts/test/`)
Used to verify functionality:
- `test_backend_path.py` - Test Flask routes
- `test_disease_case.py` - Test model predictions
- `test_disease_example.py` - Test with specific data
- `test_gender_variation.py` - Test gender encoding
- `test_svm.py`, `test_svm_fixed.py` - Test SVM model

### Debug Scripts (`scripts/debug/`)
Help identify issues:
- `debug_backend_input.py` - Debug incoming requests
- `debug_heart.py` - Debug heart disease model
- `debug_models.py` - General model debugging
- `check_scaler.py` - Verify scaler settings

### Check Scripts (`scripts/check/`)
Validate data & configurations:
- `check_car.py` - Validate car data
- `check_encoder_keys.py` - Check encoder mappings
- `validate_models.py` - Verify model integrity

### Utility Scripts (`scripts/utils/`)
Helper scripts for development:
- `create_heart_encoders.py` - Create encoders
- `get_disease_values.py` - Get disease examples
- `show_disease_examples.py` - Display examples
- `fix_columns.py` - Fix data columns

### Archive Scripts (`scripts/archive/`)
Old/superseded scripts (kept for reference):
- `train_heart_better.py`
- `train_heart_final.py`
- Others that aren't currently used

---

## ✅ Updated .gitignore

After reorganizing, your `.gitignore` should keep:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv

# Models (optional - if too large)
*.h5
*.pkl
*.joblib

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Data preprocessing outputs
*.pkl
encoders/
scalers/

# Logs
*.log
```

---

## 📚 Benefits of Organization

| Benefit | Details |
|---------|---------|
| **Easier Navigation** | Quick find scripts by category |
| **Reduced Clutter** | Root stays clean for main project files |
| **Better Collaboration** | Team sees clear structure |
| **Easier Maintenance** | Archive old scripts separately |
| **Clear Intent** | Script purpose obvious from location |

---

## 🔑 Key Directories to Keep Clean

### ✅ Keep These at Root
- `Backend/` - Core API
- `frontend-new/` - Core UI
- `Model/` - Model training
- `.github/` - GitHub workflows
- Documentation files (`*.md`)
- Configuration files (`*.json`, `.gitignore`)

### 🚫 Move These to `scripts/`
- All testing/debugging scripts
- All one-off utility scripts
- All old/superseded code

---

## 🔄 Example: Running Organized Scripts

After reorganization:

```bash
# Run a test
python scripts/test/test_disease_case.py

# Run a debug script
python scripts/debug/debug_models.py

# Run a utility
python scripts/utils/show_disease_examples.py

# Check data
python scripts/check/check_encoder_keys.py
```

Much cleaner than:
```bash
python test_disease_case.py
python debug_models.py
```

---

## 📝 Optional: Create script index

Create `scripts/README.md`:

```markdown
# Development Scripts

## Test Scripts
- `test/test_disease_case.py` - Test model predictions
- `test/test_backend_path.py` - Test API endpoints

## Debug Scripts
- `debug/debug_models.py` - Debug model issues
- `debug/debug_heart.py` - Debug heart model

... etc
```

---

## ⚡ Quick Reference: What Goes Where

| File Type | Location | Example |
|-----------|----------|---------|
| Test files | `scripts/test/` | `test_disease_case.py` |
| Debug files | `scripts/debug/` | `debug_models.py` |
| Check files | `scripts/check/` | `check_car.py` |
| Utility files | `scripts/utils/` | `get_disease_values.py` |
| Old training | `scripts/archive/` | `train_heart_final.py` |
| Documentation | Root | `SETUP.md`, `README.md` |
| Core code | `Backend/`, `frontend-new/` | API, UI code |

---

## 🎯 Next Steps

1. **Review** - Decide if reorganization matches your workflow
2. **Plan** - List any custom scripts to add
3. **Organize** - Use PowerShell/Bash commands above
4. **Update** - Update any documentation with new paths
5. **Verify** - Test scripts still work from new locations

---

## 💡 Pro Tips

1. **Keep `scripts/test/` accessible** for frequent testing
2. **Review `scripts/archive/`** periodically to delete truly obsolete code
3. **Document purpose** in script headers if not obvious
4. **Use relative imports** that work from any location

---

**This reorganization is optional but highly recommended for team collaboration!**
