# Local Development Guide

## Quick Start (5 minutes)

### Prerequisites
- Python 3.8+ installed
- Node.js 16+ installed
- All dependencies installed (see SETUP.md)

---

## Step 1: Setup Python Virtual Environment (First Time Only)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

---

## Step 2: Install Dependencies (First Time Only)

```bash
# Backend dependencies
cd Backend
pip install -r requirements.txt
cd ..

# Frontend dependencies
cd frontend-new
npm install
cd ..
```

---

## Step 3: Start Backend Server

Open **Terminal 1**:
```bash
# Activate virtual environment (if not already activated)
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Start backend
cd Backend
python main.py
```

**Expected Output**:
```
 * Running on http://127.0.0.1:8004
 * Debug mode: on
```

The backend will start on **http://localhost:8004**

---

## Step 4: Start Frontend Development Server

Open **Terminal 2**:
```bash
cd frontend-new
npm run dev
```

**Expected Output**:
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  press h + enter to show help
```

---

## Step 5: Open in Browser

Visit: **http://localhost:5173**

You should see the application with:
- Navigation menu
- ML Models Test page
- Neural Network Test page
- ML Report page
- NN Report page

---

## Testing the Models

### Test Heart Disease Prediction
1. Go to **ML Models** or **Neural Network** test page
2. Click **"Load disease Example"** button
3. Models should predict **"Heart disease"** with high confidence

**Example Values**:
- Age: 66
- Gender: Female (0)
- Fasting Blood Sugar: 177 mg/dL ⭐ (key indicator)

### Test Car Evaluation
1. Go to test page
2. Enter car features and click **Predict**
3. Should get classification (unacc, acc, good, vgood)

---

## File Changes During Development

### Frontend File Locations
```
frontend-new/src/
├── pages/
│   ├── MLTest.jsx          # Edit to modify ML test interface
│   ├── NNTest.jsx          # Edit to modify NN test interface
│   ├── MLReport.jsx        # ML models documentation
│   └── NNReport.jsx        # NN model documentation
├── components/
│   └── TestPage.jsx        # Shared test component
├── App.jsx                 # Main app logic
└── main.jsx                # Entry point
```

### Backend File Locations
```
Backend/
├── main.py                 # Edit to modify API endpoints
└── models/                 # Model files
    ├── car/model.h5
    └── heart/model.h5
```

---

## Hot Reload During Development

### Frontend (Automatic)
The frontend automatically reloads when you save changes to `.jsx` files.

### Backend (Manual Reload)
To reload backend after changes:
1. Stop the backend (Ctrl+C)
2. Make your changes to `Backend/main.py`
3. Run `python main.py` again

---

## Stopping Development Servers

To stop each server:
```bash
# In the terminal running the server
Ctrl + C
```

Then:
```bash
# Deactivate virtual environment (optional)
deactivate
```

---

## Common Development Tasks

### Adding New Test Cases

**In Frontend** (`frontend-new/src/pages/MLTest.jsx` or `NNTest.jsx`):
```jsx
// Add a new button
<button onClick={() => setHeartFields({...defaultValues})}>
  Load Custom Example
</button>
```

### Modifying API Endpoints

**In Backend** (`Backend/main.py`):
```python
@app.route('/predict/my-model', methods=['POST'])
def predict_my_model():
    data = request.get_json()
    # Process data
    return jsonify({'prediction': result})
```

### Testing API Directly

Use **curl** or **Postman**:
```bash
# Heart disease prediction
curl -X POST http://localhost:8004/predict/heart \
  -H "Content-Type: application/json" \
  -d '{"age": 66, "gender": 0, ...}'

# Car evaluation prediction
curl -X POST http://localhost:8004/predict/car \
  -H "Content-Type: application/json" \
  -d '{"buying": 1, "maint": 2, ...}'
```

---

## Debugging Tips

### Frontend Console
1. Open Browser DevTools (F12)
2. Go to **Console** tab
3. Check for JavaScript errors

### Network Tab
1. Open Browser DevTools (F12)
2. Go to **Network** tab
3. Check API requests to `http://localhost:8004`
4. Verify status codes and responses

### Backend Terminal
- Check error messages in backend terminal
- Add `print()` statements for debugging
- Look for HTTP status codes (200, 404, 500, etc.)

---

## Performance Tips

### Frontend
- Use React DevTools to profile components
- Check bundle size: `npm run build`
- Minimize re-renders with proper React hooks

### Backend
- Use Flask debugger: `debug=True` in `main.py`
- Profile slow requests with timing decorators
- Monitor memory usage during model prediction

---

## Virtual Environment Troubleshooting

### Activate fails on Windows
```bash
# Try PowerShell/Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1
```

### Python version mismatch
```bash
# Check Python version
python --version  # Should be 3.8+

# Use specific Python version
python3.10 -m venv venv
```

---

## Next Steps

After local development:
1. See **SETUP.md** for full project setup
2. See **MODEL_TRAINING.md** for model training
3. See **Backend/README.md** for API documentation

---

**Happy Coding!** 🚀
