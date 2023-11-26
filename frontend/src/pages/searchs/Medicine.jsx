
import { deleteMedicineRecordById, getMedicineRecords, getMedicineRecordByPatientId } from '../../common/api'
import GenericSearch from './GenericSearch'

export default function Medicine(){



    return(
       <GenericSearch 
        placeholder='Pesquise pelo nome do Medicamento'
        path='/form-medicine/'
        getRecords={getMedicineRecords}
        deleteRecord={deleteMedicineRecordById}
        getRecordsFromPatient={getMedicineRecordByPatientId}
        isChanged='true'
        isDeleted='true'
       />
    )
}