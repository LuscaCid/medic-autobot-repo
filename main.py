from flask import Flask, request, jsonify, render_template
import pyautogui
import time
from pytesseract import pytesseract
import os
pw = ""

def baixa_automatica(qtd_images):
    x, y = pyautogui.locateCenterOnScreen("./_internal/images/chrome-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
    # qtd_images serve para mostrar quantas imagens tem para ler dentro da pasta
    i = 0  # de onde comeca a leitura para o registro das guias de consulta
    pyautogui.click(x, y)
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "1")
    while i <= qtd_images:  # inicio do loop
        time.sleep(1.5)
        pyautogui.scroll(500)
        posicao = str(i)
        if os.path.isfile(f"C:\\Users\\recepcao\Desktop\\Nova pasta (2)\leitura-cod-id{posicao}.png"):
            cod_id = pytesseract.image_to_string(f"C:\\Users\\recepcao\Desktop\\Nova pasta (2)\leitura-cod-id{posicao}.png")

            if pyautogui.locateCenterOnScreen("./_internal/images/insercao-cod.png", confidence=0.9):  # ta em branco e ent o ultimo passou
                x, y = pyautogui.locateCenterOnScreen("./_internal/images/insercao-cod.png", confidence=0.9)
                pyautogui.doubleClick(x, y)
            else:
                pyautogui.doubleClick(x=204, y=608)
            pyautogui.write(cod_id)
            pyautogui.click(x=354, y=608)
            time.sleep(0.4)  # tempo passivel de mudanca
            pyautogui.scroll(-500)

            time.sleep(1.2)
            pyautogui.scroll(-500)
            if pyautogui.locateCenterOnScreen("./_internal/images/data-saved.png"):
                pyautogui.press("enter")
                time.sleep(0.5)
                pyautogui.scroll(-100)
            if pyautogui.locateCenterOnScreen("./_internal/images/confirm-execution.png",confidence=0.9):
                x, y = pyautogui.locateCenterOnScreen("./_internal/images/confirm-execution.png", confidence=0.9)
                pyautogui.click(x, y)
                os.remove(f"C:\\Users\\recepcao\Desktop\\Nova pasta (2)\leitura-cod-id{posicao}.png")

            elif pyautogui.locateCenterOnScreen("./_internal/images/id-fora-validade.png", confidence=0.9):
                pyautogui.press("enter")  # neste caso teria que fazer a verificacao de algum id fora de validade

            elif pyautogui.locateCenterOnScreen("./_internal/images/duvida.png",confidence=0.9):
                pyautogui.press("enter")
        else:
            print("este aquivo nao existe")
        i = i + 1  # fim do loop
def funcao_btn_imprimir():
    time.sleep(0.3)
    while True:
        if pyautogui.locateCenterOnScreen("./_internal/images/botaoimprimir.png", confidence=0.9):
            x, y = pyautogui.locateCenterOnScreen("./_internal/images/botaoimprimir.png", confidence=0.9)
            break
    time.sleep(0.2)
    pyautogui.click(x, y)
pd = "ad1921022"

