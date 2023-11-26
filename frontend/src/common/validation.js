export function isEmptyFields(fields){
    let hasError = false;
    let messageError = '';
    Object.keys(fields).map((element) => {
        if(typeof fields[element] === "string" && fields[element].trim().length === 0){
            hasError = true;
            messageError = 'Campos não podem estar vazios';
        }
    });

    if(hasError){
        return messageError;
    }

    return ''

}

export  function isValidDate(fields){
    let hasError = false;
    let messageError = '';
    Object.keys(fields).map((element) => {
        if(typeof fields[element] === "date" && (Date.now() < fields[element])){
            hasError = true;
            messageError = 'Data inválida (Não se pode colocar datas acima da data de hoje)';
        }
    });

    if(hasError){
        return messageError;
    }

    return '';
}

