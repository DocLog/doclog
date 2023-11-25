import { getPatientRecordById, sendPatientRecord } from '../../common/api';
import GenericForm from "./GenericForm";
import { showAlert } from "../../common/swalAlert";

export default function PatientForm( { onFinished } ){
    const d = new Date()

    async function submitForm(formData){
        let data = {
            "name" : formData.name,
            "surname" : formData.surname,
            "cpf" : formData.cpf,
            "birth_date": formData.birth_date,
            "blood_type": formData.blood_type,
            "register_date": d.getFullYear().toString() +'-' +(d.getMonth() + 1).toString() +'-' +d.getDate().toString() + 'T' + d.getHours().toString() + ':' + d.getMinutes().toString() + ':' + d.getSeconds().toString(),
            "notes": formData.notes
        }
        try{
            const response = await sendPatientRecord(data)
            onFinished(response)
            showAlert('Registro Criado com Sucesso!', 'success')
        }catch(err){
            if(err.response.status == 422){
                showAlert('Erro ao Salvar os dados!', 'error')
            }

            if(err.response.status == 401){
                showAlert('Não logado! Faça Login', 'error')
            }
        }
    }

    return(
        <GenericForm 
            title='Paciente'
            initialValues={{
                name: '',
                surname: '',
                cpf: '',
                birth_date: Date(),
                blood_type: '',
                notes: ''
            }}
            fieldConfig={{
                name : { type: 'text' ,label: 'Nome'},
                surname : { type: 'text', label: 'Sobrenome'},
                cpf :{ type: 'text', label: 'CPF'},
                birth_date : {type: 'date', label: 'Data de Nascimento'},
                blood_type : {type: 'select', options: ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'], label: 'Tipo Sanguíneo'},
                notes : {type: 'text', label: 'Observações'}
            }}
            onSubmit={submitForm}
            onLoad={getPatientRecordById}
        />
    )
    
}