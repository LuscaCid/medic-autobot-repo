export function Functions({
    htmlElements,
    listLiExam,
    listLiregisters,
    listGratuidades,
    actualValueOfRegisters,
    actualValueOfreg,
    actualvalueofGrat,

}){
    function adicionarRegistro(event){
        event.preventDefault()
        
        if(htmlElements.inputRegistro.value != ''){
            const reg = htmlElements.inputRegistro.value
            htmlElements.patientList.push(reg)
            console.log(htmlElements.patientList)
            const liReg = `                   
                    <span id="registro${actualValueOfreg}">Registro:<p> ${reg}</p></span>
                    <button id="close-button-reg${actualValueOfreg}">
                            <img src="../static/assets/close-button-svgrepo-com.svg">
                    </button>                 
                    `
            
            const createdElementLiRegister = document.createElement('li')
            createdElementLiRegister.id = `registro${actualValueOfreg}`
            
            listLiregisters.push(createdElementLiRegister)
            listLiregisters[actualValueOfreg].innerHTML = liReg;
            
            document.querySelector('.area-registros ul ').appendChild(createdElementLiRegister) 
            
            
            const botaoCloseReg = document.getElementById(`close-button-reg${actualValueOfreg}`)
            const elementoReg = document.getElementById(`registro${actualValueOfreg}`)
            if(botaoCloseReg){
                
                botaoCloseReg.addEventListener('click', ()=>{
                    event.preventDefault()
                    const father = botaoCloseReg.parentNode 
                    const selectedReg = father.querySelector('p')
                    const index = htmlElements.patientList.indexOf(selectedReg.textContent)
                    htmlElements.patientList.splice(index,1)
                    console.log(htmlElements.patientList)
                    elementoReg.remove()
                })
            } else {console.log('nao foi criado')}
            ++actualValueOfreg;
            
            htmlElements.inputRegistro.value = ''
            
        }
        else{alertNoData()}
    }

    /*refatoração de codigo, requalificação para envio de lista da gratuidade
    *adicao da gratuidade */

    function adicionarGratuidade(event){
        event.preventDefault()
        if(htmlElements.selectExamGrat.value!='null'){
            const createdElementLi = document.createElement('li')
            createdElementLi.id = `gratuidade${actualvalueofGrat}`
            listGratuidades.push(createdElementLi)
            console.log(listGratuidades[actualvalueofGrat])
            const actualExam=String(htmlElements.selectExamGrat.value)
            
            htmlElements.gratList.push(htmlElements.selectExamGrat.value)
            let close=  `close-button-grat${actualvalueofGrat}`
            const li = `
                <span id="grat${actualvalueofGrat}">exame: <p>${actualExam}</p></span> 
                <button id= ${close}>
                    <img src="../static/assets/close-button-svgrepo-com.svg">
                </button>     
                `
            createdElementLi.innerHTML = li
            
            console.log(htmlElements.gratList)
            
            document.querySelector('.area-gratuidades ul ').appendChild(createdElementLi) 
            
            const botaoCloseGrat = document.getElementById(`close-button-grat${actualvalueofGrat}`)
            const elemento = document.getElementById(`gratuidade${actualvalueofGrat}`)
            if(botaoCloseGrat){
                
                botaoCloseGrat.addEventListener('click', ()=>{
                    event.preventDefault()
                    const father = botaoCloseGrat.parentNode 
                    const selectededExamGrat = father.querySelector('p')
                    const index = htmlElements.gratList.indexOf(selectededExamGrat.textContent)
                    htmlElements.gratList.splice(index,1)
                    console.log(htmlElements.gratList)
                    elemento.remove()
                })
            } else {console.log('nao foi criado')}
            ++actualvalueofGrat;
            htmlElements.selectExamGrat.value = 'null'
        } else{
            alertNoData()
        }
    }

    /**acima a funcao que adiciona gratuidade */
    
    function adicionarExame(event){
        event.preventDefault()
        if(htmlElements.selectExam.value!='null'){
            const createdElementLi = document.createElement('li')
            createdElementLi.id = `exame${actualValueOfRegisters}`
            listLiExam.push(createdElementLi)
            console.log(listLiExam[actualValueOfRegisters])
            const actualExam=String(htmlElements.selectExam.value)
            
            htmlElements.examList.push(htmlElements.selectExam.value)
            let close=  `close-button${actualValueOfRegisters}`
            const li = `
                <span id="exame${actualValueOfRegisters}">exame: <p>${actualExam}</p></span> 
                <button id= ${close}>
                    <img src="../static/assets/close-button-svgrepo-com.svg">
                </button>     
                `
            createdElementLi.innerHTML = li
            
            console.log(htmlElements.examList)
    
           /* listLiExam[actualValueOfRegisters].innerHTML = li;*/
            
            document.querySelector('.area-exames ul ').appendChild(createdElementLi) 
            
            const botaoClose = document.getElementById(`close-button${actualValueOfRegisters}`)
            const elemento = document.getElementById(`exame${actualValueOfRegisters}`)
            if(botaoClose){
                
                botaoClose.addEventListener('click', ()=>{
                    event.preventDefault()
                    const father = botaoClose.parentNode 
                    const selectedExam = father.querySelector('p')
                    const index = htmlElements.examList.indexOf(selectedExam.textContent)
                    htmlElements.examList.splice(index,1)
                    console.log(htmlElements.examList)
                    elemento.remove()
                })
            } else {console.log('nao foi criado')}
            ++actualValueOfRegisters;
            htmlElements.selectExam.value = 'null'
        } else{
            alertNoData()
        }
    }

    function verifyIsNan(){
        console.log(htmlElements.crmMedInput.value)
        
        let isnum = Number(htmlElements.crmMedInput.value)
        if(isNaN(isnum)){htmlElements.alertErrorBox.classList.add('open')} 
        else{ 
            htmlElements.alertErrorBox.classList.remove('open')
            htmlElements.alertErrorBox.classList.add('close')
            setTimeout(()=>{htmlElements.alertErrorBox.classList.remove('close')},1000)
        }
        if(String(htmlElements.crmMedInput.value)=='backspace'){
            console.log('backspace')
        }
            if(isnum == 0){
                console.log('isnum ta vazio')
                htmlElements.alertErrorBox.classList.remove('open')
                
            }
    }

    function openDataSaved(){
        htmlElements.dataSaved.classList.add('open')
        setTimeout(() => {         
            htmlElements.dataSaved.classList.remove('open')
            htmlElements.dataSaved.classList.add('close')
            htmlElements.dataSaved.classList.remove('close')
        },1800);   
    }

    function alertNoData(){
            htmlElements.alertNoData.classList.add('open')
            setTimeout(() => {
            htmlElements.alertNoData.classList.remove('open') 
            htmlElements.alertNoData.classList.add('close') 
            htmlElements.alertNoData.classList.remove('close') 
        }, 2300);
    }
    
    function closeSectionGrateful(event){
        event.preventDefault()
        document.querySelector('.input-wrapper.procGrat').classList.add('hide')
        openDataSaved()
        htmlElements.gratList.splice(0, htmlElements.gratList.length)
        console.log(htmlElements.gratList)
        const allGratExams = document.querySelectorAll('.secao-gratuidade li')
        allGratExams.forEach(item => {
            item.remove()
        })
    }
    function openSectionGrateful(event){
        event.preventDefault()
        document.querySelector('.input-wrapper.procGrat').classList.remove('hide')
        /*const todasLiGrat = document.querySelector('.secao-gratuidade li')
        todasLiGrat.remove()*/
    }

    function addConsInGrat(event){
        event.preventDefault()
        htmlElements.ISConsGrat = 'sim'
        console.log(htmlElements.ISConsGrat)
        openDataSaved()
    }
    function removeConsFromGrat(event){
        event.preventDefault()
        htmlElements.ISConsGrat = 'nao'
        console.log(htmlElements.ISConsGrat)
        openDataSaved()
    }


    return {
        addConsInGrat,
        removeConsFromGrat,
        openSectionGrateful,
        closeSectionGrateful,
        alertNoData,
        openDataSaved,
        verifyIsNan,
        adicionarGratuidade,
        adicionarRegistro,
        adicionarExame,
    }

}