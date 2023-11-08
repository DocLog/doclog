import { useState } from "react";
import styles from '../../styles/User.module.css'
import HealthCareProfessionalForm from "./HealthCareProfessionalForm";
import UserFormCreate from "./UserFormCreate";
import PatientForm from "./PatientForm";

export default function UserForm(){
    const [step, setStep] = useState(0)
    const [role, setRole] = useState('1')
    const [ person, setPerson] = useState(null)
    const steps = [0, 1, 2];

    function handleBack(){
        setStep(step - 1)
    }

    function handleNext(){
        setStep(step + 1)
    }

    function handleRole(e){
        setRole(e.target.id)
        if(e.target.id === '1'){
            setStep(2)
        }else{
            handleNext()
        }
    }

    function handleFinishForm(response){
        console.log(role)
        const { data } = response
        setPerson(data.id)
        setStep(step+1)
    }

    return(
        <div className={styles.container}>

            { step === 0 ? 
                (
                    <div >
                        <h2 className={styles.title}>Escolha do tipo de usuário</h2> 
                        <div className={styles.actions}>
                            <button id='3' className={styles.action} onClick={handleRole}>Paciente</button>
                            <button id='2' className={styles.action} onClick={handleRole}>Profissional de Saúde</button>
                            <button id='1' className={styles.action} onClick={handleRole}>Administrador de Sistema</button>
                        </div>
                    </div>
                )
            : 
                ''
            }
            { step === 1 ? 
            (
                <div>
                    {role === '2' ? 
                    (
                        
                        <HealthCareProfessionalForm onFinished={handleFinishForm}></HealthCareProfessionalForm>
                        
                    )
                    :
                    (
                        <PatientForm onFinished={handleFinishForm}/>
                    )}
                </div>
            )
            : 
                ''}
            { step === 2 ? 
                <div>
                    <UserFormCreate role={role} personId={person}></UserFormCreate>
                </div> 
            : 
                ''
            }
         
        </div>
    )
}