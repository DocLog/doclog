
import { deleteConditionRecordById, getConditionRecords } from '../../common/api'
import GenericSearch from './GenericSearch'

export default function Condition(){
 

    return(
       <GenericSearch 
            placeholder='Pesquise pelo nome da condição'
            path='/form-condition/'
            getRecords={getConditionRecords}
            deleteRecord={deleteConditionRecordById}
            isChanged='true'
            isDeleted='true'
       />
    )
}