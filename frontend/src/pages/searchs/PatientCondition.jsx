
import { useParams } from 'react-router-dom'
import { deletePatientConditionRecordById, getPatientConditionRecords } from '../../common/api'
import GenericSearch from './GenericSearch'

export default function PatientCondition(){
    return(
       <GenericSearch 
        placeholder='Pesquise pelo nome da Condição'
        path='/form-patient-condition/'
        getRecords={getPatientConditionRecords}
        getRecordsFromPatient={getPatientConditionRecords}
        deleteRecord={deletePatientConditionRecordById}
        isChanged='true'
        isDeleted='false'
       />
    )
}