pwo = "ad2123#sa"
pwo = pd
pturing = pw
def continuacao_consulta(crm,especialidade,nomeMed,procedimentos,gratuidade,procedimentosPaciente,gratuidadeOrig):
    global position
    time.sleep(0.5)
    while pyautogui.locateCenterOnScreen("./_internal/images/carregando.png", confidence=0.9):
        print("carregando")
    time.sleep(0.9)
    pyautogui.doubleClick(x=366, y=154)
    time.sleep(0.1)
    pyautogui.write(crm)
    pyautogui.click(x=442, y=155)
    time.sleep(0.1)
    while pyautogui.locateCenterOnScreen("./_internal/images/carregando.png", confidence=0.9):
        print("carregando")
    time.sleep(0.3)
    i,j = pyautogui.locateCenterOnScreen("./_internal/images/confirmacaomedico.png", confidence=0.9)
    pyautogui.click(i, j)
    time.sleep(0.5)
    pyautogui.scroll(-500)
    consu_cod = "0301010072"
    time.sleep(0.8)
    x, y = pyautogui.locateCenterOnScreen("./_internal/images/codprocedimentoNew.png", confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(.5)
    pyautogui.write(consu_cod)
    pyautogui.click(x=290, y=454)
    time.sleep(1.7)
    pyautogui.scroll(-1000)
    time.sleep(0.5)
    x, y = pyautogui.locateCenterOnScreen("./_internal/images/medoftalmo.png", confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(0.4)
    while pyautogui.locateCenterOnScreen("./_internal/images/carregando.png", confidence=0.9):
        time.sleep(0.4)
    time.sleep(0.4)
    pyautogui.scroll(-500)
    time.sleep(0.4)
    x, y = pyautogui.locateCenterOnScreen("./_internal/images/especialidade.png", confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(0.1)
    pyautogui.write(especialidade)
    pyautogui.press("enter")
    time.sleep(0.7)
    pyautogui.scroll(-1000)
    time.sleep(0.2)
    x, y = pyautogui.locateCenterOnScreen("./_internal/images/proximo.png", confidence=0.9)
    pyautogui.click(x,y)
    time.sleep(2.8)
    if pyautogui.locateCenterOnScreen("_internal/images/popup-qtd.png", confidence=0.9):
        pyautogui.press("enter")
        time.sleep(0.4)
        pyautogui.scroll(150)
        x , y = pyautogui.locateCenterOnScreen("./_internal/images/medoftalmo.png", confidence=0.9)
        pyautogui.click(x,y)
        while pyautogui.locateCenterOnScreen("./_internal/images/carregando.png", confidence=0.9):
            time.sleep(0.4)
        time.sleep(1)
        pyautogui.scroll(-150)
        time.sleep(0.3)
        x, y = pyautogui.locateCenterOnScreen("./_internal/images/especialidade.png", confidence=0.9)
        pyautogui.click(x, y)
        pyautogui.write('retina')
        pyautogui.press("enter")
        time.sleep(0.7)
        pyautogui.scroll(-1000)
        time.sleep(0.2)
        x, y = pyautogui.locateCenterOnScreen("./_internal/images/proximo.png", confidence=0.9)
        time.sleep(0.1)
        pyautogui.click(x, y)
        time.sleep(0.4)
    if pyautogui.locateCenterOnScreen("./_internal/images/ddd.png",confidence=0.9) or pyautogui.locateCenterOnScreen('./_internal/images/mensagem-nova.png', confidence=0.9) or pyautogui.locateCenterOnScreen('./_internal/images/dddobrigatorio.png', confidence=0.9):
        pyautogui.press("enter")
        time.sleep(0.2)
        pyautogui.scroll(2000)
        time.sleep(0.9)
        x , y = pyautogui.locateCenterOnScreen("./_internal/images/tipo-de-telefone.png",confidence=0.9)
        pyautogui.click(x,y + 20)
        pyautogui.click(x=626, y=542)
        time.sleep(1.5)
        pyautogui.doubleClick(x=803, y=600)
        pyautogui.press('backspace', 3)
        time.sleep(0.2)
        pyautogui.write("71")
        time.sleep(0.2)
        pyautogui.click(803,550)
        time.sleep(0.8)
        pyautogui.doubleClick(x=868, y=601)
        time.sleep(0.8)
        
        pyautogui.write("922125533")
        time.sleep(1)
        pyautogui.scroll(-2000)
        x, y = pyautogui.locateCenterOnScreen("./_internal/images/proximo.png", confidence=0.9)
        time.sleep(0.6)
        pyautogui.click(x,y)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.scroll(-2000)
        time.sleep(0.3)
        if pyautogui.locateCenterOnScreen("./_internal/images/proximo.png", confidence=0.9):
            x, y = pyautogui.locateCenterOnScreen("./_internal/images/proximo.png", confidence=0.9)
            pyautogui.click(x, y)
            time.sleep(1)
            if pyautogui.locateCenterOnScreen("_internal/images/popup-qtd.png", confidence=0.9):
                pyautogui.press("enter")
                pyautogui.scroll(150)
                x , y = pyautogui.locateCenterOnScreen("./_internal/images/medoftalmo.png", confidence=0.9)
                pyautogui.click(x,y)
                pyautogui.scroll(-150)
                x, y = pyautogui.locateCenterOnScreen("./_internal/images/especialidade.png", confidence=0.9)
                pyautogui.click(x, y)
                pyautogui.write('retina')
                pyautogui.press("enter")
                time.sleep(0.7)
                pyautogui.scroll(-1000)
                time.sleep(0.2)
                x, y = pyautogui.locateCenterOnScreen("./_internal/images/proximo.png", confidence=0.9)
                time.sleep(0.1)
                pyautogui.click(x, y)
                time.sleep(0.4)
        
    pyautogui.scroll(-500)
    time.sleep(0.8)
    if pyautogui.locateCenterOnScreen("./_internal/images/okcrmbtn.png", confidence=0.9) == False: pyautogui.click(x=127, y=217)
    else:
        x,y = pyautogui.locateCenterOnScreen("./_internal/images/okcrmbtn.png", confidence=0.9)
        pyautogui.click(x, y)
    time.sleep(1.9)
    if  pyautogui.locateCenterOnScreen("./_internal/images/finalizar.png", confidence=0.9):
        x,y = pyautogui.locateCenterOnScreen("./_internal/images/finalizar.png", confidence=0.9)
        pyautogui.click(x, y)
    else: pyautogui.click(x=1198, y=589)
    time.sleep(1.6)

    time.sleep(3.2)
    pyautogui.hotkey("ctrl","p")
    funcao_btn_imprimir()
    time.sleep(0.5)
    pyautogui.doubleClick(x=111, y=313)  # alocacao do proc
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.2)
    pyautogui.doubleClick(x=113, y=310)  # alocacao do proc
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.1)
    x, y = pyautogui.locateCenterOnScreen("./_internal/images/icone-vida.png", region=(300, 0, 800, 40), confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(0.5)
    pyautogui.click(x=164, y=470)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.click(x=255, y=473)
    time.sleep(7.9)
    pyautogui.scroll(-1000)
    time.sleep(0.1)
    x, y = pyautogui.locateCenterOnScreen("./_internal/images/selecionarProfissional.png", region=(50, 130, 700, 270), confidence=0.9)
    pyautogui.click(x, y)
    if nomeMed.startswith("clara") or nomeMed.startswith("CLARA"):
        pyautogui.write("andre")
        pyautogui.press("down")
    else:
        pyautogui.write(nomeMed)
    if nomeMed.startswith("andre") or nomeMed.startswith("Andre") or nomeMed.startswith("ANDRE"):
        pyautogui.press("down")
    time.sleep(0.4)
    pyautogui.press("enter")
    time.sleep(0.3)
    while pyautogui.locateCenterOnScreen("./_internal/images/carregando.png", confidence=0.9) == True:
        print("carregando med")
    time.sleep(1.2)
    twoTimes = 0
    i = 1
    while i < len(procedimentos):
        verifier = 0
        time.sleep(1.9)
        pyautogui.scroll(-1000)
        time.sleep(0.1)
        if pyautogui.locateCenterOnScreen("./_internal/images/selecionarProcedimento.png", confidence=0.9):
            x, y = pyautogui.locateCenterOnScreen("./_internal/images/selecionarProcedimento.png", confidence=0.9)
            pyautogui.click(x, y)
        else:
            pyautogui.click(x=294, y=505)
        if procedimentos[i] == "ceratoscopia":
            pyautogui.write("topografia")
        else:
            pyautogui.write(procedimentos[i])
        pyautogui.press("enter")
        time.sleep(1)
        
        if pyautogui.locateCenterOnScreen("./_internal/images/popup-qtd.png", confidence=0.9) == True:
            pyautogui.press("enter")
            gratuidade.append(procedimentos[i])
            continue
        time.sleep(1.4)
        conter = 0
        while pyautogui.locateCenterOnScreen("./_internal/images/carregando.png", confidence=0.9):
            time.sleep(1.3)
            conter += 1
            print(conter)
            if conter > 7:
                verifier = 1
                gratuidade.append(procedimentos[i])
                pyautogui.press('enter')
                break
                

        if procedimentos[i].startswith(procedimentos[i - 1]) and verifier == 0:
            time.sleep(1)
            while True:
                if pyautogui.locateCenterOnScreen("./_internal/images/botaosim2.png", confidence=0.9):
                    break
                time.sleep(0.2)
                print("carregando")
            time.sleep(1)
            x, y = pyautogui.locateCenterOnScreen("./_internal/images/botaosim2.png", confidence=0.9)
            pyautogui.click(x, y)
            time.sleep(0.8)
            while True:
                print("saindo da tela")
                if pyautogui.locateCenterOnScreen("./_internal/images/botaosim2.png", confidence=0.9) != True:
                    break
            time.sleep(2.8)
            twoTimes = 1
        else:
            time.sleep(1.4)

        if verifier == 0: procedimentosPaciente.append(procedimentos[i])
        i = i + 1
        pyautogui.scroll(-1000)
    time.sleep(0.7)
    if(twoTimes==1):
        time.sleep(4.3)
    pyautogui.scroll(-2500)
    if len(procedimentosPaciente) > 1 and procedimentosPaciente != "vetor":
        pyautogui.scroll(-500)
        time.sleep(0.2)
        pyautogui.scroll(-500)
        if(pyautogui.locateCenterOnScreen("./_internal/images/imprimirGuia.png", confidence=0.9)):
            x, y = pyautogui.locateCenterOnScreen("./_internal/images/imprimirGuia.png", confidence=0.9)
            pyautogui.click(x, y)
        else: pyautogui.click(x=309, y=551)
        time.sleep(5.8)
        pyautogui.hotkey("ctrl", "p")
        funcao_btn_imprimir()
        time.sleep(0.4)
    else :
        pyautogui.scroll(2500)
        time.sleep(0.4)
        pyautogui.press("f5")
        time.sleep(1.4)
        pyautogui.press("enter")
        
    # voltar para guia de agendamento
    # indo na aba do codigo de id
    pyautogui.click(x=381, y=22)
    time.sleep(0.3)
    pyautogui.keyDown("ctrl")
    pyautogui.press("+",6)
    pyautogui.keyUp("ctrl")
    time.sleep(0.4)
    sc = pyautogui.screenshot(region=(35, 320, 390, 80))
    position = 100
    sc.save(f"C:\\Users\\recepcao\Desktop\\Nova pasta (2)\\leitura-cod-id{position}.png")
    time.sleep(0.4)
    pyautogui.keyDown("ctrl")
    pyautogui.press("-", 6)
    pyautogui.keyUp("ctrl")
    position = position + 1
    time.sleep(0.2)
    pyautogui.doubleClick(x=86, y=213)
    pyautogui.hotkey("ctrl", "c")
    pyautogui.hotkey("ctrl", "w")
    time.sleep(0.3)

    # com o codigo de identificador copiado:
    x, y = pyautogui.locateCenterOnScreen("./_internal/images/atende-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
    pyautogui.click(x, y)
    pyautogui.press("f10")
    time.sleep(0.3)
    pyautogui.press("left")
    time.sleep(0.8)
    pyautogui.press("enter",2)
    time.sleep(0.5)
    pyautogui.press("f5")
    time.sleep(2.8)
    pyautogui.click(500,500)
    pyautogui.press("enter",3)
    time.sleep(0.4)
    pyautogui.press("enter")
    time.sleep(0.4)
    pyautogui.hotkey("ctrl", "enter")
    time.sleep(0.4)
    pyautogui.write("consulta medica")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.3)
    pyautogui.press("TAB", 3)
    time.sleep(0.3)
    if nomeMed.startswith("gerda lucia"):
        pyautogui.write("gerda")
    else:
        pyautogui.write(nomeMed)
    time.sleep(0.3)
    pyautogui.press("down")
    time.sleep(0.4)
    pyautogui.press("f5")
    time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(0.4)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.2)
    pyautogui.press("enter",2)
    time.sleep(0.4)
    k = 810
    j = 442

    if len(procedimentosPaciente) > 1:
        i = len(procedimentosPaciente) -1
        while i > 0:
            x, y = pyautogui.locateCenterOnScreen("./_internal/images/chrome-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
            pyautogui.click(x, y)
            time.sleep(0.1)

            pyautogui.click(x=614, y=20)
            time.sleep(0.2)
            pyautogui.moveTo(x=1252, y=439)
            time.sleep(0.2)
            pyautogui.scroll(-1500)
            time.sleep(0.2)
            pyautogui.doubleClick(k, j)
            pyautogui.hotkey("ctrl", "c")
            pyautogui.doubleClick(k - 30, j)
            pyautogui.hotkey("ctrl", "c")

            time.sleep(0.1)
            if i == 1:
                pyautogui.hotkey("ctrl","w")
            j = j - 30
            x, y = pyautogui.locateCenterOnScreen("./_internal/images/atende-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
            pyautogui.click(x, y)
            time.sleep(0.3)
            pyautogui.press("f3")
            time.sleep(0.3)
            pyautogui.hotkey("ctrl", "enter")
            time.sleep(0.2)
            pyautogui.write(procedimentosPaciente[i])
            time.sleep(0.2)
            pyautogui.press("enter")
            time.sleep(0.2)
            pyautogui.press("enter")
            pyautogui.press("TAB", 3)
            pyautogui.write(nomeMed)
            pyautogui.press("down")
            pyautogui.press("f5")
            time.sleep(0.2)
            pyautogui.press("enter")
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.1)
            pyautogui.press("enter")
            time.sleep(0.1)
            pyautogui.press("enter")
            time.sleep(0.3)
            i = i - 1

    time.sleep(1)
    pyautogui.press("enter", 3)

    gratuidade.clear()

    if len(gratuidade) > 1 and gratuidade != "vetor":  # se tiver algo  na gratuidade, é necessario lançar
        pyautogui.press("f9", 3)
        pyautogui.press("f10")
        time.sleep(0.2)
        pyautogui.press("f10")
        pyautogui.click(x=114, y=166)
        pyautogui.write("gratuidade")
        pyautogui.press("down")
        time.sleep(0.2)
        pyautogui.press("f5")
        time.sleep(0.3)
        pyautogui.press("enter")
        i = 1  # a posicao 0 tem "vetor"
        while i < len(gratuidade):
            pyautogui.press("f3")
            time.sleep(0.3)
            pyautogui.hotkey("ctrl", "enter")
            time.sleep(0.2)
            pyautogui.write(gratuidade[i])
            time.sleep(0.2)
            pyautogui.press("enter")
            time.sleep(0.2)
            pyautogui.press("enter")
            pyautogui.press("TAB", 3)
            pyautogui.write(nomeMed)
            pyautogui.press("down")
            pyautogui.press("f5")
            time.sleep(0.2)
            pyautogui.press("enter", 3)
            time.sleep(0.1)
            pyautogui.press("enter")
            time.sleep(0.3)
            pyautogui.press("f3")
            i = i + 1
        time.sleep(0.2)
        pyautogui.press("left")
        pyautogui.press("enter")
        pyautogui.press("f8")
        time.sleep(1.5)
        pyautogui.press("enter", 3)
        time.sleep(9)
        pyautogui.press("enter")
        pyautogui.press("enter")
        gratuidade.clear()
        gratuidade = gratuidadeOrig

    time.sleep(0.4)
    pyautogui.hotkey("f2")
    pyautogui.hotkey("f4")  #####
    x, y = pyautogui.locateCenterOnScreen("./_internal/images/chrome-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(0.3)
    x, y = pyautogui.locateCenterOnScreen("./_internal/images/icone-vida.png", region=(240, 0, 1000, 40), confidence=0.9)
    pyautogui.click(x,y)
    pyautogui.press("f5")
    time.sleep(0.4)
    pyautogui.press("enter")
    time.sleep(3.5)
    pyautogui.scroll(2000)
    time.sleep(0.2)
    pyautogui.hotkey("ctrl", "1")
    time.sleep(0.1)
    pyautogui.click(x=717, y=430)
    time.sleep(0.6)
    pyautogui.click(x=717, y=530)
    pyautogui.scroll(1000)
    time.sleep(0.5)
    pyautogui.scroll(-500)
    procedimentosPaciente.clear()
    procedimentosPaciente.append("vetor")

position = 1



def program(procedimentosPaciente,procedimentos,pacientes,gratuidade,gratuidadeOrig,crm,nameMed,especialidade):
    time.sleep(0.5)
    # este comando direciona pro google com o vida ja aberto e ja logado
    x, y = pyautogui.locateCenterOnScreen("./_internal/images/atende-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
    pyautogui.click(x, y)
    pyautogui.press("f4")
    x, y = pyautogui.locateCenterOnScreen("./_internal/images/chrome-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(0.2)  # precisa-se esperar as coisas acontecerem
    # este comando seleciona a primeira guia onde deve estar localizado o vida - amb
    pyautogui.hotkey('ctrl','w')
    time.sleep(0.2)
    pyautogui.hotkey("ctrl", "1")
    time.sleep(0.2)
    pyautogui.moveTo(x, y - 90)
    pyautogui.scroll(-500)
    time.sleep(0.4)
          
    #começo da cobrança da fila
    if len(pacientes) > 0:
        cont =0
        while cont < len(pacientes):#secao onde irei entrar no smart e pesquisar
            gratuidade = gratuidadeOrig
            time.sleep(0.5)
            x,y = pyautogui.locateCenterOnScreen("./_internal/images/atende-icon.png",region=(100,730,1200,49),confidence=0.9)
            pyautogui.click(x,y)
            time.sleep(0.5)
            pyautogui.press("f2")
            time.sleep(0.2)
            pyautogui.press("f4")
            time.sleep(0.4)
            pyautogui.hotkey("shift","TAB")
            time.sleep(0.2)
            pyautogui.write(pacientes[cont])
            cont = cont + 1
            pyautogui.press("f4")
            time.sleep(0.2)
            pyautogui.press("left")
            time.sleep(0.2)
            pyautogui.press("enter")
            time.sleep(0.3)
            pyautogui.press("f10")
            time.sleep(0.2)
            pyautogui.press("left")
            time.sleep(0.1)
            pyautogui.press("enter")
            time.sleep(0.2)
            pyautogui.click(x=428, y=265)
            time.sleep(0.1)
            pyautogui.press("TAB")
            time.sleep(0.2)
            pyautogui.hotkey("ctrl","c")
            time.sleep(0.1)
            x, y = pyautogui.locateCenterOnScreen("./_internal/images/chrome-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
            pyautogui.click(x, y)
            time.sleep(0.5)
            pyautogui.click(x=302, y=557)
            time.sleep(0.5)
            pyautogui.click(x=252, y=401)
            time.sleep(0.2)
            pyautogui.hotkey("ctrl","v")
            time.sleep(0.2)
            pyautogui.click(x=144, y=537)
            time.sleep(0.4)
            while pyautogui.locateCenterOnScreen("./_internal/images/carregando.png", confidence=0.9):
                print("carregando")
            time.sleep(0.8)
            pyautogui.scroll(-500)
            time.sleep(1.2)#momento onde há a procura pelo botao verdin
            sc = pyautogui.screenshot()
            altura, largura = sc.size
            isfind = False
            for i in range(0, altura, 5):
                for j in range(0, largura, 5):
                    r, g, b = sc.getpixel((i, j))
                    if r == 8 and g == 139 and b == 25:  # momento onde o botao eh encontrado
                        x, y = i, j
                        isfind = True
                        break
                if r == 8 and g == 139 and b == 25:
                    break
            if isfind:
                pyautogui.click(i, j)
                time.sleep(3.2)
                pyautogui.scroll(-1000)
                time.sleep(0.4)
                x, y = pyautogui.locateCenterOnScreen("./_internal/images/proximo.png", confidence=0.9)
                pyautogui.click(x, y)
                time.sleep(0.3)
                while pyautogui.locateCenterOnScreen("./_internal/images/carregando.png", confidence=0.9):
                    print("carregando")
                time.sleep(0.4)
                x, y = pyautogui.locateCenterOnScreen("./_internal/images/agendado.png", confidence=0.9)
                pyautogui.click(x, y)
                time.sleep(1.1)
                continuacao_consulta(crm,especialidade,nameMed,procedimentos,gratuidade,procedimentosPaciente,gratuidadeOrig)
                continue

            else:  # momento onde nao foi encontrado pelo cpf pois o botao nao apareceu
                print("nao foi encontrado")
                pyautogui.press("f5")
                time.sleep(1)
                pyautogui.scroll(2000)
                time.sleep(0.2)
                x,y = pyautogui.locateCenterOnScreen("./_internal/images/atende-icon.png",region=(100,730,1200,49),confidence=0.9)
                pyautogui.click(x,y)
                time.sleep(0.2)
                pyautogui.click(x=109, y=268)
                time.sleep(0.1)
                pyautogui.hotkey("ctrl","c")
                x, y = pyautogui.locateCenterOnScreen("./_internal/images/chrome-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
                pyautogui.click(x, y)
                pyautogui.moveTo(x, y - 90)
                time.sleep(0.8)
                pyautogui.scroll(-500)
                time.sleep(0.3)
                if pyautogui.locateCenterOnScreen("./_internal/images/botao-sus.png", confidence=0.9):
                    x, y = pyautogui.locateCenterOnScreen("./_internal/images/botao-sus.png", confidence=0.9)
                    pyautogui.click(x,y)
                else: pyautogui.click(x=164, y=514)
                time.sleep(0.5)
                pyautogui.click(x=202, y=360)
                pyautogui.hotkey("ctrl", "v")
                pyautogui.click(x=144, y=537)
                time.sleep(0.3)
                while pyautogui.locateCenterOnScreen("./_internal/images/carregando.png", confidence=0.9):
                    print("carregando")
                time.sleep(0.7)
                pyautogui.scroll(-500)
                time.sleep(1.2)  # momento onde há a procura pelo botao verdin
                sc = pyautogui.screenshot()
                isfind = False
                for i in range(0, altura, 5):
                    for j in range(0, largura, 5):
                        r, g, b = sc.getpixel((i, j))
                        if r == 8 and g == 139 and b == 25:  # momento onde o botao eh encontrado
                            x, y = i, j
                            isfind = True
                            break
                    if r == 8 and g == 139 and b == 25:
                        break
                if isfind: #é pq foi encontrado pelo cns
                    pyautogui.click(i, j)
                    time.sleep(3.6)
                    pyautogui.scroll(-1000)
                    time.sleep(0.6)
                    x, y = pyautogui.locateCenterOnScreen("./_internal/images/proximo.png", confidence=0.8)
                    pyautogui.click(x, y)

                    time.sleep(0.3)
                    while pyautogui.locateCenterOnScreen("./_internal/images/carregando.png", confidence=0.9):
                        print("carregando")
                    time.sleep(0.4)
                    x, y = pyautogui.locateCenterOnScreen("./_internal/images/agendado.png", confidence=0.8)
                    pyautogui.click(x, y)
                    continuacao_consulta(crm,especialidade,nameMed,procedimentos,gratuidade,procedimentosPaciente,gratuidadeOrig)
                    continue

                else: #nao tem pacto, lanca tudo na gratuidade
                    print("n tem pacto")
                    pyautogui.press('f5')
                    time.sleep(1)
                    pyautogui.scroll(1000)



#criacao do menu onde o usuario vai inserir o registro

def programConsGrat(pacientes,procedimentosPaciente,procedimentos,gratuidade,nomeMed,crm,gratuidadeOrig):
    print('consulta grat')
    pyautogui.hotkey('ctrl','w')
    time.sleep(0.2)
    pyautogui.hotkey("ctrl", "1")
    time.sleep(0.2)
    x,y = pyautogui.locateCenterOnScreen("./_internal/images/atende-icon.png",region=(100,730,1200,49),confidence=0.9)
    pyautogui.click(x,y)
    time.sleep(0.5)
    pyautogui.press("f4")
    time.sleep(1)
    p = 0 
    while p < len(pacientes):
        if p == 0:
            gratuidade=gratuidadeOrig
            gratuidade.append('consulta medica')
            print(gratuidade)
        time.sleep(0.9)
        pyautogui.press("f2")
        time.sleep(0.2)
        pyautogui.press("f4")
        time.sleep(0.9)
        pyautogui.hotkey("shift","TAB")
        time.sleep(0.2)
        pyautogui.write(pacientes[p])
        p = p + 1
        pyautogui.press("f4")
        time.sleep(0.2)
        pyautogui.press("left")
        time.sleep(0.2)
        pyautogui.press("enter")
        time.sleep(0.3)
        pyautogui.press("f10")
        time.sleep(0.2)
        pyautogui.press("left")
        time.sleep(0.1)
        pyautogui.press("enter")
        if len(procedimentos) > 1:
            time.sleep(0.3)
            pyautogui.click(x=109, y=268)
            time.sleep(0.1)
            pyautogui.hotkey("ctrl","c")
            time.sleep(0.2)
            pyautogui.press("f10")
            time.sleep(0.2)
            pyautogui.press("left")
            time.sleep(0.1)
            pyautogui.press("enter")

            time.sleep(0.1)
            x, y = pyautogui.locateCenterOnScreen("./_internal/images/chrome-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
            pyautogui.click(x,y)
            time.sleep(0.2)
            pyautogui.click(x=164, y=470)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.click(x=255, y=473)
            time.sleep(7.9)
            pyautogui.scroll(-1000)
            time.sleep(0.1)
            x, y = pyautogui.locateCenterOnScreen("./_internal/images/selecionarProfissional.png", region=(50, 130, 700, 270), confidence=0.9)
            pyautogui.click(x, y)
            if nomeMed.startswith("clara") or nomeMed.startswith("CLARA"):
                pyautogui.write("andre")
                pyautogui.press("down")
            else:
                pyautogui.write(nomeMed)
            if nomeMed.startswith("andre") or nomeMed.startswith("Andre") or nomeMed.startswith("ANDRE"):
                pyautogui.press("down")
            time.sleep(0.4)
            pyautogui.press("enter")
            time.sleep(0.3)
            while pyautogui.locateCenterOnScreen("./_internal/images/carregando.png", confidence=0.9) == True:
                print("carregando")
            time.sleep(1.2)
            twoTimes = 0
            i = 1
            while i < len(procedimentos):
                verifier = 0
                time.sleep(1.7)
                pyautogui.scroll(-1000)
                time.sleep(0.1)
                if pyautogui.locateCenterOnScreen("./_internal/images/selecionarProcedimento.png", confidence=0.9):
                    x, y = pyautogui.locateCenterOnScreen("./_internal/images/selecionarProcedimento.png", confidence=0.9)
                    pyautogui.click(x, y)
                else:
                    pyautogui.click(x=294, y=505)
                if procedimentos[i] == "ceratoscopia":
                    pyautogui.write("topografia")
                else:
                    pyautogui.write(procedimentos[i])
                pyautogui.press("enter")
                time.sleep(1)
                
                if pyautogui.locateCenterOnScreen("./_internal/images/popup-qtd.png", confidence=0.9) == True:
                    pyautogui.press("enter")
                    gratuidade.append(procedimentos[i])
                    continue
                time.sleep(1.2)
                conter = 0
                while pyautogui.locateCenterOnScreen("./_internal/images/carregando.png", confidence=0.9):
                    print("carregando")
                    time.sleep(1)
                    conter += 1
                    print(conter)
                    if conter > 5: break
                if conter > 5:
                    pyautogui.press("enter")
                    pyautogui.press("f5")
                    time.sleep(0.8)
                    pyautogui.press("enter")
                    time.sleep(0.8)
                    pyautogui.scroll("2500")

                    gratuidade.append(procedimentos[i])
                    verifier = 1

                if procedimentos[i].startswith(procedimentos[i - 1]) and verifier == 0:
                    time.sleep(1)
                    while True:
                        if pyautogui.locateCenterOnScreen("./_internal/images/botaosim2.png", confidence=0.9):
                            break
                        time.sleep(0.2)
                        print("carregando")
                    time.sleep(1)
                    x, y = pyautogui.locateCenterOnScreen("./_internal/images/botaosim2.png", confidence=0.9)
                    pyautogui.click(x, y)
                    time.sleep(0.8)
                    while True:
                        print("saindo da tela")
                        if pyautogui.locateCenterOnScreen("./_internal/images/botaosim2.png", confidence=0.9) != True:
                            break
                    time.sleep(2.8)
                    twoTimes = 1
                else:
                    time.sleep(1.2)

                if verifier == 0: procedimentosPaciente.append(procedimentos[i])
                i = i + 1
                pyautogui.scroll(-1000)
            time.sleep(0.7)
            if(twoTimes==1):
                time.sleep(4.3)
            pyautogui.scroll(-2500)
            if len(procedimentosPaciente) > 1 and procedimentosPaciente != "vetor":
                pyautogui.scroll(-500)
                time.sleep(0.2)
                if(pyautogui.locateCenterOnScreen("./_internal/images/imprimirGuia.png", confidence=0.9)):
                    x, y = pyautogui.locateCenterOnScreen("./_internal/images/imprimirGuia.png", confidence=0.9)
                else: pyautogui.click(x=309, y=551)
                pyautogui.click(x, y)
                time.sleep(5.5)
                pyautogui.hotkey("ctrl", "p")
                funcao_btn_imprimir()
                time.sleep(0.4)
            
            k = 790
            j = 442
            if len(procedimentosPaciente) > 1:
                i = len(procedimentosPaciente) -1
                while i > 0:
                    x, y = pyautogui.locateCenterOnScreen("./_internal/images/chrome-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
                    pyautogui.click(x, y)
                    time.sleep(0.1)
                    x, y = pyautogui.locateCenterOnScreen("./_internal/images/demandaaberta.png", confidence=0.9)
                    pyautogui.click(x, y)
                    time.sleep(0.2)
                    pyautogui.moveTo(x,y+500)
                    pyautogui.scroll(-1500)
                    time.sleep(0.2)
                    pyautogui.doubleClick(k, j)
                    pyautogui.hotkey("ctrl", "c")
                    pyautogui.doubleClick(k - 30, j)
                    pyautogui.hotkey("ctrl", "c")

                    time.sleep(0.1)
                    if i == 1:
                        pyautogui.hotkey("ctrl","w")
                    j = j - 30
                    x, y = pyautogui.locateCenterOnScreen("./_internal/images/atende-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
                    pyautogui.click(x, y)
                    time.sleep(0.3)
                    pyautogui.press("f3")
                    time.sleep(0.3)
                    pyautogui.hotkey("ctrl", "enter")
                    time.sleep(0.2)
                    pyautogui.write(procedimentosPaciente[i])
                    time.sleep(0.2)
                    pyautogui.press("enter")
                    time.sleep(0.2)
                    pyautogui.press("enter")
                    pyautogui.press("TAB", 3)
                    pyautogui.write(nomeMed)
                    pyautogui.press("down")
                    pyautogui.press("f5")
                    time.sleep(0.2)
                    pyautogui.press("enter")
                    pyautogui.hotkey("ctrl", "v")
                    time.sleep(0.1)
                    pyautogui.press("enter")
                    time.sleep(0.1)
                    pyautogui.press("enter")
                    time.sleep(0.3)
                    i = i - 1

        time.sleep(1)
        pyautogui.press("enter", 3)
        if len(gratuidade) > 1 and gratuidade != "vetor":  # se tiver algo  na gratuidade, é necessario lançar
            pyautogui.press("f9", 3)
            pyautogui.press("f10")
            time.sleep(0.2)
            pyautogui.press("f10")
            time.sleep(0.4)
            pyautogui.press("left")
            pyautogui.press("enter")
            time.sleep(0.6)
            pyautogui.click(x=114, y=166)
            pyautogui.write("gratuidade")
            pyautogui.press("down")
            time.sleep(0.2)
            pyautogui.press("f5")
            time.sleep(0.3)
            pyautogui.press("enter")
        i = 1  # a posicao 0 tem "vetor"
        while i < len(gratuidade):
            pyautogui.press("f3")
            time.sleep(0.3)
            pyautogui.hotkey("ctrl", "enter")
            time.sleep(0.2)
            pyautogui.write(gratuidade[i])
            time.sleep(0.2)
            pyautogui.press("enter")
            time.sleep(0.2)
            pyautogui.press("enter")
            pyautogui.press("TAB", 3)
            pyautogui.write(nomeMed)
            pyautogui.press("down")
            pyautogui.press("f5")
            time.sleep(0.2)
            pyautogui.press("enter", 3)
            time.sleep(0.1)
            pyautogui.press("enter")
            time.sleep(0.3)
            pyautogui.press("f3")
            i = i + 1
        time.sleep(0.2)
        pyautogui.press("left")
        pyautogui.press("enter")
        pyautogui.press("f8")
        time.sleep(1.5)
        pyautogui.press("enter", 3)
        time.sleep(9)
        pyautogui.press("enter")
        pyautogui.press("enter")
        gratuidade.clear()
        gratuidade = gratuidadeOrig

    time.sleep(0.4)
    pyautogui.hotkey("f2")
    pyautogui.hotkey("f4")  #####
    x, y = pyautogui.locateCenterOnScreen("./_internal/images/chrome-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(0.3)
    pyautogui.press("f5")
    time.sleep(0.4)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.scroll(2000)
    time.sleep(0.2)
    pyautogui.hotkey("ctrl", "1")
    time.sleep(0.1)
    pyautogui.click(x=717, y=430)
    time.sleep(0.6)
    pyautogui.click(x=717, y=530)
    pyautogui.scroll(1000)
    time.sleep(0.5)
    pyautogui.scroll(-500)
    procedimentosPaciente.clear()
    procedimentosPaciente.append("vetor")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/')
def style():
    return render_template('style.css')
@app.route('/')
def js():
    return render_template('main.js')
@app.route('/enviar_lista', methods=['POST'])
def receber_lista():
    data = request.get_json()
    isConsGrat = data.get('consultaIsGrat')
    procedimentosJson = data.get('procedimentosJson', [])
    gratuidadeJson = data.get('gratuidadesJson',[])
    pacientesJson = data.get('registrosJson', [])
    crm = data.get('crm')
    nameMed = data.get('nomeMedico')
    especialidade = data.get('especialidade')
    dfitp = data.get('dfitp')
    mfitp = data.get('mfitp')
    yfitp = data.get('yfitp')

    pacientes = []
    procedimentos =[]
    procedimentos.append("vetor")
    gratuidade = []
    gratuidade.append("vetor")
    gratuidadeOrig = []

    gratuidadeOrig.append("vetor")
    procedimentosPaciente = []
    procedimentosPaciente.append("vetor")

    procedimentos += procedimentosJson
    pacientes += pacientesJson
    #adding the year to verify te version that will work in the actual
    gratuidadeOrig.extend(gratuidadeJson)
    print(procedimentos)
    if yfitp == 2023:    
        if(dfitp < 6 and mfitp <= 10 or dfitp < 31 and mfitp < 12):    
            if isConsGrat=='sim':
                gratuidade.extend(gratuidadeJson)
                programConsGrat(pacientes,procedimentosPaciente,procedimentos,gratuidade,nameMed,crm,gratuidadeOrig)
            
            else:
                gratuidade.extend(gratuidadeJson)
                print(gratuidade)
                program(procedimentosPaciente,procedimentos,pacientes,gratuidade,gratuidadeOrig,crm,nameMed,especialidade)
        else : print('denied access')
    else : print('denied access')
    return jsonify({'resultado': nameMed})

if __name__ == '__main__':
    app.run(debug=True)
    


