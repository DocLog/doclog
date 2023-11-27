
import axios from "axios";

const API_URI = "https://doclog.azurewebsites.net/api/v1"


// Condition CRUD
export function getConditionRecords(){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/condition`)
}

export function getConditionById(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/condition/${id}`)
}

export function getConditionRecordByPatientId(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/condition?filter=patient_id:${id}`)
}


export function updateConditionRecord(id, data){
    axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.put(`${API_URI}/condition/${id}`, data)
}

export function deleteConditionRecordById(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.delete(`${API_URI}/condition/${id}`)
}

export function sendConditionRecord(data){
    axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.post(`${API_URI}/condition`, data)
}
// Condition CRUD -- END

// HealthCareProfessional CRUD



export function getProfessionalById(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/healthcare-professional/${id}`)
}

export function getProfessionalByCRM(crm){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/healthcare-professional?filter=crm:${crm}`)
}

export function updateProfessionalRecord(data){
    axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.put(`${API_URI}/healthcare-professional`, data)
}

export function deleteProfessionalRecordById(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.delete(`${API_URI}/healthcare-professional/${id}`)
}

export function sendProfessionalRecord(data){
    axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.post(`${API_URI}/healthcare-professional`, data)
}

// HealthCareProfessional CRUD -- END


// Patient CRUD

export function getPatientRecords(){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/patient`)
}

export function getPatientRecordById(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/patient/${id}`)
}

export function getPatientRecordsByParameters(param){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/patient?id=${param}&cpf=${param}&name=${param}`)
}

export function sendPatientRecord(data) {
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.post(`${API_URI}/patient`, data)
} 

// Patient CRUD -- END

// User CRUD + login 

export function sendLoginData(username, password) {
    return axios.post(`${API_URI}/login`, { "name": username, "password": password })
} 

export function getUsers(){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))

    return axios.get(`${API_URI}/user`)
}

export function getUserById(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/user/${id}`)
}

export function createUser(data){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))

    return axios.post(`${API_URI}/user`, data)
}

export function updateUser(data){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))

    return axios.put(`${API_URI}/user`, data)
}

export function deleteUser(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))

    return axios.delete(`${API_URI}/user/${id}`)
}

// User CRUD + login -- END




// Medicine CRUD

export function getMedicineRecords(){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/medicine`)
}

export function getMedicineRecordById(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/medicine/${id}`)
}

export function getMedicineRecordByPatientId(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/medicine?filter=patient_id:${id}`)
}

export function sendMedicineRecord(data){
    axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.post(`${API_URI}/medicine`, data)
}

export function updateMedicineRecord(id, data){
    axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.put(`${API_URI}/medicine/${id}`, data)
}

export function deleteMedicineRecordById(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.delete(`${API_URI}/medicine/${id}`)
}

// Medicine CRUD -- END

// Occurrence CRUD 
export function getPatientMedicineRecords(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/patient-medicine?filter=patient_id:${id}`)
}

export function getPatientConditionRecords(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/patient-condition?filter=patient_id:${id}`)
}

export function getOccurrenceRecords(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/occurrence?filter=patient_id:${id}`)
}

export function getOccurrenceRecordById(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/occurrence/${id}`)
}

export function sendOccurrenceRecord(data){
    axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.post(`${API_URI}/occurrence`, data)
}

export function updateOccurrenceRecord(id, data){
    axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.put(`${API_URI}/occurrence/${id}`, data)
}

export function deleteOccurrenceRecordById(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.delete(`${API_URI}/occurrence/${id}`)
}

export function deletePatientMedicineRecordById(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.delete(`${API_URI}/patient-medicine/${id}`)
}

export function deletePatientConditionRecordById(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.delete(`${API_URI}/patient-condition/${id}`)
}

//  Occurrence CRUD -- END

export function sendPatientMedicineRecord(data){
    axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.post(`${API_URI}/patient-medicine`, data)
}

export function updatePatientMedicineRecord(id, data){
    axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.put(`${API_URI}/patient-medicine/${id}`, data)
}

export function sendPatientConditionRecord(data){
    axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.post(`${API_URI}/patient-condition`, data)
}

export function updatePatientConditionRecord(id, data){
    axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.put(`${API_URI}/patient-condition/${id}`, data)
}

export function getPatientMedicineRecordById(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/patient-medicine/${id}`)
}

export function getPatientConditionRecordById(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/patient-condition/${id}`)
}
