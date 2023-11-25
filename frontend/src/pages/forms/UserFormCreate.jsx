
import { useNavigate } from 'react-router-dom';
import { getUserById, createUser } from '../../common/api';
import GenericForm from "./GenericForm";
import { showAlert } from "../../common/swalAlert";

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
            await createUser(data)
            showAlert('Registro Criado com Sucesso!', 'success')
            navigate('/dashboard')
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
            title='Usuário'
            initialValues={
                {
                    name: '', 
                    password: '', 
                    email: ''
            }}
            fieldConfig={{
                name : {type: 'text', label: 'Nome'},
                password : {type: 'password', label: 'Senha'},
                email : {type: 'email', label: 'Email'}
            }}
            onSubmit={submitForm}
            onLoad={getUserById}
        />
    )

    
}