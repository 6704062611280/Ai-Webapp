import TestPage from "../components/TestPage";

export default function MLTest() {
  return (
    <TestPage
      title="🧠 Machine Learning Test"
      apiUrl="http://127.0.0.1:8000/predict/ml"
    />
  );
}