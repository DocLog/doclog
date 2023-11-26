
import { useNavigate, useParams } from 'react-router-dom';
import { getConditionById, sendConditionRecord, updateConditionRecord } from '../../common/api';
import GenericForm from "./GenericForm";
import { showAlert } from "../../common/swalAlert";

export default function ConditionForm(){
    const navigate = useNavigate();
    const { id } = useParams();

    async function submitForm(formData){
        let data = {
            "name" : formData.name,
            "description" : formData.description
        }
        try{

            if(id){
                await updateConditionRecord(id, data)
            }else{
                await sendConditionRecord(data)
            }
            showAlert('Registro Criado com Sucesso!', 'success')
            navigate('/conditions')

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
            title='Condição'
            initialValues={{name: '', description: ''}}
            fieldConfig={{
                name : {type: 'text', label: 'Nome', disabled: false},
                description : {type: 'textarea', label: 'Descrição', disabled: false}
            }}
            onSubmit={submitForm}
            onLoad={getConditionById}
        />
    )

    
}