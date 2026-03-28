import { BrowserRouter, Routes, Route, Link, Navigate } from "react-router-dom";
import MLReport from "./pages/MLReport";
import NNReport from "./pages/NNReport";
import MLTest from "./pages/MLTest";
import NNTest from "./pages/NNTest";

function App() {
  return (
    <BrowserRouter>
      <nav style={{
        display: "flex",
        gap: "20px",
        padding: "15px",
        background: "#222"
      }}>
        <Link to="/ml-report" style={{ color: "white" }}>ML Report</Link>
        <Link to="/nn-report" style={{ color: "white" }}>NN Report</Link>
        <Link to="/ml-test" style={{ color: "white" }}>ML Test</Link>
        <Link to="/nn-test" style={{ color: "white" }}>NN Test</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Navigate to="/ml-report" />} />
        <Route path="/ml-report" element={<MLReport />} />
        <Route path="/nn-report" element={<NNReport />} />
        <Route path="/ml-test" element={<MLTest />} />
        <Route path="/nn-test" element={<NNTest />} />
        <Route path="*" element={<h1>404 Not Found</h1>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;