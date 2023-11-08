
import {  getPatientRecords } from '../../common/api'
import GenericSearch from './GenericSearch'

export default function Patient(){
    

    return(
        <GenericSearch 
            placeholder='Pesquise pelo CPF'
            path='/form-patient/'
            getRecords={getPatientRecords}
            deleteRecord={() => {}}
            isChanged='true'
            isDeleted='false'
        />
    )
}