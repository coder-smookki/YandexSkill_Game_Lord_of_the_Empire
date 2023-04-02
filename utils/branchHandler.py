import copy


def updateBranchToResponse(event, response, firstBranchName):
    newEvent = copy.deepcopy(event)
    newResponse = copy.deepcopy(response)

    print(newResponse['session_state'])

    if 'dontUpdateBranches' in response:
        return response

    if not 'branch' in newEvent['state']['session']:
        print('zxc')
        newResponse['session_state']['branch'] = [firstBranchName]
        return newResponse

    elif not newResponse['session_state']['branch'] and newResponse['session_state']['branch'] != '':
        print('aboba')
        newResponse['session_state']['branch'] = newEvent['state']['session']['branch']
        return newResponse

    else:
        eventBranch = newEvent['state']['session']['branch']
        responseState = newResponse['session_state']['branch']
        print(1)
        # если диалог не имел брэнча
        if responseState == '' or not responseState:
            print(2)
            newResponse['session_state']['branch'] = eventBranch
            return newResponse

        # сработает, если eventbranch.index(...) найдет новый брэнч в брэнчах
        try:
            index = eventBranch.index(responseState)
            eventBranch = eventBranch[0:index + 1]
            newResponse['session_state']['branch'] = eventBranch
            return newResponse

        # в случае, если в брэнчах нету нового бренча
        except:
            eventBranch.append(responseState)
            newResponse['session_state']['branch'] = eventBranch
            return newResponse


def getDialogResponseFromEnd(event, dialogNumber, dialogs):
    branchList = event["state"]["session"]["branch"]
    if dialogNumber > len(branchList):
        response = dialogs[branchList[0]]['getResponse'](event, None)
        if 'card' in response["response"] and response["response"]['card']['description']:
            response["response"]['card']['description'] = 'Назад уже некуда. ' + response["response"]['card']['description']
        elif 'text':
            response["response"]['text'] = 'Назад уже некуда. ' + response["response"]['text']
        response["response"]['tts'] = 'Назад уже некуда. ' + response["response"]['tts']
        
        return response
    return dialogs[branchList[-dialogNumber]]['getResponse'](event, None)
