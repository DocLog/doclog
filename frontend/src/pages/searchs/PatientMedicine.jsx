
import { useParams } from 'react-router-dom'
import { deletePatientMedicineRecordById, getPatientMedicineRecords } from '../../common/api'
import GenericSearch from './GenericSearch'

export default function PatientMedicine(){
    return(
       <GenericSearch 
        placeholder='Pesquise pelo nome do Medicamento'
        path='/form-patient-medicine/'
        getRecords={getPatientMedicineRecords}
        getRecordsFromPatient={getPatientMedicineRecords}
        deleteRecord={deletePatientMedicineRecordById}
        isChanged='true'
        isDeleted='false'
       />
    )
}