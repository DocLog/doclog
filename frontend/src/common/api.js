
import axios from "axios";

const API_URI = "http://127.0.0.1:5000/api/v1"


// Condition CRUD
export function getConditionRecords(){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/condition`)
}

export function getConditionById(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.get(`${API_URI}/condition/${id}`)
}



export function updateConditionRecord(data){
    axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.put(`${API_URI}/condition`, data)
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

export function sendMedicineRecord(data){
    axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.post(`${API_URI}/medicine`, data)
}

export function updateMedicineRecord(data){
    axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.put(`${API_URI}/medicine`, data)
}

export function deleteMedicineRecordById(id){
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
    
    return axios.delete(`${API_URI}/medicine/${id}`)
}

// Medicine CRUD -- END