
import { useNavigate } from 'react-router-dom';
import { getUserById, createUser } from '../../common/api';
import GenericForm from "./GenericForm";

export default function UserFormCreate({ role, personId }){
    const navigate = useNavigate();

    async function submitForm(formData){
        let data = {
            "name" : formData.name,
            "password" : formData.password,
            "email" : formData.email,
            "role_id" : Number(role),
            "patient_id" : (role == '3' ? personId : null) ,
            "healthcare_professional_id" : (role == '2' ? personId : null),
        }
        try{
            console.log(data)
            const response = await createUser(data)
            console.log(response)
            alert('Registro Criado com Sucesso!')
            navigate('/dashboard')
        }catch(err){
            console.log('deerr')
        }
    }

    return(
        <GenericForm
            title='Usuário'
            initialValues={
                {
                    name: '', 
                    password: '', 
                    email: ''
            }}
            fieldConfig={{
                name : {type: 'text'},
                password : {type: 'password'},
                email : {type: 'email'}
            }}
            onSubmit={submitForm}
            onLoad={getUserById}
        />
    )

    
}