import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import { AuthProvider } from "./context/AuthContext"
import NoPage from "./pages/NoPage";
import MedicineForm from "./pages/forms/MedicineForm";
import ConditionForm from "./pages/forms/ConditionForm";
import Medicine from "./pages/searchs/Medicine";
import Condition from "./pages/searchs/Condition";
import Patient from "./pages/searchs/Patient";
import PatientFormView from "./pages/forms/PatientFormView";
import Profile from "./pages/Profile";
import UserForm from "./pages/forms/UserForm";
import Occurrence from "./pages/searchs/Occurrence";
import OccurrenceForm from "./pages/forms/OccurrenceForm";
import PatientMedicine from "./pages/searchs/PatientMedicine";
import PatientMedicineForm from "./pages/forms/PatientMedicineForm";
import PatientCondition from "./pages/searchs/PatientCondition";
import PatientConditionForm from "./pages/forms/PatientConditionForm";

function App() {
  return (
    <div className="App">
      <AuthProvider>
        <BrowserRouter>
          <Routes>
            <Route index element={<Login />} />
            <Route path="/login" element={<Login />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/medicines" element={<Medicine />}></Route>
            <Route path="/conditions" element={<Condition />}></Route>
            <Route path="/medicines/:id" element={<Medicine />}></Route>

            <Route path="/patient-medicine/:id" element={<PatientMedicine />}></Route>
            <Route path="/form-patient-medicine/" element={<PatientMedicineForm />}></Route>
            <Route path="/form-patient-medicine/:id?/:patient_id?" element={<PatientMedicineForm />}></Route>

            <Route path="/patient-condition/:id" element={<PatientCondition />}></Route>
            <Route path="/form-patient-condition/" element={<PatientConditionForm />}></Route>
            <Route path="/form-patient-condition/:id?/:patient_id?" element={<PatientConditionForm />}></Route>

            <Route path="/conditions/:id" element={<Condition />}></Route>
            <Route path="/patients" element={<Patient />}></Route>
            <Route path="/occurrences/:id" element={<Occurrence />}></Route>
            <Route path="/profile" element={<Profile />}/>
            <Route path="/form-user" element={<UserForm />}></Route>
            <Route path="/form-occurrence/" element={<OccurrenceForm />}></Route>
            <Route path="/form-occurrence/:id" element={<OccurrenceForm />}></Route>
            <Route path="/form-medicine" element={<MedicineForm />} />
            <Route path="/form-medicine/:id" element={<MedicineForm />} />
            <Route path="/form-condition" element={<ConditionForm />} />
            <Route path="/form-condition/:id" element={<ConditionForm />} />
            <Route path="/form-patient" element={<Dashboard />}/>
            <Route path="/form-patient/:id" element={<PatientFormView />}/>
            <Route path="*" element={<NoPage />} />
          </Routes>
        </BrowserRouter>
      </AuthProvider>
    </div >
  );
}

export default App;
