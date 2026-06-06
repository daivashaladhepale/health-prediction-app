import { useState, useEffect } from "react";
import axios from "axios";

function PatientForm({
  selectedPatient,
  setSelectedPatient
}) {

  const [formData, setFormData] = useState({
    full_name: "",
    dob: "",
    email: "",
    glucose: "",
    haemoglobin: "",
    cholesterol: ""
  });

  useEffect(() => {

    if (selectedPatient) {

      setFormData({
        full_name: selectedPatient.full_name,
        dob: selectedPatient.dob,
        email: selectedPatient.email,
        glucose: selectedPatient.glucose,
        haemoglobin: selectedPatient.haemoglobin,
        cholesterol: selectedPatient.cholesterol
      });

    }

  }, [selectedPatient]);

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });

  };

  const handleSubmit = async (e) => {

    e.preventDefault();

    try {

      if (selectedPatient) {

        await axios.put(
          `http://127.0.0.1:8000/patients/${selectedPatient.id}`,
          formData
        );

        alert("Patient Updated");

      } else {

        await axios.post(
          "http://127.0.0.1:8000/patients",
          formData
        );

        alert("Patient Added");
      }

      window.location.reload();

    } catch (error) {

      console.log(error);

    }

  };

  return (

    <div className="card shadow p-4">

      <h3>
        {selectedPatient
          ? "Update Patient"
          : "Add Patient"}
      </h3>

      <form onSubmit={handleSubmit}>

        <input
          className="form-control mb-2"
          name="full_name"
          value={formData.full_name}
          onChange={handleChange}
          placeholder="Full Name"
          required
        />

        <input
          className="form-control mb-2"
          type="date"
          name="dob"
          value={formData.dob}
          onChange={handleChange}
          max={new Date().toISOString().split("T")[0]}
          required
        />

        <input
          className="form-control mb-2"
          type="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          placeholder="Email"
          required
        />

        <input
          className="form-control mb-2"
          type="number"
          name="glucose"
          value={formData.glucose}
          onChange={handleChange}
          placeholder="Glucose"
          required
        />

        <input
          className="form-control mb-2"
          type="number"
          name="haemoglobin"
          value={formData.haemoglobin}
          onChange={handleChange}
          placeholder="Haemoglobin"
          required
        />

        <input
          className="form-control mb-3"
          type="number"
          name="cholesterol"
          value={formData.cholesterol}
          onChange={handleChange}
          placeholder="Cholesterol"
          required
        />

        <button className="btn btn-primary">

          {selectedPatient
            ? "Update Patient"
            : "Save Patient"}

        </button>

      </form>

    </div>

  );
}

export default PatientForm;