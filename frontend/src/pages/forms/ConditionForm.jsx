
import { useNavigate } from 'react-router-dom';
import { getConditionById, sendConditionRecord } from '../../common/api';
import GenericForm from "./GenericForm";

export default function ConditionForm(){
    const navigate = useNavigate();

    async function submitForm(formData){
        let data = {
            "name" : formData.name,
            "description" : formData.description
        }
        try{
            console.log(data)
            const response = await sendConditionRecord(data)
            console.log(response)
            alert('Registro Criado com Sucesso!')
            navigate('/conditions')
        }catch(err){
            console.log('deerr')
        }
    }

    return(
        <GenericForm
            title='Condição'
            initialValues={{name: '', description: ''}}
            fieldConfig={{
                name : {type: 'text'},
                description : {type: 'textarea'}
            }}
            onSubmit={submitForm}
            onLoad={getConditionById}
        />
    )

    
}