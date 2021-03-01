*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application


*** Test Cases ***
Register With Valid Username And Password
    Register  kalle  kalle123  kalle123
    Register Should Succeed

Register With Too Short Username And Valid Password
    Register  ka  kalle123  kalle123
    Registration Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Register  kalle  kal  kal
    Registration Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Register  kalle  kalle123  kalle123123
    Registration Should Fail With Message  Password and confirmation are not the same

Login After Successful Registration
    Register  kalle  kalle123  kalle123
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Register  kalle  kal  kal
    Go To Login Page
    Set Username  kalle
    Set Password  kal
    Click Button  Login
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register
    [Arguments]  ${username}  ${password}  ${password_confirmation}
    Go To Register Page
    Input Text      username  ${username}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password_confirmation}
    Click Button    Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Registration Should Fail With Message 
    [Arguments]  ${message}
    Registration Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}