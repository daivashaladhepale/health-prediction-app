import { useState } from "react";
import PatientForm from "./components/PatientForm";
import PatientTable from "./components/PatientTable";

function App() {

  const [selectedPatient, setSelectedPatient] = useState(null);

  return (
    <div className="container mt-4">

      <h1 className="text-center mb-4">
        Health Prediction Application
      </h1>

      <PatientForm
        selectedPatient={selectedPatient}
        setSelectedPatient={setSelectedPatient}
      />

      <hr />

      <PatientTable
        setSelectedPatient={setSelectedPatient}
      />

    </div>
  );
}

export default App;