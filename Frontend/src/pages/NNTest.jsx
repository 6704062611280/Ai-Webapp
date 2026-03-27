import TestPage from "../components/TestPage";

export default function NNTest() {
  return (
    <TestPage
      title="🤖 Neural Network Test"
      apiUrl="http://127.0.0.1:8000/predict/nn"
    />
  );
}