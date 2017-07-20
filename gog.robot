*** Settings ***
Library  gog_keywords.py

*** Test Cases ***
Open Test Plan For GOG
    Open Browser
    Check Category
    [Teardown]  Close Test

*** Keywords ***
Open Browser
    Set Up Browser
    ${current_url}  Check Url
    Should Contain  ${current_url}  games
    Log To Console  Open Browser

Check Category
    Select Genre
    Find All In Genre
    Log To Console  Check Category

Close Test
    Tear Down
    Log To Console  Close Browser


