
import { deleteMedicineRecordById, getMedicineRecords } from '../../common/api'
import GenericSearch from './GenericSearch'

export default function Medicine(){



    return(
       <GenericSearch 
        placeholder='Pesquise pelo nome do Medicamento'
        path='/form-medicine/'
        getRecords={getMedicineRecords}
        deleteRecord={deleteMedicineRecordById}
        isChanged='true'
        isDeleted='true'
       />
    )
}