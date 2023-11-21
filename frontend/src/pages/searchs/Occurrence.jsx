
import { useParams } from 'react-router-dom'
import { deleteOccurrenceRecordById, getOccurrenceRecords } from '../../common/api'
import GenericSearch from './GenericSearch'

export default function Occurrence(){
    return(
       <GenericSearch 
        placeholder='Pesquise pelo nome do Ocorrência'
        path='/form-occurrence/'
        getRecords={getOccurrenceRecords}
        getRecordsFromPatient={getOccurrenceRecords}
        deleteRecord={deleteOccurrenceRecordById}
        isChanged='true'
        isDeleted='false'
       />
    )
}