import { useNavigate} from 'react-router-dom';
import { getProfessionalById, sendProfessionalRecord } from '../../common/api';
import GenericForm from "./GenericForm";

export default function HealthCareProfessionalForm( { onFinished } ){
    const navigate = useNavigate();


    async function submitForm(formData){
        let data = {
            "name" : formData.name,
            "surname" : formData.surname,
            "cpf" : formData.cpf,
            "birth_date": formData.birth_date,
            "crm": formData.crm
        }
        try{
            console.log(data)
            const response = await sendProfessionalRecord(data)
            console.log(response)
            onFinished(response)
            alert('Registro Criado com Sucesso!')
        }catch(err){
            console.log('deerr')
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
                name : { type: 'text' },
                surname : { type: 'text'},
                cpf :{ type: 'text'},
                birth_date : {type: 'date'},
                crm : {type: 'text'}
            }}
            onSubmit={submitForm}
            onLoad={getProfessionalById}
        />
    )
    
}