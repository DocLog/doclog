import { getProfessionalById, sendProfessionalRecord } from '../../common/api';
import GenericForm from "./GenericForm";
import { showAlert } from "../../common/swalAlert";

export default function HealthCareProfessionalForm( { onFinished } ){

    async function submitForm(formData){
        let data = {
            "name" : formData.name,
            "surname" : formData.surname,
            "cpf" : formData.cpf,
            "birth_date": formData.birth_date,
            "crm": formData.crm
        }
        try{

            const response = await sendProfessionalRecord(data)
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
            title='Profissional'
            initialValues={{
                name: '',
                surname: '',
                cpf: '',
                birth_date: Date(),
                crm: ''
            }}
            fieldConfig={{
                name : { type: 'text' , label: 'Nome', disabled: false},
                surname : { type: 'text', label: 'Sobrenome', disabled: false},
                cpf :{ type: 'text', label: 'CPF', disabled: false},
                birth_date : {type: 'date', label: 'Data de Nascimento', disabled: false},
                crm : {type: 'text', label: 'CRM', disabled: false}
            }}
            onSubmit={submitForm}
            onLoad={getProfessionalById}
        />
    )
    
}