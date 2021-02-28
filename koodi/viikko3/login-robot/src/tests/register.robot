*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

# A new user account can be created if a proper unused username and a proper password are given

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pekka  pekka123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kalle
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kalleontaalla
    Output Should Contain  Password is long enough, but cannot have only letters


*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123