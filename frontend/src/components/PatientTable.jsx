import { useEffect, useState } from "react";
import axios from "axios";

function PatientTable({
  setSelectedPatient
}) {

  const [patients, setPatients] = useState([]);

  const fetchPatients = async () => {

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/patients"
      );

      setPatients(response.data);

    } catch (error) {

      console.log(error);

    }

  };

  const deletePatient = async (id) => {

    try {

      await axios.delete(
        `http://127.0.0.1:8000/patients/${id}`
      );

      fetchPatients();

    } catch (error) {

      console.log(error);

    }

  };

  useEffect(() => {

    fetchPatients();

  }, []);

  return (

    <div className="mt-4">

      <h3>Patient Records</h3>

      <table className="table table-bordered table-striped">

        <thead>

          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Date of Birth</th>
            <th>Email</th>
            <th>Glucose</th>
            <th>Haemoglobin</th>
            <th>Cholesterol</th>
            <th>Remarks</th>
            <th>Action</th>
          </tr>

        </thead>

        <tbody>

          {patients.map((patient) => (

            <tr key={patient.id}>

              <td>{patient.id}</td>

              <td>{patient.full_name}</td>

              <td>{patient.dob}</td>

              <td>{patient.email}</td>

              <td>{patient.glucose}</td>

              <td>{patient.haemoglobin}</td>

              <td>{patient.cholesterol}</td>

              <td>{patient.remarks}</td>

              <td>

              <button
                className="btn btn-warning btn-sm me-2"
                onClick={() =>
                  setSelectedPatient(patient)
                }
              >
                Edit
              </button>

              <button
                className="btn btn-danger btn-sm"
                onClick={() =>
                  deletePatient(patient.id)
                }
              >
                Delete
              </button>

            </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>

  );

}

export default PatientTable;