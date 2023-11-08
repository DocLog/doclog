import { useState, useEffect, useContext } from "react";
import { Context } from "../../context/AuthContext";
import { useNavigate, useParams } from 'react-router-dom';
import { getPatientRecordById } from '../../common/api';
import styles from '../../styles/Form.module.css'

export default function PatientForm(){
    const { isLogged } = useContext(Context);
    const navigate = useNavigate();
    const { id } = useParams();

    const [name, setName] = useState('');
    const [surname, setSurname] = useState('');
    const [cpf, setCPF] = useState(0)
    const [birthDate, setBirthDate] = useState(Date())
    const [bloodType, setBloodType] = useState('Selecione uma opção')
    const [registerDate, setRegisterDate] = useState(Date())
    const [notes, setNotes] = useState('')

    useEffect(() => {
        if(!isLogged){
            navigate('/login')
        }

        if(id){
            getPatientRecordById(id).then(({data}) =>{
                console.log(data)
                setName(data.name)
                setSurname(data.surname)
                setCPF(data.cpf)
                setBirthDate(data.birth_date)
                setBloodType(data.blood_type)
                setRegisterDate(data.register_date)
                setNotes(data.notes)
            })
            
        }
    }, [isLogged, navigate, id])

    

    return(
        <div className={styles.form}>
            <h2>Paciente</h2>
            <fieldset>
                <legend>Ações</legend>
                <div className={styles.actions}>
                    <button className={styles.action}>Ocorrências</button>
                    <button className={styles.action}>Medicamentos</button>
                    <button className={styles.action}>Condições</button>
                </div>
            </fieldset>

            
            <div className={styles.form_fields}>

                <div className={styles.form_group}>
                    <label htmlFor="name">Nome </label>
                    <input
                        type="text"
                        placeholder="name"
                        id="name"
                        name="name"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        disabled
                        />
                </div>

                <div className={styles.form_group}>
                    <label htmlFor="surname">Sobrenome </label>
                    <input
                        type="text"
                        placeholder="surname"
                        id="surname"
                        name="surname"
                        value={surname}
                        onChange={(e) => setSurname(e.target.value)}
                        disabled
                        />
                </div>

                <div className={styles.form_group}>
                    <label htmlFor="cpf">CPF </label>
                    <input
                        type="text"
                        placeholder="cpf"
                        id="cpf"
                        name="cpf"
                        value={cpf}
                        onChange={(e) => setCPF(e.target.value)}
                        disabled
                        />
                </div>

                <div className={styles.form_group}>
                    <label htmlFor="birthDate">Data de Nascimento </label>
                    <input
                        type="date"
                        placeholder="birthDate"
                        id="birthDate"
                        name="birthDate"
                        value={birthDate}
                        onChange={(e) => setBirthDate(e.target.value)}
                        disabled
                        />
                </div>
                
                <div className={styles.form_group}>
                    <label htmlFor="blood-type">Tipo Sanguíneo </label>
                    <select name="blood-type" onChange={(e) => {console.log(e.target.value);setBloodType(e.target.value)}} value={bloodType} disabled>
                        <option value="Selecione uma opção">Selecione uma opção</option>
                        <option value="A+">A+</option>
                        <option value="A-">A-</option>
                        <option value="B+">B+</option>
                        <option value="B-">B-</option>
                        <option value="AB+">AB+</option>
                        <option value="AB-">AB-</option>
                        <option value="O+">O+</option>
                        <option value="O-">O-</option>
                    </select>
                </div>
                <div className={styles.form_group}>
                    <label htmlFor="register-date">Data de Registro </label>
                    <input
                        type="datetime-local"
                        placeholder="register-date"
                        id="register-date"
                        name="register-date"
                        value={registerDate}
                        onChange={(e) => setRegisterDate(e.target.value)}
                        disabled
                        />
                </div>
                <div className={styles.form_group}>
                    <label htmlFor="notes">Notas </label>
                    <textarea
                        placeholder="notes"
                        id="notes"
                        name="notes"
                        value={notes}
                        onChange={(e) => setNotes(e.target.value)}
                        disabled
                        rows='3'
                        >

                    </textarea>
                </div>
                </div>
            
        </div>
    )
}