import { useEffect } from 'react'
import styles from '../styles/Card.module.css'

export default function Card(props){


    return(
        <div className={styles.container}>
            <div className={styles.title}>{props.content}</div>
            <div className={styles.actions_card}>
                {props.isDeleted === 'true' ? <div id={props.id} onClick={props.onDelete}><img id={props.id} src='/remove.png'  alt="remover"/></div> : ''}
                {props.isChanged === 'true' ? <div id={props.id} onClick={props.onEdit}><img id={props.id} src='/edit.png' alt="editar" /></div> : ''}
            </div>
        </div>
    )
}