import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import MLReport from "./pages/MLReport";
import NNReport from "./pages/NNReport";
import MLTest from "./pages/MLTest";
import NNTest from "./pages/NNTest";

function App() {
  return (
    <BrowserRouter>
      <nav style={{ display: "flex", gap: "20px" }}>
        <Link to="/ml-report">ML Report</Link>
        <Link to="/nn-report">NN Report</Link>
        <Link to="/ml-test">ML Test</Link>
        <Link to="/nn-test">NN Test</Link>
      </nav>

      <Routes>
        <Route path="/ml-report" element={<MLReport />} />
        <Route path="/nn-report" element={<NNReport />} />
        <Route path="/ml-test" element={<MLTest />} />
        <Route path="/nn-test" element={<NNTest />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;