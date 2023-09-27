export function Elements(){
    
    const nameMedInput = document.querySelector('#medic-name')
    const crmMedInput = document.querySelector('#medic-crm')
    const speciality = document.querySelector('#opcoes-especialidade')
    const procedimentos = document.querySelector('.secao-procedimentos')
    const addExamButton = document.querySelector('#add-exame')
    const addRegisterButton = document.querySelector('#add-registro')
    const selectExam = document.querySelector('#opcoes-exames')
    const selectExamGrat = document.querySelector('#opcoes-exames-gratuidade')
    const inputRegistro = document.querySelector('#registro')
    const selectEspecialidade = document.querySelector('#opcoes-especialidade')
    const alertErrorBox = document.querySelector('.alert-error')
    const alertNoData = document.querySelector('.alert-error-data')
    const dataSaved = document.querySelector('.gratRegistrada')
    const buttonRemoveItemFromExam = document.querySelector('#add-exame')
    const buttonAddExamInGratuidade = document.querySelector('#add-gratuidade')
    const sendButton = document.querySelector('#send')
    const btnConsSim = document.querySelector('#sim-cons-grat')
    const btnConsNao = document.querySelector('#nao-cons-grat')
    const yesGrat = document.getElementById('simGratuidade')
    const noGrat = document.getElementById('naoGratuidade')
    const wrap = new Date()
    const dfitp = Number(wrap.getDate())
    const mfitp = Number(wrap.getMonth()) + 1
    const yfitp = Number(wrap.getFullYear())
    let ISConsGrat = 'nao';
    let patientList = []
    let examList = []
    let gratList = []
    return {   
        yfitp,
        dfitp,
        mfitp,
        btnConsNao,
        btnConsSim,
        ISConsGrat, 
        selectEspecialidade,
        yesGrat,
        noGrat,
        dataSaved,
        sendButton,       
        buttonRemoveItemFromExam,
        alertNoData,
        gratList,
        patientList,
        examList,
        nameMedInput,
        crmMedInput,
        speciality,
        procedimentos,
        alertErrorBox,
        addExamButton,
        addRegisterButton,
        selectExam,
        selectExamGrat,
        inputRegistro,
        buttonAddExamInGratuidade,

    }
}
