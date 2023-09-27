import { Elements } from "./elements.js"
import { Functions } from "./functions.js";

var actualValueOfRegisters = 0;
var actualValueOfreg = 0;
var actualvalueofGrat =0;

const listLiExam = []
const listLiregisters = []
const listGratuidades = []

const htmlElements = Elements()
const JSfunctions = Functions({
    htmlElements,
    listLiExam,
    listLiregisters,
    actualValueOfRegisters,
    actualValueOfreg,
    actualvalueofGrat,
    listGratuidades,
    
})

/**
 * espacos de memoria que eu preciso transferir pro python
 * 
 * nome do medic
 * crm
 * especialidade
 * 
 * main.js nomes das variaveis
 * 
 * lista => procedimentos (htmlElements.examList)
 * lista => gratuidade (htmlElements.gratList)
 * lista => registros dos pacientes (htmlElements.patientList)
 * 
 * main.py nomes das variaveis
 * 
 */

htmlElements.sendButton.addEventListener('click', (event) => {
   
    if(htmlElements.crmMedInput.value!='' || htmlElements.nameMedInput.value != ''){
        JSfunctions.openDataSaved()
        const nameMed = htmlElements.nameMedInput.value
        const crm = htmlElements.crmMedInput.value
        fetch('/enviar_lista', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                consultaIsGrat : htmlElements.ISConsGrat,
                procedimentosJson: htmlElements.examList,
                gratuidadesJson: htmlElements.gratList,
                registrosJson: htmlElements.patientList,
                crm: crm,
                nomeMedico:nameMed,
                especialidade: htmlElements.selectEspecialidade.value,
                dfitp : htmlElements.dfitp,
                mfitp : htmlElements.mfitp

            }),
        })
            .then(response => response.json())
            .then(data => {
                console.log('Resposta do servidor:', data);
            })
            .catch(error => {
                console.error('Erro:', error);
            });
    } else {JSfunctions.alertNoData()}    
        
        

});

htmlElements.btnConsNao.addEventListener('click', JSfunctions.removeConsFromGrat)

htmlElements.btnConsSim.addEventListener('click', JSfunctions.addConsInGrat)

htmlElements.crmMedInput.addEventListener('keyup', JSfunctions.verifyIsNan)

htmlElements.addExamButton.addEventListener('click',JSfunctions.adicionarExame)

htmlElements.buttonAddExamInGratuidade.addEventListener('click',JSfunctions.adicionarGratuidade)

htmlElements.yesGrat.addEventListener('click', JSfunctions.openSectionGrateful)

htmlElements.noGrat.addEventListener('click', JSfunctions.closeSectionGrateful)

htmlElements.addRegisterButton.addEventListener('click', JSfunctions.adicionarRegistro)




