
import { deleteConditionRecordById, getConditionRecords, getConditionRecordByPatientId } from '../../common/api'
import GenericSearch from './GenericSearch'

export default function Condition(){
 

    return(
       <GenericSearch 
            placeholder='Pesquise pelo nome da condição'
            path='/form-condition/'
            getRecords={getConditionRecords}
            deleteRecord={deleteConditionRecordById}
            getRecordsFromPatient={getConditionRecordByPatientId}
            isChanged='true'
            isDeleted='true'
       />
    )
}